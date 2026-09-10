# Governance Changelog

## 1.0.1 — 2026-09-10

Baseline consistency correction:

- add the durable `.ai/DECISIONS.md` log referenced by the framework documentation;
- require the decision log in mechanical preflight;
- synchronize governance version markers and mark the repository code baseline ready.

## 1.0.0 — 2026-09-10

Initial production baseline:

- short root `AGENTS.md` controller with modular `.ai` sources of truth;
- mandatory request/load/preflight/plan/execute/validate/handoff lifecycle;
- risk-tiered preflight and explicit stop conditions;
- anti-drift policy;
- prompt-injection, secret, dependency, workflow, network, and destructive-action security rules;
- template initialization guard for derived repositories;
- nested `AGENTS.md` allowlist;
- dependency-free preflight/postflight validation;
- read-only GitHub Actions governance gate with immutable Action pinning;
- CODEOWNERS, PR checklist, Dependabot configuration, security and contribution guidance.
