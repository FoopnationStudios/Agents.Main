# Definition of Done

A mutating task is done only when the following are true to the extent applicable.

## Outcome

- The requested behavior or artifact exists.
- Acceptance criteria from the user are satisfied.
- No known material requirement was silently dropped.

## Scope

- The diff is causally related to the request or its validation.
- Unrelated refactors, formatting churn, dependency updates, and cleanup are absent.
- Existing user work was preserved.

## Correctness

- Applicable project validation from `.ai/PROJECT.md` ran successfully, or skipped/unavailable checks are explicitly reported.
- Failures were investigated rather than hidden by weakening tests or controls.
- Edge cases introduced by the change were considered at the appropriate risk tier.

## Security

- No secret or sensitive data was introduced or exposed.
- New dependencies, permissions, network access, or privileged behavior were justified and reviewed.
- No governance or security control was weakened incidentally.

## Repository quality

- `python3 scripts/postflight.py` passes when the environment permits it.
- The final diff was reviewed for merge markers, accidental generated artifacts, unsafe workflow changes, and unexpected files.
- Documentation/current status was updated when the change makes existing operational documentation materially false.

## Handoff

The final report distinguishes verified facts from assumptions and includes actual validation evidence. A task with unrun required validation may be implementation-complete but must not be described as fully verified.
