---
name: computer-control
description: >
  Control the computer like a human: take screenshots, move/click the mouse,
  type text, press hotkeys, scroll, launch apps, and run AppleScript — via the
  dependency-free `tarsx` CLI (zero config, no API keys). Click windows by app
  name (`clickwin`), no pixel guessing. Cross-platform core with auto-detected
  backends: macOS first (cliclick/osascript/screencapture), Linux (xdotool),
  Windows (PowerShell). Non-ASCII text (Cyrillic, emoji) works out of the box
  via clipboard paste. Use when the user asks to open/close an app, click or
  type somewhere, take a screenshot, automate a GUI application, fill a desktop
  form, check what is on screen, or any GUI automation that shell/browser tools
  cannot reach. Ukrainian triggers: "відкрий/закрий програму", "натисни",
  "набери", "зроби скріншот", "керуй комп'ютером". Inspired by Agent TARS
  (GUI-first computer use), implemented natively.
metadata:
  version: "1.0.1"
  license: "Apache-2.0"
  source: "tars-universum (Agent TARS-inspired native stack)"
---

# Computer Control (tarsx)

Control the computer through the `tarsx` CLI. Every command prints a one-line result;
errors are descriptive (most common: missing OS permissions, see Permissions).

## First step

Run `tarsx info` before any other action: it reports the platform, available
backends, and active config, so you know what works before you start.

## Install (once, if `tarsx` is not on PATH)

```bash
bash "$(dirname "$0")/scripts/install.sh"   # or an absolute path to this skill's scripts/install.sh
```

The installer copies the bundled, dependency-free `tarsx` to `~/.local/bin`.
No npm/network/API keys needed afterwards. Verify with `tarsx info`.

## Core loop (look → decide → act)

1. **Check**: `tarsx info` — confirm backends are detected on this machine.
2. **Look**: `tarsx screenshot /tmp/shot.png` — then Read the PNG file to see the screen.
3. **Locate**: pick the target element's pixel coordinates from the screenshot,
   or skip coordinates entirely with `tarsx windows [App]` + `tarsx clickwin <App>`.
4. **Act**: `tarsx click X Y` / `tarsx type "text"` / `tarsx key k --cmd`.
5. **Verify**: take another screenshot and confirm the action landed before moving on.

## Command reference

```
tarsx screenshot [out.png] [--region x,y,w,h]   # screen capture (PNG path printed)
tarsx click <x> <y> [--right] [--double]        # click at global screen points
tarsx clickwin <AppName> [--offset dx,dy]       # BEST: click inside named app's window (center by default)
tarsx windows [AppName]                         # list visible windows: app, title, x,y,w,h
tarsx scroll [up|down] [lines]                  # scroll wheel
tarsx type "text"                               # keystrokes; non-ASCII goes via clipboard+⌘V
tarsx key <char|named> [--cmd] [--ctrl] [--alt] [--shift]
        # named keys: return, tab, escape, delete, home, end, page up, page down,
        # left/right/up/down arrow, space, f1..f12
tarsx wait <seconds>                            # pause between actions (let apps load)
tarsx apps                                      # list visible running apps
tarsx open <AppName>                            # launch app ("Calculator", "Safari"...)
tarsx open <https://url>                        # open URL in default handler
tarsx osa 'tell application "Finder" to ...'    # arbitrary AppleScript (macOS: full automation)
tarsx info [--json]                             # diagnostics: detected backends + config
```
Add `--json` to any command for machine-readable output.

## Recipes

- Open an app and do something in it (no manual coordinates needed):
  `tarsx open "TextEdit"` → `tarsx wait 1.5` → `tarsx clickwin TextEdit` → `tarsx type "..."`.
- Need a specific spot inside a window: `tarsx windows TextEdit` gives x,y,w,h →
  compute the point → `tarsx click X Y`.
- Keyboard shortcut: `tarsx key s --cmd` (⌘S), `tarsx key w --cmd` (close tab/window).
- Ukrainian/Russian text: works automatically — non-ASCII is typed via clipboard paste,
  so the target field must be focused first.
- System queries that don't need GUI: prefer `tarsx osa` (e.g. battery, volume,
  window bounds: `tarsx osa 'tell application "System Events" to tell process "Safari" to get {position, size} of window 1'`).

## Permissions (macOS)

The app that runs the agent needs, in System Settings → Privacy & Security:
- **Accessibility** — clicks, typing, hotkeys (else "not allowed assistive access");
- **Screen Recording** — screenshots (else blank/wallpaper-only images);
- **Automation** — per-app consent on first AppleScript call to that app.
If a user reports nothing happened, ask them to approve the pending permission dialog.

## Safety rules

- Confirm before: deleting anything, sending messages/emails, purchases, logging out,
  closing windows with unsaved work ("Изменено"/"Edited" in the title).
- Never type passwords or one-time codes into GUI fields — ask the user to do it.
- After finishing, leave the screen in a clean state (close what you opened,
  discard test documents without saving).
- If a click "didn't land", re-screenshot instead of blindly retrying — UI may have changed.
