---
name: desktop-control-win
version: 1.0.0
description: "Control Windows desktop applications �� launch/close/focus/resize/move windows, simulate keyboard..."
tags: [automation, general, cli, api-integration]
---

# Desktop Control - Full Windows Application Control

Control any desktop application on this Windows machine. Launch programs, manage windows, simulate input, control VSCode, and monitor processes - all via PowerShell scripts.

## Dependencies

- **OS**: Windows 10/11
- **PowerShell**: 5.1+ (pre-installed)
- **VSCode**: Required for VSCode control features (optional for other features)

## Script Location

All scripts are located relative to this skill folder:

```
SKILL_DIR = ~/.openclaw/workspace/skills/desktop-control-win/scripts
```

When running scripts, always use the full path:
```powershell
powershell -ExecutionPolicy Bypass -File "$HOME/.openclaw/workspace/skills/desktop-control-win/scripts/<script>.ps1" -Action <action> [params]
```

## Safety Rules

1. **Before closing windows** - Ask user for confirmation if the window might have unsaved work
2. **Before killing processes** - Always confirm with user unless they explicitly asked to kill it
3. **Before sending input** - Make sure the correct window is focused first
4. **Clipboard** - Warn user if you are overwriting clipboard content

---

## Action Reference

### 1. Window Management (`app-control.ps1`)

Manage application windows - launch, close, focus, resize, move, snap.

#### List all visible windows
```powershell
powershell -ExecutionPolicy Bypass -File "$HOME/.openclaw/workspace/skills/desktop-control-win/scripts/app-control.ps1" -Action list-windows
```
Returns: PID, window title, position (X,Y), size (W x H), state (Normal/Minimized/Maximized)

#### Launch an application
```powershell
# By name (searches PATH and common locations)
powershell -ExecutionPolicy Bypass -File "$HOME/.openclaw/workspace/skills/desktop-control-win/scripts/app-control.ps1" -Action launch -Target "notepad"

# By full path
powershell -ExecutionPolicy Bypass -File "$HOME/.openclaw/workspace/skills/desktop-control-win/scripts/app-control.ps1" -Action launch -Target "C:\Program Files\MyApp\app.exe"

# With arguments
powershell -ExecutionPolicy Bypass -File "$HOME/.openclaw/workspace/skills/desktop-control-win/scripts/app-control.ps1" -Action launch -Target "code" -Arguments "C:\Users\project"
```

#### Focus (bring to foreground)
```powershell
# By window title (partial match)
powershell -ExecutionPolicy Bypass -File "$HOME/.openclaw/workspace/skills/desktop-control-win/scripts/app-control.ps1" -Action focus -Target "Visual Studio Code"

# By PID
powershell -ExecutionPolicy Bypass -File "$HOME/.openclaw/workspace/skills/desktop-control-win/scripts/app-control.ps1" -Action focus -ProcId 12345
```

#### Close a window gracefully
```powershell
powershell -ExecutionPolicy Bypass -File "$HOME/.openclaw/workspace/skills/desktop-control-win/scripts/app-control.ps1" -Action close -Target "Notepad"
```

#### Minimize / Maximize / Restore
```powershell
powershell -ExecutionPolicy Bypass -File "$HOME/.openclaw/workspace/skills/desktop-control-win/scripts/app-control.ps1" -Action minimize -Target "Visual Studio Code"
powershell -ExecutionPolicy Bypass -File "$HOME/.openclaw/workspace/skills/desktop-control-win/scripts/app-control.ps1" -Action maximize -Target "Visual Studio Code"
powershell -ExecutionPolicy Bypass -File "$HOME/.openclaw/workspace/skills/desktop-control-win/scripts/app-control.ps1" -Action restore -Target "Visual Studio Code"
```

#### Move a window
```powershell
powershell -ExecutionPolicy Bypass -File "$HOME/.openclaw/workspace/skills/desktop-control-win/scripts/app-control.ps1" -Action move -Target "Notepad" -X 100 -Y 200
```

#### Resize a window
```powershell
powershell -ExecutionPolicy Bypass -File "$HOME/.openclaw/workspace/skills/desktop-control-win/scripts/app-control.ps1" -Action resize -Target "Notepad" -Width 800 -Height 600
```

#### Snap a window (half-screen)
```powershell
# Options: left, right, top, bottom, topleft, topright, bottomleft, bottomright
powershell -ExecutionPolicy Bypass -File "$HOME/.openclaw/workspace/skills/desktop-control-win/scripts/app-control.ps1" -Action snap -Target "Notepad" -Position left
```

---

### 2. Input Simulation (`input-sim.ps1`)

Simulate keyboard and mouse input into any application.

**IMPORTANT:** Always focus the target window FIRST using `app-control.ps1 -Action focus` before sending input.

#### Type text
```powershell
powershell -ExecutionPolicy Bypass -File "$HOME/.openclaw/workspace/skills/desktop-control-win/scripts/input-sim.ps1" -Action type-text -Text "Hello, World!"
```

#### Send keyboard shortcut
```powershell
# Common shortcuts: Ctrl+S, Ctrl+C, Ctrl+V, Ctrl+Z, Alt+F4, Ctrl+Shift+P, Win+D
powershell -ExecutionPolicy Bypass -File "$HOME/.openclaw/workspace/skills/desktop-control-win/scripts/input-sim.ps1" -Action send-keys -Keys "Ctrl+S"
powershell -ExecutionPolicy Bypass -File "$HOME/.openclaw/workspace/skills/desktop-control-win/scripts/input-sim.ps1" -Action send-keys -Keys "Ctrl+Shift+P"
powershell -ExecutionPolicy Bypass -File "$HOME/.openclaw/workspace/skills/desktop-control-win/scripts/input-sim.ps1" -Action send-keys -Keys "Alt+Tab"
```

#### Send special keys
```powershell
# Keys: Enter, Tab, Escape, Backspace, Delete, Up, Down, Left, Right, Home, End, PageUp, PageDown, F1-F12
powershell -ExecutionPolicy Bypass -File "$HOME/.openclaw/workspace/skills/desktop-control-win/scripts/input-sim.ps1" -Action send-keys -Keys "Enter"
powershell -ExecutionPolicy Bypass -File "$HOME/.openclaw/workspace/skills/desktop-control-win/scripts/input-sim.ps1" -Action send-keys -Keys "F5"
```

#### Mouse click at coordinates
```powershell
# Left click
powershell -ExecutionPolicy Bypass -File "$HOME/.openclaw/workspace/skills/desktop-control-win/scripts/input-sim.ps1" -Action mouse-click -X 500 -Y 300

# Right click
powershell -ExecutionPolicy Bypass -File "$HOME/.openclaw/workspace/skills/desktop-control-win/scripts/input-sim.ps1" -Action mouse-click -X 500 -Y 300 -Button right

# Double click
powershell -ExecutionPolicy Bypass -File "$HOME/.openclaw/workspace/skills/desktop-control-win/scripts/input-sim.ps1" -Action mouse-click -X 500 -Y 300 -DoubleClick
```

#### Move mouse
```powershell
powershell -ExecutionPolicy Bypass -File "$HOME/.openclaw/workspace/skills/desktop-control-win/scripts/input-sim.ps1" -Action mouse-move -X 500 -Y 300
```

#### Scroll
```powershell
# Scroll up (positive) or down (negative)
powershell -ExecutionPolicy Bypass -File "$HOME/.openclaw/workspace/skills/desktop-control-win/scripts/input-sim.ps1" -Action mouse-scroll -Clicks 3
powershell -ExecutionPolicy Bypass -File "$HOME/.openclaw/workspace/skills/desktop-control-win/scripts/input-sim.ps1" -Action mouse-scroll -Clicks -3
```

---

### 3. VSCode Control (`vscode-control.ps1`)

Control Visual Studio Code through the `code` CLI and extensions.

#### Open a file
```powershell
powershell -ExecutionPolicy Bypass -File "$HOME/.openclaw/workspace/skills/desktop-control-win/scripts/vscode-control.ps1" -Action open-file -Path "C:\Users\project\main.py"
```

#### Open a file at a specific line
```powershell
powershell -ExecutionPolicy Bypass -File "$HOME/.openclaw/workspace/skills/desktop-control-win/scripts/vscode-control.ps1" -Action goto -Path "C:\Users\project\main.py" -Line 42
```

#### Open a folder/workspace
```powershell
powershell -ExecutionPolicy Bypass -File "$HOME/.openclaw/workspace/skills/desktop-control-win/scripts/vscode-control.ps1" -Action open-folder -Path "C:\Users\project"
```

#### Open diff view
```powershell
powershell -ExecutionPolicy Bypass -File "$HOME/.openclaw/workspace/skills/desktop-control-win/scripts/vscode-control.ps1" -Action open-diff -Path "file1.py" -Path2 "file2.py"
```

#### List installed extensions
```powershell
powershell -ExecutionPolicy Bypass -File "$HOME/.openclaw/workspace/skills/desktop-control-win/scripts/vscode-control.ps1" -Action list-extensions
```

#### Install an extension
```powershell
powershell -ExecutionPolicy Bypass -File "$HOME/.openclaw/workspace/skills/desktop-control-win/scripts/vscode-control.ps1" -Action install-extension -ExtensionId "ms-python.python"
```

#### Uninstall an extension
```powershell
powershell -ExecutionPolicy Bypass -File "$HOME/.openclaw/workspace/skills/desktop-control-win/scripts/vscode-control.ps1" -Action uninstall-extension -ExtensionId "ms-python.python"
```

#### Open a new terminal in VSCode
```powershell
# This focuses VSCode and sends Ctrl+` to toggle terminal
powershell -ExecutionPolicy Bypass -File "$HOME/.openclaw/workspace/skills/desktop-control-win/scripts/vscode-control.ps1" -Action new-terminal
```

#### Open VSCode command palette
```powershell
powershell -ExecutionPolicy Bypass -File "$HOME/.openclaw/workspace/skills/desktop-control-win/scripts/vscode-control.ps1" -Action command-palette
```

---

### 4. Process Management (`process-manager.ps1`)

Monitor and manage running processes.

#### List running processes
```powershell
# All processes
powershell -ExecutionPolicy Bypass -File "$HOME/.openclaw/workspace/skills/desktop-control-win/scripts/process-manager.ps1" -Action list

# Filter by name
powershell -ExecutionPolicy Bypass -File "$HOME/.openclaw/workspace/skills/desktop-control-win/scripts/process-manager.ps1" -Action list -Name "code"

# Top N by memory
powershell -ExecutionPolicy Bypass -File "$HOME/.openclaw/workspace/skills/desktop-control-win/scripts/process-manager.ps1" -Action list -SortBy memory -Top 10
```

#### Get detailed process info
```powershell
powershell -ExecutionPolicy Bypass -File "$HOME/.openclaw/workspace/skills/desktop-control-win/scripts/process-manager.ps1" -Action info -ProcId 12345
```

#### Start a new process
```powershell
powershell -ExecutionPolicy Bypass -File "$HOME/.openclaw/workspace/skills/desktop-control-win/scripts/process-manager.ps1" -Action start -Path "notepad.exe" -Arguments "C:\file.txt"
```

#### Kill a process (CONFIRM WITH USER FIRST)
```powershell
powershell -ExecutionPolicy Bypass -File "$HOME/.openclaw/workspace/skills/desktop-control-win/scripts/process-manager.ps1" -Action kill -ProcId 12345
powershell -ExecutionPolicy Bypass -File "$HOME/.openclaw/workspace/skills/desktop-control-win/scripts/process-manager.ps1" -Action kill -Name "notepad"
```

---

### 5. Screen & System Info (`screen-info.ps1`)

Get display information, window details, clipboard, and screenshots.

#### List displays/monitors
```powershell
powershell -ExecutionPolicy Bypass -File "$HOME/.openclaw/workspace/skills/desktop-control-win/scripts/screen-info.ps1" -Action displays
```

#### Get active (focused) window info
```powershell
powershell -ExecutionPolicy Bypass -File "$HOME/.openclaw/workspace/skills/desktop-control-win/scripts/screen-info.ps1" -Action active-window
```

#### Take a screenshot
```powershell
# Full screen
powershell -ExecutionPolicy Bypass -File "$HOME/.openclaw/workspace/skills/desktop-control-win/scripts/screen-info.ps1" -Action screenshot -OutputPath "$HOME/screenshot.png"

# Specific window
powershell -ExecutionPolicy Bypass -File "$HOME/.openclaw/workspace/skills/desktop-control-win/scripts/screen-info.ps1" -Action screenshot -Target "Notepad" -OutputPath "$HOME/notepad-screenshot.png"
```

#### Read/set clipboard
```powershell
powershell -ExecutionPolicy Bypass -File "$HOME/.openclaw/workspace/skills/desktop-control-win/scripts/screen-info.ps1" -Action clipboard-get
powershell -ExecutionPolicy Bypass -File "$HOME/.openclaw/workspace/skills/desktop-control-win/scripts/screen-info.ps1" -Action clipboard-set -Text "Text to copy"
```

#### Get system info
```powershell
powershell -ExecutionPolicy Bypass -File "$HOME/.openclaw/workspace/skills/desktop-control-win/scripts/screen-info.ps1" -Action system-info
```

---

## Common Workflows

### Type something into a specific application
```
1. app-control.ps1 -Action focus -Target "Notepad"
2. input-sim.ps1 -Action type-text -Text "Hello World"
```

### Arrange two windows side-by-side
```
1. app-control.ps1 -Action snap -Target "Visual Studio Code" -Position left
2. app-control.ps1 -Action snap -Target "Chrome" -Position right
```

### Kill a frozen application
```
1. process-manager.ps1 -Action list -Name "frozen-app"
   (note the PID)
2. ASK USER FOR CONFIRMATION
3. process-manager.ps1 -Action kill -ProcId <pid>
```

---

## Error Handling

| Error | Cause | Resolution |
|-------|-------|------------|
| `Window not found` | Window title doesn't match | Use `list-windows` to see exact titles, then match more precisely |
| `Access denied` | System process needs admin rights | Inform user; run PowerShell as Administrator if needed |
| `Input not working` | Target window not focused | Focus the window first with `app-control.ps1 -Action focus` |
| `VSCode CLI not found` | VSCode not in PATH | Try `code --version` first; if missing, launch VSCode from Start Menu |
| `Script execution policy` | PowerShell execution restricted | Use `-ExecutionPolicy Bypass` flag |
| `Screenshot failed` | No display or permission issue | Check display is active; some apps block screenshots (DRM) |

### Degradation Strategy

- If a script returns exit code 0 - success
- If a script returns exit code 1 - error (check stderr output for details)
- If window operations fail, fall back to `list-windows` to refresh window list
- If VSCode CLI is unavailable, use `app-control.ps1` for basic window management only
- If mouse/keyboard simulation fails, ensure no security software is blocking input injection
