# RSS Reader Schema

This generated reference belongs to the adjacent `SKILL.md`. Use it for exact action names, action slugs, parameter summaries, sample parameters, and generated JSON parameter schemas.

Product slug: `rss-reader`

x402 availability: not enabled for this product.

## `read`

Action slug: `read`

Price: `5` credits

Fetch and parse an RSS or Atom feed from a public URL. Returns feed metadata and entries with titles, links, dates, and summaries.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `feed_url` | `string` | yes | The full URL of the RSS or Atom feed to read. |
| `include_raw` | `boolean` | no | Include raw feed parsing metadata (bozo flag and exception details for debugging malformed feeds). |
| `max_items` | `integer` | no | Maximum number of feed entries to return. |
| `timeout_seconds` | `integer` | no | HTTP request timeout in seconds. |

Sample parameters:

```json
{
  "feed_url": "https://example.com",
  "include_raw": false,
  "max_items": 20,
  "timeout_seconds": 20
}
```

Generated JSON parameter schema:

```json
{
  "feed_url": {
    "description": "The full URL of the RSS or Atom feed to read.",
    "required": true,
    "type": "string"
  },
  "include_raw": {
    "default": false,
    "description": "Include raw feed parsing metadata (bozo flag and exception details for debugging malformed feeds).",
    "required": false,
    "type": "boolean"
  },
  "max_items": {
    "default": 20,
    "description": "Maximum number of feed entries to return.",
    "maximum": 200,
    "minimum": 1,
    "required": false,
    "type": "integer"
  },
  "timeout_seconds": {
    "default": 20,
    "description": "HTTP request timeout in seconds.",
    "maximum": 120,
    "minimum": 1,
    "required": false,
    "type": "integer"
  }
}
```
