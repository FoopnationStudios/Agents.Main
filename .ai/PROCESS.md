# Canonical Task Process

Every repository task is routed through this process. The purpose is consistency, not bureaucracy.

## State machine

`REQUEST -> LOAD -> PREFLIGHT -> PLAN -> EXECUTE -> VALIDATE -> HANDOFF`

A task may move backward when new evidence changes the plan. It must not skip directly from request to mutation.

## 1. REQUEST

Normalize the user's request into:

- requested outcome;
- explicit constraints;
- timeframe or urgency when relevant;
- systems/files likely involved;
- success evidence;
- unresolved ambiguity.

Do not turn a narrow request into a broader modernization project.

## 2. LOAD

Read the control-plane documents required by `AGENTS.md`, then inspect the actual relevant repository state. Prefer source-of-truth files and executable configuration over stale summaries.

## 3. PREFLIGHT

Classify risk using `PREFLIGHT.md`. Establish:

- current behavior;
- smallest authorized scope;
- expected files/systems affected;
- protected surfaces touched;
- dependencies and downstream consumers;
- validation plan;
- stop conditions.

Run `python3 scripts/preflight.py` when possible before mutation.

## 4. PLAN

Choose the smallest coherent implementation. Reuse existing patterns. For simple tasks, the plan may be a few internal steps; do not manufacture paperwork. For cross-cutting/high-risk tasks, make assumptions and rollback considerations explicit.

## 5. EXECUTE

Make only the authorized changes. Preserve unrelated work. Re-check scope when an unexpected dependency appears. Discovery of adjacent work is not authorization to perform it.

## 6. VALIDATE

Run the applicable commands documented in `PROJECT.md`, inspect failures rather than hiding them, and run `python3 scripts/postflight.py` when possible. Review the diff for security and accidental churn.

## 7. HANDOFF

Report:

- what changed and why;
- changed files/components;
- validation actually executed and observed results;
- checks that were skipped or unavailable;
- residual risks/unknowns;
- owner decisions or follow-up work, if any.

Never convert an unverified result into a claim of completion.
