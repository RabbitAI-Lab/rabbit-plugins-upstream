# AnySearch Interface Specification (for AI Agent)

## Protocol
- Endpoint: POST https://api.anysearch.com/mcp
- Format: JSON-RPC 2.0, method = "tools/call"
- Auth: Header "Authorization: Bearer <API_KEY>" (optional, anonymous has lower rate limits)

## CLI Invocation ({{LANG_NAME}})

```
{{LANG_INVOKE}} <command> [options]
```

## Available Commands

### 1. search — Single query search
Two modes: general (omit --domain) and vertical (requires --domain + --sub_domain).

| Option | Type | Required | Description |
|--------|------|----------|-------------|
| query | string | YES | Search query (positional). Vertical search MUST follow query_format from list_domains |
| --domain, -d | string | no | Vertical domain: {{DOMAINS_SPACE}} |
| --sub_domain, -s | string | no | Sub-domain routing key (e.g. finance.us_stock). REQUIRED for vertical search |
| --sub_domain_params | JSON | no | Extra params per sub_domain schema from list_domains |
| --content_types, -t | string | no | Comma-separated or JSON array: {{CONTENT_TYPES_SPACE}} |
| --zone, -z | string | no | cn / intl. Required when list_domains marks zone=CN |
| --max_results, -m | int | no | 1-100, default 10 |
| --freshness, -f | string | no | day / week / month / year |

### 2. list_domains — Query vertical domain directory
MUST be called before vertical search to discover available sub_domains and query formats.

| Option | Type | Required | Description |
|--------|------|----------|-------------|
| --domain | string | choose one | Single domain to query |
| --domains | string | choose one | Batch up to 5 domains (comma-separated). Takes precedence over --domain |

Returns a Markdown table with columns: domain, sub_domain, description, query_format, params_schema, zone.

**Cache list_domains results per domain within a session. Do NOT call repeatedly.**

### 3. batch_search — Execute 2-5 search queries in parallel
Single failure does not block others; results are merged.

| Option | Type | Required | Description |
|--------|------|----------|-------------|
| --query | string | YES (x1-5) | Repeatable single-query shorthand. Up to 5 |
| --queries, -q | JSON | YES | JSON array of query objects, or @file.json to read from file |

Each query object supports: query (required), domain, sub_domain, content_types, zone, max_results, freshness.

### 4. extract — Fetch full page content as Markdown
Truncated at 50,000 chars. HTML pages only.

| Option | Type | Required | Description |
|--------|------|----------|-------------|
| url | string | YES | Target URL (positional or via --url / -u) |

---

## Decision Flow

```
User query
  |
  +-- Has structured identifiers? (Stock:/CVE:/DOI:/IATA:/patent etc.)
  |     YES -> 1) list_domains --domain X
  |             2) read query_format from result -> construct query accordingly
  |             3) search "<query>" --domain X --sub_domain Y --zone cn
  |
  +-- Multiple independent intents?
  |     YES -> batch_search --query "..." --query "..."
  |
  +-- Need deeper content than snippets?
        YES -> extract "https://example.com/article"

  Otherwise -> search "<general query>"
```

---

## Vertical Search Semantic Constraints

Before performing vertical search, you MUST call list_domains for the target domain
and strictly obey the returned semantic constraints:

1. **query_format**: Describes exactly how to structure the query string for that sub_domain.
   Example: "直接输入股票代码（如 AAPL）、公司名称、货币对（如 EUR_USD）、商品（如 WTICO_USD）"
   -> Pass the raw ticker/name/pair directly, NOT a natural language sentence.

2. **params_schema**: JSON schema for optional extra parameters.
   Example: {"type":"object","properties":{"period":{"type":"string","enum":["1d","1w","1m","3m","1y"]}}}
   -> Pass --sub_domain_params '{"period":"1w"}' to narrow results.

3. **zone**: If "CN", you MUST set --zone cn in the search call.

4. **sub_domain selection**: Match the user's intent to the best sub_domain description.

---

## Scenario Examples

### General web search
```
python3 ~/.openclaw/workspace/skills/anysearch/scripts/anysearch_cli.py search "最新A股市场分析"
```

### Finance vertical search (stock code)
```
python3 ~/.openclaw/workspace/skills/anysearch/scripts/anysearch_cli.py list_domains --domain finance
# Read sub_domain and query_format from result
python3 ~/.openclaw/workspace/skills/anysearch/scripts/anysearch_cli.py search "600458" --domain finance --sub_domain finance.cn_stock --zone cn
```

### Batch search multiple queries
```
python3 ~/.openclaw/workspace/skills/anysearch/scripts/anysearch_cli.py batch_search --queries '[{"query":"A股今日行情"},{"query":"美股昨晚收盘"}]'
```

### Extract full page content
```
python3 ~/.openclaw/workspace/skills/anysearch/scripts/anysearch_cli.py extract --url https://finance.sina.com.cn
```

---

## API Key (Optional)

- Anonymous access: lower rate limits
- With API key: higher rate limits
- Get free key: https://anysearch.com/console/api-keys
- Store in: `~/.openclaw/workspace/skills/anysearch/scripts/.env` as `ANYSEARCH_API_KEY=<key>`