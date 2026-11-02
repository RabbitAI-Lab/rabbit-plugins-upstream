# Configuration and Platform

## Surfaces

Antigravity CLI is the terminal TUI: keyboard iteration, SSH, tmux, multiplexers, low overhead. Antigravity 2.0 is the desktop IDE: visual orchestration, multi-panel management, richer artifact review. Both share the agent harness, so reasoning and tool-use changes apply to both.

Preferences, permissions, and security config synchronize. An active CLI conversation can be exported to 2.0. The main agent decides which tools and permissions a subagent gets, including MCP and file writes.

## Local files

| Purpose | Path |
| --- | --- |
| Settings | `~/.gemini/antigravity-cli/settings.json` |
| Keybindings | `~/.gemini/antigravity-cli/keybindings.json` |
| MCP config | `~/.gemini/antigravity-cli/mcp_config.json` |
| Conversations | `~/.gemini/antigravity-cli/conversations/` |
| History | `~/.gemini/antigravity-cli/history.jsonl` |
| Global skills | `~/.gemini/antigravity-cli/skills/` |
| Workspace skills | `.agents/skills/` |

Edit through `/config` or `/settings`, `/permissions`, `/model`, `/keybindings`, or `/mcp` before editing JSON. Validate JSON syntax before restart. Key types and defaults: `references/command-reference.md`.

The six keys used most often:

- `colorScheme`: `terminal` (default), `light`, `dark`, `tokyo night`, or the solarized and colorblind variants.
- `altScreenMode`: `default`, `always`, or `never`. `never` is settings-only.
- `toolPermission`: `request-review` (default), `proceed-in-sandbox`, `always-proceed`, `strict`.
- `artifactReviewPolicy`: `asks-for-review` (default), `agent-decides`, `always-proceed`. Does not change file-edit approval.
- `enableTerminalSandbox`: default `false`. v1.4.4+: no effect when the sandbox is unavailable.
- `useG1Credits`: default `false`. Billing behavior: `references/credits.md`.

## Auth and first launch

First launch asks for color scheme, rendering mode, and workspace trust. Auth uses Apple Keychain or Linux Secret Service when available. Browser OAuth is the fallback. SSH can use manual URL auth: print ***, open it in a browser, paste the code back. Exit prints the resume command, `agy --continue` or `agy --conversation <id>`.

## Plugins, skills, hooks, MCP

Plugin root: `~/.gemini/antigravity-cli/plugins/<plugin_name>/`. Contents can include `plugin.json`, `mcp_config.json`, `hooks.json`, `skills/`, `agents/`, and `rules/`.

`agy plugin` (alias `agy plugins`) lists, installs, enables, disables, validates, and uninstalls plugins. Skills become TUI slash commands. `/hooks` shows pre-flight and post-generation checks.

MCP files: global `~/.gemini/antigravity-cli/mcp_config.json`, workspace `.agents/mcp_config.json`. The migration page instead names global `~/.gemini/config/mcp_config.json`. Confirm the file on disk before editing. `/mcp` shows status, reloads config, and shows connection logs. Remote SSE or websocket key rename: `references/gcli-migration.md`.

## Migration and docs

Gemini CLI import, skill-path changes, and the MCP path conflict are in `references/gcli-migration.md`. Load that page only when the user explicitly asks to migrate.

Current pages behind the local references:

- https://antigravity.google/docs/cli/reference/
- https://antigravity.google/docs/cli/using/
- https://antigravity.google/docs/cli/troubleshooting/
- https://antigravity.google/docs/cli/best-practices/
- https://antigravity.google/docs/cli/credits/

Older short URLs:

- https://antigravity.google/docs/cli-reference
- https://antigravity.google/docs/cli-features
- https://antigravity.google/docs/cli-using
- https://antigravity.google/docs/cli-prompting
- https://antigravity.google/docs/cli-artifacts
- https://antigravity.google/docs/cli-plugins
- https://antigravity.google/docs/cli-permissions
- https://antigravity.google/docs/cli-sandbox
- https://antigravity.google/docs/cli-best-practices
