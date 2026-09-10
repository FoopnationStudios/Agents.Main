# AI Control Plane Index

This directory is the repository's durable operating context. `AGENTS.md` is only the bootloader and map.

Read order for a normal mutating task:

1. `../AGENTS.md`
2. `PROJECT.md`
3. `STATUS.md`
4. `PROCESS.md`
5. `PREFLIGHT.md`
6. `ANTI_DRIFT.md`
7. `SECURITY_RULES.md`
8. `DEFINITION_OF_DONE.md`
9. `ARCHITECTURE.md` when structurally relevant

File responsibilities:

- `VERSION` — governance semantic version.
- `PROJECT.md` — durable project identity, owner, constraints, commands, protected areas, and operating assumptions.
- `STATUS.md` — current milestone, live priorities, known blockers, and near-term operating state.
- `PROCESS.md` — canonical request-to-handoff state machine.
- `PREFLIGHT.md` — risk tiers, stop conditions, and mandatory pre-mutation questions.
- `ANTI_DRIFT.md` — scope containment and anti-churn policy.
- `SECURITY_RULES.md` — trust boundaries, credentials, dependencies, workflows, network, and destructive actions.
- `ARCHITECTURE.md` — project architecture and governance integration points.
- `DEFINITION_OF_DONE.md` — objective completion criteria.
- `DECISIONS.md` — durable architectural/governance decisions and their rationale.
- `CHANGE_CONTROL.md` — how to modify this control plane safely.
- `CHANGELOG.md` — human-readable governance release history.
- `nested-agents.txt` — explicit allowlist for deeper `AGENTS.md` files.

## Update discipline

Durable facts belong in `PROJECT.md` or `ARCHITECTURE.md`. Fast-changing facts belong in `STATUS.md`. Architectural or governance decisions that future agents should not have to rediscover belong in `DECISIONS.md`. New policy belongs in the narrowest policy file that owns that concern. Do not grow `AGENTS.md` into a monolithic manual.

If a rule becomes obsolete, replace or remove it explicitly and update the governance version when required. Contradictory rules are defects, not an invitation for the agent to guess.
