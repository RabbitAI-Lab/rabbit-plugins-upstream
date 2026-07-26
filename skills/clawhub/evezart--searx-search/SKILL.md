# SearXNG Local Search Skill

## Overview

Query a local SearXNG instance for privacy-first web searches. Returns JSON results directly—no tracking, no external API keys.

## Endpoint

```
http://localhost:8888/search?q=<query>&format=json
```

## Usage

### Basic search

```bash
curl -s "http://localhost:8888/search?q=python+async+http&format=json"
```

### With categories

```bash
curl -s "http://localhost:8888/search?q=postgres+backups&format=json&categories=it"
```

Common categories: `general`, `images`, `videos`, `news`, `music`, `it`, `science`, `files`, `social media`.

### With language

```bash
curl -s "http://localhost:8888/search?q=recettes+fran%C3%A7aises&format=json&language=fr"
```

### With pagination

```bash
curl -s "http://localhost:8888/search?q=linux+kernel&format=json&page=2"
```

### Parse results with jq

```bash
curl -s "http://localhost:8888/search?q=terraform+aws&format=json" | jq '.results[:5] | .[] | {title, url, content}'
```

### Get just titles and URLs

```bash
curl -s "http://localhost:8888/search?q=rust+tutorial&format=json" | jq -r '.results[] | "\(.title)\n\(.url)\n"'
```

## Response Format

```json
{
  "query": "search terms",
  "number_of_results": 42,
  "results": [
    {
      "url": "https://example.com/page",
      "title": "Page Title",
      "content": "Snippet of page content...",
      "engine": "google",
      "score": 1.5,
      "category": "general"
    }
  ],
  "suggestions": ["related search 1", "related search 2"],
  "infoboxes": []
}
```

## Parameters

| Parameter    | Description                            | Example              |
|-------------|----------------------------------------|----------------------|
| `q`         | Search query (URL-encoded)             | `q=python+requests`  |
| `format`    | Always `json`                          | `format=json`        |
| `categories`| Filter by category                     | `categories=it`      |
| `language`  | Language code                           | `language=en`        |
| `page`      | Page number (1-based)                  | `page=2`             |
| `time_range`| Time filter: `day`, `week`, `month`, `year` | `time_range=week` |
| `engines`   | Comma-separated engine list             | `engines=google,ddg` |

## Container Management

```bash
# Check if running
docker ps --filter name=searx

# Start if stopped
docker start searx

# Stop
docker stop searx

# Restart
docker restart searx

# View logs
docker logs searx

# Re-create (if config changed)
docker stop searx && docker rm searx
docker run -d --name searx -p 8888:8080 -v /tmp/searxng/settings.yml:/etc/searxng/settings.yml:ro searxng/searxng
```

## Tips

- URL-encode the query: replace spaces with `+` or `%20`
- Use `jq` for clean parsing: `jq '.results[:5]'` for top 5
- SearXNG aggregates multiple engines—results may vary by instance config
- If JSON returns 403, ensure `formats: [html, json]` is in `/etc/searxng/settings.yml` under `search:`
