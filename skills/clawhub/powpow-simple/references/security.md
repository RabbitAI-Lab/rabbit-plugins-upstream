# Security Architecture & Platform API

> 仅维护/排查时参考。SKILL.md 运行时不需要通读。

## Why this skill is safe to distribute

This skill holds **no platform secrets**:

| Item | Old architecture | New architecture |
|---|---|---|
| Database access | Supabase service key (full DB, bypasses RLS) | None — platform API only |
| Identity | Any username could be passed (impersonation) | JWT from real login; you can only post as yourself |
| User password | Stored base64 in credentials.json | Never stored; used once to obtain a ~7-day token |
| Rate limits / moderation | None (client-side insert) | Enforced server-side (10 posts/hr/user, content moderation) |
| Unsplash key | Bundled | User-supplied (optional; images are optional) |

`config.json` contains ONLY `{ "platformUrl", "unsplashAccessKey"(optional),
"sessionMaxAgeDays", "skillVersion" }`. Never add Supabase keys, service roles,
or admin tokens to this skill.

### Files that must never leave the user's machine
- `<POWPOW_STATE_DIR>/session.json` (default `~/.powpow/session.json`) — the
  logged-in user's JWT (auto-expires ~7 days). Written to the user's state
  directory, never into the (possibly read-only) skill bundle.

## Platform API endpoints used

- `POST /api/auth/login` — `{step:1, username, password}` → JWT (cookie `powpow_token`)
- `GET  /api/digital-humans?scope=all&search=...` — list/search digital humans (login required)
- `GET  /api/amap/place/text?keywords=...` — place-name search (login required;
  returns GCJ-02, converted to WGS-84 client-side by geocode.js). The endpoint
  path is platform-internal and must not be surfaced to the user either — refer
  to it as 「地图数据库」 in any internal discussion (never to the user).
- `POST /api/upload/post-image` — local image upload (multipart `file`; login required)
- `POST /api/posts` — create post (login required; server enforces limits & moderation)
- `GET  /api/posts/{id}` — verify a post
- `DELETE /api/posts/{id}` — delete own post (test cleanup)
- `POST /api/digital-humans` — create a digital human (login required;
  consumes 2 badges, expires after 30 days)
- `POST /api/digital-humans/generate-avatar` — AI avatar from the persona
  (login required; 8~30s; needs a reference image URL by platform design)
- `GET  /api/badges/balance?userId=...` — badge balance pre-check

Note: the JWT is bound to a device fingerprint (User-Agent + Accept-Language). The API client pins these headers at login and reuses them automatically. If you see `DEVICE_MISMATCH` or 401, just re-login.
