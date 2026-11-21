# Direct DeepWiki MCP fallback

Use only for a confirmed public GitHub repository when no trusted configured DeepWiki route is usable, or when explicitly testing the public endpoint. Cognition documents a free, unauthenticated public MCP service at `https://mcp.deepwiki.com/mcp` (Streamable HTTP); `/sse` is legacy and being deprecated. The [official guide](https://docs.devin.ai/work-with-devin/deepwiki-mcp) documents MCP, not a separate public REST Q&A endpoint.

## One-shot usage with mcporter

Run from the skill directory in Bash. This uses an ad hoc public endpoint without adding it to a persistent configuration and without initiating OAuth. Never forward gateway credentials or known private repository information.

```bash
source scripts/deepwiki.sh
repo=$(dw_public_repo gohugoio/hugo) || exit 1
route=$(dw_public_route) || exit 1
dw_structure "$route" "$repo" || exit 1
dw_ask "$route" "Which provider is the default Markdown converter? Cite upstream source." "$repo"
```

`dw_public_route` uses `mcporter list https://mcp.deepwiki.com/mcp --schema --json --no-oauth --timeout 8000 --exit-code`. Live schema names can differ from the guide; the tested endpoint advertised unprefixed `ask_wiki_question`, `read_wiki_structure`, and `read_wiki_contents`. Use the exact names and arguments from the live schema.

## MCP clients and private repositories

For a persistent client integration requested separately, follow the [official client examples](https://docs.devin.ai/work-with-devin/deepwiki-mcp): most clients use `url`, Devin Desktop uses `serverUrl`, and Claude Code can use `claude mcp add -s user -t http deepwiki https://mcp.deepwiki.com/mcp`. Use an MCP client for handshake, version negotiation, session headers and streamed responses; a bare `curl tools/call` is not a portable Streamable HTTP example.

Private repo access is a separate [Devin MCP](https://docs.devin.ai/work-with-devin/devin-mcp) workflow requiring an approved Devin account, API key, and repository access. Do not add credentials or switch routes to evade a 401 or 403. Follow the [main workflow’s failure rules](mcporter-workflow.md#troubleshooting).
