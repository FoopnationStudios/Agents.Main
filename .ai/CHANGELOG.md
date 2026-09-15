# Governance Changelog

## 1.1.0 — 2026-09-15

Compatible governance feature release:

- add `.ai/SPECIALIST_AGENT.md` as the canonical architecture and operating standard for bounded software-backed AI agents;
- add explicit `Project-Type` classification to `.ai/PROJECT.md`;
- require derived repositories to classify as `GENERAL_SOFTWARE` or `SPECIALIST_AGENT` during initialization;
- automatically route `SPECIALIST_AGENT` projects through the specialist-agent standard from the root `AGENTS.md` boot sequence;
- require the specialist-agent policy file in mechanical preflight;
- add governance tests for the new classification and required policy;
- preserve the short-root-controller design by keeping detailed specialist policy under `.ai/` rather than expanding `AGENTS.md` into a monolith.

Migration for repositories intentionally upgrading from an earlier Agents.Main baseline:

1. add `.ai/SPECIALIST_AGENT.md` from the 1.1.0 template;
2. add `Project-Type: GENERAL_SOFTWARE` or `Project-Type: SPECIALIST_AGENT` to `.ai/PROJECT.md`;
3. if classified `SPECIALIST_AGENT`, define or reference the Agent Contract and reconcile the project architecture against the specialist standard;
4. synchronize governance-version markers and run the governance preflight/tests/postflight.

## 1.0.2 — 2026-09-10

Security/maintenance patch:

- update the immutable `actions/checkout` pin from 5.1.0 to 7.0.1 after verifying the exact v7.0.1 tag commit and a successful Dependabot governance run;
- include `.ai/STATUS.md` in governance-version consistency enforcement;
- add unit coverage for governance-version marker consistency.

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
