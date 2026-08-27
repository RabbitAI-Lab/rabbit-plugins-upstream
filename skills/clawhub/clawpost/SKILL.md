---
name: clawpost
description: Post to X (Twitter), LinkedIn, Facebook, TikTok, and Instagram via Claw Post API. Comment on Reddit threads through the user's browser. Search for Facebook groups, join them, and post to them. Use when the user wants to publish social content, reply on Reddit, discover relevant groups, or manage Facebook group membership.
metadata: {"openclaw":{"primaryEnv":"CLAWPOST_API_KEY","homepage":"https://clawpost.net/api-docs","requires":{"env":["CLAWPOST_API_KEY"]}}}
---

# Claw Post

Social posting infrastructure for AI agents. A paired browser extension publishes from the user's real browser session — no API keys to the social platforms needed.

## Why Claw Post

- **Zero credential exposure for social platforms.** No OAuth tokens or social-platform passwords are sent to the agent or to Claw Post for posting. You use one Claw Post API key for API calls only; social sessions stay in the paired Chrome browser.
- **Lower ban risk.** Posts are published through the real browser UI with human-like timing — not via automation-flagged API endpoints or headless browsers.
- **Multi-platform, one API.** X, LinkedIn, Facebook (feed and groups), TikTok, and Instagram — all through a single `POST /v1/jobs/tweet` endpoint.
- **Facebook Groups automation.** Search by keyword, filter by size and activity, join groups, and post — full discover-to-post workflows that traditional OAuth tools cannot do.
- **Native MCP support.** The public MCP endpoint (`https://mcp.clawpost.net/mcp`) uses **Streamable HTTP** with OAuth 2.0. Claude, ChatGPT, Hermes, and other agents built on the official MCP SDKs (TypeScript, Python, and compatible clients) can connect — no Claw Post API key required.
- **Simple setup.** Sign up → install extension → click extension icon and sign in with Google (auto-pairs) → provide one API key (or connect via MCP OAuth). No per-platform credentials.
- **Low cost per post.** Free tier included; paid plans scale affordably. See clawpost.net for pricing.

## Capabilities

| Capability | Endpoint | Platforms |
|-----------|----------|-----------|
| Post to feed or group | `POST /v1/jobs/tweet` | X, LinkedIn, Facebook, TikTok, Instagram |
| Comment / reply on a thread | `POST /v1/reddit/comment` | Reddit |
| Upload media for posts (small files) | `POST /v1/media/upload` | X, LinkedIn, Facebook, TikTok, Instagram |
| Upload large media (signed URL) | `POST /v1/media/upload-url` | X, LinkedIn, Facebook, TikTok, Instagram |
| Search for groups | `POST /v1/groups/search` | Facebook |
| Join a group | `POST /v1/facebook/groups/join` | Facebook |
| Check group membership | `POST /v1/facebook/groups/status` | Facebook |
| Poll any job result | `GET /v1/jobs/:id` | All |

All endpoints require the `clawpost-api-key` header.

> **MCP agents:** If your agent supports the Model Context Protocol, point it at `https://mcp.clawpost.net/mcp` and complete OAuth instead of using this REST API. Tools: `list_platforms`, `create_post`, `create_reddit_comment`, `get_upload_url`, `get_post_status`, and `get_account_status`. Use an MCP client that supports **Streamable HTTP** (current Anthropic / OpenAI SDK paths and the reference Python client).

## Prerequisites (instruct the human)

Before any action works, the human must:

1. **Sign up** at [clawpost.net](https://clawpost.net)
2. **Install** the Claw Post Chrome extension from the [Chrome Web Store](https://chromewebstore.google.com)
3. **Pair** the extension by clicking the extension icon and signing in with Google (primary flow; auto-pairs to your account)
4. **Set** the `CLAWPOST_API_KEY` environment variable in the agent (copy the key from the Dashboard — it is not embedded in this skill file)
5. **Log in** to the target platform once in their browser (x.com, linkedin.com, facebook.com, tiktok.com, instagram.com, or reddit.com)

**Extension scope.** The Chrome extension is designed to activate on supported social sites and when communicating with the Claw Post API. Verify permissions on the [Chrome Web Store](https://chromewebstore.google.com) listing and review the [Terms of Service](https://clawpost.net/terms) before installing.

If the agent gets `EXTENSION_NOT_PAIRED` or `not_logged_in`, direct the human to complete these steps.
If automatic pairing fails, use the Dashboard 6-digit code flow as a fallback.

## Authentication

All requests use the `clawpost-api-key` header:

```
clawpost-api-key: YOUR_CLAWPOST_API_KEY
```

The value above is a placeholder. Set the real secret via the `CLAWPOST_API_KEY` environment variable (or your agent’s secret store); do not paste live keys into this file or commit them to version control.

## API Base URL

```
https://api.clawpost.net
```

This is the stable, official Claw Post API endpoint. Full documentation: https://clawpost.net/api-docs

---

## 1. Posting

Create a post job, then poll for completion.

### Create post

```
POST https://api.clawpost.net/v1/jobs/tweet
Content-Type: application/json
clawpost-api-key: YOUR_CLAWPOST_API_KEY
```

**X (Twitter):**
```json
{ "text": "Hello world!", "platform": "x" }
```

**LinkedIn:**
```json
{ "text": "Hello LinkedIn!", "platform": "linkedin" }
```

**Facebook feed:**
```json
{ "text": "Hello Facebook!", "platform": "facebook" }
```

**Facebook group** (use `groupUrl` from search results, or a known `groupId`):
```json
{
  "text": "Hello group!",
  "platform": "facebook",
  "platformPayload": { "groupUrl": "https://www.facebook.com/groups/123456789/" }
}
```

**TikTok** (video + caption):
```json
{ "text": "Caption text", "platform": "tiktok", "mediaPaths": ["<url from upload>"] }
```

**Instagram** (image or video + caption):
```json
{ "text": "Caption text", "platform": "instagram", "mediaPaths": ["<url from upload>"] }
```
Instagram requires at least one media file (image or video). Text-only posts are not supported.

**Optional fields:**
- `platform` – `"x"` (default), `"linkedin"`, `"facebook"`, `"tiktok"`, or `"instagram"`
- `mediaPaths` – array of media URLs (upload first via media endpoint below)
- `idempotencyKey` – unique string to prevent duplicate posts
- `platformPayload` – Facebook group targeting: `{ "groupId": "..." }` or `{ "groupUrl": "..." }`

### Poll job status

```
GET https://api.clawpost.net/v1/jobs/:id
```

Status progresses: `queued` → `processing` → `succeeded` | `failed`.

- On success: response includes `postUrl` — the live URL of the published post. Share this with the user to confirm the post is live.
- On failure: response includes `error` and `errorCode`.
- **Timing**: posts execute through a real browser session. Allow 10–60 seconds before the job completes (longer for video uploads). Poll every 5–10 seconds.

---

## 1b. Reddit comments (browser actions)

Reply to a specific Reddit post or comment through the user's logged-in Chrome. No Reddit API key. The agent must supply the target thread/comment URL — Claw Post does not find threads for you.

```
POST https://api.clawpost.net/v1/reddit/comment
Content-Type: application/json
clawpost-api-key: YOUR_CLAWPOST_API_KEY
```

```json
{
  "text": "Useful reply text",
  "targetUrl": "https://www.reddit.com/r/example/comments/abc123/title/"
}
```

- `targetUrl` must be a Reddit URL whose path includes `/comments/` (post or comment permalink).
- Optional: `idempotencyKey`.
- Poll `GET /v1/jobs/:id` the same way as posts. On success, `postUrl` is the live comment permalink.
- Prerequisites: extension paired, Chrome open, user logged into Reddit in that browser.

---

## 2. Media upload

Upload media before posting. The returned `url` goes into the `mediaPaths` array.
Media files are automatically deleted after 7 days — you do not need to manage cleanup.

### Small files (images, short clips — under ~30 MB)

Send the file body directly to the API:

```
POST https://api.clawpost.net/v1/media/upload
clawpost-api-key: YOUR_CLAWPOST_API_KEY
Content-Type: multipart/form-data
Body: file=<media file>
```

Response:
```json
{ "url": "https://storage.googleapis.com/..." }
```

### Large files (videos and any file over ~30 MB) — two-step

For large files, get a signed upload URL first, then PUT the file directly to storage.
This bypasses all proxy limits and works for files of any size.

**Step 1 — request an upload URL:**
```
POST https://api.clawpost.net/v1/media/upload-url
Content-Type: application/json
clawpost-api-key: YOUR_CLAWPOST_API_KEY
```
```json
{ "filename": "video.mp4" }
```

`contentType` is optional — the API infers it automatically from the filename extension. Pass `platform` to validate the file type before uploading (e.g. `"platform": "x"` rejects audio files immediately).

Response:
```json
{
  "uploadUrl": "https://storage.googleapis.com/...?X-Goog-Signature=...",
  "url": "https://storage.googleapis.com/...",
  "resolvedContentType": "video/mp4"
}
```

**Step 2 — PUT the file directly to `uploadUrl` using the resolved content type (no `clawpost-api-key` header — the URL is self-authorised):**
```
PUT <uploadUrl>
Content-Type: <resolvedContentType from Step 1>
Body: <raw file bytes>
```

The signed URL will reject PUT requests with incorrect `Content-Type` headers (403). Always use the `resolvedContentType` value returned in Step 1.

Expect a `200` or `204` response from Google Storage. The upload window is 1 hour.

**Step 3 — use the `url` in the job exactly as with small files:**
```json
{ "text": "Check this out!", "platform": "tiktok", "mediaPaths": ["<url from step 1>"] }
```

The `url` is valid for 24 hours — sufficient for any normal job queue time.

---

## 3. Facebook Group Search

Discover relevant groups to join and post in. Returns ranked results with names, member counts, activity hints, and join status.

### Create search job

```
POST https://api.clawpost.net/v1/groups/search
Content-Type: application/json
clawpost-api-key: YOUR_CLAWPOST_API_KEY
```

```json
{
  "platform": "facebook",
  "query": "ai automation",
  "filters": { "minMembers": 1000, "privacy": "any" },
  "limit": 20
}
```

- `platform`: must be `"facebook"` (only supported platform for now).
- `query`: search keywords (required).
- `filters.minMembers`: minimum member count (optional).
- `filters.privacy`: `"public"`, `"private"`, or `"any"` (optional).
- `limit`: max results, up to 50 (optional, default 20).

Response:
```json
{ "jobId": "<id>" }
```

### Read search results

Poll `GET https://api.clawpost.net/v1/jobs/:id` until `status` is `succeeded`.

Results are in `details.groupSearch.results[]`. Each result:

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Group title (best-effort; may say "Group" if title not extractable) |
| `url` | string | **Canonical group URL** — use this for joining or posting |
| `platformId` | string? | Numeric Facebook group ID (when available) |
| `slug` | string? | URL slug (when available, e.g. `"aiautomationagency"`) |
| `privacy` | string? | `"public"`, `"private"`, or `"unknown"` |
| `memberCount` | number? | Approximate member count (when visible on search page) |
| `activityHint` | string? | Raw activity text, e.g. `"10 posts a day"` |
| `joinStatus` | string? | `"joined"`, `"requested"`, `"not_member"`, or `"unknown"` |
| `score` | number | 0–1 relevance score (higher = better match) |
| `reasons` | string[] | Why this group scored well (e.g. `"keyword match"`, `"large member base"`, `"active"`, `"public"`) |
| `signals` | object? | Raw numeric signals: `keywordHit`, `memberCount`, `activityPerDay` |

**Reliability notes:**
- `url` is always present and reliable. Use it as the primary identifier.
- `name`, `memberCount`, `privacy`, `activityHint`, and `joinStatus` are best-effort; they depend on what the search page exposes.
- `score` and `reasons` are computed by the extension from available signals.

---

## 4. Facebook Group Join

Join a group so you can post to it. Use the `url` from search results (extract the group ID or pass the full URL).

### Join a group

```
POST https://api.clawpost.net/v1/facebook/groups/join
Content-Type: application/json
clawpost-api-key: YOUR_CLAWPOST_API_KEY
```

```json
{ "groupId": "123456789" }
```

Response: a job object. Poll `GET /v1/jobs/:id` for completion.

On success, check `details.buttonState`:
- `"joined"` – user is now a member; you can post.
- `"requested"` – group requires approval; wait and check status later.
- `"not_member"` – join may not have worked; retry or inspect.

### Check group membership status

```
POST https://api.clawpost.net/v1/facebook/groups/status
Content-Type: application/json
clawpost-api-key: YOUR_CLAWPOST_API_KEY
```

```json
{ "groupId": "123456789" }
```

Same polling pattern. `details.buttonState` tells you the current membership state.

---

## Recommended agent workflow: discover → join → post

1. **Search** for groups: `POST /v1/groups/search` with a relevant query.
2. **Evaluate** results: prefer groups with high `score`, `memberCount` >= 1000, `privacy: "public"`, and `activityHint` showing regular posts.
3. **Check membership**: look at `joinStatus` in results:
   - `"joined"` → skip to step 5.
   - `"not_member"` or `"unknown"` → proceed to step 4.
4. **Join**: call `POST /v1/facebook/groups/join` with the group ID (extract from `url` or use `platformId`). Poll until `details.buttonState` is `"joined"` or `"requested"`.
5. **Post**: call `POST /v1/jobs/tweet` with `platform: "facebook"` and `platformPayload: { "groupUrl": "<url from search>" }`.

**Important**: Some groups require admin approval before you can post. If `details.buttonState` is `"requested"`, wait and re-check status later before attempting to post.

---

## Security and privacy

- **Social platform logins stay in the browser.** Posting uses the user’s existing session in Chrome. Claw Post does not ask you to send OAuth tokens or social passwords through this API for posting.
- **Extension scope.** The published extension declares host access for supported social domains and the Claw Post API. Inspect the Web Store listing and manifest permissions before installing.
- **API key is tenant-scoped.** Each `CLAWPOST_API_KEY` is tied to a single account and can be rotated from the Dashboard at any time.
- **HTTPS only.** All communication between the agent, the API, and the extension uses TLS.
- **No executable code.** This skill is instruction-only. It contains no scripts, no disk writes, no packages, and no persistence mechanisms.
- **Terms of Service:** [clawpost.net/terms](https://clawpost.net/terms)

---

## Error handling

| Code / errorCode | Cause | Action |
|-----------------|-------|--------|
| 401 | Invalid or missing API key | Check `clawpost-api-key` header |
| 503 / `EXTENSION_NOT_PAIRED` | No paired extension | User must install and pair the extension at clawpost.net/dashboard |
| `not_logged_in` | User not logged in to the platform | User must log in to the platform in their browser |
| `no_x_tab` / `no_platform_tab` | No browser tab for the platform | Retry; extension will try to open one |
| `content_script_unavailable` | Extension could not reach the tab | Ask user to refresh the platform tab, then retry |
| `selector_not_found` | Platform UI changed or element not found | Retry after a short delay |
| `group_not_approved` | User not approved to post in this group | Join the group first or wait for approval; do not retry immediately |
| `challenge_required` | Platform security check (captcha/checkpoint) | Ask user to complete the challenge in their browser, then retry |

On any failure, poll `GET /v1/jobs/:id` and read `error` and `errorCode` for details.

---

## Reference

Full API docs: https://clawpost.net/api-docs
