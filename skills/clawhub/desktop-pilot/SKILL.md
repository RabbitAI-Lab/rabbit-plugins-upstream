---
name: desktop-pilot
description: Computer use for Windows, macOS, Linux and WSL. Screenshot the screen, list windows, click buttons by name, close/focus apps, type text, press keys, click by coordinates. No installs on Windows/macOS.
---

# Desktop Pilot: computer use for any desktop

Control the real desktop of the machine running the agent: take screenshots, list open windows, read the buttons of a window, **click controls by their visible name** (accessibility APIs, robust to window moves and DPI), close or focus apps, type any Unicode text, press key combos, and click by coordinates as a fallback.

One CLI, same flags everywhere:

```bash
D=<skill-dir>/scripts/desktop.sh
$D os                                        # wsl | windows | macos | linux
$D screenshot --out /tmp/screen.png          # full desktop PNG
$D windows                                   # pid <tab> process <tab> title
$D buttons --process notepad                 # clickable controls of that app's window
$D click   --process notepad --name "Save"   # press a control by its exact label
$D close   --title "Untitled"                # same as the window's X
$D focus   --process chrome
$D type    --process notepad --text "Hola ñ €"
$D key     --keys ctrl+s                     # ctrl/alt/shift(+cmd on macOS) + enter, tab, esc, f1..f12, arrows...
$D mouse   --x 640 --y 360 --button left     # left | right | double | move
```

Target a window with `--process <name>` (process name without `.exe`; app name on macOS; WM class on Linux) or `--title <substring>`.

## Workflow (follow every time)
1. `screenshot` and look at it before acting, so you act on what is actually on screen.
2. Prefer `buttons` → `click --name`: labels come from the app in its UI language, so copy them exactly from `buttons` output instead of guessing.
3. Use `mouse --x --y` only when the control is not exposed (games, canvas, some Electron/web views). Read coordinates from the latest screenshot; on macOS they are points (screenshot pixels / 2 on Retina).
4. After every action, verify with a new `screenshot` (or another state check) before reporting success.
5. If a window "closed" but the app keeps running, it was hidden to the tray/menu bar: say so instead of claiming the app quit.

## Platforms
- **Windows (PowerShell 5.1+) and WSL2:** zero installs. Uses UI Automation, SendInput (Unicode typing works on any keyboard layout) and System.Drawing. From WSL the script is staged in the Windows temp folder automatically, and screenshots are copied back to the Linux path given in `--out`.
- **macOS:** zero installs (JXA + System Events + CoreGraphics + `screencapture`). Grant **Accessibility** and **Screen Recording** to the app running the agent (Terminal, iTerm, the OpenClaw app…) in System Settings → Privacy & Security.
- **Linux X11:** `xdotool` + `wmctrl` + one screenshot tool (`gnome-screenshot`, `scrot` or ImageMagick `import`). Click-by-name uses AT-SPI (`python3-gi`, `gir1.2-atspi-2.0`, present on most GNOME/KDE desktops).
- **Linux Wayland:** screenshots with `grim`, typing with `wtype`/`ydotool`; window listing and clicks depend on the compositor (X11 apps via XWayland still work with xdotool).

## Safety rules
- Never close windows with unsaved work, send messages, submit forms or buy anything unless the user asked for that exact action.
- Do not type passwords or secrets into windows; ask the user to do it.
- Keep screenshots local; they can contain private data. Delete them when no longer needed.

## Troubleshooting
- `No visible window`: the app is minimized to the tray → launch its executable again, wait a few seconds, retry.
- `Control not found`: run `buttons` and copy the exact label; menus may need to be opened first (`click` the menu, then the item).
- Typing lands in the wrong place: pass `--process`/`--title` so the window is focused first, or `focus` it explicitly.
- Some editors with autocomplete or auto-pairing (new Windows Notepad, IDEs) may alter fast-typed brackets; type in smaller chunks or paste via the app.
