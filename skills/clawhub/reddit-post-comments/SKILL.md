---
name: reddit-post-comments
description: "Fetches Reddit comment threads from a post via Reddit's public JSON API, returning flat structured comment records. Input: post ID, optional limit per batch (up to 500), comment depth, and date range filters for created_utc. Handles nested reply trees recursively and paginated overflow batches via the morechildren endpoint. Output: flat JSON array of comment objects with 30+ fields — id, post_id, parent_id, body, author, score, depth, created_utc, url, is_submitter, controversiality, collapsed state, and engagement metrics — plus more_ids list for additional batches. Use when user mentions Reddit comments, Reddit replies, fetch comments, Reddit discussion, comment thread, scrape comments, post comments, Reddit comment body, top comments, replies tree, collect comments, comment score, Reddit thread comments, extract replies, read comments from a Reddit post, Reddit comment section, comment data."
---

# Reddit — Post Comments

> Post ID → flat structured comment records with 30+ fields per comment

## Language

All process output to user (progress updates, process notifications) follows the user's language.

## Objective

Collect all comments from a Reddit post including nested replies using Reddit's public JSON API, with support for paginated overflow batches via the morechildren endpoint.

## Prerequisites

- A reddit.com page is open in the browser

## Pre-execution Checks

### 1. Tool Readiness

If browser-act has been confirmed available in the current session → skip this step.

Invoke `browser-act` via Skill tool to load usage. If installation or configuration issues arise, follow its guidance to resolve then retry.

## Capability Components

> This Skill's operational boundary = what the user can manually do in their browser. It only reads data already displayed to the user on the page, never bypassing authentication or access controls. Its role is equivalent to copy-pasting on the user's behalf — the data is already on screen, automation merely saves time. JS code is encapsulated in Python files under the `scripts/` directory, invoked via `eval "$(python scripts/xxx.py {params})"`. `$(...)` is bash syntax; it is recommended to use the bash tool for execution.

Below are all atomic capabilities discovered and verified during the exploration phase, listed by command template with parameters. Simply invoke them as needed — no need to read `scripts/*.py` source code or re-verify. Only inspect scripts when execution fails for troubleshooting. Combine freely as needed during execution.

### API: Fetch post and initial comment batch

```bash
eval "$(python scripts/fetch-comments.py '{post_id}' --limit 500)"
```

Parameters:
- `post_id` (positional): Reddit post ID — the alphanumeric segment from a post URL, e.g. `1s80pf6` from `reddit.com/r/sub/comments/1s80pf6/title/`
- `--limit`: max comments per initial fetch, 1–500 (default: `500`); higher values retrieve more nested replies in one call
- `--depth`: max nesting depth for reply trees (default: `10`)
- `--date-from`: lower date bound for comments — ISO-8601 or `YYYY-MM-DD` (default: empty)
- `--date-to`: upper date bound for comments — ISO-8601 or `YYYY-MM-DD` (default: empty)

Output example:
```json
{
  "post_id": "1s80pf6",
  "post_title": "You don't need to pay for AI tools right now",
  "post_url": "https://www.reddit.com/r/PromptEngineering/comments/1s80pf6/you_dont_need_to_pay_for_ai_tools/",
  "comments": [
    {
      "kind": "comment",
      "id": "oe2cxue",
      "post_id": "1s80pf6",
      "post_url": "https://www.reddit.com/r/PromptEngineering/comments/1s80pf6/you_dont_need_to_pay_for_ai_tools/",
      "parent_id": "t3_1s80pf6",
      "body": "Is there anything free for short animations?",
      "author": "Dtgallaspy",
      "score": 20,
      "subreddit": "PromptEngineering",
      "created_utc": "2026-06-15T10:13:48.000Z",
      "url": "https://www.reddit.com/r/PromptEngineering/comments/1s80pf6/title/oe2cxue/",
      "permalink": "/r/PromptEngineering/comments/1s80pf6/title/oe2cxue/",
      "canonical_url": "https://www.reddit.com/r/PromptEngineering/comments/1s80pf6/title/oe2cxue/",
      "old_reddit_url": "https://old.reddit.com/r/PromptEngineering/comments/1s80pf6/title/oe2cxue/",
      "root_comment_id": "oe2cxue",
      "parent_kind": "post",
      "is_deleted_or_removed": false,
      "subreddit_id": "t5_2rc7j",
      "subreddit_name_prefixed": "r/PromptEngineering",
      "edited": false,
      "retrieved_at": "2026-07-14T08:20:02.983Z",
      "age_hours": 720.1,
      "body_length": 44,
      "word_count": 8,
      "score_per_hour": 0.03,
      "stickied": false,
      "distinguished": null,
      "is_submitter": false,
      "score_hidden": false,
      "controversiality": 0,
      "depth": 0,
      "total_awards_received": 0,
      "gilded": 0,
      "author_fullname": "t2_dr3vyilor",
      "author_flair_text": null,
      "author_premium": false,
      "collapsed": false,
      "collapsed_reason": null,
      "collapsed_because_crowd_control": false,
      "unrepliable_reason": null
    }
  ],
  "more_ids": ["odeaj5d", "odjksfx", "odmcv9f"],
  "count": 89,
  "has_more": false
}
```

Error handling: `error: true` with `message: "HTTP 404 for post {id}"` when post is not found or has been deleted.

### API: Fetch additional comment batch (morechildren)

When the initial fetch returns a non-empty `more_ids` list, call this to retrieve additional comments in batches:

```bash
eval "$(python scripts/more-comments.py '{post_id}' --children '{id1,id2,id3,...}')"
```

Parameters:
- `post_id` (positional): Reddit post ID matching the initial fetch
- `--children`: comma-separated comment IDs from the `more_ids` field of a previous response; process in batches of up to 100 IDs at a time
- `--date-from`: lower date bound for comments — ISO-8601 or `YYYY-MM-DD` (default: empty)
- `--date-to`: upper date bound for comments — ISO-8601 or `YYYY-MM-DD` (default: empty)

Output example:
```json
{
  "comments": [
    {
      "kind": "comment",
      "id": "odeaj5d",
      "post_id": "1s80pf6",
      "post_url": "https://www.reddit.com/comments/1s80pf6/",
      "parent_id": "t3_1s80pf6",
      "body": "For automation use n8n instead of Zapier or Make...",
      "author": "some_user",
      "score": 15,
      "depth": 0
    }
  ],
  "more_ids": [],
  "count": 7,
  "has_more": false
}
```

Error handling: Returns `{error: true, message: "No children IDs provided via --children"}` when `--children` is empty. Returns `{error: true, message: "HTTP {status}"}` on API failure.

### Composite: Full comment thread collection

To collect all comments from a post including all overflow batches:

1. `eval "$(python scripts/fetch-comments.py '{post_id}' --limit 500)"` — initial fetch; collect `comments` array, capture `more_ids`
2. Chunk `more_ids` into batches of up to 100 IDs each
3. For each batch: `eval "$(python scripts/more-comments.py '{post_id}' --children '{batch_ids}')"` — collect `comments`, append any new `more_ids` to the remaining queue
4. Repeat step 3 until `more_ids` queue is empty
5. Merge all `comments` arrays; deduplication key: `id`

## Pagination

**API Pagination**: `more_ids` field in each response provides the next batch of IDs. Pass as `--children` to more-comments. Termination: `more_ids` is empty and `has_more` is `false`.

## Success Criteria

`result.count >= 1` and `result.comments[0].id` is a non-empty string

## Known Limitations

- Reddit's initial comment endpoint returns up to ~500 top-level comments per call with recursive replies included; highly threaded posts require multiple morechildren batches to collect all comments
- Anonymous API access is subject to Reddit's 60 requests/minute rate limit; add 1–2 second delays between morechildren batch calls
- Collapsed or crowd-control-hidden comments are included with `collapsed: true`; deleted/removed comments appear with `body: "[deleted]"` or `body: "[removed]"`
- `--depth` only affects the initial fetch; morechildren responses do not carry depth nesting
- Post IDs must be extracted from the post URL — the alphanumeric segment after `/comments/`

## Execution Efficiency

- **Batch orchestration**: Write a bash script to loop through the command templates serially within a single session; do not parallelize within one browser. Add 1–2 second delays between morechildren batch calls to respect the rate limit. For higher throughput, distribute posts across multiple parallel browser sessions
- **Test before batch execution**: After writing a batch script, you must first test with 1-2 items to verify the script runs correctly; only then run the full batch. Never skip testing and execute in batch directly
- **Reduce redundant pre-operations**: When multiple steps depend on the same prerequisite state, complete them in batch under that state to avoid repeatedly establishing the same state
- **Error resumption**: Save results item by item during batch processing; on failure, resume from the breakpoint rather than starting over

## Experience Notes

Path: `{working-directory}/browser-act-skill-forge-memories/reddit-search-scraper-reddit-post-comments.memory.md` (working directory is determined by the Agent running the Skill, typically the project root or current working directory)

**Before execution**: If the file exists, read it first — it records unexpected situations encountered during past executions (e.g., a strategy has become ineffective); adjust strategy order accordingly.

**After execution**: If an unexpected situation is encountered (strategy became ineffective, page redesigned, anti-scraping upgraded, better path discovered), append a line:
`{YYYY-MM-DD}: {what happened} → {conclusion}`

Normal execution does not write to the file. Do not record what keywords were used or how many results were returned — those are task outputs, not experience.
