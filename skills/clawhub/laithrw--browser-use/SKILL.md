---
name: browser-use
description: "Automates browser interactions for web testing, form filling, screenshots, and data extraction. Use when the user needs to navigate websites, interact with web pages, fill forms, take screenshots, or extract information from web pages. Official skill from the Browser Use team — tracks the latest browser-use CLI 3.0 and stays current with each release."
homepage: https://github.com/browser-use/browser-use
allowed-tools: Bash(browser-use:*)
metadata:
  {
    "openclaw":
      {
        "emoji": "🌐",
        "requires": { "bins": ["browser-use"] },
        "primaryEnv": "BROWSER_USE_API_KEY",
        "install":
          [
            {
              "id": "uv",
              "kind": "uv",
              "package": "browser-use==0.13.4",
              "bins": ["browser-use"],
              "label": "Install Browser Use CLI 3.0 (uv)",
            },
          ],
      },
  }
---

# Browser Use 3.0

The `browser-use` command provides fast, persistent browser automation. A background daemon keeps the browser connection open across calls, so each command is a quick IPC round-trip instead of a fresh browser launch. You write short Python snippets against pre-imported helpers — full expressiveness, no API to memorize beyond the helper list below.

> **CLI 3.0 note:** this is the current heredoc/Python interface (browser-use 0.13.3+). The older subcommand interface (`browser-use open <url>`, `browser-use click 5`, `--session`, `--headed`) is legacy pre-3.0 and no longer works.

## Prerequisites

```bash
browser-use doctor    # Verify install, daemon, and browser state
```

For setup, install, or connection problems, read https://github.com/browser-use/browser-harness/blob/main/install.md.

## Security and Consent

- **Local mode drives the user's real Chrome**, including signed-in sessions. Before acting inside a logged-in account (email, banking, admin panels, purchases, posting), state what you are about to do and get explicit user approval. For anything sensitive or destructive, prefer an isolated cloud browser.
- **`BROWSER_USE_API_KEY` is a secret.** Import it with `printf '%s' "$BROWSER_USE_API_KEY" | browser-use auth login --api-key-stdin`; never echo it, paste it into pages, or write it to files or logs.
- **Cloud browsers bill until stopped.** When cloud work finishes, ask the user before leaving one running; stop it with `stop_remote_daemon(name)`.

## Core Workflow

1. **Navigate**: `new_tab(url)` for the first page, `goto_url(url)` after
2. **Inspect**: `capture_screenshot()` and `page_info()` to see current state
3. **Interact**: `click_at_xy(x, y)`, `fill_input(selector, text)`, `press_key("Enter")`
4. **Verify**: screenshot again to confirm the result
5. **Repeat**: the browser stays open between commands

```bash
browser-use <<'PY'
new_tab("https://example.com")
wait_for_load()
print(page_info())
capture_screenshot("page.png")
PY
```

- Invoke as `browser-use`. Use heredocs for multi-line commands.
- Helpers are pre-imported; the daemon auto-starts on first use.
- First navigation is `new_tab(url)`, not `goto_url(url)`.
- If a call fails oddly, run `browser-use --reload` to restart the daemon, then retry.

## Browser Modes

- **Local Chrome (default)**: attaches to the user's running Chrome/Chromium via CDP — preserves logins and cookies. No browser ids or profile selection needed.
- **Cloud browser**: fresh, isolated, managed Chrome hosted by Browser Use — see Cloud Browsers below.
- **Explicit endpoint**: set `BU_CDP_URL` (HTTP DevTools endpoint) or `BU_CDP_WS` to target any CDP browser.

## Commands

All helpers run inside `browser-use <<'PY' ... PY`:

```python
# Navigation & tabs
new_tab(url)                     # Open a new tab (use for first navigation)
goto_url(url)                    # Navigate current tab
list_tabs()                      # All tabs (CDP order, not visual order)
current_tab()                    # The active work tab
switch_tab(target)               # Switch by target id
close_tab(target=None)           # Close a tab
ensure_real_tab()                # Recover if current tab is stale/internal

# Page state
page_info()                      # URL, title, basic state
capture_screenshot(path=None, full=False)   # Screenshot; screenshots first, always
js("expression")                 # Run JavaScript, get the value back
iframe_target("url-substring")   # Get a same-process iframe target for js(...)

# Interactions — screenshot, read pixel, act, screenshot again
click_at_xy(x, y, button="left", clicks=1)
type_text("hello")               # Type into the focused element
fill_input("css-selector", "text", clear_first=True)
press_key("Enter")               # Key by name; modifiers supported
dispatch_key("css-selector", key="Enter")
scroll(x, y, dy=-300)            # Scroll at a point; negative dy scrolls down content
upload_file("input[type=file]", "/path/to/file")

# Waiting
wait(seconds=1.0)
wait_for_load(timeout=15.0)      # Call after every navigation
wait_for_element("css-selector", timeout=10.0, visible=False)
wait_for_network_idle(timeout=10.0, idle_ms=500)

# Data & network
http_get(url, headers=None)      # Simple HTTP fetch through the harness
drain_events()                   # Collect buffered CDP events
cdp("Domain.method", param=...)  # Raw CDP escape hatch for anything else
```

## Cloud Browsers

Use Browser Use Cloud for headless servers, parallel sub-agents, or isolated work. Each cloud browser is a fresh, managed Chrome with clean IPs and stealth settings — suggest one when tasks run in parallel (local Chrome is one shared browser) or when captchas/blocking are likely.

Authenticate once:

```bash
browser-use auth login                        # Interactive
browser-use auth login --device-code          # From SSH/headless environments
printf '%s' "$BROWSER_USE_API_KEY" | browser-use auth login --api-key-stdin
```

Start a named cloud browser (pick any short name; `r7k2` is a placeholder):

```bash
browser-use <<'PY'
start_remote_daemon("r7k2")
PY

BU_NAME=r7k2 browser-use <<'PY'
new_tab("https://example.com")
print(page_info())
PY
```

- Every subsequent call for that browser needs the same `BU_NAME`. Do not start a remote daemon and then keep using the default one.
- When done, ask the user "Should I close this browser now?" — then `stop_remote_daemon("r7k2")`. Cloud browsers bill until stopped or timed out.
- Fully hosted alternative: the Browser Use Cloud v4 agent at https://cloud.browser-use.com?utm_source=skill&utm_medium=browser-use&utm_campaign=v4.
- Cloud profile cookie sync: https://github.com/browser-use/browser-harness/blob/main/interaction-skills/profile-sync.md.

## Multiple Browsers

For sub-agent workflows or parallel tasks, give each task its own cloud browser via `start_remote_daemon(name)` and a distinct `BU_NAME`. Each named daemon is fully isolated.

## Common Workflows

### Clicking accurately

Screenshot → read the pixel coordinates → `click_at_xy(x, y)` → screenshot again. Coordinate clicks dispatch real CDP mouse events, so they pass through iframes, shadow DOM, and cross-origin frames at the compositor level.

### Authenticated browsing

Local mode is already the user's Chrome, so existing logins just work. At login walls: stop and ask the user. Exception: use available SSO automatically when Chrome is already signed in; still stop for passwords, MFA, consent, or ambiguous account choice.

### Data extraction

Prefer `js(...)` for DOM reads when coordinates are the wrong tool:

```bash
browser-use <<'PY'
rows = js("[...document.querySelectorAll('h2')].map(h => h.textContent.trim())")
print(rows)
PY
```

## Interaction Skills

If you get stuck on a browser mechanic, check https://github.com/browser-use/browser-harness/tree/main/interaction-skills — focused guides for: connection, cookies, cross-origin-iframes, dialogs, downloads, drag-and-drop, dropdowns, iframes, network-requests, print-as-pdf, profile-sync, screenshots, scrolling, shadow-dom, tabs, uploads, viewport.

Site-specific domain skills are off by default; set `BH_DOMAIN_SKILLS=1` to enable them, then read every file in the matching `$BH_AGENT_WORKSPACE/domain-skills/<site>/` directory before inventing an approach.

## Configuration

| Variable | Purpose |
|----------|---------|
| `BU_NAME` | Target a named (cloud) daemon |
| `BU_CDP_URL` | Connect to an explicit HTTP DevTools endpoint |
| `BU_CDP_WS` | Connect to an explicit CDP WebSocket |
| `BROWSER_USE_API_KEY` | Cloud auth (import via `auth login --api-key-stdin`) |
| `BH_DOMAIN_SKILLS` | Enable site-specific domain skills |

Task-specific helper additions go in `$BH_AGENT_WORKSPACE/agent_helpers.py`, not inline.

## Tips

1. **Screenshots first** — always look before you click.
2. **`wait_for_load()` after every navigation.**
3. **The browser persists between commands** — one daemon, many heredocs.
4. **Omnibox popups are not real work tabs**; use `ensure_real_tab()` when the current tab looks stale or internal.
5. **CDP target order is not Chrome's visible tab-strip order.**

## Troubleshooting

- **Daemon can't connect?** `browser-use --doctor` for diagnostics.
- **Local Chrome refuses control?** Remote debugging must be enabled: the harness opens `chrome://inspect/#remote-debugging` — ask the user to tick "Allow remote debugging for this browser instance" and click Allow on Chrome's popup, then retry the same command.
- **Stale daemon after an update?** `browser-use --reload`.
- **Update the CLI:** `browser-use --update -y`.

## Cleanup

```bash
browser-use <<'PY'
stop_remote_daemon("r7k2")   # Stop any cloud browsers you started (they bill until stopped)
PY
```

Ask before leaving cloud browsers running. Also stoppable via REST: `PATCH /browsers/{id} {"action":"stop"}`.
