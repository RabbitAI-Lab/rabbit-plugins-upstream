# GTM Coach — reference

Companion to [SKILL.md](SKILL.md) and **[playbook.md](playbook.md)**. Keep `plan.json` small. Live pains/leads stay on the API. Strategy turns are a CMO board (stage + project type + channel index). Channel SOPs load only after the founder chooses to execute.

## plan.json (hot)

Copy [plan.example.json](plan.example.json). Allowed top-level keys:

| Key | Purpose |
| --- | --- |
| `version` | Plan schema version (`1`), not the Skill release version |
| `skill` | Installed Skill version, last update check/notice, and optional deferral |
| `current_week` | ISO week from `GET /status` (`2026-W38`) |
| `intake` | `blank` \| `industry` \| `idea` \| `shipped` — how much product exists |
| `product` | Pin: name, `project_type`, one_liner, icp, url, repo_confirmed |
| `strategy` | CMO board (see below). `confirmed` must be true before dumping pains/leads |
| `modules` | Exact project-type, primary-channel, and optional-campaign files loaded this week |
| `connection` | Free project-bind offer state; never stores the secret token |
| `focus` | One sentence for this week’s bet |
| `this_week` | Theme + one active experiment + 3–7 micro-tasks |
| `open_decisions` | Pointers only: `{ id, source, ask, url? }` — max 20 |
| `filters` | `ignore_pain_tags`, `prefer_subreddits`, `skip_subreddits` |
| `last_outcomes` | Compact channel/result counts + optional `manual_note` |
| `partners` | `waiting` \| `open` \| `handed_off` |

### `strategy` (required)

`product.project_type` uses the NicheReach project values: `MICRO_SAAS`, `SERVICE_FREELANCER`, `NEWSLETTER_MEDIA`, `DIGITAL_PRODUCT`, `COMMUNITY`, `CREATOR_ARTIST`, `BRAND`, `EDUCATION_COHORT`, or `PLATFORM_MARKETPLACE`. Apply the matching lens in `playbook.md`; do not assume every project ships code or converts through a trial.

| Field | Values |
| --- | --- |
| `confirmed` | `true` only after the founder agrees the board |
| `period` | `validate` \| `build` \| `cold_start` \| `launch` \| `promote` \| `monitor` |
| `build` | `not_started` \| `in_progress` \| `mvp` \| `shipped` |
| `evidence` | `none` \| `anecdote` \| `pains_scored` \| `waitlist` \| `paying` — same list as SKILL.md. `pains_scored` includes observed use. Retained/referring customers stay `paying` plus a `manual_note`. |
| `primary_channel` | `direct` \| `reddit` \| `indiehackers` \| `linkedin` \| `x` \| `short_video` \| `youtube` \| `newsletter` \| `seo` \| `producthunt` \| `hackernews` \| `webinar` \| `podcast` \| `partnerships` \| `paid` \| `other` \| `undecided` |
| `channels_this_quarter` | short list of channel ids |
| `launch_optional.producthunt` / `show_hn` | booleans — optional campaigns, not the weekly engine |
| `share_loop` | natural artifact/action or `none yet`; never force an invite |
| `paid_promotion` | `blocked` \| `validation_test` \| `eligible_to_test`; scale spend needs payment + value/retention |
| `seo_status` | `not_applicable` \| `audit_needed` \| `foundation_ready` \| `content_loop` |
| `note` | max 240 chars |

**Never store:** full `post_body`, long pain descriptions, tokens, partner pitches.

### Selective module protocol

**Board layer**

1. Persist the full `gtm-coach/` bundle into **this** agent’s skills folder if missing (see SKILL.md). Never store plan or tokens there.
2. On first write, copy [plan.example.json](plan.example.json). Load this reference only then, or when schema/API changed. Write `.gtm/` at the workspace root for the bound project (monorepos: do not nest inside `web/` unless that is the root). If `.gtm/plan.json` already exists, resume it—do not re-init. Any agent that opens the same folder can read it; each agent still needs its own skill install.
3. Resolve `strategy.period` through `stages/index.md` (use `status.picture` as a hypothesis). Store one exact path in `modules.stage` and load that SOP.
4. Resolve `product.project_type` through `project-types/index.md`; store one exact path in `modules.project_type` and load that SOP.
5. Score channels through `channels/index.md` only. Record the recommended id in `strategy.primary_channel`. Keep `modules.primary_channel` **null** until a dive.
6. Cite `outcomes.leads_pending` / `replies_posted_7d` as instrument counts on the board. Do not GET `/leads` until the founder confirms the board and chooses a community channel.

**Dive layer**

4. Load a channel SOP only after the founder chooses to execute or inspect that channel; then store its path in `modules.primary_channel`.
5. Set `modules.optional_campaign` only after the founder approves one additional campaign.
6. Do not load all stage/project/channel modules. After a dive, keep the CMO board (stage included) at the top of the turn.
7. When type/channel/stage changes, replace the path and record why in the weekly journal.

When `current_week` from `/status` differs from `plan.json`, close the old week first.

### Skill release state

`GET /api/gtm/agent` → `skill_release` is the canonical update manifest.

| Field | Rule |
| --- | --- |
| `skill.installed_version` | Last complete Skill bundle the agent loaded |
| `skill.last_checked_at` | ISO timestamp of the latest successful manifest check |
| `skill.last_update_notice_version` | Prevents repeating the same update prompt every turn |
| `skill.deferred_until` | Optional ISO date/time; do not prompt before it |

The top-level `version` remains the plan schema. Never overwrite it with a SemVer string.

Version behavior:

- PATCH: compatible fix; recommend refresh.
- MINOR: backward-compatible feature/module; show concise release note and recommend refresh.
- MAJOR: breaking behavior/schema; require explicit migration approval.
- Offline/check failure: continue the installed version and retry next new session. Never block coaching.

### Free connection state

| Field | Values / rule |
| --- | --- |
| `connection.status` | `unbound` \| `offered` \| `deferred` \| `bound` \| `declined` |
| `connection.offered_week` | ISO week; prevents repeated prompts |
| `connection.project_id` / `project_name` | Set only after bound `/status` verifies the key |

Offer free connection only after the unbound founder receives a useful GTM recommendation/artifact. `deferred` is silent for the rest of the week; `declined` is silent until they request live data or start a different project. Store the token only in `.gtm/secrets.md`/secure agent storage, never `plan.json`.

## inbox.json

Open items only. After a decision, delete the row and append a line to `journal/{week}.md`. Cap 20. See [inbox.example.json](inbox.example.json).

## journal/YYYY-Www.md

Append-only. Do not load more than the **current** and **previous** week into context. See [journal.example.md](journal.example.md).

## Decision protocol

### Pains (`source: starter`)

Ask: `build` | `later` | `not_us`

- `build` → add a micro-task (spec, copy, or ship). Remember `id` in `last_outcomes.pains_shipped` when they say it shipped.
- `later` → journal only; do not re-push for 2 weeks.
- `not_us` → add a tag or phrase to `filters.ignore_pain_tags`.

### Leads (`source: reach`)

Ask: `open in extension` | `save` | `skip`

Store `url` (the Reddit `post_url`) on the inbox row. When you show the lead, it must be a markdown link `[title](url)`.

- `open in extension` (legacy alias: `reply`) → **do not fetch the post and do not draft copy**. Send the founder to the URL with the **NicheReach Chrome extension** ([install](https://chromewebstore.google.com/detail/nichereach/meijkmdpgkfookehfglnkdcjgobheemp)). Inbox: `https://www.nichestarter.ai/reach`. Next session ask if they posted.
- `save` → journal; they can open `/reach`.
- `skip` → if the same subreddit is skipped 3 times, add to `filters.skip_subreddits`.

Do not list `r/sub 「title」` without a URL. Do not make pasting into reddit.com the default publish path. Do not scrape or open the thread in the agent to write a comment.

### Manual stats

If `/status.outcomes` cannot explain the week, ask **one** paste:

> Waitlist signups, revenue, or “I posted N replies and heard back from …” — one line is enough.

Put it in `last_outcomes.manual_note` (max 240 chars).

### Action experiment

Keep only one `this_week.active_experiment`:

| Field | Rule |
| --- | --- |
| `action` / `channel` | The chosen action and where it runs |
| `hypothesis` | One falsifiable sentence |
| `success_metric` / `target` | Closest useful outcome: qualified conversation, demo, activation, repeat use, referral, or payment |
| `baseline` | Number or `unknown`; never invent |
| `artifact_url` | Public URL when available; use `private` for email/DM/interview |
| `review_on` | Date or event trigger |
| `result` | Compact counts + qualitative lesson |
| `decision` | `pending` \| `continue` \| `change` \| `stop` |

When results arrive, judge signal quality before proposing more work. Impressions, likes, and followers alone are not proof; connect them to qualified responses or product behavior. Append the conclusion to the weekly journal.

## Copy templates

### Community replies

Do not write Reddit/Facebook comments here. Handoff: clickable `post_url` + NicheReach extension.

### X

- Offer a useful single post or a learn / ship / ask three-post set.
- One idea per post, founder’s voice, no invented metrics or fake controversy.
- Track qualified replies, site actions, and conversations; impressions are context.

### Direct outreach

- Start with a real trigger and a specific pain/job question.
- Ask for a short conversation, demo, manual pilot, or paid pilot according to evidence.
- Personalize from facts; no bulk generic pitch.

### Show HN

- Title: `Show HN: {thing} — {honest outcome}` (no “game-changer”).  
- Body: what it is, who it is for, what is still rough, link.  
- Do not claim user counts you cannot see.

### Product Hunt (only if on the strategy board)

- Name + tagline: what it does for whom.
- First comment: who it is for, what is still rough, link.
- Same week: keep one normal primary-channel action. The launch spike fades.

## API catalog (shipped)

Base `https://www.nichestarter.ai`

Module routing:

- `/skills/gtm-coach/stages/index.md` → choose one current-stage SOP.
- `/skills/gtm-coach/project-types/index.md` → choose one of nine project SOPs.
- `/skills/gtm-coach/channels/index.md` → choose one primary-channel SOP.
- Bound `/status.project_type_playbook_url` gives the exact project-type module.
- `/status.channel_playbook_url` gives the channel index because primary channel is founder/local-plan state.

| Method | Path | Auth | Role |
| --- | --- | --- | --- |
| GET | `/api/gtm/agent` | no | Canonical `skill_release` manifest + catalog/module URLs |
| GET | `/api/gtm/agent/status` | optional `nmagt_` | Release manifest + project envelope + outcomes |
| GET | `/api/gtm/agent/brief` | optional | Public teaser without a token; linked-topic pains for a bound project |
| GET | `/api/gtm/agent/leads` | `nmagt_` | Pending NicheReach leads for this project |
| GET, POST | `/api/gtm/agent/topics` | `nmagt_` | List / create / link Nichestarter searches on this project |
| GET | `/api/public/weekly-report-preview` | no | Optional Monday pain evidence |
| GET | `/api/social/daily-brief` | no | Optional recent pain evidence |

Token: same NicheMatch bind key. Header `Authorization: Bearer` plus the `nmagt_` key, or `X-NicheMatch-Token`. Never echo a pasted key. Existing keys with `profile:write` work — no re-issue required.

`GET /status` may include `picture` (suggested period, readiness, evidence) and `outcomes.kind: "instruments"`. Suggestions are not confirmation. `status.next` must not be treated as permission to fetch `/leads`.

For a bound project, brief mode is **project_topics** when Nichestarter searches are attached. With no linked topic it returns `mode: "topic_required"` and `items: []`; it never falls back to public-library keyword overlap. Ask once whether the founder wants optional project-level Reddit pain monitoring to improve the product or find adjacent opportunities. If yes, POST `{ "action": "create_from_project" }` to `/api/gtm/agent/topics` (or use `/projects`). Creating a custom topic requires Premium and an unused topic seat; otherwise the API returns 402 with `upgrade_url`. Linking an existing relevant public topic does not. If they decline or cannot upgrade, continue manual coaching.

### Capability and CTA boundaries

| Need | Available now | If unavailable / human action |
| --- | --- | --- |
| Keep monitoring linked topics | `GET /status` checks `starter.mode`; `GET /brief` returns linked-topic pains | If `topic_required`, ask once; on yes attach/create at `https://www.nichestarter.ai/projects` |
| Fetch potential customers | If `discover_enabled`, `GET /leads` returns pending Reach leads including `post_url` | If off, ask once; on yes send to `https://www.nichestarter.ai/reach`. The agent cannot start it |
| Draft and publish a reply | NicheReach Chrome extension reads the thread, drafts, and safety-checks | Founder opens `post_url` in the extension and clicks Post. Agent never fetches the post, never drafts, never posts |
| Fetch/handle partners | NicheMatch skill + same token, only while `match.marketplace.enabled` | Value Card/matching CTA: `https://www.nichestarter.ai/nichematch` |
| Persist GTM decisions | Local `.gtm` inbox/journal | Server decision endpoint is not built |

Fetched rows are **decision inputs**, not the plan:

1. Filter by confirmed ICP, period, and ignored history.
2. Explain fit in one sentence.
3. Ask one bounded decision (`build/later/not_us`, `reply/save/skip`, or partner investigate/pass).
4. Convert an accepted pain into one weekly task. Convert an accepted Reddit/Facebook lead into an extension handoff, not a drafted comment.
5. Journal/suppress rejected or deferred items so they do not recur.

## APIs not built yet (coach still runs)

Ask the founder to paste data, or send them to the web app. Do not block the week.

1. **`POST /api/gtm/agent/decisions`** — persist build/later/reply/skip on the server (today: local journal only).  
2. **`POST /api/nichereach/agent/draft`** — not used by this Skill. Drafting lives in the NicheReach Chrome extension.
3. **Watch / push webhook** — notify when new leads or pains arrive (today: they re-open the chat, or `/loop` on `/status` if they asked).  
4. **Plan sync to `/dashboard`** — optional upload of `plan.json` (today: local-only).  
5. **NicheMatch** — matching stays behind `NICHEMATCH_MARKETPLACE_LIVE`; not required for coaching.

## Gitignore

```
.gtm/
.nichematch/
```

Do **not** gitignore the agent skills folder. It has no secrets. Optional: commit project-level `gtm-coach/` under `.cursor/skills`, `.claude/skills`, `.agents/skills`, and/or `.codebuddy/skills` (or symlink one canonical copy) so teammates on that host get natural-language calling. `.gtm/` stays local and is readable by any agent that opens the same workspace.
