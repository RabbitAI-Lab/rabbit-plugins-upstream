# Find Trending Content

Check today's trends and explore trending videos.

## User Prompt

"What's trending on social media today?"

## Agent Steps

1. Get today's trends:
```bash
curl "https://api.virlo.ai/v1/trends/digest?limit=10" \
  -H "Authorization: Bearer $VIRLO_API_KEY"
```
If the user asks about a specific country, pass `region` (`us`, `gb`, `au` — default is `global`, the worldwide feed):
```bash
curl "https://api.virlo.ai/v1/trends/digest?limit=10&region=gb" \
  -H "Authorization: Bearer $VIRLO_API_KEY"
```
`GET /v1/trends/regions` (free) lists the currently available region codes — more are added over time.

If the user asks what's *emerging* or *about to take off* (rather than the full daily list), use the free, momentum-ranked emerging endpoint — composable with `region`:
```bash
curl "https://api.virlo.ai/v1/trends/emerging?region=gb&limit=20" \
  -H "Authorization: Bearer $VIRLO_API_KEY"
```
It returns only `new`/`rising` trends sorted by momentum heat (each with `status`, `momentum_score`, `views_per_hour`) — ideal for "what's emerging in the UK right now". It's a free read but rate-limited per plan.

2. Present trend names and descriptions to the user.

3. Get top viral videos:
```bash
curl "https://api.virlo.ai/v1/videos/digest?limit=10" \
  -H "Authorization: Bearer $VIRLO_API_KEY"
```

4. Show top hashtags:
```bash
curl "https://api.virlo.ai/v1/hashtags?start_date={today_minus_7}&end_date={today}&limit=10&order_by=views&sort=desc" \
  -H "Authorization: Bearer $VIRLO_API_KEY"
```

5. If the user is interested in a specific trend, offer to run a Full Niche Analysis — a one-shot agent (`POST /v1/agents` with `is_recurring: false`) seeded with the trend keywords.

## Total Cost

$0.25 for trends + $0.25 for videos + $0.05 for hashtags = $0.55 total.
