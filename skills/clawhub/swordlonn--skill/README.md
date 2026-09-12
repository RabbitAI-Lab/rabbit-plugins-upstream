# WatchItAI Skill

Cross-platform screen sharing and remote control for AI coding agents.

WatchItAI enables real-time screen sharing between AI agents (OpenClaw, Claude Code, Cursor, Trae, etc.) and human operators via WebRTC P2P direct connection — ultra-low latency, end-to-end encrypted, zero installation required on the viewer side.

**No Node.js required** — the skill uses self-contained Go binaries. Just download, unzip, and run.

## Features

- **P2P Direct** — WebRTC peer-to-peer transmission, no relay server, ultra-low latency (<200ms)
- **End-to-End Encrypted** — DTLS-SRTP encrypted channels, video data only between you and the agent
- **Zero Install** — Viewers open the link in a browser, no client or plugin needed
- **No Node.js** — Self-contained Go binary, no npm install, no runtime dependencies
- **Remote Control** — Mouse and keyboard control support (optional)
- **Cross-Platform** — Windows, macOS (Intel + Apple Silicon), Linux (x64 + ARM64)
- **Multi-Agent Support** — Works with Trae, OpenClaw, Claude Code, Cursor, and more

## Quick Start

### Install for Trae

```bash
mkdir -p ~/.trae-cn/skills && cd ~/.trae-cn/skills
curl -L https://watchitai.net/watchitai-skill.zip -o watchitai.zip
unzip watchitai.zip && rm watchitai.zip
```

### Install for OpenClaw

```bash
mkdir -p ~/.openclaw/skills && cd ~/.openclaw/skills
curl -L https://watchitai.net/watchitai-skill.zip -o watchitai.zip
unzip watchitai.zip && rm watchitai.zip
```

### Install for Claude Code

```bash
mkdir -p ~/.claude/skills && cd ~/.claude/skills
curl -L https://watchitai.net/watchitai-skill.zip -o watchitai.zip
unzip watchitai.zip && rm watchitai.zip
```

### Install for Cursor

```bash
mkdir -p ~/.cursor/skills && cd ~/.cursor/skills
curl -L https://watchitai.net/watchitai-skill.zip -o watchitai.zip
unzip watchitai.zip && rm watchitai.zip
```

### Windows

```powershell
mkdir $env:USERPROFILE\.trae-cn\skills -Force
cd $env:USERPROFILE\.trae-cn\skills
curl -L https://watchitai.net/watchitai-skill.zip -o watchitai.zip
Expand-Archive watchitai.zip -DestinationPath .
Remove-Item watchitai.zip
```

## Configuration

Edit `config.json` or set environment variables:

```json
{
  "domain": "watchitai.net",
  "bridgePort": 8765,
  "mode": "server"
}
```

| Setting | Env Variable | Description | Default |
|---------|-------------|-------------|---------|
| `domain` | `WATCHITAI_DOMAIN` | WatchItAI server domain | `watchitai.net` |
| `bridgePort` | `WATCHITAI_BRIDGE_PORT` | Local bridge port | `8765` |
| `mode` | `WATCHITAI_MODE` | Running mode | `server` |

View current config:

**macOS / Linux:**
```bash
bash run.sh config
```

**Windows:**
```cmd
run.cmd config
```

## Permissions

### macOS

First-time users need to run the permission preflight:

```bash
bash run.sh preflight
```

Required permissions:
- **Screen Recording** — for screen sharing and screenshots
- **Accessibility** — for mouse and keyboard control
- **Input Monitoring** — for keyboard event listening

Check permission status at any time:

```bash
bash run.sh permissions
```

### Linux

Install system tools (if not using nut.js):

```bash
# Debian/Ubuntu
sudo apt install xdotool scrot
```

## Usage

### Start Screen Sharing

**macOS / Linux:**
```bash
bash run.sh share
```

**Windows:**
```cmd
run.cmd share
```

This launches the bridge server and opens the WatchItAI host page in the browser. Click "Start Sharing" to generate a shareable viewer link.

### Command Reference

**macOS / Linux:**
```bash
bash run.sh share              # Start screen sharing
bash run.sh start              # Start bridge server only
bash run.sh status             # Check bridge status
bash run.sh permissions        # Check permissions
bash run.sh preflight          # Permission preflight (macOS)
bash run.sh test-mouse         # Test mouse control
bash run.sh test-keyboard      # Test keyboard control
bash run.sh test-screenshot    # Test screenshot
bash run.sh notify <title> [body]  # Show notification
bash run.sh config             # View configuration
bash run.sh info               # System info
```

**Windows:**
```cmd
run.cmd share              REM Start screen sharing
run.cmd start              REM Start bridge server only
run.cmd status             REM Check bridge status
run.cmd permissions        REM Check permissions
run.cmd preflight          REM Permission preflight
run.cmd info               REM System info
run.cmd version            REM Show version
```

## Cross-Platform Support

| Feature | Windows | macOS | Linux |
|---------|---------|-------|-------|
| Mouse move/click/scroll | ✅ | ✅ | ✅ |
| Keyboard input | ✅ | ✅ | ✅ |
| Screen capture | ✅ | ✅ | ✅ |
| System notifications | ✅ | ✅ | ✅ |

## Bridge API

WebSocket: `ws://localhost:8765/bridge`

### Message Types

| Type | Description |
|------|-------------|
| `controlMouse` | Mouse control |
| `controlKey` | Keyboard control |
| `controlWheel` | Scroll control |
| `captureScreen` | Screen capture |
| `getScreenSources` | Display list |
| `showNotification` | System notification |
| `getPermissions` | Permission status |
| `ping` | Heartbeat |

### HTTP Endpoints

| Path | Description |
|------|-------------|
| `/health` | Health check |
| `/permissions` | Permission status |
| `/screenshot` | Current screenshot (PNG) |

## Security

The bridge server only listens on localhost. Do not expose the port to the public internet.

## File Structure

```
watchitai/
├── run.sh                # Unix entry point (auto-detects platform, calls Go binary)
├── run.cmd               # Windows entry point
├── config.json           # Configuration
├── SKILL.md              # Skill metadata
├── README.md             # This file
├── bin/
│   ├── watchitai-darwin-amd64       # macOS Intel binary
│   ├── watchitai-darwin-arm64       # macOS Apple Silicon binary
│   ├── watchitai-linux-amd64        # Linux Intel binary
│   ├── watchitai-linux-arm64        # Linux ARM64 binary
│   ├── watchitai-windows-amd64.exe  # Windows x64 binary
│   └── cliclick                      # macOS mouse tool (bundled)
└── scripts/
    ├── ensure_macos_permissions.sh
    ├── take_screenshot.py
    └── take_screenshot.ps1
```

## Links

- **Website**: [https://watchitai.net](https://watchitai.net)
- **Host Page**: [https://watchitai.net/host](https://watchitai.net/host)
- **Feedback**: feedback@watchitai.net

## License

MIT
