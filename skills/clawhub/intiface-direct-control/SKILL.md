---
name: intiface-direct
description: Control 750+ BLE intimate devices via Intiface Central using direct Buttplug v4 WebSocket protocol. No MCP bridges required.
metadata: {"openclaw": {"requires": {"bins": ["node"], "skills": []}}}
---

# Intiface Direct — Buttplug v4 Device Control

Control any Buttplug.io-compatible device — 700+ toys across all major brands — using natural language through your AI agent. This skill connects **directly** to Intiface Central via WebSocket using the Buttplug v4 protocol, without relying on MCP bridges or third-party connector binaries.

## Why not mcporter + buttplug-mcp?

The existing `intiface-control` skill on ClawHub uses `mcporter` → `buttplug-mcp` → Intiface. However:

- **mcporter** is an MCP bridge tool that adds unnecessary complexity for a direct WebSocket connection
- **buttplug-mcp** v0.0.1 uses `go-buttplug` library which has nil-pointer crashes and unstable WebSocket connections with Intiface v4

This skill bypasses both and talks Intiface natively.

## How it works

```
AI Agent
    → connector.cjs (Node.js, Buttplug v4 client)
        → Intiface Central (WebSocket ws://host:port)
            → Your device (Bluetooth / USB)
```

Works on any platform where Intiface Central is running (Windows, macOS, Linux) and the agent can reach it over the network.

## Prerequisites

- [Intiface Central](https://intiface.com/central/) — free desktop app (cross-platform). Download, install, open, and click **Start Server**.
- **Node.js** — to run the connector script (bundled with OpenClaw)
- A Buttplug.io-compatible Bluetooth device (Lovense, Kiiroo, We-Vibe, Satisfyer, The Handy, and 700+ more)

## Setup

### Step 1 — Open Intiface Central

Open the app and click **Start Server**. Leave it running — it listens on `ws://localhost:12345` by default.

### Step 2 — Connect your device

Click **Start Scanning** in Intiface Central. Power on your toy. Once it appears in the device list, scanning can be stopped.

### Step 3 — Note the WebSocket address

| Scenario | URL |
|----------|-----|
| Same machine | `ws://localhost:12345` |
| Different machine on LAN | `ws://192.168.0.x:12345` |
| WSL2 → Windows | Use `ws://<Windows LAN IP>:12345` or set up localhost port forwarding |

## CLI Usage

The `connector.cjs` script provides a command-line interface:

```bash
# List connected devices
node connector.cjs list

# Vibrate device 0, feature 0, at 70% (value 70 out of 0-100)
node connector.cjs vibrate 0 0 70

# Stop device 0
node connector.cjs stop 0
```

### Environment Variables

- `INTIFACE_WS_URL` — WebSocket URL (default: `ws://localhost:12345`)

## Agent Commands

The agent can use this skill by writing and running connector scripts that communicate with Intiface. Supported operations:

- **List devices** — Connect, handshake, request DeviceList, and report what's connected
- **Vibrate** — Send `OutputCmd` with `Vibrate` command at a specified integer value
- **Stop** — Send `OutputCmd` with `Vibrate` value 0
- **Patterns** — Sequence of commands (pulses, ramps, waves, etc.)
- **Stop all** — Send `StopAllDevices` message

## Buttplug v4 Protocol Reference

All messages are JSON arrays with the message type as the key. Each message object has an `Id` field inside the message type object.

### Handshake
```json
[{"RequestServerInfo":{"Id":1,"ClientName":"MyAgent","ProtocolVersionMajor":4,"ProtocolVersionMinor":0}}]
```

### Request Device List
```json
[{"RequestDeviceList":{"Id":2}}]
```

### Vibrate (value range from DeviceList, typically 0-100)
```json
[{"OutputCmd":{"Id":3,"DeviceIndex":0,"FeatureIndex":0,"Command":{"Vibrate":{"Value":70}}}}]
```

### Stop Device
```json
[{"OutputCmd":{"Id":4,"DeviceIndex":0,"FeatureIndex":0,"Command":{"Vibrate":{"Value":0}}}}]
```

### Stop All Devices
```json
[{"StopAllDevices":{"Id":5}}]
```

### Response Types
- `ServerInfo` — handshake success, contains `ServerName`, `ProtocolVersionMajor/Minor`
- `DeviceList` — device list, `Devices` is a map keyed by device index
- `Ok` — command acknowledged
- `Error` — error with `ErrorMessage` field

### DeviceList Format (v4)
Devices are returned as an object/map, not an array:
```json
{
  "DeviceList": {
    "Id": 2,
    "Devices": {
      "0": {
        "DeviceName": "Satisfyer Strong One",
        "DeviceIndex": 0,
        "DeviceMessageTimingGap": 100,
        "DeviceFeatures": {
          "0": {
            "FeatureIndex": 0,
            "FeatureDescription": "",
            "Output": {
              "Vibrate": { "Value": [0, 100] }
            }
          }
        }
      }
    }
  }
}
```

## Strength Guide (for 0-100 range)

| Feel | Value |
|------|-------|
| Off | 0 |
| Gentle | 10-25 |
| Medium | 30-50 |
| Strong | 55-75 |
| Maximum | 80-100 |

## Supported Brands

Lovense · Kiiroo · We-Vibe · Satisfyer · The Handy · OSR-2/SR-6 · and [700+ more](https://iostindex.com)

## Agent Rules

1. **Always stop** (send value 0) after a timed session unless the user says otherwise
2. Use `DeviceIndex: 0` unless the user specifies a different device
3. Intiface Central must be running before calling commands — remind the user if connection fails
4. If the `ws` module is unavailable, install it: `npm install ws`
5. Do not use the `notify` tool
6. If using WSL2, a TCP tunnel from WSL2 localhost to Windows IP may be needed

## Troubleshooting

| Problem | Fix |
|---------|------|
| `connection refused` | Open Intiface Central and click Start Server |
| Device not found | Click Start Scanning in Intiface Central, power cycle the toy |
| Handshake fails | Use `ProtocolVersionMajor: 4, ProtocolVersionMinor: 0` (v4 required) |
| `unknown variant` | Wrong message type — use `OutputCmd` not `VibrateCmd` |
| `missing field` | Check field names match v4 spec |
| WSL2 can't connect | Use Windows LAN IP, or set up localhost port forwarding via socat/Python |
| No devices in list | Run `StartScanning` in Intiface and power on the device |

## Files

- `connector.cjs` — CLI connector script
- `README.md` — Quick start guide
- `SKILL.md` — This documentation
