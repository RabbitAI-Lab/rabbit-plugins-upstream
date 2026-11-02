---
name: antigravity-cli
description: Use when the user names agy or Antigravity CLI, or wants a one-shot prompt (agy -p), a live TUI, conversation resume, slash commands, keybindings, plugins, settings, sandbox or permissions, artifact review, AI credits, Gemini CLI migration, or hits agy command-not-found, a locked keyring, SSH clipboard paste, or the updater lock. Not for the Antigravity desktop IDE.
metadata:
  openclaw:
    emoji: 🪂
    requires:
      bins: [agy]
---

# Antigravity CLI

Use this skill for Google Antigravity CLI. The binary name is `agy`.

## Default workflow

1. Name the branch: one-shot, live TUI, configuration, artifact review, plugins, troubleshooting, or credits. Load `references/gcli-migration.md` only when the user explicitly asks to migrate from Gemini CLI. Do not load it for ordinary CLI work.
2. One-shot: `agy --print`. For JSON, streaming, stdin turns, or CI exit behavior, load `references/headless.md`. Live session: `agy` or `agy --prompt-interactive`.
3. Before quoting a flag, subcommand, or default, read the installed binary:
   ```bash
   agy --help
   agy --version
   ```
   The installed binary wins over docs and these references. The recorded flags are `agy` 1.4.12. If `agy --version` prints another version, say the notes are for 1.4.12 and tell the user to upgrade before trusting them.
4. Before changing permissions or credit settings, ask the user. This includes `toolPermission`, `enableTerminalSandbox`, permission allow/ask/deny rules, `--sandbox`, `--dangerously-skip-permissions`, and `useG1Credits`. Leave `useG1Credits` off unless the user confirms they want to spend AI credits after plan quota.
5. Change other settings with `/config`, `/permissions`, `/model`, `/keybindings`, or `/mcp`. Edit JSON only when the TUI is unavailable or the user asks for a file change.

## References

Load the one page for the branch. Slash commands, keybindings, startup flags, and `settings.json` keys: `references/command-reference.md`. Other pages point there instead of repeating it.

- `references/cli-usage.md`: one-shot launch, resume, local `agy` 1.4.12 flags, subcommands, plugins, install, update.
- `references/headless.md`: print-mode stdout/stderr, JSON and stream events, stdin turns, permissions, exit status, timeout.
- `references/command-reference.md`: official slash commands, keybindings, flags, settings keys.
- `references/overview-workflows.md`: CLI vs Antigravity 2.0, short workflow.
- `references/best-practices.md`: verify first, explore/plan/execute, mentions, recovery, pipelines.
- `references/tui.md`: prompt composition, media, session steering.
- `references/settings-and-tips.md`: `/config` vs launch flags, prompt tips, `keybindings.json`.
- `references/artifacts.md`: review, approve, reject, media drawer.
- `references/security-permissions.md`: sandbox, rules, presets, risk.
- `references/config-platform.md`: paths, plugins, MCP, skills, auth, SSH, Antigravity 2.0.
- `references/gcli-migration.md`: load only for an explicit Gemini CLI migration. First-run import, skill paths, MCP path conflict, `serverUrl`.
- `references/troubleshooting.md`: PATH, keyring, SSH clipboard, updater lock.
- `references/credits.md`: status-line credits, `/credits`, `/usage`, `useG1Credits`.

## Gotchas

Local lookup does not spell these out. Flag names and defaults stay in the two reference pages above.

- `--prompt` is the non-interactive alias of `--print`.
- `agy` 1.4.12 has no `--cwd`. Launch from the repo. The public best-practices `--cwd` example does not apply. Recheck `agy --help` on any other version.
- `agy plugin` manages plugins. Agent Skills stay in the skill paths.
- Artifact review is a TUI panel. A headless prompt asks for the patch summary or command output.
