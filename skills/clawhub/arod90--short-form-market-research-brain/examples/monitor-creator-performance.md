# Monitor Creator Performance

Track a creator over time, collect metric snapshots, and get AI analysis reports. Each tracking cycle collects metrics AND generates an AI report as one bundled operation.

## User Prompt

"Start tracking @khaby.lame on TikTok every 12 hours"

## Agent Steps

1. Start tracking the creator (initial cycle starts immediately). Add `collection_depth` to also back-fill a deeper post history (and per-post sound) right away — `standard` (50 videos, +$0.50), `deep` (200, +$1.00), or `full` (500, +$2.00):
```bash
curl -X POST https://api.virlo.ai/v1/tracking/creators \
  -H "Authorization: Bearer $VIRLO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "platform": "tiktok",
    "handle": "khaby.lame",
    "scrape_cadence": "twelve_hours",
    "collection_depth": "deep"
  }'
```

2. Check the creator's current data. The main scrape finishes fast, but secondary jobs (AI report, audience snapshot) may still be running — rely on `finalized: true`, not `status`. While `finalized` is `false`, `pending_jobs[]` lists each in-flight job with its `poll_url` and `retry_after_seconds`; any `null` fields just mean "not computed yet," not "no data":
```bash
curl https://api.virlo.ai/v1/tracking/creators/{id} \
  -H "Authorization: Bearer $VIRLO_API_KEY"
```

3. After a few cycles, review growth snapshots:
```bash
curl https://api.virlo.ai/v1/tracking/creators/{id}/snapshots \
  -H "Authorization: Bearer $VIRLO_API_KEY"
```

4. Read the latest AI report (generated automatically on every cycle):
```bash
curl https://api.virlo.ai/v1/tracking/creators/{id}/report \
  -H "Authorization: Bearer $VIRLO_API_KEY"
```

5. Enumerate the creator's collected posts with per-post metrics, outlier flags, and the per-post `sound` object. `sound.external_id` is the platform-native sound id (TikTok music/clip id, Instagram audio id; `null` for YouTube) a music catalog matches against — filter or group posts by it to see which tracks a creator uses:
```bash
curl "https://api.virlo.ai/v1/tracking/creators/{id}/posts?sort=views_desc&limit=50" \
  -H "Authorization: Bearer $VIRLO_API_KEY"
```

6. Deepen the post history on demand at any time (populates per-post sound for TikTok/Instagram always, YouTube on deep/full):
```bash
curl -X POST https://api.virlo.ai/v1/tracking/creators/{id}/posts/collect \
  -H "Authorization: Bearer $VIRLO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{ "depth": "deep" }'
```

7. Adjust cadence or pause tracking:
```bash
curl -X PATCH https://api.virlo.ai/v1/tracking/creators/{id} \
  -H "Authorization: Bearer $VIRLO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{ "scrape_cadence": "daily" }'
```

## Total Cost

$0.25 per tracking cycle (including the initial cycle when you start tracking). An optional initial `collection_depth` adds $0.50/$1.00/$2.00 (standard/deep/full), and on-demand `posts/collect` costs the same by depth — both charged when the request is accepted. All GET, PATCH, and DELETE endpoints are free.
