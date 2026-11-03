# CLI Usage

Flag catalog and defaults: `references/command-reference.md`. This page records `agy` 1.4.12, checked with `agy --help` and `agy help <subcommand>` on 2026-10-31. The user's installed binary wins. If `agy --version` is not 1.4.12, treat this page as stale and tell the user to upgrade.

## Quick start

```bash
agy --print "Answer this question..."
agy -p "Review this git diff and draft a conventional commit message"
agy --prompt "Prompt..."                 # alias of --print; not interactive
agy --continue                           # or -c; most recent conversation
agy --conversation <id>
agy --prompt-interactive "Summarize this codebase"   # or -i
cat notes.md | agy --prompt-interactive "Analyze"
```

## Local flag notes

- Quote defaults from `agy --help`, not from older docs.
- `--print-timeout` defaults to `0s` on local 1.4.12. `0` waits until the turn ends. The public headless page says `5m`. Print mode only. Example bound: `agy -p "/skill-name ..." --print-timeout 15m`.
- `--input-format stream-json` reads one NDJSON message per line and requires `--output-format stream-json`. Event shape and the mistakes that drop turns: `references/headless.md`.
- `--json-schema` on `stream-json` applies only to the final result.
- `--add-dir` is repeatable and defaults to `[]`. It adds a workspace directory. It does not change the process working directory.
- `--settings` is session-only JSON, inline or a file path. It is never saved.
- There is no `--cwd`. The skill gotchas record that mismatch.

## Subcommands

`agy plugins` aliases `agy plugin`. `agy agents` and `agy agent` both list agents and take no flags. Version is `agy --version`. `agy version` is not a subcommand and exits with an error.

- `agy install`: paths and shell settings. `--dir <path>` sets a custom PATH directory. `--skip-aliases` skips alias purging. `--skip-path` skips PATH appending.
- `agy plugin`: `list [--json]`; `import [gemini|claude]`; `install <target>` including `plugin[@marketplace]`; `uninstall <name>`; `enable <name>`; `disable <name>`; `validate [path] [--strict] [--json]`; `link <marketplace> <target>`.
- `agy mcp`: flags go before `<name>`. `add [--type stdio|http] [--env KEY=value] [--header "Key: Value"] <name> <command-or-url> [args...]`. Short forms: `-e`, `-H`, `-t`. HTTP URLs are detected, so `--type` is usually unnecessary. Put `--` before a command or arg that starts with `-`. Also `remove`, `enable`, `disable`, `list`.
- `agy remote-control`: `start [--name <instance>] [--session]`, `status`, `stop`. `--session` is login-scoped: it stops at logout and does not start at boot.
- `agy mic-serve [--addr <host:port>]`: default `127.0.0.1:4713`. Keep it on loopback.
- `agy models` and `agy changelog`: no extra flags.
- `agy update`: local 1.4.12 accepts neither `-h` nor `--help`. It prints `Usage of update:` and exits.

## Install

OS setup, auth, and enterprise parameters stay in the official install docs.

```bash
curl -fsSL https://antigravity.google/cli/install.sh | bash
```

```powershell
irm https://antigravity.google/cli/install.ps1 | iex
```

```cmd
curl -fsSL https://antigravity.google/cli/install.cmd -o install.cmd && install.cmd && del install.cmd
```

- https://antigravity.google/docs/cli-install
- https://antigravity.google/docs/cli-overview
- https://antigravity.google/docs/cli-getting-started
- https://antigravity.google/docs/cli-tutorial

After install, update with `agy update`.

## Which command

- `agy --print`: stdout is enough.
- `agy --prompt-interactive`: live session seeded with context.
- `agy --continue`: only when the latest conversation is acceptable.
- `agy --conversation <id>`: when the session must be reproducible.
- `--add-dir`: extra workspace roots. To run a slash skill in one directory: `cd /path/to/repo && agy -p "/skill-name ..."`.
- Automation: put the verification command in the `agy -p` prompt.
