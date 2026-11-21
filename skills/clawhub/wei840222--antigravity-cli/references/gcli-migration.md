# Gemini CLI Migration

Load this page only when the user explicitly asks to migrate from Gemini CLI. Do not load it for ordinary CLI setup, MCP edits, or skill-path questions.

Source: <https://antigravity.google/docs/cli/gcli-migration/>. Current path layout stays in `references/config-platform.md`. Where this page names a different MCP path, it says so.

## First launch

The first `agy` run in a directory with legacy Gemini CLI config detects existing profiles and shows a checklist:

- Choose which extensions and global config to convert.
- Active session tokens move into the OS keyring.
- Visual defaults and rendering buffers map onto the new settings profile.

Manual import, after that checklist or instead of relying on it:

```bash
agy plugin import gemini
```

The command reads legacy local directories and extension manifests. A plugin report marks each block `ok`, `skipped (none detected)`, or converted. Legacy `commands` become skills. `mcpServers` entries move into `mcp_config.json`. `skills` and `agents` are processed when present.

## Rules that stay

Workspace context rules are unchanged. Keep `GEMINI.md` and `AGENTS.md` in the active directory. Global rules stay at `~/.gemini/GEMINI.md`.

## Skills paths

| Scope | Gemini CLI | Antigravity CLI |
| --- | --- | --- |
| Global | `~/.gemini/skills/` | `~/.gemini/skills/` or `~/.gemini/antigravity-cli/skills/` |
| Workspace | `.gemini/skills/` | `.agents/skills/` |

## MCP

Gemini CLI nested servers inside `~/.gemini/settings.json`. Antigravity CLI uses a separate file.

The migration page names:

- Global: `~/.gemini/config/mcp_config.json`
- Workspace: `.agents/mcp_config.json`

`references/config-platform.md` names the global file `~/.gemini/antigravity-cli/mcp_config.json`. Both pages agree on the workspace file. Check the installed machine before editing either global path.

Remote WebSocket or SSE entries change key name. Legacy keys are `url` and `httpUrl`. The current key is `serverUrl`.

```json
{
  "mcpServers": {
    "remote-indexer": {
      "serverUrl": "https://mcp.example.com/sse",
      "env": {
        "AUTH_TOKEN": "***"
      }
    }
  }
}
```

The official sample uses a real-looking token string. Treat that value as a placeholder. Do not copy it into a config.
