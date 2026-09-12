# Artifact Recipes — fastest ways for the user to produce common inputs

Copy the recipe into the ask; don't improvise one. Match their OS first.

## Screenshots (the #1 ask)

| OS | Fastest |
|---|---|
| Windows | `Win+Shift+S` → drag region → paste straight into chat |
| macOS | `Cmd+Shift+4` (region); `Cmd+Shift+4` then `Space` (window) |
| Linux | Spectacle (KDE), `gnome-screenshot -a`, or `flameshot gui` |

- Full / scrolling web page: DevTools (`F12`) → `Ctrl/Cmd+Shift+P` → "Capture full size screenshot" — built into Chrome, Edge, and Firefox, no extension needed.
- One element only: DevTools → select the element → `Ctrl/Cmd+Shift+P` → "Capture node screenshot".
- Android: `Power+Vol−`, or `adb exec-out screencap -p > screen.png`. iOS: `Power+Vol+` (or the screenshot button in Control Center).

## Screen recordings (interactions, lag, animation)

- Windows: `Win+Alt+R` starts/stops Game Bar recording.
- macOS: `Cmd+Shift+5` → Record.

## What a page actually requested (HAR)

Any browser: `F12` → Network tab → reproduce the problem → right-click any row → "Save all as HAR with content" → send the file.

## The real HTML/CSS of an element

DevTools → right-click the element → Inspect → right-click the node → Copy → outerHTML. For styles: Computed panel → "Copy all styles" or a screenshot of the panel.

## Console errors

DevTools → Console tab → screenshot it, or gear icon → "Save as…".

## Documents and data

Drag the file into the chat or paste its path — docx/xlsx/pptx/pdf/ipynb/csv are all readable directly. No conversion needed.

## PDF of anything printable

Browser: `Ctrl+P` → destination "Save as PDF".

## Audio

Phone voice memo → send as attachment. Most agents transcribe audio themselves.

## Mobile screen driven from the desktop

scrcpy (free, one install) mirrors and controls an Android over USB — use when the needed artifact is "what the app does", not a still image.

## No recipe fits

Search for "<verb> <object> tool <their OS> free" → recommend the first credible result with a one-line how-to. Prefer built-ins → free one-command installs → paid (say which you chose). You may recommend tools you cannot run yourself — the user is the one who runs them.
