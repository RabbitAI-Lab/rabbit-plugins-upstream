# Instagram API endpoint reference (SocialAPIs)

Base URL: `https://api.socialapis.io` · Auth: header `x-api-token: $SOCIALAPIS_API_KEY` · All endpoints are `GET` with query parameters.

Generated from the full reference in the `socialapis` skill. Machine-readable: https://socialapis.io/openapi.json

### `GET /instagram/user/id`

Docs and live example: https://socialapis.io/api-sources/instagram-user-id

Resolve an Instagram username or profile URL to its two IDs: user_id (long, e.g. 17841401474538262), used by `/instagram/profile/posts` and `/instagram/profile/reels`, and pk (short, e.g. 528817151), used by `/instagram/profile/highlights`. Pricing: 1 credit per call.

| Parameter | Required | Description |
|---|---|---|
| `link` | no | Instagram profile URL |
| `username` | no | Instagram username |

### `GET /instagram/profile/details`

Docs and live example: https://socialapis.io/api-sources/instagram-profile-details

Get an Instagram profile by username: bio, follower and post counts, verification status and related profiles. Pricing: 1 credit per call.

| Parameter | Required | Description |
|---|---|---|
| `username` | yes | Instagram username |
| `link` | no | Instagram profile URL (alternative to username) |

### `GET /instagram/profile/posts`

Docs and live example: https://socialapis.io/api-sources/instagram-profile-posts

List an Instagram profile's posts (photos, videos, carousels) with captions, like and comment counts and media URLs. Pass username (returns more results) or user_id (the long user_id from `/instagram/user/id`, not the pk). Returns an end_cursor for the next page. For reels only, use `/instagram/profile/reels`. Pricing: 1 credit per call.

| Parameter | Required | Description |
|---|---|---|
| `username` | no | Instagram username (recommended — returns more results) |
| `user_id` | no | Long Instagram user ID: user_id from `/instagram/user/id` (e.g. 17841401474538262), not the pk. Alternative to username. |
| `end_cursor` | no | Pagination cursor for next page |

### `GET /instagram/profile/reels`

Docs and live example: https://socialapis.io/api-sources/instagram-profile-reels

List an Instagram profile's reels with play counts, captions, video URLs and audio metadata. Needs the long user_id from `/instagram/user/id` (not the pk). Returns an end_cursor for the next page. Pricing: 1 credit per call.

| Parameter | Required | Description |
|---|---|---|
| `user_id` | yes | Long Instagram user ID: user_id from `/instagram/user/id` (e.g. 17841401474538262), not the pk. |
| `end_cursor` | no | Pagination cursor for next page |

### `GET /instagram/profile/highlights`

Docs and live example: https://socialapis.io/api-sources/instagram-profile-highlights

List an Instagram profile's story highlights with titles, cover images and highlight IDs. Needs the profile's pk from `/instagram/user/id`, passed as user_id (not the long user_id). Use `/instagram/highlight/details` to get the stories in one highlight. Pricing: 1 credit per call.

| Parameter | Required | Description |
|---|---|---|
| `user_id` | yes | The profile's pk from `/instagram/user/id` (e.g. 528817151), not the long user_id. |

### `GET /instagram/highlight/details`

Docs and live example: https://socialapis.io/api-sources/instagram-highlight-details

Get the stories inside one Instagram highlight. Needs a highlight_id from `/instagram/profile/highlights`. Pricing: 1 credit per call.

| Parameter | Required | Description |
|---|---|---|
| `highlight_id` | yes | Highlight ID (from profile highlights endpoint) |

### `GET /instagram/post/id`

Docs and live example: https://socialapis.io/api-sources/instagram-post-id

Extract the shortcode from an Instagram post or reel URL. `/instagram/post/details` needs the shortcode. Pricing: 1 credit per call.

| Parameter | Required | Description |
|---|---|---|
| `link` | yes | Instagram post URL |

### `GET /instagram/post/details`

Docs and live example: https://socialapis.io/api-sources/instagram-post-details

Get one Instagram post or reel in full: caption, media URLs, engagement counts, timestamp and owner. Needs the shortcode (the part after /p/ or /reel/ in the URL, or from `/instagram/post/id`). Pricing: 1 credit per call.

| Parameter | Required | Description |
|---|---|---|
| `shortcode` | yes | Instagram post shortcode (e.g., DMF-GjGO0-q) |

### `GET /instagram/reels/feed`

Docs and live example: https://socialapis.io/api-sources/instagram-reels-feed

Get Instagram's recommended and trending reels. Pass clips_media_id from a previous result to continue the feed or get similar reels by the same author. Not tied to a user; for one profile's reels use `/instagram/profile/reels`. Pricing: 1 credit per call.

| Parameter | Required | Description |
|---|---|---|
| `clips_media_id` | no | Clip media ID for chaining/pagination (from previous response) |

### `GET /instagram/reels/audio`

Docs and live example: https://socialapis.io/api-sources/instagram-reels-by-audio

List Instagram reels that use a given sound. Needs the audio_id (music/audio cluster ID) found in reel results' audio metadata. Pass max_id from the previous response for the next page. Pricing: 1 credit per call.

| Parameter | Required | Description |
|---|---|---|
| `audio_id` | yes | Audio cluster ID (music ID) |
| `max_id` | no | Pagination cursor for next page |

### `GET /instagram/search`

Docs and live example: https://socialapis.io/api-sources/instagram-popular-search

Search Instagram by keyword and get the top matching users, hashtags and places. Use it to find a username, or a place's location_id for `/instagram/location/posts`. Returns an end_cursor for more. Pricing: 1 credit per call.

| Parameter | Required | Description |
|---|---|---|
| `keyword` | yes | Search keyword/query |
| `end_cursor` | no | Pagination cursor for next page |

### `GET /instagram/location/posts`

Docs and live example: https://socialapis.io/api-sources/instagram-location-posts

List Instagram posts tagged at a location: top posts (tab=ranked) or most recent (tab=recent). Needs a location_id, e.g. from a place in `/instagram/search`. Returns an end_cursor for the next page. Pricing: 1 credit per call.

| Parameter | Required | Description |
|---|---|---|
| `location_id` | yes | Instagram location ID |
| `tab` | no | Filter: "recent" or "ranked" |
| `end_cursor` | no | Pagination cursor for next page |

### `GET /instagram/location/nearby`

Docs and live example: https://socialapis.io/api-sources/instagram-nearby-locations

List Instagram places near a given location, with name, category, coordinates and post count. Needs a location_id, e.g. from a place in `/instagram/search`. Pricing: 1 credit per call.

| Parameter | Required | Description |
|---|---|---|
| `location_id` | yes | Instagram location ID |
