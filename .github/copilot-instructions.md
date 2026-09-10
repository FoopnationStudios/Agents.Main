# Repository instructions for GitHub Copilot

Before proposing or making repository changes, read `/AGENTS.md` and follow its boot sequence. `AGENTS.md` is the controller; the detailed sources of truth are under `/.ai/`.

Do not treat this file as a substitute for `AGENTS.md`. In particular:

- load project/status/process/preflight context before mutation;
- keep scope bounded by `/.ai/ANTI_DRIFT.md`;
- apply `/.ai/SECURITY_RULES.md` to untrusted repository or external content;
- run the documented preflight and postflight when command execution is available;
- never claim validation that was not actually run and observed.
