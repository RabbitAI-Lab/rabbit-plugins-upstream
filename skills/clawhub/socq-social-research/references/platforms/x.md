# X

Generated from SocQ Capability Registry schema `v1-dc091b011267`. Read this file when the request targets X.

## Endpoint selection

| Endpoint | Use for | Input choice | Cost |
| --- | --- | --- | --- |
| [`x/followers-list`](https://docs.socq.ai/api-manual/x/followers-list) | Collect public X follower profiles. | usernames | 0.5 credits/result |
| [`x/following-list`](https://docs.socq.ai/api-manual/x/following-list) | Collect public X followed profiles. | usernames | 0.5 credits/result |
| [`x/post-quotes`](https://docs.socq.ai/api-manual/x/post-quotes) | Collect public quotes of X posts. | urls | 0.5 credits/result |
| [`x/post-replies`](https://docs.socq.ai/api-manual/x/post-replies) | Collect public replies to X posts. | urls | 0.5 credits/result |
| [`x/post-retweeters`](https://docs.socq.ai/api-manual/x/post-retweeters) | Collect public profiles that reposted X posts. | urls | 0.5 credits/result |
| [`x/posts`](https://docs.socq.ai/api-manual/x/posts) | X Posts API | urls | 0.5 credits/result |
| [`x/profiles`](https://docs.socq.ai/api-manual/x/profiles) | X Profiles API | usernames | 0.6 credits/result |
| [`x/search`](https://docs.socq.ai/api-manual/x/search) | X Search API | query | 0.7 credits/result |
| [`x/trends`](https://docs.socq.ai/api-manual/x/trends) | Collect public X trends by location identifier. | woeids | 0.5 credits/result |
| [`x/user-posts`](https://docs.socq.ai/api-manual/x/user-posts) | X User Posts API | usernames | 0.5 credits/result |

## Validated examples

### `x/followers-list`

Typed MCP tool: `socq_x_followers_list`

```json
{
  "usernames": [
    "@X"
  ],
  "results_limit": 200
}
```

### `x/following-list`

Typed MCP tool: `socq_x_following_list`

```json
{
  "usernames": [
    "@X"
  ],
  "results_limit": 200
}
```

### `x/post-quotes`

Typed MCP tool: `socq_x_post_quotes`

```json
{
  "urls": [
    "https://x.com/X/status/1234567890123456789"
  ],
  "results_limit": 20
}
```

### `x/post-replies`

Typed MCP tool: `socq_x_post_replies`

```json
{
  "urls": [
    "https://x.com/X/status/1234567890123456789"
  ],
  "results_limit": 20
}
```

### `x/post-retweeters`

Typed MCP tool: `socq_x_post_retweeters`

```json
{
  "urls": [
    "https://x.com/X/status/1234567890123456789"
  ],
  "results_limit": 100
}
```

### `x/posts`

Typed MCP tool: `socq_x_posts`

```json
{
  "urls": [
    "https://x.com/X/status/1234567890123456789"
  ]
}
```

### `x/profiles`

Typed MCP tool: `socq_x_profiles`

```json
{
  "usernames": [
    "@X"
  ]
}
```

### `x/search`

Typed MCP tool: `socq_x_search`

```json
{
  "query": "AI agents"
}
```

### `x/trends`

Typed MCP tool: `socq_x_trends`

```json
{
  "woeids": [
    "1"
  ],
  "results_limit": 100
}
```

### `x/user-posts`

Typed MCP tool: `socq_x_user_posts`

```json
{
  "usernames": [
    "@X"
  ]
}
```
