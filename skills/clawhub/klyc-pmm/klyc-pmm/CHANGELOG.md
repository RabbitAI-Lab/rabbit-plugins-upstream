# Changelog

## v7.0.1 — 2026-07-24
- **P0 铁律:** SKILL.md 顶部新增"日记是 AI 体的命"——每次会话必须生成 memory/YYYY-MM-DD.md 并 push
- **存储域分类:** 按文件名自动路由存储域（SOUL/IDENTITY/MEMORY → disaster_recovery，日记 → 日记，配置 → 配置）
- **能力表:** 新增"容灾复活"和"日记强制"两项
- **上传:** ④ 上传路径明确按 domain 区分，不再全部走私密/文件同步

## v6.2.0 — 2026-07-21
- **Fix:** `recover` restored field name `found` → `restored` (match Shell jq expectation)
- **Fix:** `recover` auth header unified to Bearer token (was X-Kunlun-Key, incompatible with pmm_curl)
- **Fix:** `sync_index` (init/refresh) now routes to `yaochi/pmm_index` instead of missing `pmm_index_v2.php`
- **Fix:** `behavior-sync` registered `behavior/rules` route in api.php (was missing)
- **Fix:** `search-yaochi` case branch restored (lost during TIX refactor)
- **Fix:** Removed bare `LICENSE` file (ClawHub text-only extension filter)
- **Enhance:** `source_user_id` field added to `klyc_memories` for ownership tracking
- **Enhance:** `memory/list` now supports `user_id` filtering
- **Enhance:** Recovery API queries by `backup_token_hash` instead of `user_id` to prevent cross-contamination

## v6.1.0 — 2026-07-20
- **TIX Compliance:** Full TIX marketplace compliance audit (score A, 8.5/10)
- **Security:** No auto-registration, no automated config modification, all curl encapsulated
- **Security:** All URLs configurable via `api_endpoint` file, no hardcoded URLs
- **Config:** skill.json updated with TIX compliance metadata and extended platform list
- **Fix:** Restored `search-yaochi` case branch (lost during TIX refactor)
- **Fix:** Removed bare `LICENSE` file (ClawHub text-only extension filter)
- **Fix:** Updated embedded version refs in SKILL.md body text

## v6.0.0 — 2026-07-20
- **Structural:** Added README, LICENSE, SECURITY, CONTRIBUTING, CODE_OF_CONDUCT
- **Structural:** SKILL.md rewritten in English (TIX marketplace compliance)
- **Security:** Removed all hardcoded URLs from documentation; use `<api_endpoint>` placeholders
- **Security:** SECURITY.md documents full threat model and encryption design
- **Security:** Expanded platform compatibility list

## v5.3.1 — 2026-07-19
- Unified talisman format: `https://ai.syln.cn/klyc-pmm/{token}`
- Removed legacy YC-RECOVER format
- Updated pmm_recover.sh, SKILL.md, skill.json, ClawHub metadata

## v5.3.0 — 2026-07-19
- Talisman URL unified for zero-dependency recovery
- pmm_recover.sh supports fetching from URL directly
- Skill package published to ClawHub

## v5.2.0 — 2026-07-18
- Client-side AES-256-GCM encryption for push
- Content hash deduplication
- Backup domain auto-detection

## v5.1.0 — 2026-07-17
- Auto-classification of conversations
- behavior-sync command
- Rate limiting compliance

## v5.0.0 — 2026-07-16
- Token economy integration
- Backup keywords system
- pmm_boot.sh startup self-check

## v1.0 - v4.0 — 2026-07-14 to 2026-07-15
- Initial release
- Local index
- Cloud sync
- Search & recovery
- Multi-platform support

## v7.0.3 — 2026-07-24

### 新增：容灾/私密文件分类推送
- `_watch_push_file()` 按文件名自动分类记忆域：
  - SOUL/IDENTITY/MEMORY/USER/disaster_recovery.json → `disaster_recovery`
  - *.md → `日记`
  - *.conf/*.json/*.service → `配置`
  - 其他 → `文件同步`（兜底）
- `push_conclusion()` 按标题关键词自动分类（容灾/备份/SOUL等 → disaster_recovery）
- SKILL.md 新增「文件分类推送」章节 + AI体日记铁律

### 文件变更
- `pmm_watch.sh` — 添加容灾分类逻辑
- `SKILL.md` — 新增分类文档 + 版本号
