import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts import preflight  # noqa: E402


class GovernanceUnitTests(unittest.TestCase):
    def test_version_is_semver(self):
        version = (ROOT / ".ai/VERSION").read_text(encoding="utf-8").strip()
        self.assertRegex(version, preflight.SEMVER_RE)

    def test_governance_version_markers_match(self):
        version = (ROOT / ".ai/VERSION").read_text(encoding="utf-8").strip()
        for rel in ("AGENTS.md", ".ai/PROJECT.md", ".ai/STATUS.md"):
            text = (ROOT / rel).read_text(encoding="utf-8")
            self.assertIn(f"Governance-Version: {version}", text, rel)

    def test_pinned_action_is_accepted(self):
        yaml = "uses: actions/checkout@" + ("a" * 40) + "\n"
        self.assertEqual(preflight.workflow_violations(yaml, "test.yml"), [])

    def test_tagged_action_is_rejected(self):
        errors = preflight.workflow_violations("uses: actions/checkout@v5\n", "test.yml")
        self.assertTrue(any("full commit SHA" in item for item in errors))

    def test_pull_request_target_is_rejected(self):
        errors = preflight.workflow_violations("on:\n  pull_request_target:\n", "test.yml")
        self.assertTrue(any("pull_request_target" in item for item in errors))

    def test_write_all_is_rejected(self):
        errors = preflight.workflow_violations("permissions: write-all\n", "test.yml")
        self.assertTrue(any("write-all" in item for item in errors))

    def test_project_field_parser(self):
        text = "Initialization-State: ACTIVE\nRepository: owner/repo\n"
        self.assertEqual(preflight.parse_project_field(text, "Repository"), "owner/repo")

    def test_inline_pull_request_target_is_rejected(self):
        errors = preflight.workflow_violations("on: [pull_request, pull_request_target]\n", "test.yml")
        self.assertTrue(any("pull_request_target" in item for item in errors))

    def test_mutable_container_action_is_rejected(self):
        errors = preflight.workflow_violations("uses: docker://alpine:3.20\n", "test.yml")
        self.assertTrue(any("sha256" in item for item in errors))

    def test_digest_pinned_container_action_is_accepted(self):
        yaml = "uses: docker://alpine@sha256:" + ("a" * 64) + "\n"
        self.assertEqual(preflight.workflow_violations(yaml, "test.yml"), [])


if __name__ == "__main__":
    unittest.main()
