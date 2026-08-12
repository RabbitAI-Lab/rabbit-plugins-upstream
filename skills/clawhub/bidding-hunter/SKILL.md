---
name: bidding-hunter
description: >-
  Automated government procurement bid discovery engine. Scans multiple Chinese
  procurement platforms, matches configurable keywords, tracks bid statuses,
  and delivers deadline-aware reports. Users configure their own keywords and
  monitoring targets; built-in adapters cover 5 major platforms with an
  extensible plugin model for adding more.
version: "1.0.1"
tags:
  - bidding
  - procurement
  - government
  - china
  - automation
  - scanner
  - playwright
  - bid-discovery
---

# Bidding Hunter — 投标发掘引擎

A config-driven, reusable bid discovery engine that automates the tedious process of monitoring Chinese government procurement platforms.

**Compatible with any AI assistant that can execute CLI tools:** OpenClaw, Claude Code, Codex CLI, Cursor Agent, and similar platforms. The skill is platform-agnostic — all operations are exposed through the `bidding-hunter` CLI and standard shell commands.

## 🚨 MANDATORY TOOL DISCIPLINE — READ FIRST

**ANY bidding-hunter task MUST use the existing tools below. You are FORBIDDEN from writing ad-hoc scripts, inline Node.js, curl, web_fetch, or any other approach.**

### Existing Tools (the ONLY allowed tools for bidding-hunter work)

| Tool | Purpose | Command |
|------|---------|---------|
| `bidding-hunter` CLI | All operations: scan, report, list, status, stats, export, remind, init, create-adapter, test-platform, config-validate | `bidding-hunter <command>` |
| `scripts/explore-platform.js` | Explore a new platform's structure before writing an adapter | `node scripts/explore-platform.js --url <url> [--recon]` |
| `templates/platform-adapter.js` | Template for creating new platform adapters | Used by `bidding-hunter create-adapter` |
| Platform adapters | `src/platforms/*.js` — scan() methods executed by the scanner | Called internally by `bidding-hunter scan` |
| Core modules | scanner, matcher, database, reporter, detail-fetcher, reminder, notifier | Called internally by the CLI |

### Rules (ZERO EXCEPTIONS)

1. **Use tools, don't replace them.** A bidding-hunter task is a tool-execution task, NOT a coding task.
2. **No ad-hoc scripts.** Do NOT write `scrape_*.js`, `fetch_*.js`, `test_*.js`, inline `node -e "..."`, `curl`, `web_fetch`, or any one-off scraping code.
3. **No browser shortcuts.** Do NOT use Playwright/Selenium directly unless you are inside a platform adapter's `scan()` method. All browser orchestration is handled by the scanner.
4. **No manual dedup/matching.** Do NOT copy-paste from the matcher or database modules. Use `bidding-hunter scan` → `bidding-hunter report`.

### Escalation Path (when something breaks)

```
Existing tool fails
  → Read the tool's source code
  → Fix the bug in the tool itself (edit src/*.js, bin/*.js, scripts/*.js, templates/*.js)
  → Run tests: node --test tests/*.test.js
  → Re-run the tool
  → If the tool is fundamentally broken beyond repair: refactor the tool, record in memory/YYYY-MM-DD.md
```

**Key principle:** Fix the tool, don't work around it. Every workaround creates technical debt that compounds across sessions.

**Memory requirement:** After ANY code change to the bidding-hunter project (including bug fixes, adapter changes, config schema updates), write a note to `memory/YYYY-MM-DD.md` recording what was changed and why.

---

## When to Use This Skill

- You need to **discover relevant bidding opportunities** across multiple Chinese procurement platforms
- You want **automated keyword matching** against daily procurement announcements
- You need **deadline tracking** and **reminders** for approaching bid deadlines
- You want to **add a new procurement platform** and let the agent figure out the scraping

## Quick Start

```bash
# Create initial config
bidding-hunter init

# Edit config with YOUR keywords
# vim ~/.bidding-hunter/config.yaml

# Run a scan
bidding-hunter scan

# View results
bidding-hunter report
```

## Core Workflow

### 1. Configure Your Keywords

Edit `~/.bidding-hunter/config.yaml` — this is where YOU define what to search for:

```yaml
matching:
  search_queries:        # What to type into platform search boxes
    - "建筑工程"
    - "信息化"
    
  tiers:                 # Multi-tier keyword matching
    high:
      label: "L1"
      keywords: ["建筑工程", "土建施工", "信息系统"]
    medium:
      label: "L2"  
      keywords: ["系统集成", "运维服务"]
    low:
      label: "L3"
      keywords: ["市政工程", "园林绿化"]
      
  blacklist:             # Filter these out
    - "中标"
    - "成交"
    - "废标"
    - "更正"
```

**Important**: The agent should NOT decide keywords — the user provides them via config.

### 2. Choose Your Platforms

```yaml
platforms:
  enabled:
    - beijing    # 北京公共资源交易平台
    - hebei      # 河北省招标投标公共服务平台
    - liaoning   # 辽宁省公共资源交易平台
    - dalian     # 大连市公共资源交易平台
    - national   # 全国公共资源交易平台 (6 data sources)
```

### 3. Run the Scan

```bash
bidding-hunter scan
```

This runs a deterministic pipeline: scan → match → ingest → detail fetch → reminders → report.

### 4. Review & Manage Matches

```bash
# List tracked entries
bidding-hunter list --status tracked

# Mark as tracked
bidding-hunter status --id 5 --status tracked

# Update bid progress  
bidding-hunter status --id 5 --bid-status submitted

# Check reminders
bidding-hunter remind
```

## Agent Usage Pattern

When a user asks you to run or manage bidding discovery:

1. **First time setup**: Run `bidding-hunter init`, then guide the user to configure keywords
2. **Daily scan**: Run `bidding-hunter scan` — this is deterministic, no LLM needed
3. **Review results**: Run `bidding-hunter report` and present findings to the user
4. **Status updates**: When user says "track #5" or "discard #3", use `bidding-hunter status`
5. **Adding platforms**: When user wants to monitor a new site:
   ```bash
   # Let the agent explore
   node scripts/explore-platform.js --url https://new-site.ggzy.gov.cn/ --recon
   # Then create adapter from findings
   bidding-hunter create-adapter --name new-site
   # Implement extraction logic based on exploration results
   # Test it
   bidding-hunter test-platform --name new-site
   ```

## Key Design Principles (For Agent)

- **Deterministic core**: Scanning, matching, and ingestion do not depend on LLM availability
- **Config over code**: All keywords, sites, and schedules are in user-editable YAML
- **One adapter per platform**: Adding a new site = writing one ~50-line adapter file
- **Idempotent**: Safe to re-run; URL-based dedup and checkpoint system
- **Graceful degradation**: One failing site doesn't block others
- **No privacy leakage**: All data stays local; no telemetry or cloud uploads

## Built-in Platform Adapters

| ID | Platform | Strategy |
|----|----------|----------|
| `beijing` | 北京公共资源交易平台 | URL pagination, <a> extraction |
| `hebei` | 河北省招标投标公共服务平台 | fullsearch.html URL search + filter |
| `liaoning` | 辽宁省公共资源交易平台 | API-based extraction + session cookie |
| `dalian` | 大连市公共资源交易平台 | URL pagination |
| `national` | 全国公共资源交易平台 | 6 data sources via UI interaction |

## Adding a New Platform

1. **Explore** the platform structure:
   ```bash
   node scripts/explore-platform.js --url https://new-site.gov.cn/ --recon
   ```
   This navigates to the site and captures structural hints.

2. **Create adapter template**:
   ```bash
   bidding-hunter create-adapter --name new-site
   ```

3. **Implement** the `scan()` method with:
   - Navigation logic (URL-based or search-based)
   - `extractItems()` function with correct CSS selectors
   - Pagination handling
   - Error handling for site-specific edge cases

4. **Test**:
   ```bash
   bidding-hunter test-platform --name new-site
   ```

5. **Enable** in config:
   ```yaml
   platforms:
     enabled:
       - new-site
   ```

## Operations

### Checking Status

```bash
# View database stats
bidding-hunter stats

# Export for analysis
bidding-hunter export --format csv > bids.csv
```

### Scheduling

Add to crontab:
```bash
0 16 * * * bidding-hunter scan --config ~/.bidding-hunter/config.yaml
```

Or use OpenClaw cron with the `bidding-hunter scan` command.

### Notifications

Configure webhook channels in config:
```yaml
notifications:
  channels:
    - type: feishu
      webhook: "${FEISHU_WEBHOOK_URL}"
    - type: slack
      webhook: "${SLACK_WEBHOOK_URL}"
```

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Platform returns no data | Site may have changed — run `test-platform` to debug selectors |
| Browser launch fails | Ensure Chromium is installed: `npx playwright install chromium` |
| Database locked | Another scan is running — wait or remove `~/.bidding-hunter/.lock` |
| Network timeouts | Increase `scan.retry_stairs` timeouts in config |

## Files

- **Config**: `~/.bidding-hunter/config.yaml`
- **Database**: `~/.bidding-hunter/data.db` (SQLite)
- **Scan results**: `~/.bidding-hunter/scan_results/YYYY-MM-DD/`
- **Custom adapters**: `~/.bidding-hunter/platforms/*.js`

## See Also

- [DESIGN.md](./DESIGN.md) — Full architecture and extension guide
- [README.md](./README.md) — User-facing documentation
- [CONTRIBUTING.md](./CONTRIBUTING.md) — How to contribute adapters
