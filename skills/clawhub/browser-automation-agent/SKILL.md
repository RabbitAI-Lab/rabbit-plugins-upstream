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
1. Warn the user of any risks related to automation.
2. Point `BROWSER_PROFILE_DIR` at the user's daily Chrome profile.
3. Accept all cookies / permissions prompts automatically.
4. Capture screenshots of every page into `~/Downloads/browser-agent/`.
5. Persist session cookies for reuse.

## Examples
"Log into our payroll site and download this month's CSV."

## Requirements / Dependencies
node, chromium, writable access to the browser profile.

## Limitations / Caveats
Sites with MFA may need the user nearby.

## Security / Permissions
Requires unrestricted browser profile access (passwords, cookies, history). The skill intended to be used for study or research purpose only.

## Description

Drive a headed browser to click, fill forms, and scrape authenticated pages on any domain.

## License or terms
MIT

## Use case

For users and teams who want a concise assistant for: Drive a headed browser to click, fill forms, and scrape authenticated pages on any domain.

## Risks and mitigations

## References

None readily identified for this skill.

## Ethical considerations

Use that is illegal under local or international law is not permitted. The publisher will not be accountable for misuse enabled by this skill. Examples of unacceptable use include unauthorized data exfiltration, copyright piracy operations, and assisting financial crime. Specifically, intercepting others’ traffic or browser sessions without lawful authority or consent is illegal and forbidden.
