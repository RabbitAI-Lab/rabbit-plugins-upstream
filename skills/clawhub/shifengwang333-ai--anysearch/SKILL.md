---
name: anysearch
description: Real-time search engine supporting web search, vertical domain search, parallel batch search, and URL content extraction.
version: 2.0.0
authors:
  - AnySearch Team
credentials:
  - name: ANYSEARCH_API_KEY
    required: false
    description: "API key for higher rate limits. Anonymous access available with lower rate limits."
    storage: ".env file, environment variable, or --api_key CLI flag"
---

## Overview

AnySearch is a unified real-time search service supporting general web search, vertical domain search, parallel batch search, and full-page content extraction. It exposes a single JSON-RPC 2.0 endpoint and requires no MCP server installation.

## Trigger

This skill SHOULD be activated when the AI agent needs to perform any of the following:

1. **Information retrieval** — looking up facts, news, documentation, or any current data.
2. **Fact-checking** — verifying claims, cross-referencing statements.
3. **Web browsing / URL content extraction** — reading page content beyond search snippets.
4. **Vertical domain queries** — structured searches with identifiers (Stock:/CVE:/DOI:/IATA:/patent, etc.).
5. **Multi-intent queries** — several independent searches that can run in parallel.

**Vertical domain rule:** For queries that may belong to a supported domain (finance, academic, travel, health, code, geo, etc.), **always call `list_domains` first** to get the correct `sub_domain` and `query_format` before searching.

## Recommended Entry Point

When this skill is first loaded, the agent MUST run the active CLI's `doc` command to obtain the complete interface specification:

| Runtime | Command |
|---------|---------|
| Python | `python3 ~/.openclaw/workspace/skills/anysearch/scripts/anysearch_cli.py doc` |
| Node.js | `node ~/.openclaw/workspace/skills/anysearch/scripts/anysearch_cli.js doc` |
| Bash/sh | `bash ~/.openclaw/workspace/skills/anysearch/scripts/anysearch_cli.sh doc` |

## Platform Detection & CLI Routing

Priority: Python > Node.js > Shell

## API Key Management

- Anonymous access available (lower rate limits)
- Optional API key: visit https://anysearch.com/console/api-keys
- Key can be stored in `scripts/.env` as `ANYSEARCH_API_KEY=<key>`

## Available Commands

### 1. search — Single query search
```bash
python3 ~/.openclaw/workspace/skills/anysearch/scripts/anysearch_cli.py search "query" [--domain finance] [--sub_domain finance.us_stock] [--zone cn] [--max_results 10] [--freshness week]
```

### 2. list_domains — Query vertical domain directory
```bash
python3 ~/.openclaw/workspace/skills/anysearch/scripts/anysearch_cli.py list_domains --domain finance
```

### 3. batch_search — Execute 2-5 search queries in parallel
```bash
python3 ~/.openclaw/workspace/skills/anysearch/scripts/anysearch_cli.py batch_search --queries '[{"query":"AAPL"},{"query":"GOOG"}]'
```

### 4. extract — Fetch full page content as Markdown
```bash
python3 ~/.openclaw/workspace/skills/anysearch/scripts/anysearch_cli.py extract --url https://example.com
```

## Vertical Domains

Available: code, travel, home, ecommerce, gaming, film, music, finance, academic, legal, business, ip, health, geo, environment, energy

For finance queries (stock codes, financial data), ALWAYS use `--domain finance` with appropriate sub_domain.

## Decision Flow

```
User query
  |
  +-- Has structured identifiers? (Stock:/CVE:/DOI:/IATA:/patent etc.)
  |     YES -> 1) list_domains --domain X
  |             2) read query_format from result
  |             3) search "<query>" --domain X --sub_domain Y
  |
  +-- Multiple independent intents?
  |     YES -> batch_search --query "..." --query "..."
  |
  +-- Need deeper content than snippets?
        YES -> extract "https://example.com/article"

  Otherwise -> search "<general query>"
```