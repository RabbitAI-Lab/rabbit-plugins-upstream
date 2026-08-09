# Threads

Generated from SocQ Capability Registry schema `v1-dc091b011267`. Read this file when the request targets Threads.

## Endpoint selection

| Endpoint | Use for | Input choice | Cost |
| --- | --- | --- | --- |
| [`threads/posts`](https://docs.socq.ai/api-manual/threads/posts) | Threads Posts API | urls | 0.5 credits/result |
| [`threads/profiles`](https://docs.socq.ai/api-manual/threads/profiles) | Threads Profiles API | urls | 0.6 credits/result |
| [`threads/user-posts`](https://docs.socq.ai/api-manual/threads/user-posts) | Threads User Posts API | urls | 0.5 credits/result |

## Validated examples

### `threads/posts`

Typed MCP tool: `socq_threads_posts`

```json
{
  "urls": [
    "https://www.threads.net/@instagram/post/ABC123/"
  ]
}
```

### `threads/profiles`

Typed MCP tool: `socq_threads_profiles`

```json
{
  "urls": [
    "https://www.threads.net/@instagram/"
  ]
}
```

### `threads/user-posts`

Typed MCP tool: `socq_threads_user_posts`

```json
{
  "urls": [
    "https://www.threads.net/@instagram/"
  ]
}
```
