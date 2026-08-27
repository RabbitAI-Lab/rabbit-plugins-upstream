# Set Up Niche Monitoring

Create an automated recurring search for a topic. Uses the unified `/v1/agents` API in recurring mode (`is_recurring: true`).

## User Prompt

"Set up weekly monitoring for TikTok Shop strategies"

## Agent Steps

1. Create a recurring agent (the old Comet — now `POST /v1/agents` with `is_recurring: true`):
```bash
curl -X POST https://api.virlo.ai/v1/agents \
  -H "Authorization: Bearer $VIRLO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "is_recurring": true,
    "intent": "track what is working for TikTok Shop sellers week over week",
    "name": "TikTok Shop Strategies",
    "keywords": ["TikTok Shop success", "TikTok Shop strategies", "TikTok Shop tips", "TikTok Shop sellers", "TikTok Shop marketing"],
    "platforms": ["youtube", "tiktok", "instagram"],
    "cadence": "weekly",
    "meta_ads_enabled": true
  }'
```

2. Confirm the agent was created and share the next run time. Creating a recurring agent is **free** — you're billed per run.

3. The first run queues immediately. Poll every ~60s until `finalized: true` (~15-20 min), then check results:
```bash
curl "https://api.virlo.ai/v1/agents/{id}/videos?limit=20&order_by=views&sort=desc" \
  -H "Authorization: Bearer $VIRLO_API_KEY"
```

4. (Optional) Let it self-optimize. Review any change proposals and approve the first one to unlock autopilot:
```bash
curl "https://api.virlo.ai/v1/agents/{id}/proposals?status=pending" \
  -H "Authorization: Bearer $VIRLO_API_KEY"
```

## Total Cost

Free to create. Each recurring run is billed like a search ($0.50/run, or +$1.00/run with `data_intelligence_enabled`). Retrieval of results is always free.

> **Legacy note:** `POST /v1/comet` still works but is deprecated (removed Aug 3, 2026). An existing `comet_id` is a valid agent id.
