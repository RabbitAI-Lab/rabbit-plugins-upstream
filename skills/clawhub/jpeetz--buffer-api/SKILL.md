---
name: buffer-api
description: Schedule, manage and analyze social media posts via the Buffer GraphQL API from any AI agent.
version: 1.0.0
author: Joerg Peetz (@JPeetz) + Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [buffer, social, scheduler, graphql, posting, scheduling, instagram, tiktok, linkedin, publishing]
  agentskills:
    categories: [social-media, automation, marketing]
---

# Buffer API — Schedule, Manage & Analyze Social Posts

Use Buffer's GraphQL API to schedule, manage, and analyze social posts across
Instagram, Threads, LinkedIn, X/Twitter, Facebook, Google Business, Mastodon,
YouTube, Pinterest, and Bluesky — from any AI agent (Claude, Cursor, Codex,
OpenClaw, Hermes, n8n).

## When to Use
- Schedule/create/delete/retrieve posts or drafts in a Buffer queue.
- Automate repetitive posting or cross-platform content distribution.
- Retrieve account, organization, channel, idea, post-metric state.
- Route TikTok (and other owned-account) automation through Buffer's approved
  integration instead of a platform's Direct Post API.

## Progress Disclosure (read only what you need)
- **Quick operation** (list channels, schedule a post, check a post) → SKILL.md alone.
- **Media / images / video / per-network metadata / threads** → `references/media-and-metadata.md`.
- **Full API reference (all types, unions, inputs)** → local spec at
  `../openclaw-imports/openclaw-seo-geo-optimization/...` if needed; else fetch
  https://developers.buffer.com/reference.html.
- **MCP alternative** (if your host supports Model Context Protocol): Buffer ships a
  first-party MCP server at `https://mcp.buffer.com/mcp` with header
  `Authorization: Bearer <API_KEY>`. Prefer the raw GraphQL below when a script
  exists or when you need the bytes (binary media) that MCP tends to not expose.

## Prerequisites
- A Buffer account with **at least one connected channel** and an **API key**
  (https://publish.buffer.com/settings/api). The key acts on YOUR OWN account.
- Auth: send `Authorization: Bearer <API_KEY>` on every request to
  `https://api.buffer.com` (GraphQL, POST, `Content-Type: application/json`).
- Least-privilege: the API key is scoped to your own Buffer account; never ask a
  user for a platform's account password. Use the Buffer key the same way you would
  an app password.
- For images/video on a post: the **asset URL must be public**. See
  `references/media-and-metadata.md` for hosting + verification.

## Core Endpoint & Auth
```
POST https://api.buffer.com
Authorization: Bearer <API_KEY>
Content-Type: application/json
Body: {"query": "<graphql>", "variables": {...}}
```
The API is **GraphQL only**. Use the Buffer API Explorer (https://developers.buffer.com/explorer.html) to exercise schema. Scalar `DateTime` is ISO 8601 UTC.

## 1. Account & Organization
Find org + channel IDs — the two IDs you'll need for nearly everything.
```
query GetAccount {
  account { id email organizations { id name } }
}
```
```
query GetChannels {
  channels(input: { organizationId: "ORG_ID" }) { id name service type }
}
```
`service` = the platform (instagram, tiktok, linkedin, twitter/mastodon/youtube/pinterest/bluesky/facebook/gbp).
`type` = Page/Profile/Business/Group/Account.

## 2. Create a Post
```
mutation CreatePost {
  createPost(input: {
    text: "Hello from the Buffer API!"
    channelId: "CHANNEL_ID"
    schedulingType: automatic
    mode: addToQueue           # addToQueue or customScheduled
    # dueAt: "2026-03-10T15:00:00.000Z"   # required when mode=customScheduled
  }) {
    ... on PostActionSuccess { post { id text dueAt } }
    ... on MutationError { message }
  }
}
```
- Required: `text`, `channelId`, `schedulingType: automatic`. At least one of
  `mode` (addToQueue / customScheduled) or `dueAt`.
- `mode: addToQueue` → next available slot from the channel's posting schedule.
- `mode: customScheduled` + `dueAt` → exact date/time (ISO 8601, UTC).
- ALWAYS spread both `PostActionSuccess` AND `MutationError` (or your `... on { }`)
  so errors surface, not silently vanish.

## 3. Images / Video / Assets (media by public URL)
`assets` is an ordered list; each entry carries exactly one of `image`, `video`,
`document`, or `link`. For an image post:
```
createPost(input: {
  text: "Hello there, this is another one!"
  channelId: "CHANNEL_ID" schedulingType: automatic mode: addToQueue
  assets: [ { image: { url: "https://your-cdn.example.com/image.jpg" } } ]
}) { ... on PostCreatedSuccess { post { id assets { id mimeType } } } ... on CreateError { message } }
```
The `url` MUST be publicly reachable — Buffer fetches media from that URL. See
`references/media-and-metadata.md` (hosting + a `curl` verification you should run
before creating the post).

## 4. Retrieve / Manage Posts
- **Get one post** (poll status — note: Buffer polls by `post(input: { id })`, NOT a `getPost` field):
```
query PostById { post(input: { id: "POST_ID" }) { id text status dueAt channelId } }
```
  `status` values: `scheduled` → `sent` (successfully published) → `error`. Confirm
  `status == "sent"` (the string is `sent`, not `published`).
- **List posts (cursor pagination):**
```
query GetPosts {
  posts(first: 20, after: "CURSOR", input: { organizationId: "ORG_ID"
    filter: { status: [scheduled, sent] channelIds: ["CHANNEL_ID"] } }) {
    edges { node { id text status dueAt } }
    pageInfo { endCursor hasNextPage }
  }
}
```
  `first` + `after` are cursor-based; loop `after` until `hasNextPage` is false.
- **Edit** `editPost` mutation (same union shape).
- **Delete** `deletePost(input: { postId })` (returns DeletePostPayload union).
- **Move in queue** `movePostInQueue` (experimental) — reorder queued posts.

## 5. Ideas (save content for later)
- **Create:** `createIdea(input: { organizationId ideaGroupId text media })`.
- **List:** `ideas(input: { organizationId } )`. Media attaches via `url` too
  (image/video/gif document/link; video not exposed on public API).
- **Idea groups:** `ideaGroups(input:)`.

## 6. Post Metrics
Once a post is `sent`, per-network performance is normalized on `Post.metrics`.
- `aggregatedPostMetrics` (aggregate across channels/posts)
- `dailyPostingLimits` (per-channel daily caps)
- `post(input: { id }) { metrics { ... } }` for a single post.
Metrics are read-only and available for personal/workflow use.

## Supported Platforms & Per-Network Metadata
Supported services: instagram, threads, linkedin, twitter, facebook, google-business-profiles, mastodon, youtube, pinterest, bluesky.
Beyond the shared fields, `metadata` on `createPost` per network enables:
- **Threads / X / Bluesky / Mastodon:** create a threaded post (`metadata.{network}.thread`)
- **LinkedIn / Facebook / Instagram:** add a first comment on the scheduled post
- **Instagram:** post type (post / story / reel), user tags per image
- **Pinterest:** attach a board to a pin

You only provide the metadata for the network the channel belongs to. Read
`references/media-and-metadata.md` for the exact per-network shape.

## Errors & Error Handling
- Always include the `... on <Error>` fragment so mutation errors surface.
- Common: invalid channelId; missing required text/channelId; queue limit reached.
- A "same thing twice so close together" from Buffer = ALREADY QUEUED (the mutation
  returns a limit/duplicate-like error). Treat `ok=false` on a retry as already-queued,
  do NOT keep re-submitting.
- Union types: `createPost` returns `PostActionPayload` (union). Spread:
  `{ ... on PostCreatedSuccess { post {...} } ... on CreateError { message } }`.
- `post` QUERY (not `getPost`): Buffer has NO `getPost` field; the arg is `input: { id }`.
- **urllib / non-ASCII bodies:** if you are writing Python, `urllib.request` throws
  `UnicodeEncodeError: 'latin-1'` on a non-ASCII char (e.g. an em dash) in a JSON body —
  use `requests.post(..., json=...)` for non-ASCII payloads. This is a real, repeated gotcha.
- **JSON-LD/latin-1 hardware:** run scripted API calls with a healthy interpreter
  (`env -u PYTHONPATH python3` on the Hermes box).
- **Auth is Bearer only.** The legacy REST (`api.bufferapp.com/1/`) is RETIRED
  (2027-02-01) and 401s "Public API tokens are not accepted for REST API access."
  Do not use it.

## End-to-end flows (cheat sheets)
- **Schedule next available:**
  account → organizations → channels(input:{organizationId}) → createPost(mode:addToQueue) → poll `post(input:{id})` until status -> sent.
- **Post with an image:**
  host public URL → verify (GET 200) → createPost(assets:[{image:{url}}]) → poll.
- **Stand up TikTok / IG automation:**
  use Buffer + `metadata` (post type) for owned-account scheduling, not the platform's
  Direct Post API (Triggered-Use) — one shared API key across channels, no per-platform
  token juggling.

## Pitfalls & Hard-Won Lessons
1. **API is GraphQL, not REST.** Point everything at `https://api.buffer.com`. Legacy
   REST is retired. `api.bufferapp.com/1/` is dead.
2. **Polling is `post(input:{ id })`, not `getPost`.** A query field named `getPost`
   does NOT exist. Use `post(input: { id: "..." }) { id status }`. Poll confirms both
   creation and `sending->sent`.
3. **`status == "sent"`** — the string is `sent`, not `published`, in Buffer GraphQL.
4. **Asset URL must be public** — images/videos via `assets:[{image:{url}}]`. No
   raw blob upload mutation. Verify with a HEAD/GET (200) before creating.
5. **JSON-LD / non-ASCII bodies:** use `requests` or any JSON-safe HTTP client, not
   `urllib` (latin-1 crash). 
6. **Don't hammer a duplicate.** Close-together repeat of the same post = already
   queued. Handle `ok=false` as already-queued; don't retry.
7. **Rate / queue limits** surface as `CreateError` / `LimitReachedError` — read the
   message, adjust cadence, never blind-retry-loop.
8. **No auth to Publish UI** for most graph ops — some preview `🧪` endpoints
   (post templates, updatePostTemplate) are preview-only.
9. **Custom scalars ≠ generic `ID` (verified live).** Buffer params like
   `organizationId`/`channelId`/`postId` use DISTINCT custom scalars
   (`OrganizationId!`, `ChannelId!`, `PostId!`). Declaring a query variable as
   `ID!` where the field expects `OrganizationId!` fails GraphQL validation. Either
   inline the ID as a string literal or type the variable with the exact scalar.

## References
- `references/api-reference.md` — full GraphQL schema: all queries/mutations, type
  fields, unions (account, channels, posts, ideas, metrics, post templates).
- `references/media-and-metadata.md` — public media hosting + verification, per-network
  metadata shapes (threads/bluesky/mastodon threads; LI/FB/IG first comment; IG post
  type/user tags; Pinterest board), scheduling, ideas.
- `references/graphql-helpers.md` — ready-to-run queries and mutation templates.
- `scripts/buffer_graphql.py` — a small, dependency-light Python helper to POST JSON
  GraphQL safely (handles non-ASCII, unions, pagination), so you don't re-render a
  fragment stack.

## Verification
- Run `scripts/buffer_graphql.py --query "{ account { id organizations { id } } }"`
  → expect `{"account":{...}}` (proves auth + endpoint).
- After creating a post, poll `post(input:{ id })` and confirm `status`:
  `scheduled -> sent`.

---
**Last verified:** 2026-08-21 against https://developers.buffer.com (guide + reference).
