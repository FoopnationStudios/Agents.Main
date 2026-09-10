# Project Source of Truth

Initialization-State: BASELINE
Repository: FoopnationStudios/Agents.Main
Primary-Owner: @FoopnationStudios
Governance-Version: 1.0.1

## Purpose

Agents.Main is the canonical reusable governance template for AI-assisted project development. It provides an agent boot process, preflight and postflight controls, anti-drift rules, security boundaries, and GitHub CI policy checks.

## Current lifecycle

Framework baseline. This repository is the template origin, so `Initialization-State: BASELINE` is valid here. Any repository created from this template must change the state to `ACTIVE` and replace the repository and owner fields before its governance check can pass.

## Technology and runtime

- Markdown for policy and project context.
- Python 3 standard library for governance checks.
- GitHub Actions for the repository policy gate.
- No runtime third-party Python dependencies are required by the governance framework.

## Project validation commands

These commands are trusted project documentation for agents. CI does not parse and execute commands from this Markdown file.

- Governance preflight: `python3 scripts/preflight.py`
- Governance tests: `python3 -m unittest discover -s tests -p "test_*.py"`
- Governance postflight: `python3 scripts/postflight.py`
- Application build: N/A for the template origin.
- Application test: N/A for the template origin.
- Lint/type-check: N/A for the template origin.
- Security scan: use repository-native GitHub security features when enabled; no bundled third-party scanner is executed automatically.

## Non-negotiable constraints

- The root `AGENTS.md` remains a short routing layer, not an encyclopedia.
- The control plane must remain understandable to a non-expert project owner.
- CI must not execute arbitrary shell commands extracted from editable Markdown.
- External GitHub Actions must be pinned to full commit SHAs.
- The default governance workflow must run with read-only repository permissions and no project secrets.
- Framework defaults must be secure enough for public repositories and adaptable to private repositories.

## Protected/high-risk surfaces

Treat these as high-risk unless the requested task clearly says otherwise:

- authentication and authorization;
- credentials, tokens, signing, secrets, and environment configuration;
- payments or billing;
- production deployment and release workflows;
- data migrations, destructive data operations, and user/customer data;
- GitHub Actions permissions and event triggers;
- branch/ruleset/security configuration;
- dependency and package-manager changes that alter the supply chain.

## Derived-project initialization

When this template is copied:

1. Set `Initialization-State: ACTIVE`.
2. Set `Repository:` to the exact `owner/name` value.
3. Set `Primary-Owner:` to the responsible GitHub user or team.
4. Update `.github/CODEOWNERS`.
5. Replace this purpose/lifecycle/technology section with project facts.
6. Add real setup, build, test, lint, type-check, security, and run commands.
7. Update `.ai/ARCHITECTURE.md` and `.ai/STATUS.md`.
8. Run the preflight and postflight scripts.
9. Configure repository rules and security settings before treating `main` as protected production source of truth.
