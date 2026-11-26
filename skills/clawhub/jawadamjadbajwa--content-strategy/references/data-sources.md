# Data sources and the evidence ledger

## Which source answers which question

| Question | Best source | Fallback | Confidence |
|---|---|---|---|
| What does the audience search for or ask? | Search autocomplete (`research_helper.py suggest`), Reddit/forum threads (WebSearch + WebFetch) | WebSearch "people also ask" style queries | Estimated |
| Is demand growing, flat or seasonal? | Google Trends CSV export (`trends-csv`) | WebSearch for industry trend reports | Estimated |
| Real search volume, difficulty, CPC | Semrush or Ubersuggest connector, or a paid API such as DataForSEO | None; use autocomplete rank and Trends as proxies | Verified (tool) |
| How do the user's own pages perform? | Google Search Console or analytics (connector or user export) | Ask the user for a CSV export | Verified |
| What do competitors post and how often? | `yt_competitors.py` for YouTube channels | WebFetch of their public pages, WebSearch | Verified (API) / Page-visible |
| What outperforms in the niche on YouTube? | `yt_research.py search` (outlier_x, views_per_day) | WebSearch "most popular videos" lists | Verified (API) |
| Audience language, objections, pain points | `yt_research.py comments`, Reddit threads | WebSearch for reviews and forums | Page-visible |
| Instagram, TikTok, X performance | Not retrievable reliably; qualitative only | User screenshots or exports | Low |

## Tool options, honestly

- **YouTube Data API v3:** free (10,000 units/day). A key comes from Google Cloud Console (create a project, enable the API, create an API key). A search costs 100 units, most other calls 1.
- **Google Trends:** there is no general public API. Google has an invite-only alpha; everyone else uses the website. Ask the user to open trends.google.com, enter up to 5 terms, pick region and the last 5 years, and use Download to get a CSV. Terms exported together share one scale, so they are comparable with each other.
- **Search autocomplete:** an undocumented endpoint that can change or throttle. Treat output as a relative demand signal, never as volume. Earlier suggestions are stronger signals.
- **Semrush and Ubersuggest:** available as connectors in the connector directory. They are the route to real keyword volume and competitor keyword data, but require the user's own account; check current pricing on their sites. Offer them when the plan depends on SEO volume.
- **DataForSEO:** pay-as-you-go keyword, SERP and Trends data via API. Good for automation, but needs an account and credit.
- **Google Search Console:** the most valuable source *if the user already has a site*, because it shows real queries driving impressions and clicks. Reachable through marketing-analytics connectors or a CSV export.

When the user pastes an API key, use it inline for that command only (for example `YOUTUBE_API_KEY=... python ...`). Do not write it to files, the report or memory.

## Evidence ledger

Create `evidence.csv` early and add rows as you go.

| column | meaning |
|---|---|
| id | E1, E2, ... used for citations in the strategy |
| source | tool, URL or file |
| claim | one plain sentence of what was found |
| metric | the number or signal (with unit) |
| date | date pulled |
| confidence | verified / page-visible / estimated / assumption |

Rules: one finding per row; every decision in the strategy cites at least one id or is tagged **assumption**; when two sources disagree, record both and say which you trust and why.
