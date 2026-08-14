# Full Niche Analysis

Search for a topic across all platforms, get an AI intelligence report, explore videos and creators. Uses the unified `/v1/agents` API in one-shot mode (`is_recurring: false`).

## User Prompt

"Research the jeep wrangler modification niche across all platforms"

## Agent Steps

1. Create a one-shot agent (the old Orbit — now `POST /v1/agents` with `is_recurring: false`):
```bash
curl -X POST https://api.virlo.ai/v1/agents \
  -H "Authorization: Bearer $VIRLO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "is_recurring": false,
    "intent": "understand what content and mods win in the jeep wrangler niche",
    "name": "Jeep Wrangler Mods Research",
    "keywords": ["jeep wrangler mods", "jeep wrangler accessories", "jeep upgrades"],
    "platforms": ["youtube", "tiktok", "instagram"],
    "meta_ads_enabled": true
  }'
```

2. Poll every ~60 seconds until `finalized: true` (don't loop tightly, and never hard-timeout — a broad run with ads can take up to 45 min; `partial_failure` is a usable terminal state):
```bash
curl https://api.virlo.ai/v1/agents/{id} \
  -H "Authorization: Bearer $VIRLO_API_KEY"
```

3. Get the AI intelligence report:
```bash
curl "https://api.virlo.ai/v1/agents/{id}/analysis/latest" \
  -H "Authorization: Bearer $VIRLO_API_KEY"
```

4. Get top videos — apply any view/date filters here at read time (free), since collection is system-managed and broad:
```bash
curl "https://api.virlo.ai/v1/agents/{id}/videos?limit=20&order_by=views&sort=desc&min_views=100000&start_date=2026-01-01T00:00:00Z" \
  -H "Authorization: Bearer $VIRLO_API_KEY"
```

5. Find rising creators (rank by `weighted_score`, not raw `outlier_ratio`):
```bash
curl "https://api.virlo.ai/v1/agents/{id}/creators/outliers?limit=10&order_by=weighted_score&sort=desc" \
  -H "Authorization: Bearer $VIRLO_API_KEY"
```

## Total Cost

$0.50 for the one-shot agent. All retrieval is free.

> **Legacy note:** `POST /v1/orbit` + `GET /v1/orbit/:orbit_id/…` still work but are deprecated (removed Aug 3, 2026). An existing `orbit_id` is a valid agent id, so the read paths above also work under `/v1/orbit/:orbit_id/…`.
