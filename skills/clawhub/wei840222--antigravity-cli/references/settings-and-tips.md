# Settings and Tips

Source: <https://antigravity.google/docs/cli/using/>. Key names and defaults: `references/command-reference.md`. Prompt composition: `references/tui.md`.

## Precedence

- Disk: `~/.gemini/antigravity-cli/settings.json`.
- `/config` or `/settings` saves the selection immediately and returns to the list.
- Launch flags such as `--sandbox` and `--dangerously-skip-permissions` override the session. The menu names the source, for example sandbox mode overridden by `--sandbox`. The disk edit remains, but this session keeps the flag until restart.
- Local 1.4.12 `--settings` is session-only JSON, inline or a file. It is never saved. The public using page does not list it.

## Prompt tips not in the keybinding table

| Action | How |
| --- | --- |
| Clear prompt box | `Esc Esc`, when nothing is streaming |
| Shell command from prompt | Leading `!` |
| List slash commands | `?` |
| Quiet tool calls | Verbosity `low` in `/config` |
| Resume after exit | CLI prints the exact resume command |

`@`, `/rewind`, `/fork`, `/clear`, `/resume`, and `/permissions` are in `references/command-reference.md`.

## Custom keybindings

File: `~/.gemini/antigravity-cli/keybindings.json`. Edit with `/keybindings`, or edit JSON. Delete the file to reset. One action can map to several keys. An empty list disables that action. A malformed file keeps valid actions and uses defaults for broken ones.

This is the customizable set. `references/command-reference.md` wins on command behavior.

| Action | Keys |
| --- | --- |
| Clear screen | `Ctrl+L` |
| Submit | `Enter` |
| Cancel | `Ctrl+C`, `Esc` |
| Exit | `Ctrl+D` |
| Suspend | `Ctrl+Z` |
| Edit proposed command | `e` |
| Decline / approve command | `n` / `y` |
| External editor | `Ctrl+G` |
| Paste | `Ctrl+V` |
| Redo | `Ctrl+Shift+Z` |
| Undo | `Ctrl+_`, `Ctrl+Shift+-` |
| Yank | `Ctrl+Y` |
| Down / up | `Down` / `Up` |
| Bottom / top | `Ctrl+End` / `Ctrl+Home` |
| Cursor left / right | `Left` / `Right` |
| Page down / up | `PgDn` or `Shift+Down`; `PgUp` or `Shift+Up` |
| Autofill or focus | `Tab` |
| Newline | `Alt+Enter`, `Ctrl+J`, `Shift+Enter` |
