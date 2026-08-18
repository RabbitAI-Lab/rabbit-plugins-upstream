# SEO

Generated from SocQ Capability Registry schema `v1-d93e6d4f8368`. Read this file when the request targets SEO.

## Endpoint selection

| Endpoint | Use for | Input choice | Standard schema | Cost |
| --- | --- | --- | --- | --- |
| [`seo/google-organic-serp`](https://docs.socq.ai/api-manual/seo/google-organic-serp) | Retrieve live organic search results. | query | `serp-result@1.0` | 0.1 credits/result |
| [`seo/keyword-difficulty`](https://docs.socq.ai/api-manual/seo/keyword-difficulty) | Calculate ranking difficulty for each input keyword. | keywords | `seo-keyword@1.0` | 0.1 credits/input |
| [`seo/keyword-overview`](https://docs.socq.ai/api-manual/seo/keyword-overview) | Return combined metrics for each input keyword. | keywords | `seo-keyword@1.0` | 0.15 credits/input |
| [`seo/keyword-search-volume`](https://docs.socq.ai/api-manual/seo/keyword-search-volume) | Batch search volume, CPC, competition, and monthly trends. | keywords | `seo-keyword@1.0` | 24 credits/request |
| [`seo/keyword-suggestions`](https://docs.socq.ai/api-manual/seo/keyword-suggestions) | Find long-tail terms containing a seed keyword. | query | `seo-keyword@1.0` | 0.1 credits/result |
| [`seo/keywords-for-site`](https://docs.socq.ai/api-manual/seo/keywords-for-site) | Generate keywords relevant to a website. | target | `seo-keyword@1.0` | 0.1 credits/result |
| [`seo/ranked-keywords`](https://docs.socq.ai/api-manual/seo/ranked-keywords) | Find keywords already ranked by a domain or page. | target | `seo-keyword@1.0` | 0.1 credits/result |
| [`seo/related-keywords`](https://docs.socq.ai/api-manual/seo/related-keywords) | Find semantically and lexically related keywords. | query | `seo-keyword@1.0` | 0.1 credits/result |
| [`seo/relevant-pages`](https://docs.socq.ai/api-manual/seo/relevant-pages) | Find pages with measurable SEO value. | target | `serp-result@1.0` | 0.15 credits/result |
| [`seo/search-intent`](https://docs.socq.ai/api-manual/seo/search-intent) | Classify the intent of each input keyword. | keywords | `seo-keyword@1.0` | 0.1 credits/input |

## Validated examples

### `seo/google-organic-serp`

Typed MCP tool: `socq_seo_google_organic_serp`

```json
{
  "query": "keyword research",
  "location_code": 2840,
  "language_code": "en",
  "results_limit": 10
}
```

### `seo/keyword-difficulty`

Typed MCP tool: `socq_seo_keyword_difficulty`

```json
{
  "keywords": [
    "keyword research"
  ],
  "location_code": 2840,
  "language_code": "en"
}
```

### `seo/keyword-overview`

Typed MCP tool: `socq_seo_keyword_overview`

```json
{
  "keywords": [
    "keyword research"
  ],
  "location_code": 2840,
  "language_code": "en"
}
```

### `seo/keyword-search-volume`

Typed MCP tool: `socq_seo_keyword_search_volume`

```json
{
  "keywords": [
    "keyword research"
  ],
  "location_code": 2840,
  "language_code": "en"
}
```

### `seo/keyword-suggestions`

Typed MCP tool: `socq_seo_keyword_suggestions`

```json
{
  "query": "keyword research",
  "location_code": 2840,
  "language_code": "en",
  "results_limit": 100
}
```

### `seo/keywords-for-site`

Typed MCP tool: `socq_seo_keywords_for_site`

```json
{
  "target": "example.com",
  "location_code": 2840,
  "language_code": "en",
  "results_limit": 100
}
```

### `seo/ranked-keywords`

Typed MCP tool: `socq_seo_ranked_keywords`

```json
{
  "target": "example.com",
  "location_code": 2840,
  "language_code": "en",
  "results_limit": 100
}
```

### `seo/related-keywords`

Typed MCP tool: `socq_seo_related_keywords`

```json
{
  "query": "keyword research",
  "location_code": 2840,
  "language_code": "en",
  "results_limit": 100
}
```

### `seo/relevant-pages`

Typed MCP tool: `socq_seo_relevant_pages`

```json
{
  "target": "example.com",
  "location_code": 2840,
  "language_code": "en",
  "results_limit": 100
}
```

### `seo/search-intent`

Typed MCP tool: `socq_seo_search_intent`

```json
{
  "keywords": [
    "keyword research"
  ],
  "language_code": "en"
}
```
