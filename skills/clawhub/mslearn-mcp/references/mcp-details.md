# Microsoft Learn MCP reference

Facts below were checked against a live `tools/list` and `tools/call` on 2026-10-25, the MicrosoftDocs/mcp README, the `@microsoft/learn-cli` 1.0.0 help output, mcporter 0.16.0 and the OpenClaw 2026.10 CLI docs. Re-check them when any of those change.

## Server

The endpoint is `https://learn.microsoft.com/api/mcp`, served over Streamable HTTP. It is free, needs no key or sign-in, and only covers public Microsoft Learn content (Azure, .NET, Microsoft 365, Power Platform, Entra ID, Windows, SQL Server, Visual Studio and the SDKs). Opening it in a browser returns HTTP 405; that is expected, because it only answers MCP clients.

Microsoft documents two experimental options, both subject to change.

- `https://learn.microsoft.com/api/mcp?maxTokenBudget=2000` truncates search responses to roughly that many tokens. Use it as the server URL when context is tight.
- `https://learn.microsoft.com/api/mcp/openai-compatible` follows OpenAI's MCP profile for Deep Research models. OpenClaw does not need it.

## Tools

| Tool | Input | Notes |
|------|-------|-------|
| `microsoft_docs_search` | `query` | Semantic search. Returns excerpts with title and URL, from docs pages and from Microsoft Q&A threads. |
| `microsoft_docs_fetch` | `url` | Converts one Learn page to markdown. Pages can be long; fetch only what you need. |
| `microsoft_code_sample_search` | `query`, optional `language` | Official snippets. Set `language` to cut noise. |

Microsoft states that tool names, parameters and responses may change and asks clients to discover tools at runtime instead of hard-coding them. Version 1.0 of this skill listed `locale` and `product` parameters; they do not exist.

## Setting it up

### OpenClaw native MCP

```bash
openclaw mcp add mslearn --url https://learn.microsoft.com/api/mcp --transport streamable-http
openclaw mcp doctor mslearn --probe     # connects and lists the tools
openclaw mcp status --verbose           # shows what is saved, without connecting
openclaw mcp unset mslearn              # removes it
```

`--transport streamable-http` matters: without it OpenClaw assumes SSE. Saving a server proves nothing about reachability, so always run the probe. With Gateway hot reload enabled the next turn picks up the new server; otherwise restart the Gateway. `openclaw mcp tools mslearn --include 'microsoft_docs_search,microsoft_docs_fetch'` limits which tools agents see. All of these change OpenClaw config, so they need the user's approval.

### Microsoft Learn CLI

`@microsoft/learn-cli` is Microsoft's own command-line client for the same server. It needs Node.js 22+ and installs the `mslearn` binary.

```bash
npx -y @microsoft/learn-cli@1.0.0 search "<query>" [--json]
npx -y @microsoft/learn-cli@1.0.0 fetch "<learn url>" [--section "<heading>"] [--max-chars <n>]
npx -y @microsoft/learn-cli@1.0.0 code-search "<query>" [--language <name>] [--json]
npx -y @microsoft/learn-cli@1.0.0 doctor [--format json]
```

The skill pins 1.0.0. Bump it deliberately after reading the package changelog. `mslearn setup` installs Microsoft's own discovery skill for Copilot, Claude Code or Codex; it does not target OpenClaw and is not needed here.

### mcporter

The 1.0 version of this skill used `mcporter config add --name mslearn --url ... --type http`, which mcporter 0.16 does not accept (it registers a server literally named `--name`). The working forms are:

```bash
# No config: call the URL directly
mcporter call https://learn.microsoft.com/api/mcp.microsoft_docs_search query="Azure Functions triggers"

# Persist a named server in ~/.mcporter/mcporter.json
mcporter config add mslearn https://learn.microsoft.com/api/mcp --scope home
mcporter list mslearn --schema
mcporter call mslearn.microsoft_code_sample_search query="Python blob upload" language=python --output json
mcporter config remove mslearn
```

mcporter reads `./config/mcporter.json` in the current project and `~/.mcporter/mcporter.json` for the user, in the `mcpServers` shape. OpenClaw's `openclaw mcp list` does not show mcporter servers and vice versa.

## Microsoft's official skills

The MicrosoftDocs/mcp repository ships `microsoft-docs`, `microsoft-code-reference` and `microsoft-skill-creator` skills for Copilot, Claude Code and Codex. They assume the MCP tools are already wired into the agent. This skill exists because OpenClaw needs the setup paths above; if an OpenClaw build ever ships a Learn connector of its own, prefer that.

## Troubleshooting

| Symptom | Check |
|---------|-------|
| Tools missing after `openclaw mcp add` | Run `openclaw mcp doctor mslearn --probe`. If it passes, the Gateway has not reloaded yet. |
| Probe fails with a connection error | DNS or proxy on the host. `npx -y @microsoft/learn-cli@1.0.0 doctor` gives a clearer diagnosis. |
| `Unknown tool` or invalid parameter | The server changed its schema. Re-list the tools and adapt the call. |
| HTTP 429 or repeated timeouts | Rate limit. Stop, wait, and tell the user; do not loop. |
| HTTP 405 | Something is calling the endpoint like a web page. Use an MCP client or the CLI. |
| Search results off-topic | Make the query more specific: product name, feature, SKU or version. |

## Links

- https://github.com/MicrosoftDocs/mcp (README, issues, skills)
- https://learn.microsoft.com/en-us/training/support/mcp-release-notes
- https://www.npmjs.com/package/@microsoft/learn-cli
- https://modelcontextprotocol.io/
