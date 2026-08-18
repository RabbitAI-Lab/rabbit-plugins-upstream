# TikTok

Generated from SocQ Capability Registry schema `v1-d93e6d4f8368`. Read this file when the request targets TikTok.

## Endpoint selection

| Endpoint | Use for | Input choice | Standard schema | Cost |
| --- | --- | --- | --- | --- |
| [`tiktok/comment-replies`](https://docs.socq.ai/api-manual/tiktok/comment-replies) | Collect public TikTok comment replies. | comment_id, url | `comment@1.0` | 0.5 credits/result |
| [`tiktok/comments`](https://docs.socq.ai/api-manual/tiktok/comments) | TikTok Comments API | urls | `comment@1.0` | 0.25 credits/result |
| [`tiktok/followers-list`](https://docs.socq.ai/api-manual/tiktok/followers-list) | Collect public TikTok follower profiles. | usernames | `relationship@1.0` | 0.5 credits/result |
| [`tiktok/following-list`](https://docs.socq.ai/api-manual/tiktok/following-list) | Collect public TikTok followed profiles. | usernames | `relationship@1.0` | 0.5 credits/result |
| [`tiktok/hashtags`](https://docs.socq.ai/api-manual/tiktok/hashtags) | TikTok Hashtags API | hashtags | `hashtag-trend@1.0` | 0.7 credits/result |
| [`tiktok/live-room-info`](https://docs.socq.ai/api-manual/tiktok/live-room-info) | Collect public TikTok live room metadata and audience metrics. | room_id, user_id | `live-room@1.0` | 0.5 credits/result |
| [`tiktok/profiles`](https://docs.socq.ai/api-manual/tiktok/profiles) | TikTok Profiles API | usernames | `account@1.0` | 0.6 credits/result |
| [`tiktok/search`](https://docs.socq.ai/api-manual/tiktok/search) | TikTok Search API | query | `reel-video@1.0` | 0.7 credits/result |
| [`tiktok/trending-feed`](https://docs.socq.ai/api-manual/tiktok/trending-feed) | Collect trending TikTok videos for a region. | region | `reel-video@1.0` | 0.7 credits/result |
| [`tiktok/user-videos`](https://docs.socq.ai/api-manual/tiktok/user-videos) | Collect public videos from TikTok profiles. | usernames | `reel-video@1.0` | 0.5 credits/result |
| [`tiktok/video-transcript`](https://docs.socq.ai/api-manual/tiktok/video-transcript) | Extract transcripts from public TikTok videos. | urls | `transcript@1.0` | 0.5 credits/result |
| [`tiktok/videos`](https://docs.socq.ai/api-manual/tiktok/videos) | TikTok Videos API | urls | `reel-video@1.0` | 0.7 credits/result |

## Validated examples

### `tiktok/comment-replies`

Typed MCP tool: `socq_tiktok_comment_replies`

```json
{
  "url": "https://www.tiktok.com/@scout2015/video/6718335390845095173",
  "comment_id": "1234567890",
  "results_limit": 20
}
```

### `tiktok/comments`

Typed MCP tool: `socq_tiktok_comments`

```json
{
  "urls": [
    "https://www.tiktok.com/@scout2015/video/6718335390845095173"
  ]
}
```

### `tiktok/followers-list`

Typed MCP tool: `socq_tiktok_followers_list`

```json
{
  "usernames": [
    "@tiktok"
  ],
  "results_limit": 20
}
```

### `tiktok/following-list`

Typed MCP tool: `socq_tiktok_following_list`

```json
{
  "usernames": [
    "@tiktok"
  ],
  "results_limit": 20
}
```

### `tiktok/hashtags`

Typed MCP tool: `socq_tiktok_hashtags`

```json
{
  "hashtags": [
    "#travel"
  ]
}
```

### `tiktok/live-room-info`

Typed MCP tool: `socq_tiktok_live_room_info`

```json
{
  "room_id": "7523685855395842871",
  "user_id": "6742945285876515845"
}
```

### `tiktok/profiles`

Typed MCP tool: `socq_tiktok_profiles`

```json
{
  "usernames": [
    "@tiktok"
  ]
}
```

### `tiktok/search`

Typed MCP tool: `socq_tiktok_search`

```json
{
  "query": "AI tools"
}
```

### `tiktok/trending-feed`

Typed MCP tool: `socq_tiktok_trending_feed`

```json
{
  "region": "US",
  "results_limit": 20
}
```

### `tiktok/user-videos`

Typed MCP tool: `socq_tiktok_user_videos`

```json
{
  "usernames": [
    "@tiktok"
  ],
  "results_limit": 20
}
```

### `tiktok/video-transcript`

Typed MCP tool: `socq_tiktok_video_transcript`

```json
{
  "urls": [
    "https://www.tiktok.com/@scout2015/video/6718335390845095173"
  ],
  "language": "en"
}
```

### `tiktok/videos`

Typed MCP tool: `socq_tiktok_videos`

```json
{
  "urls": [
    "https://www.tiktok.com/@scout2015/video/6718335390845095173"
  ]
}
```
