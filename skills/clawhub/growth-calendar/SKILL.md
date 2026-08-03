---
name: growth-calendar
description: Plan, inspect and generate SEO articles on a Timothe Growth Calendar. Use when the user asks about their content calendar, article schedule, planned or published posts, topic clusters, or wants to plan or write SEO articles for their site.
homepage: https://timothe.ai/growth-calendar
metadata:
  openclaw:
    emoji: "📅"
---

# Timothe's Growth Calendar

Product page: [Growth Calendar](https://timothe.ai/growth-calendar)

Growth Calendar keeps a workspace's SEO content schedule: planned articles with publish dates,
reminder notes, and the articles already generated. Each planned article has a reservation that
fires on its date and writes the article without anyone being present.

The MCP tools act on the user's own workspace. Everything is scoped to the workspace their
connection is bound to, so there is no tenant to choose.

## Setup

The tools come from Timothe's hosted MCP server; nothing runs locally. If the tools named below are
not available yet, configure the server and sign in:

```bash
openclaw mcp add growth-calendar --url https://timothe.ai/mcp/growth-calendar --transport streamable-http --auth oauth
openclaw mcp login growth-calendar
```

The `--transport streamable-http` flag matters: the default SSE transport fails against this server
with a 405.

`login` opens a browser to sign in to Timothe; the client registers itself, so there is no API key
to paste. Credentials refresh on their own afterwards, and `openclaw mcp logout growth-calendar`
removes them. The connection acts on one Timothe workspace: whichever one the account is on when it
first signs in.

## Linking the user to their calendar

These tools return data, not a screen. When you report on something the user might want to look at
or edit by hand, give them the link:

- The calendar itself: `https://timothe.ai/tools/growth-calendar/app`
- One generated article: `https://timothe.ai/tools/growth-calendar/app?article=<trackId>/<date>`

The article parameter is the track id and the publish date joined by a slash, which is exactly the
pair you passed to `read_article`. For the "guides" track on 14 August 2026 that is
`?article=guides/2026-08-14`. Both values are URL-safe by schema, so nothing needs encoding.

## Read before you write

Start with `list_tracks`, then `get_calendar` for the month in question. A track is the
continuing publishing line a set of planned articles belongs to; its track id carries their
language and timezone, so you cannot write a correct `create_note` or `plan_cluster` call without
knowing which tracks exist. Guessing a track id creates a second, near-duplicate track.

`get_cluster_context` tells you what a track's current topic cluster is about and which dates
still expect an article. Read it before proposing new topics for an existing track, otherwise you
will suggest things the plan already covers.

## What costs credits

| Tool | Credits | Notes |
| --- | --- | --- |
| `serp_top` | 2 | Cheap enough to use freely |
| `site_keywords` | 5 | One domain per call |
| `keyword_ideas` | 20 | Priced per CALL, not per seed |
| `keyword_volumes` | 20 | Priced per CALL, not per keyword |
| `plan_cluster` | 200 | Takes several minutes |
| `generate_article` | 600 | Takes several minutes |

All six require a paid plan. Everything else is free.

Check `get_credits` before proposing the expensive two. It reports the balance and whether the
workspace is on a paid plan, so you can say "this costs 600 and you have 1,200" instead of starting
a run that gets refused. It is free to call.

Treat `plan_cluster` and `generate_article` as actions the user authorizes, not as steps you take to
explore. Say what it will cost and what it will produce, get a clear yes, then call it once. Never
call either one to find out what happens, and never retry after a failure without checking `get_run`
first: the run may have succeeded and the retry would be charged again.

The research tools are different in kind. They are cheap and fast, so once the user has agreed to
look into a topic, run them without asking permission for each one. Do tell them roughly what you
spent when you report back.

## Checking a market before committing to it

`serp_top`, `keyword_volumes`, `keyword_ideas` and `site_keywords` return real Google demand and
competition data for one market, in seconds. They exist so you can judge a topic yourself instead of
spending 200 credits on `plan_cluster` and finding out afterwards that nobody searches for it.

A market is a language plus a country, and the two matter independently: English sold to the UK is a
different demand curve and a different SERP from English sold to the US. Pass the `country` when you
know it, and take it from the track when you are working on an existing one.

A workable sequence before planning a cluster:

1. `keyword_ideas` on a few seed phrases, to see what the neighbourhood looks like and how big it is
2. `serp_top` on the two or three queries that matter most, to see who you would be up against
3. `keyword_volumes` on everything you are considering, in ONE call, to confirm the numbers

`site_keywords` is the one that finds angles you would not have thought of: point it at a competitor
domain and it shows which topics actually bring them traffic.

The cost discipline that matters: `keyword_ideas` and `keyword_volumes` are priced per call, so
sending 60 keywords in one call costs 20 credits and sending them one at a time costs 1,200. Collect
everything you want to check, then make one call. `keyword_volumes` takes up to 100 keywords and
`keyword_ideas` up to 20 seeds.

Report volumes you actually looked up. A keyword that comes back with no data has negligible volume,
which is a finding; do not fill the gap with an estimate.

## Long-running work

`plan_cluster` and `generate_article` return a run id immediately rather than a result. Poll
`get_run` with that id and the matching `job` value until the status is no longer `pending` or
`running`. A few minutes is normal. Leave a real gap between polls instead of checking in a tight
loop, and tell the user it is running rather than going silent.

## Planning a cluster

`plan_cluster` researches one pillar topic and lays a finite set of articles onto the calendar, one
planned item plus one reservation per publish date. It needs:

- `trackId`: an existing track id, or a new short one (`ja`, `en`) if this is a new track
- `topic`: the pillar topic to build around
- `language` and `timezone`: what the articles are written in and when they publish
- `startDate` and `count`: the first publish date and how many articles

Ask about the business before choosing a topic, then check the topic against the research tools
above. A cluster planned from a guess produces a month of articles the user did not want, and each
one costs 600 credits to regenerate. Twenty credits of `keyword_volumes` is the cheapest insurance
available against that.

## Editing the plan

`update_plan_item` changes one planned article: its title, writer guidance, URL slug, or the day
and time it publishes. It only works before the article is generated, and it rejects dates in the
past or dates that already have an article.

`delete_plan_item` removes one planned article and frees its day. It is destructive and takes one
item at a time by design. Confirm each deletion with the user, and when they ask to clear several,
list what you are about to delete and get one explicit confirmation before starting.

`create_note` adds a dated reminder that gets emailed on its date. Use it for things the user needs
to do, not for articles to write.

## Reading and editing articles

`update_plan_item` above only works before an article exists. Once it has been generated, the
article itself is edited with `read_article` and `edit_article`.

`read_article` returns the editable source: line 1 is `revision: N`, then a blank line, then a
frontmatter with the editable fields (title, description, slug, note) followed by the markdown body.
That text is the exact thing `edit_article` matches against, so read before every edit rather than
working from an earlier copy.

`edit_article` applies exact string replacements in order. Copy each `oldString` verbatim from what
`read_article` returned and include enough surrounding context to make it unique, or pass
`replaceAll`. Frontmatter fields are edited like any other line, and deleting an optional
frontmatter line clears that field. Pass the revision you just read as `expectedRevision`.

Leave image lines and `gcimg:` placeholders alone. They are resolved when the article is displayed,
and rewriting them breaks the images.

The whole edit either applies and is saved, or nothing changes. On a revision conflict or a failed
match, read the article again and rebuild the edits against the new text; do not retry the same
strings. The result comes back with any remaining prose-lint warnings, which are advisory.

`get_calendar` returns a whole month and can be long. Summarize it for the user instead of pasting
it back.

## Workspace styles

Two workspace-wide documents steer every article the calendar generates: the writing style (voice,
structure, wording) and the image style (the art direction for the images generated inside
articles). Both follow the same read/update pattern as articles: the get returns `version: N` on
line 1, and the update takes that N as `expectedVersion`.

Read the relevant one (`get_writing_style` / `get_image_style`) before offering opinions on how
articles are written or how their images look. An image style at `version: 0` means the workspace
has not saved one; the built-in default returned after that line is what currently applies.

`update_writing_style` and `update_image_style` replace the whole document, so carry over
everything that should stay and change only what the user asked to change. On a version conflict,
read again and rebuild against the fresh text instead of retrying the same call. Style changes
apply to articles generated from then on, not to the ones that already exist.

Keep the image style a compact art-direction block: overall look, palette (hex values work well),
composition, mood. It is appended verbatim to every image-generation prompt, so vague prose
weakens every image and 1,200 characters is the hard cap.

The app also offers preset image styles (a look plus a color palette). When one is selected,
`get_image_style` shows a `preset:` line under the version, and `update_image_style` replaces that
selection with your custom text. That is the right call when the user wants a custom style; when
they just want a different look or color scheme, point them to the presets in the app instead.
