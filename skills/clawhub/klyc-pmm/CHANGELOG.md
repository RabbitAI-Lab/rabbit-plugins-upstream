# Changelog

## v7.0.2 — 2026-07-23
- **hooks-pull 增量合并:** 按 ID 去重 + 标题相似检测 + 本地保留不动，远程新增追加不覆盖
- **watch 全自动 hooks-pull:** watch 守护循环内嵌入自动蒸馏钩子拉取（默认6h，可调 `--hooks-interval`）
- **智能归属:** hooks-pull 按脚本路径自动选择 openclaw/lightclaw 对应的 MEMORY.md
- **防覆盖:** 本地独有条目绝不丢失；白板 AI 体首次注入完整钩子；已有钩子合并新增
- **蒸馏管道:** BGE-M3 embedding 缓存自积累（`klyc_memory_embeddings` 表），越跑越快

## v7.0.1 — 2026-07-23
- **隐私优先:** push/watchdog 显式传 `--argjson pub 0`，所有自动同步默认私密
- **API 安全:** `klyc_memory_create.php` 默认 `is_public=0`（铁律 #28）
- **千人千面:** wrapper `pmm-watch-kunlun.sh` 从 IDENTITY.md 自动解析 user_id，不再写死
- **文档脱敏:** SKILL.md 示例 `--user-id N` 全部改为 `$YOUR_ID`
- **守护增强:** wrapper 自动包含 `arena/` 目录和 `TOOLS.md`

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
