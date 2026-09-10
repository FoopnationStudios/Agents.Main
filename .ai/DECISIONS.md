# Governance Decision Log

Record durable decisions here when future maintainers or agents would otherwise have to rediscover why the framework works a particular way. Keep entries concise. Do not use this file as a task log.

## D-001 — Short root controller, modular control plane

Date: 2026-09-10  
Status: Accepted

**Decision:** Keep `AGENTS.md` small and use it as a routing/controller document. Store detailed context and policy in focused `.ai/` files.

**Reason:** Always-loaded context is scarce, monolithic instruction files become stale and internally contradictory, and smaller policy files are easier to review and validate mechanically.

## D-002 — Separate behavioral policy from mechanical enforcement

Date: 2026-09-10  
Status: Accepted

**Decision:** Agent instructions define expected behavior; Python checks, GitHub Actions, review routing, and repository rules provide independent enforcement/evidence where feasible.

**Reason:** Markdown instructions alone cannot guarantee that every external AI client will read or obey them.

## D-003 — CI does not execute commands parsed from Markdown

Date: 2026-09-10  
Status: Accepted

**Decision:** `.ai/PROJECT.md` documents project validation commands for agents, but the governance workflow does not parse that file and execute arbitrary command strings. Project-specific CI must be encoded explicitly in reviewed workflow/script files.

**Reason:** Executing editable documentation as shell input would create an unnecessary command-injection boundary and make workflow behavior difficult to audit.

## D-004 — Immutable external Action references

Date: 2026-09-10  
Status: Accepted

**Decision:** External GitHub Actions must be pinned to full commit SHAs. `docker://` images must use a `sha256` digest. Local actions remain allowed.

**Reason:** Mutable tags add avoidable software-supply-chain risk. Immutable references make reviewed automation reproducible.

## D-005 — Derived repositories fail until initialized

Date: 2026-09-10  
Status: Accepted

**Decision:** Repositories created from this template must set `Initialization-State: ACTIVE`, declare their actual `owner/name`, and replace the template CODEOWNERS identity before the governance gate passes.

**Reason:** A copied template that silently retains the original project's identity or ownership metadata gives agents false context and creates misleading review controls.

## D-006 — Nested agent instructions are explicit

Date: 2026-09-10  
Status: Accepted

**Decision:** Tracked nested `AGENTS.md` files must be registered in `.ai/nested-agents.txt`, and tracked `AGENTS.override.md` files are prohibited.

**Reason:** Deeper agent files can change instruction precedence. Making their existence explicit reduces accidental or malicious policy shadowing.

## Superseding a decision

Do not erase history simply because a decision changes. Mark the old entry `Superseded`, reference the replacement decision, and add the new rationale. If the change affects governance behavior, follow `.ai/CHANGE_CONTROL.md` and version it appropriately.
