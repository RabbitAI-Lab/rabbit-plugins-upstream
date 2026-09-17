# news-briefing-research — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Endpoints this skill uses, grouped by platform. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**28 endpoints across 5 platform group(s).**

## GDELT (12)

### `gdelt_context`

- **HTTP:** `GET /gdelt/context`
- **What:** Sentence-level co-occurrence search across recent GDELT coverage. Search recent (last 72 hours) GDELT-monitored news for.
- **Params:** `domain` (string, optional) — Convenience domain filter, appended to the query as domain:VALUE.; `from` (string, optional) — Start of an absolute time window. Accepts YYYY-MM-DD, RFC3339, or GDELT's raw YYYYMMDDHHMMSS. Cannot be combined with timespan; GDELT caps this endpoint's window at 72 hours.; `is_quote` (boolean, optional) — Only return sentences GDELT identified as a quotation.; `language` (string, optional) — Source-language filter (GDELT's searchlang parameter). Space-segmented languages only (excludes CJK and similar).; `maxrecords` (integer, optional) — Rows to return. GDELT's own hard cap is 200 for this endpoint (lower than gdelt-search's 250); there is no pagination cursor beyond it.; `query` (string, **required**) — GDELT query string. All terms must co-occur in the same sentence. Supports quoted phrases, (a OR b), domain:example.com.; `sort` (string, optional) — Result order.; `timespan` (string, optional) — Relative time window ending now, e.g. 30min, 6h, 3d. Cannot be combined with from/to. GDELT caps this endpoint's window at 72 hours.; `to` (string, optional) — End of an absolute time window. Same formats as from.

### `gdelt_search`

- **HTTP:** `GET /gdelt/search`
- **What:** Search global news coverage indexed by GDELT. Search the GDELT Project's continuously updated global news.
- **Params:** `country` (string, optional) — Convenience source-country filter, appended to the query as sourcecountry:VALUE. Accepts a GDELT-recognized country name (no spaces) or 2-letter FIPS code.; `domain` (string, optional) — Convenience domain filter, appended to the query as domain:VALUE.; `from` (string, optional) — Start of an absolute time window. Accepts YYYY-MM-DD, RFC3339, or GDELT's raw YYYYMMDDHHMMSS. Cannot be combined with timespan; GDELT only indexes roughly the last 3 months.; `language` (string, optional) — Convenience source-language filter, appended to the query as sourcelang:VALUE. Accepts a GDELT-recognized language name or 3-letter code.; `maxrecords` (integer, optional) — Rows to return. GDELT's own hard cap is 250; there is no pagination cursor beyond it.; `query` (string, **required**) — GDELT query string. Supports GDELT's own search operators: quoted phrases, (a OR b), theme:NAME, tone<N / tone>N, near20:\; `sort` (string, optional) — Result order.; `timespan` (string, optional) — Relative time window ending now, e.g. 1h, 2d, 1w, 3m. Cannot be combined with from/to.; `to` (string, optional) — End of an absolute time window. Same formats as from.

### `gdelt_timeline`

- **HTTP:** `GET /gdelt/timeline`
- **What:** Coverage volume or tone over time for a GDELT query. Return how a query's global news coverage has trended over.
- **Params:** `country` (string, optional) — Convenience source-country filter, appended to the query as sourcecountry:VALUE.; `domain` (string, optional) — Convenience domain filter, appended to the query as domain:VALUE.; `from` (string, optional) — Start of an absolute time window. Accepts YYYY-MM-DD, RFC3339, or GDELT's raw YYYYMMDDHHMMSS. Cannot be combined with timespan.; `language` (string, optional) — Convenience source-language filter, appended to the query as sourcelang:VALUE.; `metric` (string, optional) — Timeline metric. lang and country return one series per language/country instead of one aggregate series.; `query` (string, **required**) — GDELT query string. Same syntax as gdelt-search's query.; `smooth` (integer, optional) — Moving-window smoothing applied to the timeline, in steps. 0 disables smoothing.; `timespan` (string, optional) — Relative time window ending now, e.g. 1h, 2d, 1w, 3m. Cannot be combined with from/to.; `to` (string, optional) — End of an absolute time window. Same formats as from.

### `gdelt_tonechart`

- **HTTP:** `GET /gdelt/tonechart`
- **What:** Sentiment histogram for a GDELT query. Return a sentiment (tone) histogram for a query's matching.
- **Params:** `country` (string, optional) — Convenience source-country filter, appended to the query as sourcecountry:VALUE.; `domain` (string, optional) — Convenience domain filter, appended to the query as domain:VALUE.; `from` (string, optional) — Start of an absolute time window. Accepts YYYY-MM-DD, RFC3339, or GDELT's raw YYYYMMDDHHMMSS. Cannot be combined with timespan.; `language` (string, optional) — Convenience source-language filter, appended to the query as sourcelang:VALUE.; `query` (string, **required**) — GDELT query string. Same syntax as gdelt-search's query.; `timespan` (string, optional) — Relative time window ending now, e.g. 1h, 2d, 1w, 3m. Cannot be combined with from/to.; `to` (string, optional) — End of an absolute time window. Same formats as from.

### `gdelt_tv_concept_entities`

- **HTTP:** `GET /gdelt/tv-concept-entities`
- **What:** List GDELT Television 2.0 AI concept entities. Return GDELT's own catalog of Google Knowledge Graph concept.
- **Params:** `limit` (integer, optional) — Maximum entries to return, most-frequent first.

### `gdelt_tv_search`

- **HTTP:** `GET /gdelt/tv-search`
- **What:** Search US television news coverage (transcripts, captions, OCR, visual labels). Search GDELT's Television 2.0 AI index of US television news.
- **Params:** `caption` (array, optional) — Search human-provided closed captioning (GDELT's cap: operator). Repeatable; multiple values are OR'd together.; `concept` (array, optional) — Search Google Knowledge Graph concepts extracted from captioning, by MID code (GDELT's capnlp: operator). Repeatable; multiple values are OR'd together.; `day_of_week` (integer, optional) — Limit to a day of week, 0 (Sunday) through 7 (Saturday), PST.; `exclude_caption` (array, optional) — Exclude clips whose closed captioning matches this value (GDELT's -cap: operator). Repeatable; every value must be absent.; `exclude_concept` (array, optional) — Exclude clips whose extracted concepts match this MID code (GDELT's -capnlp: operator). Repeatable; every value must be absent.; `exclude_onscreen_text` (array, optional) — Exclude clips whose OCR'd onscreen text matches this value (GDELT's -ocr: operator). Repeatable; every value must be absent.; `exclude_transcript` (array, optional) — Exclude clips whose speech-to-text transcript matches this value (GDELT's -asr: operator). Repeatable; every value must be absent.; `exclude_visual` (array, optional) — Exclude clips whose visual labels match this value (GDELT's -visual: operator). Repeatable; every value must be absent.; `from` (string, optional) — Start of an absolute time window. Accepts YYYY-MM-DD, RFC3339, or GDELT's raw YYYYMMDDHHMMSS. Cannot be combined with timespan.; `maxrecords` (integer, optional) — Rows to return. GDELT's own hard cap is 3000 for this endpoint; there is no pagination cursor beyond it.; `onscreen_text` (array, optional) — Search OCR'd onscreen text/chyrons (GDELT's ocr: operator). Repeatable; multiple values are OR'd together. Short phrases only (GDELT caps each at 5 words).; `show` (string, optional) — Limit to an exact show name.; `sort` (string, optional) — Result order.; `station` (string, **required**) — Station to search.; `timespan` (string, optional) — Relative time window ending now, e.g. 1h, 7d, 3m, 1y. Cannot be combined with from/to. GDELT's TV archive starts July 6, 2010.; `to` (string, optional) — End of an absolute time window. Same formats as from.; `transcript` (array, optional) — Search machine-generated speech-to-text transcripts (GDELT's asr: operator). Repeatable; multiple values are OR'd together. Short phrases only (GDELT caps each at 5 words).; `visual` (array, optional) — Search visual object/activity labels from computer vision (GDELT's visual: operator). Repeatable; multiple values are OR'd together.

### `gdelt_tv_showchart`

- **HTTP:** `GET /gdelt/tv-showchart`
- **What:** Top US television shows by coverage share for a query. Return the top shows by result percentage for a query.
- **Params:** `caption` (array, optional) — Search human-provided closed captioning (GDELT's cap: operator). Repeatable; multiple values are OR'd together.; `concept` (array, optional) — Search Google Knowledge Graph concepts extracted from captioning, by MID code (GDELT's capnlp: operator). Repeatable; multiple values are OR'd together.; `exclude_caption` (array, optional) — Exclude clips whose closed captioning matches this value (GDELT's -cap: operator). Repeatable; every value must be absent.; `exclude_concept` (array, optional) — Exclude clips whose extracted concepts match this MID code (GDELT's -capnlp: operator). Repeatable; every value must be absent.; `exclude_onscreen_text` (array, optional) — Exclude clips whose OCR'd onscreen text matches this value (GDELT's -ocr: operator). Repeatable; every value must be absent.; `exclude_transcript` (array, optional) — Exclude clips whose speech-to-text transcript matches this value (GDELT's -asr: operator). Repeatable; every value must be absent.; `exclude_visual` (array, optional) — Exclude clips whose visual labels match this value (GDELT's -visual: operator). Repeatable; every value must be absent.; `from` (string, optional) — Start of an absolute time window. Accepts YYYY-MM-DD, RFC3339, or GDELT's raw YYYYMMDDHHMMSS. Cannot be combined with timespan.; `onscreen_text` (array, optional) — Search OCR'd onscreen text/chyrons (GDELT's ocr: operator). Repeatable; multiple values are OR'd together. Short phrases only (GDELT caps each at 5 words).; `show` (string, optional) — Limit to an exact show name.; `station` (array, **required**) — Required, repeatable. One or more stations, OR'd together.; `timespan` (string, optional) — Relative time window ending now, e.g. 1h, 7d, 3m, 1y. Cannot be combined with from/to. Omit both for GDELT's full archive (auto-resolution, back to July 6, 2010).; `to` (string, optional) — End of an absolute time window. Same formats as from.; `transcript` (array, optional) — Search machine-generated speech-to-text transcripts (GDELT's asr: operator). Repeatable; multiple values are OR'd together. Short phrases only (GDELT caps each at 5 words).; `visual` (array, optional) — Search visual object/activity labels from computer vision (GDELT's visual: operator). Repeatable; multiple values are OR'd together.

### `gdelt_tv_stationchart`

- **HTTP:** `GET /gdelt/tv-stationchart`
- **What:** Compare US television news coverage across stations. Return a result-count comparison across the requested.
- **Params:** `caption` (array, optional) — Search human-provided closed captioning (GDELT's cap: operator). Repeatable; multiple values are OR'd together.; `concept` (array, optional) — Search Google Knowledge Graph concepts extracted from captioning, by MID code (GDELT's capnlp: operator). Repeatable; multiple values are OR'd together.; `exclude_caption` (array, optional) — Exclude clips whose closed captioning matches this value (GDELT's -cap: operator). Repeatable; every value must be absent.; `exclude_concept` (array, optional) — Exclude clips whose extracted concepts match this MID code (GDELT's -capnlp: operator). Repeatable; every value must be absent.; `exclude_onscreen_text` (array, optional) — Exclude clips whose OCR'd onscreen text matches this value (GDELT's -ocr: operator). Repeatable; every value must be absent.; `exclude_transcript` (array, optional) — Exclude clips whose speech-to-text transcript matches this value (GDELT's -asr: operator). Repeatable; every value must be absent.; `exclude_visual` (array, optional) — Exclude clips whose visual labels match this value (GDELT's -visual: operator). Repeatable; every value must be absent.; `from` (string, optional) — Start of an absolute time window. Accepts YYYY-MM-DD, RFC3339, or GDELT's raw YYYYMMDDHHMMSS. Cannot be combined with timespan.; `onscreen_text` (array, optional) — Search OCR'd onscreen text/chyrons (GDELT's ocr: operator). Repeatable; multiple values are OR'd together. Short phrases only (GDELT caps each at 5 words).; `show` (string, optional) — Limit to an exact show name.; `station` (array, **required**) — Required, repeatable. One or more stations, OR'd together.; `timespan` (string, optional) — Relative time window ending now, e.g. 1h, 7d, 3m, 1y. Cannot be combined with from/to. Omit both for GDELT's full archive (auto-resolution, back to July 6, 2010).; `to` (string, optional) — End of an absolute time window. Same formats as from.; `transcript` (array, optional) — Search machine-generated speech-to-text transcripts (GDELT's asr: operator). Repeatable; multiple values are OR'd together. Short phrases only (GDELT caps each at 5 words).; `visual` (array, optional) — Search visual object/activity labels from computer vision (GDELT's visual: operator). Repeatable; multiple values are OR'd together.

### `gdelt_tv_stationdetails`

- **HTTP:** `GET /gdelt/tv-stationdetails`
- **What:** List GDELT Television 2.0 AI stations. Return GDELT's own current list of Television 2.0 AI.
- **Params:** _none_

### `gdelt_tv_timeline`

- **HTTP:** `GET /gdelt/tv-timeline`
- **What:** Airtime volume over time for US television news coverage. Return how much airtime a query's matching US television.
- **Params:** `caption` (array, optional) — Search human-provided closed captioning (GDELT's cap: operator). Repeatable; multiple values are OR'd together.; `concept` (array, optional) — Search Google Knowledge Graph concepts extracted from captioning, by MID code (GDELT's capnlp: operator). Repeatable; multiple values are OR'd together.; `exclude_caption` (array, optional) — Exclude clips whose closed captioning matches this value (GDELT's -cap: operator). Repeatable; every value must be absent.; `exclude_concept` (array, optional) — Exclude clips whose extracted concepts match this MID code (GDELT's -capnlp: operator). Repeatable; every value must be absent.; `exclude_onscreen_text` (array, optional) — Exclude clips whose OCR'd onscreen text matches this value (GDELT's -ocr: operator). Repeatable; every value must be absent.; `exclude_transcript` (array, optional) — Exclude clips whose speech-to-text transcript matches this value (GDELT's -asr: operator). Repeatable; every value must be absent.; `exclude_visual` (array, optional) — Exclude clips whose visual labels match this value (GDELT's -visual: operator). Repeatable; every value must be absent.; `from` (string, optional) — Start of an absolute time window. Accepts YYYY-MM-DD, RFC3339, or GDELT's raw YYYYMMDDHHMMSS. Cannot be combined with timespan.; `onscreen_text` (array, optional) — Search OCR'd onscreen text/chyrons (GDELT's ocr: operator). Repeatable; multiple values are OR'd together. Short phrases only (GDELT caps each at 5 words).; `show` (string, optional) — Limit to an exact show name.; `station` (string, **required**) — Station to search.; `timespan` (string, optional) — Relative time window ending now, e.g. 1h, 7d, 3m, 1y. Cannot be combined with from/to. Omit both for GDELT's full archive (auto-resolution, back to July 6, 2010).; `to` (string, optional) — End of an absolute time window. Same formats as from.; `transcript` (array, optional) — Search machine-generated speech-to-text transcripts (GDELT's asr: operator). Repeatable; multiple values are OR'd together. Short phrases only (GDELT caps each at 5 words).; `visual` (array, optional) — Search visual object/activity labels from computer vision (GDELT's visual: operator). Repeatable; multiple values are OR'd together.

### `gdelt_tv_visual_entities`

- **HTTP:** `GET /gdelt/tv-visual-entities`
- **What:** List GDELT Television 2.0 AI visual entities. Return GDELT's own catalog of computer-vision object/activity.
- **Params:** `limit` (integer, optional) — Maximum entries to return, most-frequent first.

### `gdelt_tv_wordcloud`

- **HTTP:** `GET /gdelt/tv-wordcloud`
- **What:** Word cloud for US television news coverage. Return a frequency-ranked word/label cloud for one match.
- **Params:** `caption` (array, optional) — Search human-provided closed captioning (GDELT's cap: operator). Repeatable; multiple values are OR'd together.; `channel` (string, **required**) — Required. Which match channel to build a word cloud from.; `concept` (array, optional) — Search Google Knowledge Graph concepts extracted from captioning, by MID code (GDELT's capnlp: operator). Repeatable; multiple values are OR'd together.; `day_of_week` (string, optional) — Limit to a day of week, 0 (Sunday) through 7 (Saturday), PST.; `exclude_caption` (array, optional) — Exclude clips whose closed captioning matches this value (GDELT's -cap: operator). Repeatable; every value must be absent.; `exclude_concept` (array, optional) — Exclude clips whose extracted concepts match this MID code (GDELT's -capnlp: operator). Repeatable; every value must be absent.; `exclude_onscreen_text` (array, optional) — Exclude clips whose OCR'd onscreen text matches this value (GDELT's -ocr: operator). Repeatable; every value must be absent.; `exclude_transcript` (array, optional) — Exclude clips whose speech-to-text transcript matches this value (GDELT's -asr: operator). Repeatable; every value must be absent.; `exclude_visual` (array, optional) — Exclude clips whose visual labels match this value (GDELT's -visual: operator). Repeatable; every value must be absent.; `from` (string, optional) — Start of an absolute time window. Accepts YYYY-MM-DD, RFC3339, or GDELT's raw YYYYMMDDHHMMSS. Cannot be combined with timespan.; `onscreen_text` (array, optional) — Search OCR'd onscreen text/chyrons (GDELT's ocr: operator). Repeatable; multiple values are OR'd together. Short phrases only (GDELT caps each at 5 words).; `show` (string, optional) — Limit to an exact show name.; `station` (string, **required**) — Required. Station to search.; `timespan` (string, optional) — Relative time window ending now, e.g. 1h, 7d, 3m, 1y. Cannot be combined with from/to. GDELT's TV archive starts July 6, 2010.; `to` (string, optional) — End of an absolute time window. Same formats as from.; `transcript` (array, optional) — Search machine-generated speech-to-text transcripts (GDELT's asr: operator). Repeatable; multiple values are OR'd together. Short phrases only (GDELT caps each at 5 words).; `visual` (array, optional) — Search visual object/activity labels from computer vision (GDELT's visual: operator). Repeatable; multiple values are OR'd together.

## BBC (4)

### `bbc_article`

- **HTTP:** `GET /bbc/article`
- **What:** Get BBC News article content. Returns a BBC News article's public metadata and body paragraphs from a canonical article URL. Live pages are not supported.
- **Params:** `url` (string, **required**) — Canonical BBC News article URL

### `bbc_headlines`

- **HTTP:** `GET /bbc/headlines`
- **What:** Get BBC News section headlines. Returns fresh headlines from a public BBC News RSS section. section defaults to world.
- **Params:** `section` (string, optional) — BBC News RSS section, defaults to world

### `bbc_live`

- **HTTP:** `GET /bbc/live`
- **What:** Get a BBC News live-page text snapshot. Returns the current server-rendered text updates from one canonical BBC News live URL. It does not subscribe to updates or return broadcast, player, or stream data.
- **Params:** `url` (string, **required**) — Canonical BBC News live URL

### `bbc_search`

- **HTTP:** `GET /bbc/search`
- **What:** Search public BBC pages. Returns a bounded page of public BBC search-result metadata. Media entries link only to their BBC landing pages; streams, downloads, and transcripts are not returned.
- **Params:** `page` (integer, optional) — Results page, defaults to 1; `q` (string, **required**) — Search query, up to 120 characters

## CNN (3)

### `cnn_article`

- **HTTP:** `GET /cnn/article`
- **What:** CNN article content. Returns a CNN article's headline, description, author, publication and update times, section, image, and body paragraphs. Provide a canonical cnn.com article URL.
- **Params:** `url` (string, **required**) — Canonical cnn.com article URL

### `cnn_headlines`

- **HTTP:** `GET /cnn/headlines`
- **What:** CNN section headlines. Returns the current CNN headline stream for one section, including title, article URL, description, publication time, and image when available.
- **Params:** `section` (string, optional) — CNN section. Allowed values: world, us, politics, business, health, entertainment, style, travel, sports, science, climate, weather, opinion. Default world.

### `cnn_live_story`

- **HTTP:** `GET /cnn/live-story`
- **What:** CNN live story updates. Returns a CNN live story's title, description, update time, and chronological post updates. Provide a canonical cnn.com live-news URL.
- **Params:** `url` (string, **required**) — Canonical cnn.com live-news URL

## Guardian (3)

### `guardian_article`

- **HTTP:** `GET /guardian/article`
- **What:** Get Guardian article content. Returns a Guardian article's public metadata and body paragraphs from a canonical article URL. Live-blog timelines are not supported.
- **Params:** `url` (string, **required**) — Canonical www.theguardian.com article URL

### `guardian_headlines`

- **HTTP:** `GET /guardian/headlines`
- **What:** Get Guardian section headlines. Returns fresh headlines from a public Guardian RSS section. section defaults to world.
- **Params:** `section` (string, optional) — Guardian RSS section, defaults to world

### `guardian_topic`

- **HTTP:** `GET /guardian/topic`
- **What:** Get Guardian topic archive. Returns a paginated public Guardian topic or category archive. topic is a Guardian tag or section slug and page defaults to 1.
- **Params:** `page` (integer, optional) — 1-based archive page, defaults to 1; `topic` (string, **required**) — Guardian tag or section slug

## Yahoo News (6)

### `yahoo_news_article`

- **HTTP:** `GET /yahoo-news/article`
- **What:** Yahoo News article content. Returns a single Yahoo News article's full content: headline, description, author, publish/update time, section, image, keywords, original publisher, and body paragraphs. Accepts a canonical yahoo.com/news article URL, such as one returned by the home or category story streams.
- **Params:** `url` (string, **required**) — Canonical www.yahoo.com/news article URL

### `yahoo_news_category`

- **HTTP:** `GET /yahoo-news/category`
- **What:** Yahoo News section story stream. Returns a Yahoo News section's story stream: title, destination URL, summary, source, publish time, comment count, and thumbnail images for each story. Sourced from Yahoo News's own server-rendered section pages.
- **Params:** `category` (string, **required**) — Yahoo News section

### `yahoo_news_comment_replies`

- **HTTP:** `GET /yahoo-news/comments/replies`
- **What:** Yahoo News comment replies. Returns a page of a comment's replies: author, body, reaction counts, and pin status, with sort order and cursor-based pagination. Sourced from Yahoo's own comment platform gateway.
- **Params:** `comment_id` (string, **required**) — Parent comment id (the id field returned by /yahoo-news/comments); `content_id` (string, **required**) — Article id (the id field returned by home/category/article); `count` (integer, optional) — Number of replies to return, default 10, clamped to 1..50; `cursor` (string, optional) — Pagination cursor from a previous response's next_cursor; `sort` (string, optional) — Sort order, defaults to newest

### `yahoo_news_comments`

- **HTTP:** `GET /yahoo-news/comments`
- **What:** Yahoo News article comments. Returns a page of an article's top-level comments: author, body, reaction counts, reply count, and pin status, with sort order and cursor-based pagination. Sourced from Yahoo's own comment platform gateway.
- **Params:** `content_id` (string, **required**) — Article id (the id field returned by home/category/article); `count` (integer, optional) — Number of comments to return, default 10, clamped to 1..50; `cursor` (string, optional) — Pagination cursor from a previous response's next_cursor; `sort` (string, optional) — Sort order, defaults to top

### `yahoo_news_home`

- **HTTP:** `GET /yahoo-news/home`
- **What:** Yahoo News homepage story stream. Returns Yahoo News's homepage "need to know" story stream: title, destination URL, summary, source, publish time, comment count, and thumbnail images for each story. Sourced from Yahoo News's own server-rendered homepage.
- **Params:** _none_

### `yahoo_news_suggest`

- **HTTP:** `GET /yahoo-news/suggest`
- **What:** Yahoo News search autocomplete suggestions. Returns Yahoo News's own search-box autocomplete suggestions for a partial query: a flat list of suggested news search terms.
- **Params:** `count` (integer, optional) — Number of suggestions to return, default 10, clamped to 1..20; `q` (string, **required**) — Partial search query to autocomplete
