# Contributing

Agents.Main uses pull requests as the normal integration path after bootstrap.

Before changing the repository, read `AGENTS.md` and the referenced `.ai` control-plane files. Keep each change focused on one requested outcome. Run the applicable validation documented in `.ai/PROJECT.md`, then run the governance preflight/postflight.

Control-plane changes require `.ai/CHANGE_CONTROL.md`. Do not mix policy weakening, permission expansion, or unrelated refactors into ordinary product work.

For a repository created from this template, complete the initialization steps in `README.md` before relying on the governance status check.

Never contribute real secrets, private keys, production `.env` files, customer data, or privileged logs.
