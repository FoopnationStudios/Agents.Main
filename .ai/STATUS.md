# Current Operating State

Last-Updated: 2026-09-10
Governance-Version: 1.0.0
State: BASELINE_BOOTSTRAP

## Current objective

Establish Agents.Main as the reusable baseline for future AI-assisted development projects.

## Current priorities

1. Keep the instruction entrypoint compact and deterministic.
2. Make every mutation pass through a documented preflight and postflight.
3. Enforce basic governance integrity in GitHub Actions without executing arbitrary project commands from documentation.
4. Protect the control plane against accidental drift, prompt injection, secret exposure, and unsafe workflow configuration.
5. Keep project-specific customization concentrated in a small number of obvious files.

## Known manual setup outside repository contents

Repository settings are not encoded by these files. The owner must still:

- mark this repository as a GitHub template;
- configure an active ruleset/branch protection for the default branch;
- require the `Governance / policy` check after its first successful run;
- enable the desired secret scanning, push protection, Dependabot/security alerts, code scanning, and private vulnerability reporting features available to the repository;
- review GitHub Actions repository/organization policy, including least privilege and SHA pinning requirements.

## Blockers

None in the repository framework itself. Protection settings remain a manual GitHub administration step.

## Update rule

This file is intentionally operational and may change frequently without a governance version bump unless the change also modifies policy or architecture.
