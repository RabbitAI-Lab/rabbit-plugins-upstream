# LinkedIn

Generated from SocQ Capability Registry schema `v1-dc091b011267`. Read this file when the request targets LinkedIn.

## Endpoint selection

| Endpoint | Use for | Input choice | Cost |
| --- | --- | --- | --- |
| [`linkedin/companies`](https://docs.socq.ai/api-manual/linkedin/companies) | LinkedIn Companies API | urls | 2 credits/result |
| [`linkedin/jobs`](https://docs.socq.ai/api-manual/linkedin/jobs) | LinkedIn Jobs API | urls | 0.8 credits/result |
| [`linkedin/posts`](https://docs.socq.ai/api-manual/linkedin/posts) | LinkedIn Posts API | urls | 1 credits/result |
| [`linkedin/profiles`](https://docs.socq.ai/api-manual/linkedin/profiles) | LinkedIn Profiles API | urls | 2.5 credits/result |

## Validated examples

### `linkedin/companies`

Typed MCP tool: `socq_linkedin_companies`

```json
{
  "urls": [
    "https://www.linkedin.com/company/microsoft/"
  ]
}
```

### `linkedin/jobs`

Typed MCP tool: `socq_linkedin_jobs`

```json
{
  "urls": [
    "https://www.linkedin.com/jobs/view/1234567890/"
  ]
}
```

### `linkedin/posts`

Typed MCP tool: `socq_linkedin_posts`

```json
{
  "urls": [
    "https://www.linkedin.com/posts/microsoft_ai-activity-1234567890"
  ]
}
```

### `linkedin/profiles`

Typed MCP tool: `socq_linkedin_profiles`

```json
{
  "urls": [
    "https://www.linkedin.com/in/satyanadella/"
  ]
}
```
