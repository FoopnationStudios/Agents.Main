# Governance Change Control

The governance control plane is deliberately easier to update than hard-coded agent prompts, but changes must remain reviewable and non-accidental.

## Control-plane paths

Changes to any of these are governance changes:

- `/AGENTS.md`
- `/.ai/**`
- `/.github/CODEOWNERS`
- `/.github/copilot-instructions.md`
- `/.github/workflows/**`
- `/scripts/preflight.py`
- `/scripts/postflight.py`
- `/tests/test_governance.py`

`STATUS.md` may change operationally without a version bump unless it also changes policy or architecture.

## Required process

1. Isolate governance changes from unrelated product work whenever practical.
2. State the problem the policy change solves.
3. Check for contradictions with existing policy and agent precedence.
4. Update tests for any mechanically enforceable rule.
5. Run preflight, governance tests, and postflight.
6. Update `.ai/CHANGELOG.md` for policy/framework changes.
7. Update `.ai/VERSION`, the `Governance-Version` values in `AGENTS.md` and `PROJECT.md`, and relevant docs when the change requires a version bump.
8. Obtain control-plane owner review when repository protection supports it.

## Semantic versioning

- **PATCH**: clarification or non-breaking policy/tooling correction that preserves required agent behavior.
- **MINOR**: new compatible control, new document, or stricter behavior that does not invalidate existing initialized projects without a documented migration.
- **MAJOR**: precedence changes, removed guarantees, weakened security/scope controls, incompatible initialization requirements, or control-plane redesign requiring derived-project migration.

Security weakening is never hidden in a patch release.

## Emergency fixes

A clearly exploitable control-plane defect may be fixed urgently, but the change still requires validation and a changelog entry. Do not use "emergency" to bypass permanent review controls.
