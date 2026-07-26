---
name: rss-reader
description: "RSS Reader: Parse RSS/Atom feeds. Returns feed metadata and entries with. Use when an agent needs rss reader, aggregating blog posts from multiple sources into a unified content dashboard, monitoring news feeds for keyword mentions or topic alerts in media tracking workflows, pulling podcast episode listings for automated show note generation, tracking competitor blog updates or product announcements for market intelligence, read, feed url, max items through AgentPMT-hosted remote tool calls."
version: 1.0.0
homepage: https://www.agentpmt.com/marketplace/rss-reader
compatibility: "Agent instructions for AgentPMT-hosted remote tool calls. Follow this skill body for supported account, wallet, and setup routes. No local command runtime is declared."
metadata: {"author":"agentpmt","openclaw":{"homepage":"https://www.agentpmt.com/marketplace/rss-reader"}}
---
# RSS Reader

## Freshness
Last updated: `2026-06-24`.

If the current date is more than 7 days after the last updated date, reinstall this skill from skills.sh or ClawHub before relying on endpoints, schemas, setup steps, or examples.

## What This Tool Does
Lightweight feed parsing utility that fetches and extracts structured content from RSS and Atom feeds for content aggregation and monitoring workflows. This function retrieves feed data from any publicly accessible URL using configurable HTTP timeouts up to 120 seconds, then parses the XML content using the feedparser library to extract both feed-level metadata and individual entry details. The response includes comprehensive feed information such as title, link, last updated timestamp, and description, alongside an array of entries containing each item's title, link, publication date, summary, and full content when available. Users can limit results with the max_items parameter, retrieving anywhere from 1 to 200 entries per request to balance completeness with response size. The optional include_raw flag exposes parsing diagnostics including the bozo flag and any exception details, useful for debugging malformed or non-standard feeds. With its straightforward interface and consistent JSON output structure, the RSS Reader provides an efficient bridge between syndicated web content and downstream processing pipelines that need to consume, filter, or aggregate published articles, blog posts, podcasts, or news updates.

## Product Instructions
### RSS Reader

Fetch and parse RSS and Atom feeds from any public URL. Returns structured feed metadata and entries including titles, links, publication dates, and summaries.

---

#### Actions

##### read

Fetch and parse an RSS or Atom feed.

**Required fields:**
- `action` (string): `"read"`
- `feed_url` (string): The full URL of the RSS or Atom feed to read

**Optional fields:**
- `max_items` (integer): Maximum number of feed entries to return. Range: 1-200. Default: 20
- `include_raw` (boolean): Include raw feed parsing metadata (e.g., whether the feed had parsing errors). Default: false
- `timeout_seconds` (integer): HTTP request timeout in seconds. Range: 1-120. Default: 20

**Example — Read a news feed:**
```json
{
  "action": "read",
  "feed_url": "https://feeds.bbci.co.uk/news/rss.xml",
  "max_items": 10
}
```

**Example — Read a blog feed with raw metadata:**
```json
{
  "action": "read",
  "feed_url": "https://blog.example.com/feed",
  "max_items": 5,
  "include_raw": true
}
```

**Response structure:**
```json
{
  "feed": {
    "title": "Feed Title",
    "link": "https://example.com",
    "updated": "2026-03-10T12:00:00Z",
    "description": "Feed description"
  },
  "entries": [
    {
      "title": "Article Title",
      "link": "https://example.com/article",
      "published": "2026-03-10T10:00:00Z",
      "summary": "Brief summary of the article...",
      "content": null
    }
  ],
  "count": 1
}
```

When `include_raw` is true, the response also includes:
```json
{
  "raw": {
    "bozo": false,
    "bozo_exception": null
  }
}
```
A `bozo` value of `true` indicates the feed had XML parsing issues but was still partially parsed.

---

#### Common Workflows

1. **Monitor news sources** — Read feeds from news outlets to get the latest headlines, then filter or summarize entries by title or summary.
2. **Aggregate multiple feeds** — Call `read` multiple times with different feed URLs, then combine and sort entries by publication date.
3. **Validate feed health** — Use `include_raw: true` to check whether a feed has parsing errors before relying on it for automation.
4. **Limit bandwidth usage** — Set a lower `max_items` value (e.g., 5) when you only need the most recent entries, or increase `timeout_seconds` for slow feeds.

---

#### Important Notes

- Only publicly accessible RSS and Atom feed URLs are supported. Feeds behind authentication will fail.
- The `feed_url` must be a direct link to the XML feed, not a webpage that contains a feed link.
- Feeds with malformed XML may still return partial results. Use `include_raw` to detect parsing issues.
- The `content` field in entries may be `null` if the feed only provides summaries.
- Maximum of 200 items can be returned per request.

## When To Use
- Use this skill for `RSS Reader` on AgentPMT.
- Use it when an agent needs this specific tool's behavior, schema, inputs, outputs, and invocation shape.
- Search and activation keywords: rss reader, aggregating blog posts from multiple sources into a unified content dashboard, monitoring news feeds for keyword mentions or topic alerts in media tracking workflows, pulling podcast episode listings for automated show note generation, tracking competitor blog updates or product announcements for market intelligence, read, feed url, max items.
- Supported action names: `read`.

## Use Cases
- Aggregating blog posts from multiple sources into a unified content dashboard
- monitoring news feeds for keyword mentions or topic alerts in media tracking workflows
- pulling podcast episode listings for automated show note generation
- tracking competitor blog updates or product announcements for market intelligence
- populating content queues for social media scheduling automation
- building personalized news digests by combining entries from curated feed lists
- monitoring release notes or changelog feeds for software dependency updates
- extracting publication metadata for citation management or research aggregation
- feeding content pipelines that summarize or categorize incoming articles
- triggering notification workflows when specific publishers release new content

## Categories And Industries
No categories or industry tags are published for this tool.

## Actions And Schema
Complete generated action schema: `./schema.md`.
Supported action count: `1`.
x402 availability: not enabled for this product.

- `read` (action slug: `read`): Fetch and parse an RSS or Atom feed from a public URL. Returns feed metadata and entries with titles, links, dates, and summaries. Price: `5` credits. Parameters: `feed_url`, `include_raw`, `max_items`, `timeout_seconds`.

## Live Schema And Examples
Use the compact schema above for ordinary calls. Before a new production integration, or whenever parameters, enum values, nested objects, outputs, or examples are unclear, fetch live details first.

- Exact schema: call `agentpmt-tool-search-and-execution` with `action: "get_schema"`, and `tool_id: "rss-reader"`.
- Detailed examples: call `agentpmt-tool-search-and-execution` with `action: "get_instructions"` and `tool_id: "rss-reader"`, or call this product with `action: "get_instructions"` when the product tool is already selected.
- Treat returned live schema and instructions as more specific than this generated summary.

MCP schema lookup through the main AgentPMT MCP server:

```json
{
  "method": "tools/call",
  "params": {
    "name": "AgentPMT-Tool-Search-and-Execution",
    "arguments": {
      "action": "get_schema",
      "tool_id": "rss-reader"
    }
  }
}
```

For live examples, keep the same MCP tool and use these arguments:

```json
{
  "action": "get_instructions",
  "tool_id": "rss-reader"
}
```

Authenticated AgentPMT REST schema lookup body:

```json
{
  "name": "agentpmt-tool-search-and-execution",
  "parameters": {
    "action": "get_schema",
    "tool_id": "rss-reader"
  }
}
```

Authenticated AgentPMT REST live examples body:

```json
{
  "name": "agentpmt-tool-search-and-execution",
  "parameters": {
    "action": "get_instructions",
    "tool_id": "rss-reader"
  }
}
```

## Call This Tool
Product slug: `rss-reader`

Marketplace page: https://www.agentpmt.com/marketplace/rss-reader

- AgentPMT account route: first use `../agentpmt-account-mcp-rest-api-setup` to connect the main MCP server or REST API for an Agent Group where this tool is enabled.
- x402 route: not enabled for this product.
- AgentPMT overview: use `../what-is-agentpmt` for marketplace, Agent Group, workflow, MCP, REST, and payment concepts.

If those setup skills are not installed beside this product skill, use the downloads below.

Core AgentPMT setup skills:
- What AgentPMT is: ../what-is-agentpmt
  - ClawHub page: https://clawhub.ai/agentpmt/what-is-agentpmt
  - OpenClaw install: `openclaw skills install what-is-agentpmt`
  - skills.sh install: `npx skills add AgentPMT/agent-skills --skill what-is-agentpmt`
- AgentPMT account MCP/REST setup: ../agentpmt-account-mcp-rest-api-setup
  - ClawHub page: https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup
  - OpenClaw install: `openclaw skills install agentpmt-account-mcp-rest-api-setup`
  - skills.sh install: `npx skills add AgentPMT/agent-skills --skill agentpmt-account-mcp-rest-api-setup`

skills.sh install script:

```bash
npx skills add AgentPMT/agent-skills --skill what-is-agentpmt
npx skills add AgentPMT/agent-skills --skill agentpmt-account-mcp-rest-api-setup
```

MCP call shape after the main AgentPMT MCP server is connected:

```json
{
  "method": "tools/call",
  "params": {
    "name": "RSS-Reader",
    "arguments": {
      "action": "read",
      "feed_url": "https://example.com",
      "include_raw": false,
      "max_items": 20,
      "timeout_seconds": 20
    }
  }
}
```

Use the exact tool name returned by `tools/list`; the name above is the expected readable form.

Authenticated AgentPMT REST call body:

```json
{
  "name": "rss-reader",
  "parameters": {
    "action": "read",
    "feed_url": "https://example.com",
    "include_raw": false,
    "max_items": 20,
    "timeout_seconds": 20
  }
}
```

Use the setup skill for the account connection details before making REST calls.

## Response Handling
- Treat the returned JSON as the source of truth for this tool call.
- If the response includes warnings or correction targets, apply them before retrying.
- If the response includes a `passed` or success-style boolean, use it as the workflow gate.
- If validation fails or the response shape is unclear, call `get_schema` or `get_instructions` before retrying.
- If `read` fails, preserve the request parameters and retry only after fixing schema, auth, or payment errors.

## Security
- Do not place account secrets, wallet private keys, mnemonics, signatures, or payment headers in prompts or logs.
- Keep tool inputs scoped to the minimum content needed for the task.
- Use the setup skills for credential handling; this product skill only defines product-specific behavior.

## AgentPMT Reference
- What AgentPMT is: ../what-is-agentpmt (ClawHub: `what-is-agentpmt`, page: https://clawhub.ai/agentpmt/what-is-agentpmt; skills.sh: `npx skills add AgentPMT/agent-skills --skill what-is-agentpmt`)
- AgentPMT account MCP/REST setup: ../agentpmt-account-mcp-rest-api-setup (ClawHub: `agentpmt-account-mcp-rest-api-setup`, page: https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup; skills.sh: `npx skills add AgentPMT/agent-skills --skill agentpmt-account-mcp-rest-api-setup`)
- Marketplace product: https://www.agentpmt.com/marketplace/rss-reader
- AgentPMT main MCP server: https://api.agentpmt.com/mcp/
- AgentPMT REST invoke endpoint: https://api.agentpmt.com/products/purchase
