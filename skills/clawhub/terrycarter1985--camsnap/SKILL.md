---
name: camsnap
description: Camera snapshot and monitoring skill for OpenClaw — capture, compare, and manage camera snapshots with automated detection and alerts
metadata: {"clawdbot":{"emoji":"📷","requires":{"commands":["camsnap"]}}}
version: 0.1.1
---

# CamSnap — Camera Snapshot & Monitoring

Capture snapshots from connected cameras, detect changes between frames, and trigger alerts when motion or scene changes are detected.

## Quick Start

```bash
# Capture a snapshot from the default camera
camsnap capture

# Capture from a specific camera
camsnap capture --camera front-door

# List available cameras
camsnap list

# Compare two snapshots
camsnap diff snapshot1.jpg snapshot2.jpg

# Watch mode — continuous monitoring with change detection
camsnap watch --interval 30 --threshold 0.05
```

## Commands

### Capture

```bash
camsnap capture [--camera <name>] [--output <path>] [--quality <1-100>]
```

### List Cameras

```bash
camsnap list [--json]
```

### Diff / Compare

```bash
camsnap diff <image-a> <image-b> [--threshold <float>] [--json]
```

### Watch Mode

```bash
camsnap watch [--camera <name>] [--interval <seconds>] [--threshold <float>]
              [--on-change <command>] [--output-dir <path>]
```

### History

```bash
camsnap history [--camera <name>] [--limit <n>] [--since <duration>]
```

## Configuration

Configuration lives in `~/.config/camsnap/config.yaml`:

```yaml
cameras:
  default:
    device: /dev/video0
    resolution: 1920x1080
  front-door:
    device: /dev/video1
    resolution: 1280x720

watch:
  interval: 30
  threshold: 0.05
  output_dir: ~/.local/share/camsnap/snapshots
  on_change: null  # e.g. "notify-send 'CamSnap' 'Change detected'"
```

## Output Format

### `camsnap capture --json`

```json
{
  "success": true,
  "data": {
    "path": "/home/user/.local/share/camsnap/snapshots/2026-08-01T03-45-00.jpg",
    "camera": "default",
    "resolution": "1920x1080",
    "size_bytes": 245760,
    "timestamp": "2026-08-01T03:45:00Z"
  }
}
```

### `camsnap diff --json`

```json
{
  "success": true,
  "data": {
    "diff_score": 0.12,
    "changed": true,
    "threshold": 0.05,
    "regions": [
      {"x": 120, "y": 80, "w": 200, "h": 300, "score": 0.34}
    ]
  }
}
```

## Best Practices

1. **Use watch mode with `--on-change`** to trigger alerts or webhooks
2. **Set appropriate thresholds** — too low = false positives, too high = missed events
3. **Archive snapshots** to object storage for long-term retention
4. **Use named cameras** for multi-camera setups
5. **Rotate old snapshots** with `camsnap history --prune --older-than 30d`

## Installation

```bash
npm install -g camsnap
# or from source
cargo install camsnap
```

## License

MIT
