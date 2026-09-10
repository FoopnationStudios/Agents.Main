#!/usr/bin/env python3
"""Dependency-free repository governance preflight."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
ORIGIN_REPOSITORY = "FoopnationStudios/Agents.Main"
ORIGIN_OWNER_TOKEN = "@FoopnationStudios"

REQUIRED_FILES = (
    "AGENTS.md",
    ".ai/README.md",
    ".ai/VERSION",
    ".ai/PROJECT.md",
    ".ai/STATUS.md",
    ".ai/PROCESS.md",
    ".ai/PREFLIGHT.md",
    ".ai/ANTI_DRIFT.md",
    ".ai/SECURITY_RULES.md",
    ".ai/ARCHITECTURE.md",
    ".ai/DEFINITION_OF_DONE.md",
    ".ai/DECISIONS.md",
    ".ai/CHANGE_CONTROL.md",
    ".ai/CHANGELOG.md",
    ".ai/nested-agents.txt",
    ".github/copilot-instructions.md",
    ".github/CODEOWNERS",
    ".github/pull_request_template.md",
    ".github/dependabot.yml",
    ".github/workflows/governance.yml",
    ".gitignore",
    "SECURITY.md",
    "CONTRIBUTING.md",
    "scripts/preflight.py",
    "scripts/postflight.py",
    "tests/test_governance.py",
)

HIGH_RISK_TRACKED_NAMES = {
    ".env",
    "id_rsa",
    "id_ed25519",
}
HIGH_RISK_SUFFIXES = {".p12", ".pfx", ".key"}
PRIVATE_KEY_RE = re.compile(
    r"-----BEGIN (?:RSA |EC |DSA |OPENSSH |ENCRYPTED )?PRIVATE KEY-----"
)
USES_RE = re.compile(r"^\s*-?\s*uses\s*:\s*['\"]?([^\s'\"#]+)", re.MULTILINE)
FULL_SHA_RE = re.compile(r"^[0-9a-fA-F]{40}$")
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")


def git(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def tracked_files() -> list[Path]:
    result = git("ls-files", "-z")
    if result.returncode != 0:
        return [p.relative_to(ROOT) for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.parts]
    return [Path(item) for item in result.stdout.split("\0") if item]


def read_text(rel: str | Path) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def parse_project_field(text: str, field: str) -> str | None:
    match = re.search(rf"^{re.escape(field)}:\s*(.+?)\s*$", text, re.MULTILINE)
    return match.group(1).strip() if match else None


def allowed_nested_agents() -> set[str]:
    allowed: set[str] = set()
    path = ROOT / ".ai/nested-agents.txt"
    if not path.exists():
        return allowed
    for raw in path.read_text(encoding="utf-8").splitlines():
        value = raw.strip()
        if value and not value.startswith("#"):
            allowed.add(Path(value).as_posix())
    return allowed


def workflow_violations(text: str, rel: str) -> list[str]:
    errors: list[str] = []
    if re.search(r"^[^#\n]*\bpull_request_target\b", text, re.MULTILINE):
        errors.append(f"{rel}: pull_request_target is prohibited by baseline policy")
    if re.search(r"^\s*permissions\s*:\s*write-all\s*$", text, re.MULTILINE):
        errors.append(f"{rel}: permissions: write-all is prohibited")

    for target in USES_RE.findall(text):
        if target.startswith("./"):
            continue
        if target.startswith("docker://"):
            if "@sha256:" not in target:
                errors.append(f"{rel}: container Action/image must be pinned by sha256 digest: {target}")
            continue
        if "@" not in target:
            errors.append(f"{rel}: external Action is not pinned: {target}")
            continue
        _, ref = target.rsplit("@", 1)
        if not FULL_SHA_RE.fullmatch(ref):
            errors.append(f"{rel}: external Action must use a full commit SHA: {target}")
    return errors


def run_checks(ci: bool = False) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    for rel in REQUIRED_FILES:
        required = ROOT / rel
        if not required.is_file():
            errors.append(f"missing required file: {rel}")
        elif required.is_symlink():
            errors.append(f"control-plane file must not be a symlink: {rel}")

    if errors:
        return errors, warnings

    version = read_text(".ai/VERSION").strip()
    if not SEMVER_RE.fullmatch(version):
        errors.append(".ai/VERSION must contain semantic version X.Y.Z")
    for rel in ("AGENTS.md", ".ai/PROJECT.md", ".ai/STATUS.md"):
        if f"Governance-Version: {version}" not in read_text(rel):
            errors.append(f"{rel}: Governance-Version does not match .ai/VERSION ({version})")

    project = read_text(".ai/PROJECT.md")
    state = parse_project_field(project, "Initialization-State")
    declared_repo = parse_project_field(project, "Repository")
    current_repo = os.environ.get("GITHUB_REPOSITORY")
    if current_repo:
        if current_repo == ORIGIN_REPOSITORY:
            if state != "BASELINE":
                errors.append("template origin must use Initialization-State: BASELINE")
            if declared_repo != ORIGIN_REPOSITORY:
                errors.append("template origin Repository field is incorrect")
        else:
            if state != "ACTIVE":
                errors.append("derived repository must set Initialization-State: ACTIVE in .ai/PROJECT.md")
            if declared_repo != current_repo:
                errors.append(f"derived repository must set Repository: {current_repo} in .ai/PROJECT.md")
            codeowners = read_text(".github/CODEOWNERS")
            if ORIGIN_OWNER_TOKEN in codeowners:
                errors.append("derived repository must replace template CODEOWNERS entries")

    files = tracked_files()
    allow_nested = allowed_nested_agents()
    found_nested = {
        rel.as_posix()
        for rel in files
        if rel.name == "AGENTS.md" and rel.as_posix() != "AGENTS.md"
    }
    for path in sorted(found_nested - allow_nested):
        errors.append(f"unregistered nested AGENTS.md: {path}")
    for path in sorted(allow_nested - found_nested):
        warnings.append(f"nested-agents allowlist entry does not exist: {path}")

    for rel_path in files:
        rel = rel_path.as_posix()
        name = rel_path.name.lower()
        suffix = rel_path.suffix.lower()
        if name in HIGH_RISK_TRACKED_NAMES or name.startswith(".env.") or suffix in HIGH_RISK_SUFFIXES:
            if name != ".env.example":
                errors.append(f"high-risk secret/key file is tracked: {rel}")

        if rel_path.name == "AGENTS.override.md":
            errors.append(f"tracked AGENTS.override.md is prohibited: {rel}")

        full = ROOT / rel_path
        if full.is_symlink():
            continue
        try:
            text = full.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue

        if "<<<<<<< " in text and "=======\n" in text and ">>>>>>> " in text:
            errors.append(f"unresolved merge-conflict markers: {rel}")
        if PRIVATE_KEY_RE.search(text):
            errors.append(f"private-key material detected in tracked text: {rel}")

        if rel.startswith(".github/workflows/") and rel_path.suffix.lower() in {".yml", ".yaml"}:
            errors.extend(workflow_violations(text, rel))

    status = git("status", "--porcelain")
    if status.returncode == 0 and status.stdout.strip() and not ci:
        warnings.append("working tree has uncommitted changes; preserve unrelated user work")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ci", action="store_true", help="CI mode; suppress local dirty-tree warning")
    args = parser.parse_args()

    errors, warnings = run_checks(ci=args.ci)
    for warning in warnings:
        print(f"WARN: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    if errors:
        print(f"PREFLIGHT FAILED: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1
    print(f"PREFLIGHT PASS: 0 errors, {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
