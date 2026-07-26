# zAI Web Search

Search the web using Z.AI (GLM) Web Search API.

## When to use
- User asks to search the web, look something up, or find current information
- You need real-time data not in your training
- User explicitly asks for zAI search

## How to use
Run the search script:

```sh
bash ~/.openclaw/workspace/skills/zai-web-search/zai-search.sh "search query" [count]
```

- `count` is optional, default 5, max 50
- Output is plain text: title, URL, summary for each result

## Requirements
- `ZAI_API_KEY` env var or key file at `~/.openclaw/.zai-key`
- `jq` and `curl` installed

## Notes
- Endpoint: `https://api.z.ai/api/coding/paas/v4/web_search`
- Search engine: `search-prime` (zAI's enhanced search)
