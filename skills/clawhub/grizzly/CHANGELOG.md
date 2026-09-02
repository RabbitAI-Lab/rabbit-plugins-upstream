## 2.4.1 — canonical slug `grizzly` (display name Grizzly); `yieldingbear` redirects

# Changelog

## 2.4.0 — 2026-09-01

- **Title: Grizzly** — hub-facing name + SEO tags (llm-gateway, openai-compatible, smart-routing, cost-optimization, multi-model).
- Punchy high-volume ROI copy: routing + cache + one-key multi-model.
- API keys now issued as `grizzly_live_sk_…` (legacy `yb_live_sk_…` still accepted).

## 2.3.2 — 2026-09-01

- Fix fetch_recs exit status under `set -e` (explain/set-routing).

## 2.3.1 — 2026-09-01

- **Routing mode Auto | Manual** in install Step 3 and dashboard Active Model (same toggle).
- Auto → `yieldingbear/grizzly-1.0g-pro` (classifier high/mid/free); Manual → pin catalog model with live YB recommendation chips.
- Public `GET /api/public/routing-recommendations` shared by CLI + UI.
- `yb.sh set-routing auto|manual [model]`; doctor shows local vs server prefs.
- API key auth on `PUT/GET /api/user/default-model` so install syncs dashboard.
- Fixed tier_routes keys to gateway slots (`high`/`mid`/`low`) in ActiveModelCard.

## 2.2.0 — 2026-09-01

- Full install walkthrough: signup → plan fork → live models → doctor.
- CLI Pro offer `$10×3` via `/offer/cli10x3`.
- `yb.sh` doctor / models / set-model / explain / smoke.
