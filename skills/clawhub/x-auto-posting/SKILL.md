---
name: x-auto-posting
description: "X (Twitter) auto-posting and content operations workflow: keyword-driven topic collection → case reference extraction → user topic confirmation → tweet drafting → publish to X → 24-hour performance tracking. Executes the complete content cycle from keyword to published tweet in a single run. Use when user mentions post on X, post on Twitter, auto tweet, X auto posting, Twitter auto posting, tweet from keywords, generate tweet, X content operations, X account management, operate X account, schedule tweet, publish tweet, track tweet metrics, X posting workflow, daily X post, X 发推, X 自动发帖, X 运营, 发推文, 推文追踪, 追踪效果, 看数据, 发推, 内容运营."
---

# X (Twitter) — Auto-Posting

> keywords + authenticated browser session → published tweet + performance record

## Language

All process output to user (progress updates, process notifications) follows the user's language.

## Objective

Execute the complete X content operations cycle: keyword-driven topic collection → case reference extraction → user topic confirmation → tweet drafting → publish → 24h performance tracking.

## Prerequisites

- Target page is already open in the browser: `https://x.com/home`
- User is logged in to X (account avatar or handle is visible on the page)

## Pre-execution Checks

### 1. Tool Readiness

If browser-act has been confirmed available in the current session → skip this step.

Invoke `browser-act` via Skill tool to load usage. If installation or configuration issues arise, follow its guidance to resolve then retry.

### 2. Login Verification

If login status for X has been confirmed in the current session → skip this step.

Otherwise: navigate to `https://x.com/home` and check:

```bash
browser-act --session {SESSION} navigate "https://x.com/home"
browser-act --session {SESSION} wait stable --timeout 15000
eval "$(python scripts/check-login.py)"
```

- `logged_in: true` → continue
- `logged_in: false` → inform user that login is required; assist the login flow via `remote-assist --objective "Log in to X"`

User refuses or cannot log in → terminate execution.

---

## Phase 0 — Configuration

### 0.1 Session State Load

Read `workspaces/x-posting/session_state.json`:
- File does not exist → run **0.2 First-Run Configuration Wizard**
- File exists → load and display current config; user confirms or modifies

`session_state.json` schema:

```json
{
  "session_name": "<session_name>",
  "account": {
    "handle": "@YourHandle",
    "profile": "your-account-profile-description"
  },
  "product": {
    "name": "",
    "tagline": "",
    "url": ""
  },
  "keywords_file": "workspaces/x-posting/keywords.json",
  "posting": {
    "daily_limit": 3,
    "min_interval_hours": 2,
    "last_posted_at": null,
    "today_count": 0
  }
}
```

### 0.2 First-Run Configuration Wizard (file does not exist)

Invoke AskUserQuestion tool to collect from user:
1. Session name (the `--session` name used for the active X browser session)
2. Product name, tagline, URL (used for CTA links in content writing)
3. Keyword list (at least 3 keywords, written to `workspaces/x-posting/keywords.json`)
4. Daily posting quota (default 3 posts, minimum 2 hours between posts)

Write `workspaces/x-posting/session_state.json` and `workspaces/x-posting/keywords.json`, then continue to 0.3.

### 0.3 Account Safety Check

- Read `session_state.json` field `posting.last_posted_at`
- If time since last post is less than `min_interval_hours` → notify user and ask whether to force-continue
- If today's cumulative post count ≥ `daily_limit` → notify user and ask whether to continue
- X enforces rate limits on automated posting; this Skill defaults to conservative limits — do not modify

---

## Phase 1 — Topic Collection

Detailed execution parameters: `references/phase1-topic-collection.md`

**Overview:**

1. **Keyword rotation**: read next keyword from `workspaces/x-posting/keywords.json` (`sequential` mode); advance `last_index` after successful post
2. **X search**: navigate to `https://x.com/search?q={KEYWORD}&src=typed_query&f=top`
3. **Network capture**: extract top tweets from `SearchTimeline` GraphQL response
4. **Score and rank**: `score = likes + retweets*2 + replies*1.5 + bookmarks*1.5 + quotes*2`
5. **Generate report**: output to `workspaces/x-posting/<date>/topics/TOPICS_<kw-slug>.md`
6. **Display Top 5** and wait for user selection

---

## Phase 2 — Case Collection (Style Reference)

Detailed execution parameters: `references/phase2-case-collection.md`

**Overview:**

1. Reuse Phase 1 search results (shared `SearchTimeline` response — no need to re-search)
2. For the top 3 high-engagement tweets, extract: opening hook, paragraph rhythm, emoji density, hashtag usage, media presence (image/video), and CTA type
3. Generate Style Fingerprint and write to `workspaces/x-posting/<date>/style_fingerprint.json`

Phase 2 runs **in parallel with Phase 1** (analyzes the same search response from a different angle).

---

## Phase 3 — Topic Confirmation

> **Hard block**: Phase 3 MUST invoke the AskUserQuestion tool. Do NOT simply print the Top 5 in chat text then `end_turn` waiting for the next user message — that halts the entire flow. AskUserQuestion is the only correct way to end this Phase.

Invoke AskUserQuestion tool, using the Top 5 topics as options (one-line summary of each as the option label):

- Options 1-N: one option per candidate topic
- Option: `skip` — do not post today
- (`Other` is provided automatically by the UI for free-form input such as "1 3")

**After** AskUserQuestion returns the user's answer (not before), write:

1. **Required**: write the selected topic list to `workspaces/x-posting/<date>/selected_topics.json` (schema in `references/phase1-topic-collection.md §5`). This is the input contract for Phase 4 Pre-Write Gate — missing this causes Phase 4 to refuse to start drafting.
2. **Required**: for each selected topic, invoke AskUserQuestion again to confirm "publish now" or "save as draft", and append the answer to the `publish_mode` field of each record in `selected_topics.json`

If user replies "skip" → end this run, do not advance `last_index`, do not create `selected_topics.json`.

---

## Phase 4 — Content Writing

Detailed writing specifications: `references/phase4-writing.md`

> **Hard block**: every draft preview in Phase 4 **MUST** be confirmed via AskUserQuestion tool before deciding next step (publish / revise / save as draft). Do NOT print the preview in chat text then `end_turn` — this halts the flow mid-execution. AskUserQuestion is the only correct pause mechanism in this Phase.

For each selected topic, **draft one at a time**: after drafting, generate preview, **immediately use AskUserQuestion to get user decision**, then start the next.

**Writing framework**: hook (1 line) → pain point / observation / counter-intuitive insight → concrete evidence (numbers / screenshot description / comparison) → call to action (CTA)

**Hard requirements**:
- Body ≤ 280 characters (ASCII = 1 char, CJK = 2 chars, URL = 23 chars)
- No WeChat IDs, phone numbers, or suspicious redirect links
- Hashtags: 0–2, naturally embedded, no spamming
- Must include specific "verifiable details" (numbers, screenshot descriptions, quotes); generic slogans are prohibited
- If image/video: prepare local file, record absolute path

**Pre-Write Gate** (verify all before drafting — if any item is missing, go back to Phase 3 / Phase 2 to fill it):
1. `workspaces/x-posting/<date>/selected_topics.json` exists and contains the topic to draft (produced by Phase 3 — must be on disk, cannot be skipped)
2. `key_quote` (original tweet verbatim) has been extracted from Phase 1
3. `pain_description` has been confirmed from Phase 1
4. Product/project info has been read from `workspaces/x-posting/session_state.json` (for CTA)
5. Style fingerprint (`style_fingerprint.json`) has been read

After drafting, generate HTML preview (see `references/phase4-writing.md §5`), **MUST invoke AskUserQuestion tool** to await user approval:

- question: display preview path + character count + plain text body
- options:
  - `ok` — publish
  - `draft` — save as draft, do not publish
  - `edit` — use Other to enter revision instructions
  - `skip` — skip this post, do not save

**Absolutely prohibited patterns**:
- Print preview to chat text, then `end_turn` waiting for user reply
- Enter Phase 5 without having invoked AskUserQuestion
- Assume user will see the chat preview and reply — the runtime does not guarantee this interaction

---

## Phase 5 — Publishing

Detailed execution parameters: `references/phase5-publish.md`

**Overview:**

1. **Content Verification Gate**: character count ≤ 280, no blacklisted external links, no contact info, image path exists (if with image)
2. **Navigate to compose**: `browser-act --session {SESSION} navigate https://x.com/compose/post`
3. **Fill body text**: locate compose editor via `browser-act --session {SESSION} state`, note `{EDITOR_IDX}` for element with `aria-label="Post text" role=textbox`, then:
   ```bash
   browser-act --session {SESSION} click {EDITOR_IDX}
   browser-act --session {SESSION} input {EDITOR_IDX} "{TWEET_TEXT}"
   ```
   (CDP keyboard path — click before input to avoid first-character loss)
4. **Verify**: `eval "$(python scripts/verify-post-ready.py)"` — confirm `post_enabled: true`
5. **Upload image/video** (optional): `python scripts/inject-media.py "{LOCAL_PATH}" | browser-act --session {SESSION} eval --stdin`
6. **Pre-publish screenshot**: `browser-act --session {SESSION} screenshot workspaces/x-posting/<date>/drafts/<slug>/pre_publish.png` — ask user to confirm via AskUserQuestion
7. **Publish**: `eval "$(python scripts/click-post.py)"`
8. **Capture tweet_id**: `browser-act --session {SESSION} network requests --filter CreateTweet --method POST --format json` → get request_id → `browser-act --session {SESSION} network request <request_id> --format json | python scripts/parse-create-tweet.py`
9. **Write record**: update `workspaces/x-posting/<date>/published.json`; update `session_state.json` fields `posting.last_posted_at` and `today_count`

**Gate**: execute click-post only after user approves content and confirms the screenshot is correct. Automatic publishing of unapproved content is not allowed.

---

## Phase 6 — Performance Tracking

Detailed execution parameters: `references/phase6-tracking.md`

**Standalone trigger**: user says "track performance" / "check metrics" → jump directly to this Phase.

**Sub-actions:**

| Sub-action | Trigger | Description |
|------------|---------|-------------|
| 6.1 Single-post 24h tracking | Auto-scheduled after Phase 5 publish | Revisit tweet_id after 24h, update metrics via `TweetDetail` response |
| 6.2 Batch data collection | User-triggered / weekly | Pull latest data for all tweets in `published.json` from the past N days |
| 6.3 View comments | User-triggered | View new replies, draft responses, invoke AskUserQuestion for approval, then reply (reuse Phase 5 compose flow with `in_reply_to`) |
| 6.4 Generate report | User-triggered | Aggregate `tracking/` data, output table report |

Data is stored locally in `workspaces/x-posting/tracking/`.

---

## Capability Components

> This Skill's operational boundary = what the user can manually do in their browser. It only reads data already displayed to the user on the page, never bypassing authentication or access controls. JS code is encapsulated in Python files under the `scripts/` directory, invoked via `eval "$(python scripts/xxx.py {params})"`. `$(...)` is bash syntax; use the bash tool for execution. **Exception**: `inject-media.py` embeds base64-encoded binary data that can exceed shell argument limits — invoke it via stdin pipe: `python scripts/inject-media.py "{path}" | browser-act --session {SESSION} eval --stdin`.

### DOM: Login Verification

`eval "$(python scripts/check-login.py)"`

Output example:
```json
{
  "logged_in": true,
  "username": "example_user",
  "handle": "@example_user",
  "url": "https://x.com/home",
  "title": "(1) Home / X"
}
```

### Network Capture: Search Tweets (topic collection)

Parameters injected via URL; API response read from traffic (`SearchTimeline` requests contain dynamic `x-client-transaction-id` signatures and cannot be fetched directly):

1. `browser-act --session {SESSION} navigate "https://x.com/search?q={KEYWORD_ENCODED}&src=typed_query&f={top|live}"` (`top` = top results, `live` = most recent)
2. `browser-act --session {SESSION} wait stable --timeout 20000`
3. `browser-act --session {SESSION} network requests --type xhr,fetch --filter SearchTimeline --format json` → get latest `request_id`
4. `browser-act --session {SESSION} network request <request_id> --format json | python scripts/parse-search-timeline.py --top 20 --non-reply-only`

Endpoint characteristic: URL contains `/i/api/graphql/*/SearchTimeline`

Error handling: no matching request found → verify login status, confirm page is `x.com/search`, confirm `wait stable` completed; if still empty, reload page and retry once.

Output example:
```json
{
  "count": 20,
  "tweets": [
    {
      "id": "2000000000000000001",
      "url": "https://x.com/example_author/status/2000000000000000001",
      "text": "Example tweet content here...",
      "lang": "en",
      "created_at": "Mon Jan 01 00:00:00 +0000 2026",
      "author": {
        "screen_name": "example_author",
        "name": "Example Author",
        "followers": 10000,
        "verified": false
      },
      "metrics": {
        "likes": 500,
        "replies": 30,
        "retweets": 80,
        "quotes": 10,
        "bookmarks": 200,
        "views": 50000
      },
      "hashtags": [],
      "mentions": [],
      "has_media": false,
      "media": [],
      "is_reply": false,
      "score": 1005.0
    }
  ]
}
```

### Network Capture: Single Tweet Metrics (performance tracking)

Parameters injected via URL; response read from `TweetDetail` traffic:

1. `browser-act --session {SESSION} navigate "https://x.com/{SCREEN_NAME}/status/{TWEET_ID}"`
2. `browser-act --session {SESSION} wait stable --timeout 20000`
3. `browser-act --session {SESSION} network requests --type xhr,fetch --filter TweetDetail --format json` → get latest `request_id`
4. `browser-act --session {SESSION} network request <request_id> --format json | python scripts/parse-tweet-detail.py {TWEET_ID}`

Endpoint characteristic: URL contains `/i/api/graphql/*/TweetDetail`

Error handling: `tweet-{id}` not found in entries → tweet may have been deleted, set to private, or URL redirected to other content; verify URL and retry once.

Output example:
```json
{
  "id": "2000000000000000001",
  "url": "https://x.com/example_author/status/2000000000000000001",
  "text": "Example tweet content here...",
  "lang": "en",
  "created_at": "Mon Jan 01 00:00:00 +0000 2026",
  "author": {"screen_name": "example_author", "name": "Example Author"},
  "metrics": {"likes": 500, "replies": 30, "retweets": 80, "quotes": 10, "bookmarks": 200, "views": 50000}
}
```

### DOM: Fill Compose Body (CDP keyboard path — primary)

Draft.js (the rich-text framework X compose uses) only accepts real keyboard events. `document.execCommand('insertText')` can write characters to the DOM but does not update Draft.js internal `EditorState` — Post button remains disabled. The only reliable text injection path is via CDP `Input.dispatchKeyEvent`, i.e., `browser-act input`.

```bash
# 1. Navigate to compose page
browser-act --session {SESSION} navigate "https://x.com/compose/post"
browser-act --session {SESSION} wait stable --timeout 15000

# 2. Locate compose editor (role=textbox with aria-label="Post text")
browser-act --session {SESSION} state
# Find *[N]<div aria-label=Post text role=textbox /> in output, record N as {EDITOR_IDX}

# 3. Click to focus first, then input (two separate steps — avoids first-character loss)
browser-act --session {SESSION} click {EDITOR_IDX}
browser-act --session {SESSION} input {EDITOR_IDX} "{TWEET_TEXT}"

# 4. Verify Draft.js accepted the text and Post button is enabled
eval "$(python scripts/verify-post-ready.py)"
```

`verify-post-ready.py` output example:
```json
{
  "compose_text": "your tweet text here",
  "compose_length": 20,
  "post_enabled": true,
  "post_button_found": true,
  "media_attached": 0
}
```

Error handling:
- `compose_text` missing first character → click and input MUST be two separate steps; if character still missing, use `eval "$(python scripts/clear-compose.py)"` then retry
- `post_enabled: false` but `compose_text` is correct → confirm you are on `/compose/post` modal (not the `/home` inline composer); home inline compose requires an initial expand click
- `compose_text` is empty → CDP keyboard event did not land on the correct element; re-run `browser-act --session {SESSION} state` to refresh the index and retry

### DOM: Fill Compose (JS path — diagnostic only, unreliable)

`eval "$(python scripts/fill-compose.py '{TWEET_TEXT}')"`

Attempts to write text via `beforeinput` + `execCommand('insertText')` + `input` events. **Not recommended as a publishing path** — in the current version of X, Draft.js ignores these synthetic events in most cases; the DOM shows the text but the Post button remains disabled.

Retain this capability only for:
- Diagnosing whether the page DOM structure is intact
- Future fallback if X replaces Draft.js

### DOM: Clear Compose

`eval "$(python scripts/clear-compose.py)"`

Use before retry after a failed publish to reset the input field.

Output example:
```json
{ "cleared": true, "remaining": "\n" }
```

### DOM: Verify Post Ready

`eval "$(python scripts/verify-post-ready.py)"`

Check that Draft.js has accepted compose text and the Post button is enabled. Run after `browser-act input` to confirm text was registered.

Output example: see CDP keyboard path section above.

### DOM: Upload Image / Video

`python scripts/inject-media.py "{LOCAL_PATH}" [--mime image/png] | browser-act --session {SESSION} eval --stdin`

> **Why stdin pipe**: this script base64-encodes the media file inline in JS. Large files produce output that exceeds shell command-line length limits, making `eval "$(python ...)"` unreliable. Stdin pipe is the correct invocation for this script.

Parameters:
- `LOCAL_PATH`: absolute or relative path to the local media file. Supported: `image/jpeg`, `image/png`, `image/webp`, `image/gif`, `video/mp4`, `video/quicktime`
- `--mime`: override MIME type (default: guessed from file extension)

Output example:
```json
{
  "injected": true,
  "filename": "cover.png",
  "mime": "image/png",
  "size_bytes": 102400,
  "preview_visible": true
}
```

Error handling: `preview_visible: false` but `injected: true` → wait 1–2 seconds then re-run `browser-act --session {SESSION} state` to check; X silently rejects oversized files (images >5MB, videos >512MB) or unsupported formats.

### DOM: Click Publish

`eval "$(python scripts/click-post.py)"`

Verifies the Post button is not disabled, then clicks it. Ensure the Content Verification Gate has passed and the user has given final approval before running this.

Output example:
```json
{ "clicked": true, "button_text": "Post" }
```

Error handling: `clicked: false, message: "post button disabled"` → text is empty, exceeds 280 characters, or attachment upload not yet complete; `message: "post button not found"` → not on the compose page.

### Parser: CreateTweet Response (extract new tweet ID)

After publishing, capture the `CreateTweet` response from network traffic to get the new tweet ID:

1. `browser-act --session {SESSION} network requests --type xhr,fetch --filter CreateTweet --method POST --format json` → get latest `request_id`
2. `browser-act --session {SESSION} network request <request_id> --format json | python scripts/parse-create-tweet.py`

Endpoint characteristic: `POST /i/api/graphql/*/CreateTweet`

Output example:
```json
{
  "id": "2000000000000000001",
  "url": "https://x.com/example_author/status/2000000000000000001",
  "author": "example_author",
  "text": "your published tweet text",
  "created_at": "Mon Jan 01 00:00:00 +0000 2026"
}
```

Error handling: `errors` field contains `duplicate_tweet` → content duplicates a recent tweet; `rest_id` missing → navigate to own profile to observe new tweet.

---

## Pagination

**DOM Pagination** (SearchTimeline): Search results load as an infinite scroll. Trigger more: `browser-act --session {SESSION} scroll down --amount 1500` → `browser-act --session {SESSION} wait stable --timeout 10000` → re-run `parse-search-timeline.py`. Termination: `count` does not increase across 2 consecutive scrolls, or target tweet count is reached.

---

## Success Criteria

- `logged_in: true` returned by `check-login.py` eval
- `SearchTimeline` network request captured with `count >= 1` after keyword search
- `post_enabled: true` returned by `verify-post-ready.py` after CDP text fill (`compose_text` non-null)
- `clicked: true` returned by `click-post.py`
- `CreateTweet` response captured with `id` non-null within 10 seconds of clicking Post
- `published.json` record count increments by 1 after each successful post

## Known Limitations

- **`x-client-transaction-id` dynamic signature**: all GraphQL endpoints (SearchTimeline, TweetDetail, CreateTweet) include a per-request dynamically generated signature header. This Skill does not reproduce that header — all API access uses the "browser sends request, we read the response" path. This is also why the Skill must run inside a real logged-in browser
- **Draft.js rejects execCommand**: `document.execCommand('insertText')` only updates DOM without triggering React state — submit button stays disabled. Must use `browser-act input` (CDP keyboard path) for reliable text injection
- **280-character limit**: hard limit for free accounts; exceeding it causes truncation or publish failure
- **View count delay**: newly published tweets may have `views` as `null` or `0` for minutes to hours before data appears
- **Hashtag autocomplete unresponsive to programmatic input**: embed `#tag` text directly in the body; do not attempt to trigger the autocomplete dropdown
- **inject-media size limit**: X silently rejects images >5MB and videos >512MB; compress before injection if needed
- **API endpoint query_id may change**: hashes in GraphQL URLs (e.g., CreateTweet) may update on X deploys; since this Skill reads responses rather than calling APIs directly, hash changes have no impact

## Execution Efficiency

- **Batch orchestration**: write a bash script to loop through command templates serially within a single session; do not parallelize within one browser (prone to triggering anti-scraping restrictions). Refer to rate information in "Known Limitations" above to add appropriate intervals
- **Test before batch execution**: after writing a batch script, first test with 1–2 items to verify the script runs correctly; only then run the full batch. Never skip testing and execute in batch directly
- **Reduce redundant pre-operations**: when multiple steps depend on the same prerequisite state, complete them in batch under that state to avoid repeatedly establishing the same state
- **Error resumption**: save results item by item during batch processing; on failure, resume from the breakpoint rather than starting over

## Experience Notes

Path: `{working-directory}/browser-act-skill-forge-memories/x-auto-posting-x-auto-posting.memory.md` (working directory is determined by the Agent running the Skill, typically the project root or current working directory)

**Before execution**: if the file exists, read it first — it records unexpected situations encountered during past executions (e.g., a strategy has become ineffective); adjust strategy order accordingly.

**After execution**: if an unexpected situation is encountered (strategy became ineffective, X UI redesigned, anti-scraping upgraded, better path discovered), append a line:
`{YYYY-MM-DD}: {what happened} → {conclusion}`

Normal execution does not write to the file. Do not record which keywords were used or how many results were obtained — those are task outputs, not experience.
