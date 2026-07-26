# DeepWiki MCP API Fallback

Use this reference only when the preferred `mcporter` workflow is unavailable, when validating a direct DeepWiki MCP integration, or when the task specifically asks whether DeepWiki has an API.

## API Status

The official Devin documentation exposes DeepWiki programmatic access through a remote MCP server. No separate official REST API for DeepWiki public repository Q&A was found in the provided official docs.

Use the official MCP endpoint:

- Base server URL: `https://mcp.deepwiki.com/`
- Recommended Streamable HTTP endpoint: `https://mcp.deepwiki.com/mcp`
- Legacy SSE endpoint: `https://mcp.deepwiki.com/sse`

The public DeepWiki MCP server is free and does not require authentication for public repositories.

Search found third-party projects that describe unrelated or unofficial DeepWiki-style APIs. Do not treat them as official Cognition/Devin API documentation unless the user explicitly asks to inspect those projects.

## Client Config

Most MCP clients:

```json
{
  "mcpServers": {
    "deepwiki": {
      "url": "https://mcp.deepwiki.com/mcp"
    }
  }
}
```

Devin Desktop uses `serverUrl`:

```json
{
  "mcpServers": {
    "deepwiki": {
      "serverUrl": "https://mcp.deepwiki.com/mcp"
    }
  }
}
```

Claude Code:

```bash
claude mcp add -s user -t http deepwiki https://mcp.deepwiki.com/mcp
```

## Direct MCP JSON-RPC

Use direct MCP only for integration debugging. Prefer `mcporter` for normal work.

List tools:

```bash
curl --location "https://mcp.deepwiki.com/mcp" \
  --header "content-type: application/json" \
  --header "accept: application/json, text/event-stream" \
  --data '{
    "method": "tools/list",
    "jsonrpc": "2.0",
    "id": 1
  }'
```

Call `read_wiki_structure`:

```bash
curl --location "https://mcp.deepwiki.com/mcp" \
  --header "content-type: application/json" \
  --header "accept: application/json, text/event-stream" \
  --data "$(jq -nc --arg repo "$repo_name" '{
    method: "tools/call",
    params: {name: "read_wiki_structure", arguments: {repoName: $repo}},
    jsonrpc: "2.0",
    id: 2
  }')"
```

Call `ask_question`:

```bash
curl --location "https://mcp.deepwiki.com/mcp" \
  --header "content-type: application/json" \
  --header "accept: application/json, text/event-stream" \
  --data "$(jq -nc --arg repo "$repo_name" --arg question "What is the high level architecture?" '{
    method: "tools/call",
    params: {name: "ask_question", arguments: {repoName: $repo, question: $question}},
    jsonrpc: "2.0",
    id: 3
  }')"
```

## MCP Equivalent Through mcporter

After Server Discovery in `mcporter-workflow.md` selected `$deepwiki_server`:

```bash
mcporter call "$deepwiki_server.DeepWiki-read_wiki_structure" \
  --args "$(jq -nc --arg repo "$repo_name" '{repoName: $repo}')" \
  --output json

mcporter call "$deepwiki_server.DeepWiki-ask_question" \
  --args "$(jq -nc --arg repo "$repo_name" --arg question "What is the high level architecture?" '{repoName: $repo, question: $question}')" \
  --output json
```

## Private Repositories

The public DeepWiki MCP server is for public repositories. For private repositories, the official docs say to use a Devin account and the Devin MCP server with a Devin API key.

Do not attempt to send private repository data to public DeepWiki MCP without explicit user approval and a confirmed safe integration path.

## Official References

- DeepWiki: `https://deepwiki.com/`
- Devin DeepWiki docs: `https://docs.devin.ai/work-with-devin/deepwiki`
- DeepWiki MCP docs: `https://docs.devin.ai/work-with-devin/deepwiki-mcp`
