# Publishing reference

Full tool reference for the Socialync MCP server, plus the failure modes that
matter when an agent is posting unattended.

## Connecting

The server is a remote streamable-HTTP MCP endpoint at `https://mcp.socialync.io/mcp`,
authenticated with OAuth 2.0 using dynamic client registration.

```bash
openclaw mcp add socialync \
  --url https://mcp.socialync.io/mcp \
  --transport streamable-http
openclaw mcp login socialync
openclaw mcp tools socialync
```

The user signs in with their Socialync account in a browser window. No API key is
pasted into the client. The same endpoint works in Claude Desktop, Claude Code,
Cursor, ChatGPT, or any MCP client, and the connection can be revoked from
Socialync account settings at any time.

Do this once, at the point of publishing. Nothing in Stage 1 of the skill requires
it. Planning, drafting, per-platform formatting, and calendar building all work
with no account and no connection.

Posts publish only through social accounts the user already authorized inside
Socialync. If the sign-in has not happened or has been revoked, say so plainly and
point the user at the connect step. Do not silently fall back to drafting and
imply the post was scheduled.

MCP and API access are included on the free plan. A user can sign up for $0 with no
credit card and start publishing, 5 posts per calendar month across all 8 platforms.
Never tell a user they need to pay before they can connect. Paid plans start at
$20/month and remove the post cap.

One publish counts as one post regardless of how many platforms it targets, so a
five-platform cross-post costs one of the five. Say that plainly when a free user asks
how far their allowance goes.

One API key per brand, and ten AI-created posts per day per brand. Read the live
numbers from `check_quota` instead of assuming them.

## Tools

**Discovery and preflight**

- `list_profiles`: every profile this connection can manage, with id, name,
  default flag, connected platform count, and whether the profile is eligible for
  agent management. Call first. Pass the chosen id as `profileId` on every write.
- `list_connections`: connected platforms for a profile with connection health.
  Check before drafting against a platform.
- `check_quota`: plan, remaining posts, per-platform daily caps, schedule
  horizon, and supported platforms. Call before every batch.

**Writing**

- `create_post_draft`: build a draft without sending it.
- `get_draft_status`: poll a draft that is still processing.
- `approve_draft`: user approval gate before anything goes live.
- `schedule_post_draft`: put an approved draft on the calendar.
- `publish_now`: immediate publish. Use only with explicit user confirmation.
- `publish_scheduled`: fire something already scheduled, early.
- `generate_content`: AI drafting where the plan is available.

**Media**

- `create_media_upload` then `finalize_media_upload`: two-step process. Media must be
  finalized before it can attach to a post.
- `list_media`: assets already uploaded.

**Reading back**

- `get_scheduled_posts`: the calendar. Always read back after writing.
- `get_post_history`: what has already shipped.
- `delete_scheduled_post`: reverse a scheduled post.
- `get_analytics`: reach and engagement per platform.
- `get_top_posts`: best performers, for pattern-matching the next batch.
- `list_audiences`: audience segments where configured.

## Failure handling

**Duplicate posts are the number one agent failure.** A network timeout on
`publish_now` does not mean the post failed. It often means the response was
lost after the post succeeded. Socialync has duplicate protection, so a retry
cannot publish twice, and failed posts are retried automatically. Even so, call
`get_post_history` or `get_scheduled_posts` first and confirm the post is absent
before trying again, so you report the truth to the user.

**Quota exhaustion mid-batch** leaves a half-published week. Read
`maxPostsPerPlatformPerDay` from `check_quota` and plan the whole batch against
it before the first write. LinkedIn's cap is lower than the others.

**A disconnected platform fails at publish time, not at schedule time.** Check
`list_connections` during planning so the user reconnects before a scheduled post
silently fails days later.

**Schedule horizon is bounded.** `check_quota` returns `maxScheduleMonths`.
Scheduling past it will be rejected, so clamp the calendar to the horizon and tell
the user rather than letting individual writes fail.

**Profile eligibility.** Not every profile can be managed by an agent. Read the
eligibility flag from `list_profiles` and say plainly if the profile the user
named needs an upgrade, rather than failing on the write.

## Confirmation policy

Default to drafting. Show the user what will go out, on which platform, at what
time, and wait for a yes. Publishing to a real audience is not reversible in any
meaningful sense; a deleted post has already been seen.

The one exception is when the user has explicitly set up a recurring autonomous
schedule and asked for it to run without prompts. Even then, report what went out.
