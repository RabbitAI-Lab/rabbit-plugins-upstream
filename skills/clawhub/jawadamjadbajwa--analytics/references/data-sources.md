# Data sources

Confidence: **verified** (read from the provider's documentation in Nov 2026) or **not verified** (general knowledge; check before relying on it). The scripts in this skill read CSV files; APIs are listed so the user (or another tool) can pull data.

## Start with the platforms' own exports

Every platform's native analytics can export or show per-post numbers; this is the simplest and safest source, needs no developer access, and matches what the platform reports. Ask for one export per platform and a date range of at least 8 to 12 weeks. Exact menu names change, so ask the user to look for "Export", "Download" or "Advanced mode" in the analytics area (not verified for each platform here).

## YouTube

- **YouTube Analytics API** (verified): `reports.query` needs `ids` (`channel==MINE` or a channel id), `startDate`, `endDate`, `metrics` (for example `views`, `estimatedMinutesWatched`, `averageViewDuration`, `averageViewPercentage`, `subscribersGained`, `likes`), optional `dimensions` (for example `day`, `video`) and `filters`. OAuth scope `https://www.googleapis.com/auth/yt-analytics.readonly`; revenue metrics need `yt-analytics-monetary.readonly`. Recent days may be missing from `day` queries. The owner must authorise the app.
- **YouTube Data API** (public statistics for any video or channel): views, likes, comments for public videos; the `viral-content-research` skill's `yt_research.py` does this if present. It cannot give private analytics such as impressions CTR or retention.
- **YouTube Studio exports**: per-video tables with views, impressions, impressions CTR, average view duration, watch time; use `--map` to match column names.

## Instagram (professional accounts)

Verified from Meta's Instagram Platform documentation:
- Media insights metrics: `reach`, `shares`, `reposts`, `views`, `total_interactions` for feed, Reels and Stories; `comments`, `likes`, `saved` for feed and Reels; `follows`, `profile_activity`, `profile_visits` for feed and Stories; Reels also `ig_reels_avg_watch_time`, `ig_reels_video_view_total_time`, `reels_skip_rate`; Stories also `link_clicks`, `navigation`, `replies`.
- `impressions` is deprecated for media created after 2 July 2024 (still available for older media). Some metrics are labelled "in development" or "estimated".
- Data can lag up to 48 hours and is stored for up to 2 years; unavailable data returns an empty set, not 0; no insights for media inside albums; Story metrics only for 24 hours; Story values under 5 return an error.
- Access needs a professional account, an app with the `instagram_manage_insights` (Facebook Login) or `instagram_business_manage_insights` (Instagram Login) permission, and the relevant token. Apps usually need Meta app review for other people's accounts.

## X (Twitter)

Verified from X's documentation: the API uses pay-per-usage credits with no subscription; reading posts costs about $0.005 per post returned and "owned reads" of your own data about $0.001 per resource; creating a post costs about $0.015 per request ($0.20 with a URL); there is a 3 million post-read monthly cap on pay-per-use; usage is tracked in the Developer Console. The page did not describe an analytics product, so use X's native analytics export for impressions and engagement. Prices change; confirm before building on them.

## LinkedIn, TikTok, Facebook, Threads, Pinterest

Not verified in this session. Use each platform's native analytics export. If the user wants API access, ask for the current developer documentation link and check access requirements (approved apps, permissions, partner programs) before planning a pipeline.

## Third-party tools

Scheduling and social suites (Buffer, Metricool, Hootsuite, Sprout, and similar) offer cross-platform exports; check their plans, limits and data definitions before relying on them. Treat their numbers as "as reported by the tool". Connectors for such tools may exist in the session (check with the connector search).

## Website and conversion data

- Use UTM parameters on every link from social: `utm_source` (platform), `utm_medium` (social), `utm_campaign` (campaign), `utm_content` (post or variant id). Keep a naming sheet so tags stay consistent.
- Read results in the user's web analytics (for example GA4 or the CRM). Compare sessions, sign-ups and purchases by `utm_campaign` and `utm_content`.
- Ask how leads are recorded (forms, WhatsApp, DM, calls); a lot of social-driven conversion happens in DMs, so add a "how did you hear about us" question.
- Respect privacy law and platform terms when tracking; do not collect personal data in analysis files.

## Data hygiene

- Keep raw exports unchanged; work on copies.
- Record the export date, time zone and filters.
- Note boosted or paid posts; analyse organic and paid separately.
- Remove posts that are not comparable (deleted, collaborations with another account's audience) or flag them.
