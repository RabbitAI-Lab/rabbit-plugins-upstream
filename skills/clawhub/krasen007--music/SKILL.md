---
name: aimp-controller
description: "Control AIMP music player via native command-line switches (play, pause, stop, next, prev)."
version: 1.0.0
author: community
license: MIT
platforms: [windows]
metadata:
  hermes:
    tags: [Music, AIMP, Audio, Player, Playback, Control]
    homepage: https://aimp.ru
prerequisites:
  commands: [terminal]  
---

# aimp-controller

Direct AIMP music player control using standard Windows command-line switches.
No Python or external dependencies required — just AIMP installed and running.

## Prerequisites

1. **AIMP must be installed** on Windows.
2. **AIMP must be running** before you send commands.

### Check if AIMP is running:
```bash
tasklist /FI "IMAGENAME eq aimp.exe"
```

## Quick Start

```bash
# Play/Pause toggle
aimp-player playpause

# Start playback
aimp-player play

# Pause playback
aimp-player pause

# Skip next song
aimp-player next

# Skip previous song
aimp-player prev

# Stop music
aimp-player stop
```

## Usage Patterns

### Toggle Play/Pause
```bash
"C:\Program Files (x86)\AIMP\AIMP.exe" /PLAYPAUSE
```

### Start Playback Explicitly
```bash
"C:\Program Files (x86)\AIMP\AIMP.exe" /PLAY
```

### Pause Playback Explicitly
```bash
"C:\Program Files (x86)\AIMP\AIMP.exe" /PAUSE
```

### Skip to Next Song
```bash
"C:\Program Files (x86)\AIMP\AIMP.exe" /NEXT
```

### Skip Previous Song
```bash
"C:\Program Files (x86)\AIMP\AIMP.exe" /PREV
```

### Stop Music
```bash
"C:\Program Files (x86)\AIMP\AIMP.exe" /STOP
```

## AIMP Command Switches Reference

| Switch | Description |
|--------|-------------|
| `/PLAY` | Start playback |
| `/PAUSE` | Pause playback |
| `/PLAYPAUSE` | Toggle between play and pause |
| `/NEXT` | Skip to next track |
| `/PREV` | Skip to previous track |
| `/STOP` | Stop all playback immediately |

## Examples with Hermes

### Simple command in a conversation:
```bash
# Ask me to skip the next song
"C:\Program Files (x86)\AIMP\AIMP.exe" /NEXT
```

### Stop current song, then close the player entirely:
```bash
# Stop playback and exit the application
"C:\Program Files (x86)\AIMP\AIMP.exe" /STOP
```

## Notes

- Commands execute immediately and silently.
- AIMP responds to switches in real-time while playing.
- Windows Explorer path with spaces must be quoted: `"C:\Program Files (x86)\AIMP\AIMP.exe"`.

## Troubleshooting

**AIMP not responding:**
```bash
# Make sure AIMP is running first
tasklist /FI "IMAGENAME eq aimp.exe"

# If not running, start it manually:
"C:\Program Files (x86)\AIMP\AIMP.exe"
```

**Command fails with exit code 1:**
- AIMP might be closed or unavailable.
- Try launching AIMP and retrying the switch.
