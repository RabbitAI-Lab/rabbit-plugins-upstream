# Changelog

All notable changes to Bidding Hunter will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.1] - 2026-07-22

### Fixed
- Critical: Added missing `database.ingest()` function to both SQLite and JSON backends
- Critical: YAML `wait_until` silently ignored by `gotoWithRetry` (snake_case ↔ camelCase mismatch) — added normalization in config.js
- Critical: `/home/$USER` literal string bug in 3 files (database.js, lock.js, notifier.js) — replaced with `path.join('/home', process.env.USER)`
- Warning: `updates.note` vs `updates.notes` inconsistency in SQLite history recording
- Warning: `package.json` repository URL was placeholder (`user/bidding-hunter`)
- Warning: Example keywords in README.md exposed business domain — replaced with generic construction procurement terms
- Warning: Platform-specific URL transformation in detail-fetcher.js extracted to adapter `transformDetailUrl()` hook
- Warning: national.js DATA_SOURCES reordered 1→6 to sequential 1→2→3→4→5→6
- Warning: hebei.js and liaoning.js had hardcoded default query `['视频']` — removed, errors instead
- Info: SKILL.md example keywords synced with README (generic construction/IT terms)
- Info: `fetchDetails` builds URL transform closure once (was O(n×m) adapter loading)
- Info: CLI `fetchDetail` falls back to registry for URL transform when no options passed
- Info: database.js `new Database()` wrapped in try/catch for graceful fallback when native binding missing
- Info: `notifier.js` uses centralized `resolvePath()` instead of inline regex
- Info: `DATE_RE` global regex state protected with try-finally
- Reporter: Skip empty scan stats line when no stats available

### Changed
- SKILL.md: Added mandatory tool-discipline section (agents must use existing tools, not write ad-hoc scripts)
- SKILL.md: Added platform compatibility note (works with any AI assistant that can execute CLI tools)
- BasePlatformAdapter: Added `transformDetailUrl(url)` hook for platform-specific URL transformations
- Registry: Added `findTransformDetailUrl()` for adapter URL transform lookup
- Scanner: Null element tracking and filtering during item collection
- Scanner: `politeDelay` from config passed to adapterContext (was hardcoded per-adapter)
- All platform adapters: use `ctx.politeDelay` instead of hardcoded `waitForTimeout` values

## [1.0.0] - 2026-07-22

### Added
- Core scanning engine with pluggable platform adapter system
- 5 built-in platform adapters: Beijing, Hebei, Liaoning, Dalian, National
- Configurable multi-tier keyword matching engine
- SQLite database with JSON fallback for storage
- Detail page fetcher with automatic date/budget/method extraction
- Deadline tracking and reminder engine (urgent/open-results/missing-dates)
- Multi-channel notification system (stdout, file, webhook, Feishu, DingTalk, Slack)
- Markdown and JSON report generation
- CLI with 12 commands (scan, report, list, status, remind, stats, export, init, explore, create-adapter, test-platform)
- File-based lock for concurrent-run prevention
- Checkpoint system for idempotent runs
- URL-based deduplication across platforms
- Platform exploration helper for adding new sites
- Platform adapter template with documentation
- Comprehensive test suite with fixtures
- Full documentation: README, DESIGN.md, CONTRIBUTING.md, SKILL.md
