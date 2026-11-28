# Frameworks

## 1. Niche analysis

Answer with evidence ids, in this order:
- **Size and direction:** is demand growing, flat or shrinking (Trends slope, autocomplete breadth)?
- **Seasonality:** peak and trough months (`trends-csv` reports them when the export spans two or more years).
- **Audience segments:** who asks what (questions grouped by intent).
- **Competitive density:** how many active channels, their size spread, and how concentrated attention is (a few giants with all the views, or many mid-size winners).
- **Saturation by topic:** which topics have many near-identical videos and which have almost none.
- **Monetization routes:** how players in this niche make money (this shapes the funnel).

## 2. Evidence-based personas (2 to 3, not 8)

A persona is only useful if it changes what you make. Template:

- **Name and one-line description** (a role, not a stereotype)
- **Job to be done:** what they are trying to achieve
- **Top 3 pains and top 3 questions**, in their own words (from comments, Reddit, autocomplete) with evidence ids
- **Where they spend time** (platforms, with evidence)
- **Trigger moments:** what makes them search or buy
- **Objections** that block conversion
- **Content they respond to:** formats and lengths, from what outperforms

If there is no data for a field, write "hypothesis" and list how to test it. Never fill personas with invented demographics.

## 3. Competitor analysis

Per competitor (from `yt_competitors.py` plus web research): platform presence, posting cadence, median views, outlier share (how often they beat their own baseline), formats and length, title patterns, upload days, top 3 performers and why, and what they do not cover. Then summarize: the benchmark (typical cadence and median views for the niche), the winning formats, and the openings.

## 4. Gap matrix (demand vs supply)

1. Build a demand list: keywords or questions from `suggest`, Trends, forums, and SEO tools (each with a relative demand score).
2. Build a supply list: competitor and niche video titles (CSV with a `title` column; add `views` if available).
3. Run `research_helper.py gap`. Each demand item is classed: **gap** (no title covers it), **thin** (1 to 2 covers), or **contested** (many).
4. Judge the result: a gap with strong demand is a candidate, a thin topic whose few videos perform well is *proven demand with low supply* (the best kind), a contested topic needs a sub-angle or a quality edge.
5. Remember the limit: the gap list is only as complete as the supply sample. State how many titles were compared.

## 5. Pillar rubric (score each candidate pillar 1 to 5)

| Criterion | Weight | Question |
|---|---|---|
| Audience demand | 30% | Is there evidence people search or ask for this? |
| Business fit | 25% | Does it lead toward the goal (leads, sales, authority)? |
| Gap or edge | 20% | Is supply thin, or does the user have a real edge? |
| Proven performance | 15% | Do similar videos or posts outperform in the data? |
| Production fit | 10% | Can the user make this consistently with their capacity? |

Weighted score out of 5. Keep 3 to 5 pillars; assign each a share of posts (for example 40/30/20/10), a funnel stage, and 5 or more evidence-backed topic seeds.

## 6. Funnel mapping

| Stage | Purpose | Typical content | Intent signals | Core KPIs |
|---|---|---|---|---|
| Awareness | Reach new people | Short-form, trend and curiosity topics, "how/what/why" | Informational queries, outlier hooks | Reach, views, follows, share rate |
| Engagement | Build trust and habit | Deep tutorials, series, stories, community prompts | Comments, saves, return viewers | Watch time or completion, saves, comments, repeat viewers |
| Conversion | Turn trust into action | Comparisons, case studies, offers, demos, FAQs | Commercial and comparison queries ("best", "vs", "pricing") | Click-through, leads, sign-ups, sales |

`suggest` tags each keyword with an intent (question, comparison, commercial, informational), which gives a first-pass funnel assignment. Check the mix: most brands over-produce awareness content and starve conversion.

## 7. KPI selection

Pick 1 primary KPI tied to the goal, 2 to 3 stage KPIs, and a few diagnostic metrics. Each KPI needs: a baseline (or "to be measured in week 1"), a 90-day target, the measurement source, and a review rhythm. Targets from general benchmarks are labelled low confidence and revised after the first month of the user's own data.

## 8. Posting frequency and format logic

1. Start from capacity: realistic posts per week the user can sustain for 90 days.
2. Compare with the competitor benchmark (posts per week of winners in the data).
3. Apply platform norms as a sanity check, labelled as general knowledge.
4. Recommend a range, plus a minimum viable cadence and a stretch cadence.
5. Pick formats by stage and platform, then confirm with data: share of short-form among competitors' outliers, median duration of top videos, title patterns that recur.
6. Batch production: group by format to cut cost per post.

## 9. Test-and-learn plan

Every strategy ends with experiments: what to test (hook style, format, length, posting day), how many posts per test (at least 5 to 8), the metric to judge it, and the decision rule (double down, adjust, or drop). Review monthly; the strategy is a version 1.
