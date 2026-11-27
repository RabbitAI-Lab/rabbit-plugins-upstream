# KPIs and interpretation

## KPIs by goal

| Goal | Primary KPIs | Supporting |
|---|---|---|
| Awareness | reach, views, new followers, shares | impressions, profile visits, share of reach from non-followers (where the platform shows it) |
| Engagement | saves, shares, comments (quality), engagement rate | watch time or average view duration, retention, replies |
| Traffic | link clicks, click-through rate, sessions from UTM | bounce or engaged sessions on the site |
| Leads | sign-ups, form fills, DMs started, cost or time per lead | lead quality (qualified rate) |
| Sales | orders, revenue from UTM or coupon, conversion rate | average order value, repeat rate |
| Community | replies, repeat commenters, group activity, sentiment | response time |

Pick 2 to 4 KPIs, define each (formula, source, period), and set a target only after seeing a baseline of 4 to 8 weeks.

## Definitions used by the script

- `interactions` = likes + comments + shares + saves (only the parts present in the export).
- `er` (engagement rate) = interactions / reach; if reach is missing, / views; else / impressions. Percent.
- `ctr` = clicks / impressions (else / views). Percent.
- Group statistics use medians. Platforms define reach, views and impressions differently, and Instagram's `views` and `reach` are marked as in development in Meta's docs; do not compare ER across platforms.

## Sample size and noise

- Under about 5 posts per group: anecdote. 5 to 15: suggestive. More, with consistent direction across weeks: reasonably reliable. These are rules of thumb, not statistical guarantees.
- One viral post can dominate averages; check the median and the spread.
- Weekly numbers wobble; compare 4-week windows rather than week to week.
- Seasonal effects (holidays, exams, sales periods) and algorithm changes can look like performance changes.

## A/B tests that mean something

1. One variable (thumbnail, title, hook, caption, CTA, time). Everything else the same.
2. Decide the metric (for example CTR for thumbnails, saves per reach for carousels) and the sample size before starting; avoid stopping early when the result "looks good".
3. For thumbnails and titles, YouTube Studio may offer a built-in test (not verified here): use it when available. Otherwise compare periods carefully, knowing the audience and topic differ.
4. Use `abtest` on counts (clicks and impressions): it reports the difference with a 95% interval and a p-value from a simple two-proportion test. Check that both variants had similar exposure and timing. If events are fewer than 10 in any cell, wait for more data.
5. Look at the second metric too: a thumbnail that raises clicks but lowers watch time may be misleading.
6. Log every test: hypothesis, variants, dates, numbers, decision.

## Reading patterns

- High reach, low engagement: the hook got attention, the value did not hold it; check the first line, the length, the promise.
- Low reach, high engagement rate on a small base: loyal audience, weak discovery; try format, topic, or collaboration changes.
- High saves and shares: reference value or identity value; make more of that type.
- High comments with low saves: debate or questions; fine for community, check intent.
- High CTR, low average view percentage (YouTube): packaging promises more than the video gives.
- Falling numbers everywhere at once: look for platform changes, season, posting gaps, or data issues before blaming content.

## Report structure

1. Summary: 3 bullets with the answer and the decision needed.
2. Context: period, platforms, posts, what changed.
3. KPIs vs baseline or target.
4. What worked (with n and a quote or example) and what did not.
5. Hypotheses (why) and confidence labels.
6. Recommendations: repeat / stop / test, with the metric and sample size for each test.
7. Data notes and limits.

## Common traps

- Quoting benchmark numbers as the user's data. 
- Comparing a Reel with a text post without noting the format.
- Counting boosted posts as organic.
- Using "best time to post" tables from articles instead of the user's own slots.
- Treating followers as the goal when sales or leads are the goal.
- Declaring a winner after two posts.
- Reading comments and DMs as "no engagement": qualitative signals (questions, objections, quotes) belong in the report.
