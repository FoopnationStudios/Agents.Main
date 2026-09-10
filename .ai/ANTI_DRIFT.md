# Anti-Drift Policy

The user's requested outcome is the scope anchor. Adjacent problems are evidence, not authorization.

## Default rule

Make the minimum coherent change that satisfies the request and preserves surrounding behavior.

## Do not, unless required by the task

- refactor unrelated code;
- rename unrelated files, symbols, APIs, or concepts;
- reformat untouched areas;
- reorganize folders for preference;
- upgrade packages or toolchains;
- replace working architecture with a preferred architecture;
- add speculative abstractions, feature flags, telemetry, configuration, or future-proofing;
- fix unrelated bugs or technical debt;
- rewrite documentation unrelated to the changed behavior;
- change tests merely to make a broken implementation appear correct;
- weaken assertions, security rules, linting, or CI gates to obtain a green result.

## When adjacent work is discovered

1. Determine whether it blocks the requested outcome.
2. If it does not block the task, leave it unchanged and mention it only if it is materially useful.
3. If it does block the task, make only the minimum prerequisite change within the same risk model.
4. If that prerequisite materially expands risk or product behavior, stop and request authorization.

## Scope re-check

Before finalizing, compare the diff to the original request. Every changed file should have a defensible causal relationship to the requested outcome or its validation.
