# 📘 Microsoft Learn MCP for OpenClaw

**Stop your agent guessing about Azure. Ground every Microsoft answer in the official docs, with citations.**

An OpenClaw skill that connects agents to Microsoft's free [Learn MCP server](https://github.com/MicrosoftDocs/mcp) for current documentation and official code samples across Azure, .NET, Microsoft 365, Power Platform, Entra ID, Windows and SQL Server.

- **Native MCP, no API key.** One `openclaw mcp add` and the tools show up in every agent, with hot reload and no Gateway restart.
- **Fallbacks that work.** Microsoft's own `@microsoft/learn-cli` (pinned) or mcporter, with commands checked against the current releases.
- **Lean on context.** Search first, fetch at most two pages, trim sections, and cite the learn.microsoft.com URLs.
- **Safe by default.** No secrets in queries, fetched pages treated as data, and no retry loops on rate limits.

## Install

From ClawHub: `openclaw skills install @ricardodpalmeida/mslearn-mcp`. Or copy this folder into your workspace `skills/` directory.

For the native path, register the server once:

```bash
openclaw mcp add mslearn --url https://learn.microsoft.com/api/mcp --transport streamable-http
openclaw mcp doctor mslearn --probe
```

No API key is needed. Queries are sent to Microsoft; nothing else leaves the machine.

## Files

`SKILL.md` holds the agent instructions. `references/mcp-details.md` has the tool reference, setup commands for each client and troubleshooting.

## License

[MIT-0](LICENSE) (MIT No Attribution): use, copy, modify and redistribute it for any purpose, with no attribution required. The same license applies on ClawHub.

## More from the author

Made by Ricardo Pacheco Almeida. I write about applied AI, agents and enterprise architecture at [ricbits](https://me.ricbits.cc).

| Skill | What it does |
|-------|--------------|
| [whetstone](https://github.com/Ricardodpalmeida/whetstone) | Makes a coding agent size every change by risk before it touches anything, then scale the process to match. |
| [LadybugDB openCypher](https://clawhub.ai/ricardodpalmeida/ladybug-opencypher-updated) | Design and query LadybugDB graphs with openCypher, including imports, full-text search and Neo4j query adaptation. |
| [Book Capture for Obsidian](https://clawhub.ai/ricardodpalmeida/book-capture-obsidian) | Turns a cover photo, barcode, ISBN or Goodreads export into linked Obsidian book notes and a library dashboard. |
| [Excalidraw Diagrams for Obsidian](https://clawhub.ai/ricardodpalmeida/excalidraw-diagrams) | Turns boxes and arrows into clean, hand-drawn Excalidraw diagrams for Obsidian or excalidraw.com. |
