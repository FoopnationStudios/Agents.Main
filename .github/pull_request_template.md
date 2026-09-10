## Requested outcome

<!-- What user/issue outcome does this PR satisfy? -->

## Scope

<!-- What changed, and what nearby work was intentionally left out? -->

## Preflight

- [ ] Risk tier identified (0 / 1 / 2 / 3)
- [ ] Current behavior/state inspected
- [ ] Protected/high-risk surfaces identified
- [ ] Smallest authorized scope established
- [ ] Validation and rollback/stop conditions considered where relevant

## Validation evidence

<!-- List commands/checks actually run and observed results. Do not write "passed" for checks not executed. -->

- [ ] Applicable project tests/checks completed or explicitly documented as unavailable
- [ ] `python3 scripts/preflight.py` completed
- [ ] `python3 scripts/postflight.py` completed
- [ ] Final diff reviewed for accidental churn and secrets

## Governance/security

- [ ] No unrelated refactor or dependency change
- [ ] No secret/sensitive data introduced
- [ ] No security or CI control weakened to obtain a passing result
- [ ] If the control plane changed, `.ai/CHANGE_CONTROL.md` was followed and version/changelog updated when required

## Residual risk / follow-up

<!-- Remaining uncertainty, skipped checks, owner decisions, or intentionally deferred adjacent work. -->
