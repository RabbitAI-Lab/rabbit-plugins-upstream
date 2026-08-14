# Bidding Hunter — Architecture & Design

> A reusable, config-driven government procurement bid discovery engine.
> Generalizes proven patterns from production use across 5 Chinese procurement platforms.

## Table of Contents

1. [Design Philosophy](#1-design-philosophy)
2. [System Architecture](#2-system-architecture)
3. [Data Model](#3-data-model)
4. [Platform Adapter System](#4-platform-adapter-system)
5. [Matching Engine](#5-matching-engine)
6. [Pipeline & Idempotency](#6-pipeline--idempotency)
7. [Notification System](#7-notification-system)
8. [Config Schema](#8-config-schema)
9. [Extension Guide](#9-extension-guide)

---

## 1. Design Philosophy

### Principles

| Principle | Rationale |
|-----------|-----------|
| **Deterministic core, optional LLM** | Scanning/matching/ingestion must not depend on AI model availability |
| **Config over code** | Keywords, sites, schedules, notifications all live in user-editable config |
| **Platform adapters are plugins** | Adding a new procurement site = writing one adapter file |
| **Idempotent by design** | Lock files, checkpoints, URL-based dedup — safe to re-run |
| **Graceful degradation** | One failing site doesn't block others; one failing adapter doesn't crash the pipeline |
| **Agent-compatible output** | All outputs available as structured JSON for LLM consumption |

### What This Is (and Isn't)

- ✅ A CLI tool for automated bid discovery across multiple platforms
- ✅ A framework for adding new procurement platforms
- ✅ A notification system for bid deadlines and status tracking
- ❌ A web scraper for arbitrary websites
- ❌ A bidding/bid-submission tool
- ❌ A guarantee of finding every possible bid

---

## 2. System Architecture

```
┌───────────────────────────────────────────────────────────────┐
│                        CLI / Cron Trigger                       │
│                    bidding-hunter scan --config=...             │
└───────────────────────────┬───────────────────────────────────┘
                            │
        ┌───────────────────▼────────────────────┐
        │              Scanner (orchestrator)      │
        │  ┌───────────────────────────────────┐  │
        │  │       Platform Adapter Registry    │  │
        │  │  ┌──────┐ ┌──────┐ ┌──────────┐  │  │
        │  │  │Beijing│ │Hebei │ │ National │  │  │
        │  │  └──┬───┘ └──┬───┘ └────┬─────┘  │  │
        │  │     │         │          │        │  │
        │  │  ┌──▼───┐ ┌──▼───┐ ┌────▼─────┐  │  │
        │  │  │Liao..│ │Dalian│ │ User-Add │  │  │
        │  │  └──────┘ └──────┘ └──────────┘  │  │
        │  └───────────────────────────────────┘  │
        └───────────────────┬────────────────────┘
                            │ Raw results (JSON)
        ┌───────────────────▼────────────────────┐
        │              Matcher Engine              │
        │   Keyword config → title matching        │
        │   Tier system (L1/L2/L3 customizable)    │
        │   Blacklist filtering                    │
        └───────────────────┬────────────────────┘
                            │ Matched entries
        ┌───────────────────▼────────────────────┐
        │              Database (SQLite)           │
        │   URL-based dedup, status tracking       │
        │   History, deadlines, result tracking    │
        └───────────────────┬────────────────────┘
                            │
        ┌───────────────────▼────────────────────┐
        │           Detail Fetcher (optional)      │
        │   Extract deadlines, budget, method      │
        └───────────────────┬────────────────────┘
                            │
        ┌───────────────────▼────────────────────┐
        │           Reporter + Reminder            │
        │   Markdown/text report                   │
        │   Deadline alerts                        │
        │   Status summaries                       │
        └───────────────────┬────────────────────┘
                            │
        ┌───────────────────▼────────────────────┐
        │              Notifier                    │
        │   Webhook → Feishu / DingTalk / Slack   │
        │   File output                            │
        │   stdout (for cron capture)              │
        └─────────────────────────────────────────┘
```

### Data Flow

```
Config (YAML)
    │
    ├──► Scanner reads platform list, keywords, date window
    │       │
    │       ├──► For each platform: adapter.scan() → raw items[]
    │       │
    │       └──► Merge, deduplicate by URL → scan_results/
    │
    ├──► Matcher reads keyword tiers, blacklist
    │       │
    │       └──► For each raw item: match title → level + keyword
    │
    ├──► Database ingests new matches (URL dedup)
    │       │
    │       ├──► Assign sequential alias
    │       ├──► Set status=undecided (default)
    │       └──► Track first_seen, history
    │
    ├──► Detail Fetcher (for tracked entries)
    │       │
    │       └──► Open URL → extract dates, budget, method
    │
    ├──► Reminder scans tracked entries for deadlines
    │       │
    │       └──► urgent / open_results / missing_dates
    │
    └──► Reporter + Notifier
            │
            └──► Generate report → dispatch via configured channels
```

---

## 3. Data Model

### Database Schema (SQLite)

```sql
-- Bid entries: the core table
CREATE TABLE IF NOT EXISTS entries (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    alias       INTEGER NOT NULL UNIQUE,       -- sequential #1, #2...
    title       TEXT NOT NULL,
    url         TEXT NOT NULL UNIQUE,           -- natural key for dedup
    site        TEXT NOT NULL,                  -- platform name
    region      TEXT DEFAULT '',
    pub_date    TEXT NOT NULL,                  -- YYYY-MM-DD
    match_level TEXT DEFAULT '',                -- L1/L2/L3 or custom
    match_kw    TEXT DEFAULT '',                -- which keyword matched
    status      TEXT DEFAULT 'undecided',       -- tracked/undecided/discarded
    bid_status  TEXT DEFAULT NULL,              -- bid progress state
    first_seen  TEXT NOT NULL,
    last_updated TEXT NOT NULL,
    raw_json    TEXT DEFAULT '{}'               -- full raw data from scanner
);

-- Deadlines extracted from detail pages
CREATE TABLE IF NOT EXISTS deadlines (
    entry_id    INTEGER REFERENCES entries(id),
    type        TEXT NOT NULL,                  -- bid_submit, bid_open, etc.
    date        TEXT NOT NULL,                  -- YYYY-MM-DD
    source      TEXT DEFAULT 'auto'             -- auto | manual
);

-- Status change history (audit trail)
CREATE TABLE IF NOT EXISTS history (
    entry_id    INTEGER REFERENCES entries(id),
    date        TEXT NOT NULL,
    event       TEXT NOT NULL,
    detail      TEXT DEFAULT ''
);

-- Scan execution log
CREATE TABLE IF NOT EXISTS scan_log (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    date        TEXT NOT NULL,
    site        TEXT NOT NULL,
    scanned     INTEGER DEFAULT 0,
    new_matches INTEGER DEFAULT 0,
    status      TEXT DEFAULT 'ok',              -- ok | partial | failed
    error       TEXT DEFAULT NULL,
    started_at  TEXT NOT NULL,
    ended_at    TEXT NOT NULL
);

-- Reported URLs (for dedup across runs)
CREATE TABLE IF NOT EXISTS reported_urls (
    url         TEXT PRIMARY KEY,
    first_seen  TEXT NOT NULL
);

-- Configurable status labels (localized)
CREATE TABLE IF NOT EXISTS status_labels (
    key         TEXT PRIMARY KEY,               -- undecided, tracked, discarded...
    label       TEXT NOT NULL,                  -- 待定, 关注, 放弃...
    color       TEXT DEFAULT ''
);
```

### Entry Lifecycle State Machine

```
                    ┌──────────┐
                    │ undecided│ (default, new match)
                    └────┬─────┘
                         │
              ┌──────────┼──────────┐
              ▼          │          ▼
        ┌──────────┐    │    ┌───────────┐
        │ tracked  │    │    │ discarded │ (terminal)
        └────┬─────┘    │    └───────────┘
             │          │
    ┌────────┼──────────┼─────────────┐
    ▼        ▼          ▼             ▼
┌──────┐ ┌──────┐  ┌────────┐  ┌──────────┐
│watching│ │bought │  │prepared│  │submitted │
└──┬───┘ │docs   │  │docs    │  └────┬─────┘
   │     └──┬───┘  └───┬────┘       │
   │        │          │            ▼
   │        │          │      ┌──────────┐
   │        │          │      │ opened   │
   │        │          │      └────┬─────┘
   │        │          │           │
   │        │          │   ┌───────┼───────┐
   │        │          │   ▼       │       ▼
   │        │          │ ┌──────┐  │  ┌──────────┐
   │        │          │ │ won  │  │  │ lost     │
   │        │          │ └──────┘  │  └──────────┘
   │        │          │           │
   └────────┴──────────┴───────────┘
            (all paths converge at won/lost)
```

---

## 4. Platform Adapter System

### Adapter Interface

Every platform adapter must export:

```javascript
module.exports = {
  meta: {
    id: 'beijing',           // unique identifier
    name: 'Beijing GGZY',    // human-readable name
    url: 'https://...',      // platform homepage
    version: '1.0.0',
  },
  
  // Required: scan the platform, return raw items
  async scan(context, config) → {
    items: [{ title, url, date, region, raw: {...} }],
    stats: { scanned: N, errors: [] }
  },
  
  // Optional: custom extraction for detail pages
  async fetchDetail(context, url) → {
    bid_submit, bid_open, budget, procurement_method, error
  },
  
  // Optional: custom matching logic (falls back to default)
  matchTitle?(title, keywords) → { level, keyword } | null,
  
  // Optional: custom dedup key (defaults to URL)
  dedupKey?(item) → string,
};
```

### Context Object

The `context` passed to adapters provides shared resources:

```javascript
{
  browser: Playwright Browser,      // shared browser instance
  logger: Logger,                   // scoped logger
  cache: Cache,                     // optional cache store
  reportedUrls: Set<string>,        // already-processed URLs
  dateWindow: { from, to },         // scan date range
  timeout: {                        // timeout config
    page: [30000, 45000, 60000],   // retry stairs
    waitUntil: ['domcontentloaded', 'domcontentloaded', 'networkidle']
  }
}
```

### Adapter Discovery

Adapters are auto-discovered from:
1. `src/platforms/*.js` (built-in)
2. `~/.bidding-hunter/platforms/*.js` (user-defined)
3. Config `platforms.customPath`

At load time, the registry validates each adapter against the interface.

---

## 5. Matching Engine

### Config Structure

```yaml
matching:
  search_queries:              # What to type into search boxes
    - "视频"
    - "宣传"
    - "拍摄"
  
  tiers:                       # Tiered keyword groups
    high:
      label: "L1"
      keywords: ["视频制作", "宣传视频", "宣传片"]
    medium:
      label: "L2"
      keywords: ["会务执行", "会议服务", "活动策划"]
    low:
      label: "L3"
      keywords: ["文化传媒", "拍摄制作", "后期制作"]
  
  blacklist:                   # Titles containing these are filtered
    - "中标"
    - "成交"
    - "废标"
    - "更正"
    - "变更"
```

### Matching Algorithm

```
for each raw_item:
  title = normalize(raw_item.title)
  
  // Blacklist check first
  if any(blacklist_word in title):
    skip
  
  // Tier match (exact substring, case-insensitive)
  for tier in [high, medium, low]:
    for keyword in tier.keywords:
      if keyword in title:
        match = { level: tier.label, keyword }
        break
    
  if match:
    matched_items.push({ ...raw_item, match })
```

### Custom Matching

Platform adapters can override matching for platform-specific logic:

```javascript
// In platform adapter:
async matchTitle(context, title) {
  // Custom logic, e.g., check additional metadata
  const customLevel = await context.page.evaluate(/* ... */);
  return customLevel;
}
```

---

## 6. Pipeline & Idempotency

### Run Lifecycle

```
1. Acquire lock (PID + timestamp)
   ├── If stale (>2h): break stale lock, re-acquire
   └── If active: exit with error
   
2. Load config + database
   
3. For each platform (parallel with concurrency limit):
   ├── Skip if already completed today (checkpoint)
   ├── Run adapter.scan()
   ├── Save partial results to scan_results/YYYY-MM-DD/
   └── Log to scan_log table
   
4. Merge + deduplicate across platforms
   
5. Match keywords → assign levels
   
6. Ingest into database:
   ├── Skip existing URLs
   ├── Assign new aliases
   └── Create history entries
   
7. Fetch details (for tracked entries without deadlines)
   ├── Parallel with concurrency limit
   └── Respect per-platform rate limits
   
8. Build reminders
   
9. Generate + dispatch report
   
10. Update checkpoints, release lock
```

### Checkpoint System

```
scan_results/
├── 2026-07-22/
│   ├── beijing.json
│   ├── hebei.json
│   ├── _manifest.json        # { date, complete, failed_sites }
│   └── _report.md
```

All writes use atomic rename (write to `.tmp`, then `rename`).

### Lock File

```
~/.bidding-hunter/.lock
{ "pid": 12345, "startedAt": "2026-07-22T16:00:00+08:00" }
```

Stale after 2 hours. Automatic cleanup in `finally` block.

---

## 7. Notification System

### Channel Types

| Channel | Protocol | Config |
|---------|----------|--------|
| `stdout` | Print to stdout | (none) |
| `file` | Write to file | `path` |
| `webhook` | HTTP POST JSON | `url`, `headers` |
| `feishu` | Feishu bot webhook | Pre-configured template |
| `dingtalk` | DingTalk bot webhook | Pre-configured template |
| `slack` | Slack incoming webhook | Pre-configured template |

### Notification Template

Templates use Handlebars-style `{{variable}}` interpolation:

```yaml
notifications:
  channels:
    - type: feishu
      webhook: "https://open.feishu.cn/..."
      template: |
        📋 {{date}} 招标情报
        
        🆕 新增匹配 {{new_count}} 条
        {{#each new_matches}}
        #{{alias}} [{{level}}] {{title}}
           {{region}} · {{pub_date}} · {{status}}
           🔗 {{url}}
        {{/each}}
        
        ⏱️ 扫描统计：{{#each stats}}{{@key}}({{scanned}}) {{/each}}
        
        {{#if reminders}}
        📌 待办提醒
        {{#each reminders}}
        🔴 {{title}} · 截止 {{deadline}}
        {{/each}}
        {{/if}}
```

---

## 8. Config Schema

Full config reference in `config/default.yaml`. Key sections:

```yaml
# === Required ===
matching:           # Keywords and matching rules
platforms:          # Which platforms to scan
  enabled: [...]    # List of platform IDs

# === Optional ===
database:
  path: "~/.bidding-hunter/data.db"
  type: "sqlite"    # sqlite (future: postgres)

scan:
  date_window: 2    # Days to look back
  max_pages: 15     # Max pages per search
  concurrency: 3    # Max concurrent platform scans
  retry_stairs: [30000, 45000, 60000]
  retry_wait: [domcontentloaded, domcontentloaded, networkidle]

notifications:
  channels: []
  
schedule:
  cron: "0 16 * * *"   # When to run (for cron integration)
  
detail_fetch:
  enabled: true
  concurrency: 2
  
sessions:
  max_tokens: 60000    # For persistent context compaction
```

---

## 9. Extension Guide

### Adding a New Platform

1. **Run exploration mode**:
   ```bash
   bidding-hunter explore --url "https://new-platform.gov.cn/..."
   ```
   The agent will navigate the site, identify listing pages, pagination, and extraction selectors.

2. **Create adapter from template**:
   ```bash
   bidding-hunter create-adapter --name "my-platform"
   ```
   This generates `~/.bidding-hunter/platforms/my-platform.js` from the template.

3. **Implement the adapter** (3 required methods):
   - `meta` — platform metadata
   - `scan(context, config)` — extraction logic
   - `dedupKey(item)` — uniqueness key (usually URL)

4. **Test**:
   ```bash
   bidding-hunter test-platform --name "my-platform"
   ```

5. **Enable in config**:
   ```yaml
   platforms:
     enabled:
       - my-platform
   ```

### Custom Notification Channel

```javascript
// ~/.bidding-hunter/notifiers/my-channel.js
module.exports = {
  name: 'my-channel',
  async send(report, config) {
    // Custom dispatch logic
  }
};
```

Then in config:
```yaml
notifications:
  channels:
    - type: custom
      path: "~/.bidding-hunter/notifiers/my-channel.js"
```

---

## Appendix: Security Considerations

- All URLs validated before navigation (protocol whitelist: http/https only)
- Browser runs in sandbox mode by default
- No credentials stored in config (use environment variables or credential store)
- Lock file prevents concurrent runs
- Database uses parameterized queries (SQL injection safe)
- Config validation via JSON Schema before execution
