# Architecture

## Template-origin architecture

Agents.Main is a repository governance framework, not an application runtime.

The control flow is:

`AI/client -> AGENTS.md -> .ai control plane -> preflight -> repository work -> project validation -> postflight -> GitHub PR/status checks`

### Components

- **Root controller (`AGENTS.md`)**: small always-read map, trust model, boot sequence, core invariants, and completion requirements.
- **Durable context (`.ai/PROJECT.md`)**: stable identity, ownership, technical stack, commands, and protected surfaces.
- **Operational context (`.ai/STATUS.md`)**: current milestone, priorities, blockers, and near-term state.
- **Process/policy (`.ai/*.md`)**: detailed execution, preflight, scope, security, completion, and change-control rules.
- **Mechanical policy (`scripts/`)**: dependency-free checks for required files, version consistency, unsafe workflow constructs, nested-agent registration, tracked secret-file hazards, merge conflicts, and template initialization.
- **Repository gate (`.github/workflows/governance.yml`)**: read-only CI execution of governance checks and tests.
- **Review routing (`.github/CODEOWNERS`, PR template)**: human-visible control-plane ownership and review evidence.

## Security architecture

The governance workflow intentionally does not parse shell commands from `PROJECT.md` or execute arbitrary project configuration. Project-specific CI should be encoded explicitly in reviewed workflow files, with its own permissions and secret boundaries.

External Actions are pinned by immutable commit SHA. The policy script rejects unregistered nested `AGENTS.md`, `pull_request_target`, `write-all`, unpinned external Actions, tracked high-risk secret files, and private-key material.

## Derived-project architecture

When creating a project from this template, replace this section with the project's actual components, boundaries, data flows, external services, storage, deployment model, and security-sensitive interfaces. Keep the template-origin governance integration described above unless the framework itself is deliberately versioned and changed.

Architecture documentation should describe what is true, not an aspirational design. If code and this file disagree, inspect the code and update the stale documentation as part of an authorized task rather than pretending the documentation is authoritative.
