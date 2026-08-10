# Monitor Creator Performance

Track a creator over time, collect metric snapshots, and get AI analysis reports. Each tracking cycle collects metrics AND generates an AI report as one bundled operation.

## User Prompt

"Start tracking @khaby.lame on TikTok every 12 hours"

## Agent Steps

1. Start tracking the creator (initial cycle starts immediately):
```bash
curl -X POST https://api.virlo.ai/v1/tracking/creators \
  -H "Authorization: Bearer $VIRLO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "platform": "tiktok",
    "handle": "khaby.lame",
    "scrape_cadence": "twelve_hours"
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

5. Adjust cadence or pause tracking:
```bash
curl -X PATCH https://api.virlo.ai/v1/tracking/creators/{id} \
  -H "Authorization: Bearer $VIRLO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{ "scrape_cadence": "daily" }'
```

## Total Cost

$0.25 per tracking cycle (including the initial cycle when you start tracking). All GET, PATCH, and DELETE endpoints are free.
