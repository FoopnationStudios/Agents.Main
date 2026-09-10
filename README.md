# Agents.Main

Agents.Main is a portable governance framework for AI-assisted software development. It is designed to make repository-aware coding agents load the same project context, run the same preflight, stay inside authorized scope, validate their work, and leave a consistent handoff.

The repository is intentionally framework-first. `AGENTS.md` is the entrypoint and routing layer; the detailed sources of truth live under `.ai/`. This keeps the always-loaded instruction surface small while making the operating rules easy to update as the framework evolves.

## Core task lifecycle

Every mutating task follows the same state machine:

`REQUEST -> LOAD CONTEXT -> PREFLIGHT -> PLAN -> EXECUTE -> VALIDATE -> HANDOFF`

The framework separates instruction from enforcement. Markdown establishes agent behavior; `scripts/preflight.py`, `scripts/postflight.py`, GitHub Actions, CODEOWNERS, and repository rules provide mechanical checks and review gates.

## Use this as a project template

1. Create a repository from this template.
2. Update `.ai/PROJECT.md` and set `Initialization-State: ACTIVE`.
3. Replace the repository and owner values in `.ai/PROJECT.md`.
4. Replace the entries in `.github/CODEOWNERS` with the new repository's actual owner or team.
5. Rewrite the project-specific section of `.ai/ARCHITECTURE.md` and update `.ai/STATUS.md`.
6. Add project-specific build, test, lint, type-check, and security commands to `.ai/PROJECT.md`. These commands are documentation for agents; the governance workflow deliberately does not execute arbitrary commands read from Markdown.
7. Run `python3 scripts/preflight.py` and `python3 scripts/postflight.py`.
8. Configure the GitHub repository protections described below before production work begins.

Derived repositories fail the governance check if they retain this template's initialization state or repository identity.

## Agent entrypoints

OpenAI Codex should discover the root `AGENTS.md` automatically. GitHub Copilot receives `.github/copilot-instructions.md`, which routes it back to `AGENTS.md`.

For an AI client that does not natively discover repository instructions, begin the task with: `Read and follow /AGENTS.md before making changes.` No repository file can technically force an arbitrary external AI client to read it, so this explicit bootstrap remains the compatibility fallback.

## Control plane

- `AGENTS.md` — short root controller and mandatory boot sequence.
- `.ai/PROCESS.md` — canonical task state machine.
- `.ai/PROJECT.md` — project identity, constraints, ownership, and validation commands.
- `.ai/STATUS.md` — current operating state and priorities.
- `.ai/PREFLIGHT.md` — risk classification and checks before mutation.
- `.ai/ANTI_DRIFT.md` — scope discipline and anti-refactor rules.
- `.ai/SECURITY_RULES.md` — prompt-injection, credential, workflow, dependency, and destructive-action rules.
- `.ai/DEFINITION_OF_DONE.md` — completion standard.
- `.ai/CHANGE_CONTROL.md` — how the governance framework itself is changed.
- `scripts/preflight.py` / `scripts/postflight.py` — dependency-free mechanical validation.
- `.github/workflows/governance.yml` — CI policy gate.

See `.ai/README.md` for the complete index.

## Recommended GitHub protections

After the first successful `Governance / policy` run, configure a ruleset for the default branch. At minimum:

- require a pull request before merging;
- require the `Governance / policy` status check;
- require conversation resolution;
- block force pushes and branch deletion;
- require CODEOWNERS review for control-plane changes only when there is an independent trusted reviewer; do not create a self-review deadlock in a solo repository;
- enable secret scanning and push protection when available;
- set GitHub Actions to least-privilege defaults and require actions to be pinned to full commit SHAs when available.

For higher-assurance or production repositories, also consider signed commits, code scanning merge protection, dependency review, environment protection rules, and deployment approvals.

## Security posture

The bundled workflow uses an explicit read-only token, does not receive project secrets, avoids `pull_request_target`, and pins external Actions to immutable commit SHAs. The framework treats source files, comments, issues, fixtures, generated content, logs, and external text as untrusted data rather than instructions.

Do not put credentials, private keys, production secrets, customer data, or privileged environment values in this repository or in agent prompts.

## Updating the framework

The current governance version is stored in `.ai/VERSION`. Governance changes should be isolated, tested, recorded in `.ai/DECISIONS.md` when architectural, and documented in `.ai/CHANGELOG.md`. See `.ai/CHANGE_CONTROL.md` for versioning and review rules.

## License

Agents.Main is released under the MIT License. See `LICENSE` for the full terms.
