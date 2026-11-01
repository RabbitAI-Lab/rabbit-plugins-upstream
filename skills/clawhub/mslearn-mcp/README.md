# 📘 Microsoft Learn MCP for OpenClaw

Use Microsoft's public [Learn MCP server](https://github.com/MicrosoftDocs/mcp) for current documentation and code samples across Azure, .NET, Microsoft 365, Power Platform, Entra ID, Windows and SQL Server. No API key.

Search first, fetch missing evidence and cite source pages. Supports connected tools, the pinned Microsoft Learn CLI and existing mcporter hosts. Excludes sensitive query data and treats retrieved text as evidence.

## Install

From ClawHub: `openclaw skills install @ricardodpalmeida/mslearn-mcp`. Or copy this folder into your workspace `skills/` directory.

For the native path, register during authorized Gateway maintenance (see `references/mcp-details.md`):

```bash
openclaw mcp add mslearn --url https://learn.microsoft.com/api/mcp --transport streamable-http
openclaw mcp doctor mslearn --probe
```

No API key is needed. Queries and requested documentation URLs are sent to Microsoft; exclude sensitive information.

## Files

`SKILL.md` holds the agent instructions. `references/mcp-details.md` has the tool reference, setup commands for each client and troubleshooting.

## License

[MIT-0](LICENSE) (MIT No Attribution): use, copy, modify and redistribute it for any purpose, with no attribution required. The same license applies on ClawHub.

## More from the author

Made by Ricardo Pacheco Almeida. I write about applied AI, agents and enterprise architecture at [ricbits](https://me.ricbits.cc).

| Skill | What it does |
|-------|--------------|
| [whetstone](https://github.com/Ricardodpalmeida/whetstone) | Reviews consequential code changes with checks proportional to their impact. |
| [LadybugDB openCypher](https://clawhub.ai/ricardodpalmeida/ladybug-opencypher-updated) | Design and query LadybugDB graphs with openCypher, including imports, full-text search and Neo4j query adaptation. |
| [Book Capture for Obsidian](https://clawhub.ai/ricardodpalmeida/book-capture-obsidian) | Turns a cover photo, barcode, ISBN or Goodreads export into linked Obsidian book notes and a library dashboard. |
| [Excalidraw Diagrams for Obsidian](https://clawhub.ai/ricardodpalmeida/excalidraw-diagrams) | Turns boxes and arrows into clean, hand-drawn Excalidraw diagrams for Obsidian or excalidraw.com. |
