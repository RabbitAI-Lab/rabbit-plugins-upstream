---
name: instagram-api
description: Read public Instagram data: profiles (followers, bio, business contact), a profile's posts, reels and story highlights, one post's details, reels by audio, places and the posts at a place, and Instagram search, through the SocialAPIs REST API. Use for influencer or creator research, competitor monitoring, engagement analysis, or code that reads public Instagram without the Graph API.
---

# Instagram API (SocialAPIs)

Public Instagram profiles, posts, reels, highlights and places as JSON. One API key, no Instagram login, no Graph API app.

- Website: https://socialapis.io · this API: https://socialapis.io/api-sources/instagram-profile-details
- Free API key: https://socialapis.io/auth/signup (200 credits a month, no card)
- Free Instagram follower count, no signup: https://socialapis.io/tools/instagram-follower-count
- Every parameter: [references/endpoints.md](references/endpoints.md) · OpenAPI: https://socialapis.io/openapi.json · llms.txt: https://socialapis.io/llms.txt

## Setup

1. The user needs an API key from https://socialapis.io/dashboard.
2. Read it from the environment, `SOCIALAPIS_API_KEY`. **Never** hard-code it, print it, or ask the user to paste it into the chat. If it is missing, tell the user to set it.
3. Send it in the **`x-api-token` header**, never in the URL.

If SocialAPIs MCP tools are available in this session (`facebook_page`, `facebook_ads`, `instagram_profile`, …), use them instead of raw HTTP. Hosted MCP server: `https://mcp.socialapis.io/mcp`.

## Making a call

```bash
curl -s -H "x-api-token: $SOCIALAPIS_API_KEY" \
  "https://api.socialapis.io/instagram/profile/details?username=nike"
```

```python
import os, requests

r = requests.get(
    "https://api.socialapis.io/instagram/profile/details",
    params={"username": "nike"},
    headers={"x-api-token": os.environ["SOCIALAPIS_API_KEY"]},
    timeout=120,
)
r.raise_for_status()
data = r.json()
```

SDKs: Python `pip install socialapis-sdk`, JavaScript `npm install socialapis-sdk`, PHP `composer require socialapishub/socialapis`.

## Endpoints

All `GET`, base URL `https://api.socialapis.io`. Each link opens the endpoint's page with a live example.

| Endpoint | What it returns | Credits |
|---|---|---|
| [`/instagram/user/id`](https://socialapis.io/api-sources/instagram-user-id) | Resolve an Instagram username or profile URL to its two IDs: user_id (long, e.g. | 1 credit per call |
| [`/instagram/profile/details`](https://socialapis.io/api-sources/instagram-profile-details) | Get an Instagram profile by username: bio, follower and post counts, verification status and related profiles. | 1 credit per call |
| [`/instagram/profile/posts`](https://socialapis.io/api-sources/instagram-profile-posts) | List an Instagram profile's posts (photos, videos, carousels) with captions, like and comment counts and media URLs. | 1 credit per call |
| [`/instagram/profile/reels`](https://socialapis.io/api-sources/instagram-profile-reels) | List an Instagram profile's reels with play counts, captions, video URLs and audio metadata. | 1 credit per call |
| [`/instagram/profile/highlights`](https://socialapis.io/api-sources/instagram-profile-highlights) | List an Instagram profile's story highlights with titles, cover images and highlight IDs. | 1 credit per call |
| [`/instagram/highlight/details`](https://socialapis.io/api-sources/instagram-highlight-details) | Get the stories inside one Instagram highlight. | 1 credit per call |
| [`/instagram/post/id`](https://socialapis.io/api-sources/instagram-post-id) | Extract the shortcode from an Instagram post or reel URL. | 1 credit per call |
| [`/instagram/post/details`](https://socialapis.io/api-sources/instagram-post-details) | Get one Instagram post or reel in full: caption, media URLs, engagement counts, timestamp and owner. | 1 credit per call |
| [`/instagram/reels/feed`](https://socialapis.io/api-sources/instagram-reels-feed) | Get Instagram's recommended and trending reels. | 1 credit per call |
| [`/instagram/reels/audio`](https://socialapis.io/api-sources/instagram-reels-by-audio) | List Instagram reels that use a given sound. | 1 credit per call |
| [`/instagram/search`](https://socialapis.io/api-sources/instagram-popular-search) | Search Instagram by keyword and get the top matching users, hashtags and places. | 1 credit per call |
| [`/instagram/location/posts`](https://socialapis.io/api-sources/instagram-location-posts) | List Instagram posts tagged at a location: top posts (tab=ranked) or most recent (tab=recent). | 1 credit per call |
| [`/instagram/location/nearby`](https://socialapis.io/api-sources/instagram-nearby-locations) | List Instagram places near a given location, with name, category, coordinates and post count. | 1 credit per call |

## Things that matter

- **Two IDs per profile.** `/instagram/user/id` returns the long `user_id` (for `/instagram/profile/posts` and `/instagram/profile/reels`) and the short `pk` (for `/instagram/profile/highlights`, which still calls it `user_id`). The wrong one returns nothing.
- One post: `/instagram/post/details?shortcode=<code>`, the code being the part after `/p/` or `/reel/` in its URL.
- Engagement rate = (likes + comments) / followers over the last 9 to 12 posts; use the median per post so one viral post does not decide it.
- **Credits:** the response headers `X-SocialAPIs-Credits-Deducted` and `X-SocialAPIs-Credits-Remaining` say what a call cost. Before a large batch, check `/usage` (free) and tell the user roughly what it will cost.
- **Pagination:** list endpoints return a page plus `end_cursor`; pass it back as `end_cursor` until it is missing or the user has enough.
- **Slow calls:** a call can take up to about 90 seconds. Use a timeout of at least 120 s and don't fire hundreds of calls in parallel (`/usage/limits` shows the plan's rate limit).
- **Errors:** `401` bad or missing key · `403` out of credits or account paused · `429` rate limit, retry with backoff · `502` / `504` the source failed or timed out, retry once later. Failed calls are not charged.

Other SocialAPIs skills: `facebook-pages-api` (Facebook pages, posts and comments), `facebook-ads-library-api` (Meta Ads Library), `facebook-marketplace-api` (Facebook Marketplace), `facebook-groups-api` (public Facebook groups), and `socialapis` for every endpoint at once.
