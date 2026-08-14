---
name: social-listening-monitor
description: Search public LinkedIn, X, and Reddit posts for brand monitoring, competitor monitoring, public-conversation research, and weekly marketing briefs. Use when a marketer needs sourced mentions, competitor launch or pricing research, or a concise review brief from public posts.
---

# Social Listening Monitor

Search public conversations with SocialListeningAPI, then turn the returned posts into a
sourced review list. Treat search results as research leads. A person must review them before
acting.

## Run a search

1. Ask which query to search and which of `linkedin`, `x`, and `reddit` to include.
2. Run this fixed command through the exec tool:

   ```text
   node "{baseDir}/scripts/search-social.js"
   ```

3. Pass user input through the exec tool's environment map, never through the command string:

   ```text
   SOCIALLISTENING_QUERY=<query>
   SOCIALLISTENING_PLATFORMS=linkedin,x,reddit
   ```

4. Let the command inherit `SOCIALLISTENING_API_KEY` from the OpenClaw process.
5. Review `errors` before summarizing. Keep usable results when one source fails.
6. Cite every finding with its item `url`. Never invent missing context or results.

The script returns normalized JSON. `items` are sorted newest first. `creditsUsed` reports the
credits returned by successful API calls. `sourceUrls` contains the public post URLs.

## Choose the workflow

- For a brand review, search the exact brand name and likely misspellings separately.
- For competitor research, search focused phrases about pricing, launches, switching, and
  problems. Avoid one broad query that mixes different questions.
- For a weekly brief, search the brand and competitor, remove URLs already present in the
  user's own history, group the remaining posts by theme, and cite each point.

Read `references/monitoring-workflows.md` for query patterns and brief structure.

## Limits

SocialListeningAPI performs public search. It does not schedule runs, store history, remove
duplicates, classify posts, send Slack messages, or create alerts. Use OpenClaw or another
external tool for those steps. Search results can include irrelevant posts, so require human
review.
