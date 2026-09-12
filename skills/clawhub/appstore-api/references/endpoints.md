# Endpoint examples - ReplyNodes App Store Public Reads (v1)

All operations below are GET-only public reads. Replace `BASE_URL` with your
workspace gateway URL and `API_KEY` with your ReplyNodes fetcher API key.
Never commit real keys.

- All nine reviewed public read methods are exposed as stable capability identifiers in the manifest: app, list, search, developer, privacy, suggest, similar, reviews, and ratings.
- Each route uses the provider method name and exact option names; app-shaped results are normalized into the public App contract and raw provider records never cross the public gateway.
- No availability, uptime, latency, or success-rate figure is claimed; example payloads are illustrative fixtures.
- Package access uses prepaid credits only: one long-lived fetcher key is sent as Authorization: Bearer YOUR_FETCHER_KEY

## Complete endpoint inventory

- `GET /v1/appstore/apps/{id}` (operation `app`)
- `GET /v1/appstore/list` (operation `list`)
- `GET /v1/appstore/search` (operation `search`)
- `GET /v1/appstore/developer` (operation `developer`)
- `GET /v1/appstore/privacy` (operation `privacy`)
- `GET /v1/appstore/suggest` (operation `suggest`)
- `GET /v1/appstore/apps/{id}/similar` (operation `similar`)
- `GET /v1/appstore/reviews` (operation `reviews`)
- `GET /v1/appstore/ratings` (operation `ratings`)

## Generic HTTP (curl)

### GET /v1/appstore/apps/{id} - lookup by track id

```sh
curl -sS \
  -H 'Authorization: Bearer YOUR_FETCHER_KEY' \
  "BASE_URL/v1/appstore/apps/1234567890"
```

### GET /v1/appstore/apps/{id} - lookup by bundle id

```sh
curl -sS \
  -H 'Authorization: Bearer YOUR_FETCHER_KEY' \
  "BASE_URL/v1/appstore/apps/1234567890?appId=com.example.app"
```

### GET /v1/appstore/search

```sh
curl -sS \
  -H 'Authorization: Bearer YOUR_FETCHER_KEY' \
  "BASE_URL/v1/appstore/search?term=example&num=5&country=us&lang=en-us"
```

`num` is forwarded unchanged to the pinned provider; provider-specific bounds apply.

### GET /v1/appstore/apps/{id}/similar

```sh
curl -sS \
  -H 'Authorization: Bearer YOUR_FETCHER_KEY' \
  "BASE_URL/v1/appstore/apps/1234567890/similar"
```

### Sample success payload (normalized v1 shape; illustrative fixture,
### not a captured response)

```json
{
  "data": [
    {
      "id": "ios:app:1234567890",
      "platform": "ios",
      "bundle_id": "com.example.app",
      "title": "Example App",
      "url": "https://apps.example.com/example-app",
      "icon_url": null,
      "description": "An illustrative application used by documentation fixtures.",
      "release_notes": "Documentation fixture release notes.",
      "developer": {
        "name": "Example Developer",
        "id": "ios:developer:987654321"
      },
      "primary_genre": "Productivity",
      "genres": ["Productivity"],
      "content_rating": "4+",
      "languages": ["EN"],
      "version": "1.0.0",
      "size_bytes": null,
      "min_os_version": "15.0",
      "released_at": "2025-03-01T00:00:00Z",
      "updated_at": "2026-07-15T00:00:00Z",
      "rating": { "score": 4.2, "ratings_count": 128, "reviews_count": null },
      "pricing": { "price": null, "currency": null, "free": true },
      "screenshot_urls": []
    }
  ],
  "meta": {
    "request_id": "req-8f14e45fce",
    "contract_version": "v1",
    "generated_at": "2026-08-23T00:00:00Z",
    "availability": "partial",
    "missing_fields": ["*.icon_url", "*.pricing.price", "*.pricing.currency", "*.rating.reviews_count", "*.size_bytes"],
    "detail": "Some fields were omitted by the upstream source."
  }
}
```

`null` means the public source omitted the value; zeros are never fabricated.
`meta.missing_fields` uses dotted `*.paths` that apply to every element of
`data`, reported in a fixed deterministic order.

### Handling errors and quotas

```sh
# 429 example - honor Retry-After before retrying
curl -sS -i \
  -H 'Authorization: Bearer YOUR_FETCHER_KEY' \
  "BASE_URL/v1/appstore/apps/1234567890"
# HTTP/1.1 429 Too Many Requests
# Retry-After: 30
# ...
{"error":{"code":"rate_limited","message":"The upstream quota is exhausted; retry later.","request_id":"req-0f341b6a2c"}}
```

Retry guidance: retry idempotent reads on 502/503 with backoff; treat
400/404 as terminal for the request.

## OpenClaw agents

Install this skill directory into the agent's skills folder so `SKILL.md` and
`llms.txt` are discoverable, then instruct it naturally:

```text
Use the ReplyNodes App Store skill to look up com.example.app, then find
related apps and summarize ratings. Surface meta.availability and null
counters honestly, and respect any 429 Retry-After you receive.
```

The agent resolves BASE_URL/API_KEY from its environment configuration; the
skill text never contains either.

## Hermes-style function calling

Register the nine tools; execute by issuing the mapped HTTPS GET:

```json
[
  {
    "name": "appstore_app",
    "description": "Look up one public App Store application. Look up one public App Store application. Returns the normalized public contract; raw provider records are internal to the runtime boundary and never cross the public gateway.",
    "parameters": {
      "type": "object",
      "properties": {
        "appId": {
          "type": "string",
          "description": "Bundle id fallback."
        },
        "country": {
          "type": "string",
          "description": "Two-letter storefront code."
        },
        "lang": {
          "type": "string",
          "description": "Language code."
        },
        "ratings": {
          "type": "boolean",
          "description": "Include ratings information."
        }
      },
      "required": [],
      "additionalProperties": false
    }
  },
  {
    "name": "appstore_list",
    "description": "List applications from a storefront collection. List applications from a storefront collection. Returns the normalized public contract; raw provider records are internal to the runtime boundary and never cross the public gateway.",
    "parameters": {
      "type": "object",
      "properties": {
        "collection": {
          "type": "string",
          "description": "Provider collection constant."
        },
        "category": {
          "type": "string",
          "description": "Provider category constant."
        },
        "country": {
          "type": "string",
          "description": "Two-letter storefront code."
        },
        "lang": {
          "type": "string",
          "description": "Language code."
        },
        "num": {
          "type": "integer",
          "description": "Number of applications; values outside 1..200 are rejected.",
          "minimum": 1,
          "maximum": 200
        },
        "fullDetail": {
          "type": "boolean",
          "description": "Request detail enrichment."
        }
      },
      "required": [],
      "additionalProperties": false
    }
  },
  {
    "name": "appstore_search",
    "description": "Search public App Store applications by term. Search public App Store applications by term. Returns the normalized public contract; raw provider records are internal to the runtime boundary and never cross the public gateway.",
    "parameters": {
      "type": "object",
      "properties": {
        "term": {
          "type": "string",
          "description": "Search term."
        },
        "num": {
          "type": "integer",
          "description": "Number of results; values outside 1..50 are rejected.",
          "minimum": 1,
          "maximum": 50,
          "default": 20
        },
        "page": {
          "type": "integer",
          "description": "Result page.",
          "minimum": 1,
          "maximum": 200
        },
        "country": {
          "type": "string",
          "description": "Two-letter storefront code."
        },
        "lang": {
          "type": "string",
          "description": "Language code."
        },
        "idsOnly": {
          "type": "boolean",
          "description": "Return ids without detail lookups."
        }
      },
      "required": [
        "term"
      ],
      "additionalProperties": false
    }
  },
  {
    "name": "appstore_developer",
    "description": "List applications by developer. List applications by developer. Returns the normalized public contract; raw provider records are internal to the runtime boundary and never cross the public gateway.",
    "parameters": {
      "type": "object",
      "properties": {
        "devId": {
          "type": "string",
          "description": "public developer identifier."
        },
        "country": {
          "type": "string",
          "description": "Two-letter storefront code."
        },
        "lang": {
          "type": "string",
          "description": "Language code."
        }
      },
      "required": [
        "devId"
      ],
      "additionalProperties": false
    }
  },
  {
    "name": "appstore_privacy",
    "description": "Read public App Store privacy details. Read public App Store privacy details. Returns the normalized public contract; raw provider records are internal to the runtime boundary and never cross the public gateway.",
    "parameters": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string",
          "description": "public application identifier."
        }
      },
      "required": [
        "id"
      ],
      "additionalProperties": false
    }
  },
  {
    "name": "appstore_suggest",
    "description": "Suggest public App Store search terms. Suggest public App Store search terms. Returns the normalized public contract; raw provider records are internal to the runtime boundary and never cross the public gateway.",
    "parameters": {
      "type": "object",
      "properties": {
        "term": {
          "type": "string",
          "description": "Search term."
        }
      },
      "required": [
        "term"
      ],
      "additionalProperties": false
    }
  },
  {
    "name": "appstore_similar",
    "description": "List apps related to an application. List apps related to an application. Returns the normalized public contract; raw provider records are internal to the runtime boundary and never cross the public gateway.",
    "parameters": {
      "type": "object",
      "properties": {
        "appId": {
          "type": "string",
          "description": "Bundle id fallback."
        },
        "country": {
          "type": "string",
          "description": "Two-letter storefront code."
        },
        "lang": {
          "type": "string",
          "description": "Language code."
        }
      },
      "required": [],
      "additionalProperties": false
    }
  },
  {
    "name": "appstore_reviews",
    "description": "Read a page of public app reviews. Read a page of public app reviews. Returns the normalized public contract; raw provider records are internal to the runtime boundary and never cross the public gateway.",
    "parameters": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string",
          "description": "public application identifier; provide this or appId."
        },
        "appId": {
          "type": "string",
          "description": "Bundle id; provide this or id."
        },
        "country": {
          "type": "string",
          "description": "Two-letter storefront code."
        },
        "page": {
          "type": "integer",
          "description": "Review page; values outside 1..10 are rejected.",
          "minimum": 1,
          "maximum": 10
        },
        "sort": {
          "type": "string",
          "description": "Provider review sort constant."
        }
      },
      "required": [],
      "additionalProperties": false
    }
  },
  {
    "name": "appstore_ratings",
    "description": "Read public app ratings. Read public app ratings. Returns the normalized public contract; raw provider records are internal to the runtime boundary and never cross the public gateway.",
    "parameters": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string",
          "description": "public application identifier; provide this or appId."
        },
        "country": {
          "type": "string",
          "description": "Two-letter storefront code."
        },
        "appId": {
          "type": "string",
          "description": "Bundle id; provide this or id."
        }
      },
      "required": [],
      "additionalProperties": false
    }
  }
]
```

## ChatGPT actions (OpenAPI import)

1. Import `openapi/appstore-public-v1.openapi.json` as an action schema.
2. Choose *API key* auth with the *Bearer* scheme and supply the workspace key
   as a saved credential (never paste it into conversations).
3. The three operations appear under their operationIds `get_app`,
   `search_apps`, and `get_similar_apps`, limited to GET requests.

## Claude tool use

Declare the same three tools via native tool-use definitions or point an MCP
client at `mcp/appstore-mcp.schema.json`. Tool results are the raw JSON
responses shown above - surface `meta.availability` and null counters honestly
to the user instead of inventing values.

## MCP agents

Manifest: `mcp/appstore-mcp.schema.json`. It declares transport (HTTP with
bearer authentication), server `instructions`, and three read-only tools
(`appstore_get_app`, `appstore_search_apps`, `appstore_get_similar_apps`)
whose input schemas mirror the capability parameters exactly. Distribution
note inside the manifest marks it as a local artifact; registry publication
is out of scope.

## Error reference

| HTTP | Code | Meaning |
| --- | --- | --- |
| 400 | `invalid_request` | Malformed input such as a bad id, empty term, or out-of-range limit. |
| 404 | `not_found` | Resource does not exist or is not public. |
| 429 | `rate_limited` | Quota exhausted; honor Retry-After before retrying. |
| 502 | `upstream_unavailable` | The public read could not be completed at this time; retry later. |
| 503 | `degraded` | Operation not enabled (dormant or killed) or fail-closed state. |

## Unsupported capabilities (do not improvise)

| Capability | Reason | Notes |
| --- | --- | --- |
| `version_history` | not supported by pinned provider | No version_history method exists in the pinned provider source. |
| `writes_auth_private` | read only policy | Writes and authenticated/private operations are excluded by the domain read-only policy. |

Regenerate this file with `bash ../catalog/generate_appstore.sh` after editing
catalog_appstore.json.
