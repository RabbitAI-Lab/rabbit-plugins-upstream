# File Structure

> 仅维护/排查时参考。SKILL.md 运行时不需要通读。

```
powpow-feed-poster/
├── SKILL.md                          # 主文件（已瘦身，详见 references/）
├── config.json                       # platformUrl + optional user's Unsplash key (NO secrets)
├── config/                           # auto-created at first login (not present in a fresh install)
│   └── session.json                  # Local JWT session (~7 day expiry; skill re-login margin 6 days)
├── scripts/
│   ├── doctor.js                     # first-run self-check (node/config/network/session)
│   ├── login.js                      # username/password → JWT (password never stored, hidden prompt)
│   ├── compose.js                    # ONE-COMMAND post HTML assembly (the only supported way; fully local)
│   ├── publish.js                    # upload local images + POST /api/posts as the logged-in user
│   ├── verify.js                     # verify post by ID via platform API
│   ├── delete-post.js                # delete own post (test cleanup)
│   ├── geocode.js                    # place name → WGS-84 candidates (user confirms)
│   ├── list-digital-humans.js        # list/search with health filtering
│   ├── match-digital-human.js        # topic → ranked healthy candidates
│   ├── create-digital-human.js       # create a map digital human (2 badges, 30-day expiry; avatar: generate/upload/URL)
│   ├── search-image.js               # Unsplash (user's own key, optional; also resolves photo-page links)
│   ├── upload-image.js               # local image → platform storage → public URL (used by publish.js)
│   └── lib/
│       ├── api-client.js             # platform API client (JWT, pinned headers)
│       ├── dh-match.js               # shared DH health filter + topic ranking (name 3x, desc 1x, discipline-term masking)
│       ├── coord-transform.js        # GCJ-02 ↔ WGS-84 conversion (iterative inverse)
│       └── html-formatter.js         # HTML components + CJK-aware word count
└── references/
    ├── changelog.md                  # 历史变更（5.3 → 5.7.0）
    ├── security.md                   # 安全架构 + 平台接口清单
    └── file-structure.md             # 本文件
```
