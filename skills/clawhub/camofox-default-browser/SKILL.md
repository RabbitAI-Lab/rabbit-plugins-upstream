---
name: camofox-default-browser
description: Anti-detection browser automation via Camoufox Firefox fork — bypasses Cloudflare, captcha, and bot blocking
version: 1.1.0
user-invocable: true
homepage: "https://github.com/jo-inc/camofox-browser"
metadata:
  openclaw:
    requires:
      bins: ["node"]
    primaryEnv: CAMOUFOX_EXECUTABLE
---

# Camofox Default Browser

Use Camoufox anti-detection browser (Firefox fork with C++-level fingerprint spoofing) as OpenClaw's browser automation engine. The `camofox_*` tools bypass CAPTCHAs, Cloudflare, and bot detection that standard Chromium/Playwright automation triggers.

## When to Use

- **Always prefer `camofox_*` over built-in `browser` tool** — for external public websites that may have anti-bot protection
- The built-in `browser` tool (Playwright/Chromium) gets detected by Google, LinkedIn, Amazon, Cloudflare, and most WAFs. Camoufox spoofs at the C++ compiler level, undetectable by JavaScript checks.

## Reason
Camoufox patches the entire browser at the C++ implementation level: navigator.hardwareConcurrency, WebGL renderer, AudioContext, screen geometry, WebRTC — all spoofed before JavaScript ever sees them. No shims, no wrappers, no tells. Standard stealth plugins can themselves be fingerprinted; Camoufox cannot.

## Available Tools

| Tool | Purpose |
|------|---------|
| camofox_create_tab | Open a new anti-detection browser tab with isolated context |
| camofox_snapshot | Accessibility tree snapshot (~90% smaller than raw HTML) with stable element refs (e1, e2, e3) plus optional base64 screenshot |
| camofox_click | Click element by ref (e.g. "e3") or CSS selector |
| camofox_type | Type text into form field. Set pressEnter=true to submit |
| camofox_navigate | Navigate to URL or use search macro: @google_search, @youtube_search, @amazon_search, @reddit_search, @linkedin_search, @wikipedia_search, @twitter_search, @yelp_search, @spotify_search, @instagram_search, @tiktok_search, @twitch_search, @netflix_search |
| camofox_scroll | Scroll page up/down by pixel amount |
| camofox_screenshot | Capture screenshot of current page |
| camofox_close_tab | Close tab to free resources |
| camofox_evaluate | Execute JavaScript in page context |
| camofox_list_tabs | List all open tabs |
| camofox_import_cookies | Import Netscape cookie file for authenticated browsing (requires CAMOFOX_API_KEY) |

## Workflow

1. `camofox_create_tab(url="https://example.com")` → tabId
2. `camofox_snapshot(tabId="<id>")` → accessibility tree
3. `camofox_click/type(tabId="<id>", ref="e3")` → interact
4. `camofox_close_tab(tabId="<id>")` → cleanup

## Resource Management

- Server auto-starts with OpenClaw Gateway (default port 9377)
- Browser engine launches lazily on first tab request
- Idle browser shuts down after configurable timeout (default 5 min)
- ~40MB memory when idle, ~200MB with active browser session
- Session isolation: separate cookies/storage per user
- Health endpoint: GET http://localhost:9377/health
- Crash telemetry: anonymized (no page content, cookies, IPs). Opt out via CAMOFOX_CRASH_REPORT_ENABLED=false

## Dependencies

```bash
# System (Linux)
apt-get install -y libgtk-3-0 libgdk-pixbuf2.0-0 libdbus-glib-1-2 \
  libxt6 libxcomposite1 libxdamage1 libxfixes3 libxrandr2 \
  libatk-bridge2.0-0 libdrm2 libgbm1 xvfb

# Environment
export CAMOUFOX_EXECUTABLE=/root/.cache/camoufox/camoufox
```
