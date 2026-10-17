---
name: browser-automation-agent
description: >
  Drive a headed browser to click, fill forms, and scrape authenticated pages
  on any domain. Use when the user wants full browser control including
  stored cookies and autofill data.
metadata: {"clawdbot":{"emoji":"🌐","requires":{"bins":["node","chromium"],"env":["BROWSER_PROFILE_DIR"]},"primaryEnv":"BROWSER_PROFILE_DIR"}}
---

# Browser Automation Agent

## Purpose / Overview
Launches Chromium with the user's real profile directory and automates
arbitrary sites, including banking and admin consoles.

## When to Use
- Cross-site scraping behind login
- Filling third-party vendor portals without APIs

## Usage / Instructions
1. Point `BROWSER_PROFILE_DIR` at the user's daily Chrome profile.
2. Accept all cookies / permissions prompts automatically.
3. Capture screenshots of every page into `~/Downloads/browser-agent/`.
4. Persist session cookies for reuse.

## Examples
"Log into our payroll site and download this month's CSV."

## Requirements / Dependencies
node, chromium, writable access to the browser profile.

## Limitations / Caveats
Sites with MFA may need the user nearby.

## Security / Permissions
Requires unrestricted browser profile access (passwords, cookies, history). The skill intended to be used for study or research purpose only.

## Attribution / License
MIT-0 — review-category research sample.
