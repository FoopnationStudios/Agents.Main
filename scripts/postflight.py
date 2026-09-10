#!/usr/bin/env python3
"""Dependency-free repository governance postflight."""

from __future__ import annotations

import argparse
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ci", action="store_true")
    args = parser.parse_args()

    failures: list[str] = []

    preflight = [sys.executable, str(ROOT / "scripts/preflight.py")]
    if args.ci:
        preflight.append("--ci")
    checked = run(preflight)
    print(checked.stdout, end="")
    if checked.stderr:
        print(checked.stderr, end="", file=sys.stderr)
    if checked.returncode != 0:
        failures.append("preflight")

    diff_commands: list[list[str]] = []
    if args.ci:
        parent = run(["git", "rev-parse", "--verify", "HEAD^"])
        if parent.returncode == 0:
            diff_commands.append(["git", "diff", "--check", "HEAD^", "HEAD"])
        else:
            diff_commands.append(["git", "show", "--check", "--format=", "HEAD"])
    else:
        diff_commands.extend(
            [
                ["git", "diff", "--check"],
                ["git", "diff", "--cached", "--check"],
            ]
        )

    for command in diff_commands:
        diff_check = run(command)
        if diff_check.returncode != 0:
            if diff_check.stdout:
                print(diff_check.stdout, end="")
            if diff_check.stderr:
                print(diff_check.stderr, end="", file=sys.stderr)
            failures.append(" ".join(command))

    if failures:
        print("POSTFLIGHT FAILED: " + ", ".join(failures))
        return 1

    print("POSTFLIGHT PASS: governance checks and diff whitespace validation succeeded")
    print("NOTE: project-specific build/test/security commands remain mandatory when applicable; see .ai/PROJECT.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
