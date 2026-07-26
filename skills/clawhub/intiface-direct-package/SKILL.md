---
name: intiface-direct
description: Control 750+ BLE intimate devices (Lovense, Kiiroo, We-Vibe, Satisfyer, etc.) from natural language via Intiface Central using direct Buttplug v4 WebSocket protocol. No MCP bridges required.
metadata: {"openclaw": {"requires": {"bins": ["node"], "skills": []}}}
---

# Intiface Direct — Buttplug v4 Device Control

Control any [Buttplug.io-compatible device](https://iostindex.com) — 700+ toys across all major brands — using natural language through OpenClaw. Connects directly to Intiface Central via WebSocket using the Buttplug v4 protocol.

## How it works

```
OpenClaw agent
    → Node.js script (Buttplug v4 WebSocket client)
    → Intiface Central (WebSocket ws://host:port)
    → Your device (Bluetooth / USB)
```

Works on any platform where Intiface Central is running (Windows, macOS, Linux).

---

## Prerequisites

- [Intiface Central](https://intiface.com/central/) — free desktop app (cross-platform)
- Node.js (included with OpenClaw)

---

## Setup (one time)

### Step 1 — Install and open Intiface Central

Download from [intiface.com/central](https://intiface.com/central/). Open the app and click **Start Server**. Leave it running — it listens on `ws://localhost:12345` by default.

### Step 2 — Connect your device

In Intiface Central, click **Start Scanning**. Power on your toy. Once it appears in the device list, scanning can be stopped.

### Step 3 — Install dependencies

```bash
cd skills/intiface-direct
npm install
```

---

## The Connector Script

File: `skills/intiface-direct/connector.cjs`

### Usage

```bash
# List devices
node connector.cjs list

# Vibrate once (exits after)
node connector.cjs vibrate <device> <feature> <value>

# Continuous vibration (resends every 3s to prevent timeout)
node connector.cjs loop <device> <feature> <value> [interval_seconds]

# Stop a device
node connector.cjs stop <device>

# Custom WebSocket URL (e.g. if Intiface is on another machine)
INTIFACE_WS_URL=ws://192.168.0.13:12345 node connector.cjs list
```

### Parameters

| Param | Description |
|-------|-------------|
| `<device>` | Device index from list (usually 0 for first device) |
| `<feature>` | Feature index (usually 0 for vibration) |
| `<value>` | Intensity 0–100 (see strength guide below) |
| `[interval_seconds]` | For `loop`: how often to resend (default 3) |

### Strength Guide (0–100 range)

| Feel | Value |
|------|-------|
| Off | 0 |
| Gentle | 10–25 |
| Medium | 30–50 |
| Strong | 55–75 |
| Maximum | 80–100 |

---

## Creating Custom Patterns (for AI agents)

The connector does basic commands, but the **real power** is writing tiny temporary scripts that send any sequence of vibrations over a single WebSocket connection. This lets you create ramps, waves, pulses, and complex patterns.

### Why this works

The Buttplug v4 protocol uses one persistent WebSocket connection. You can send **multiple `OutputCmd` messages** over the same connection, one after another — no need to reconnect for each value change. The `ws` library is already installed in `node_modules/`.

### Pattern recipe

Write temporary scripts using the same pattern below. The AI should generate these on-the-fly and run them with `node`:

#### Example: Ramp up, hold, pulse, fade

```javascript
const WebSocket = require('ws');
const ws = new WebSocket('ws://localhost:12345');
let id = 1;

function send(type, params) {
  params.Id = id++;
  ws.send(JSON.stringify([{[type]: params}]));
}

ws.on('open', () => {
  send('RequestServerInfo', {
    ClientName: 'PatternGen',
    ProtocolVersionMajor: 4,
    ProtocolVersionMinor: 0
  });
});

ws.on('message', (raw) => {
  const msgs = JSON.parse(raw.toString());
  for (const m of msgs) {
    if (m.ServerInfo) {
      // Sequence: ramp 10→20→30→40→50 (every 500ms)
      [10, 20, 30, 40, 50].forEach((v, i) => {
        setTimeout(() => {
          send('OutputCmd', {
            DeviceIndex: 0,
            FeatureIndex: 0,
            Command: { Vibrate: { Value: v } }
          });
        }, i * 500);
      });
      // Hold at 50 for 2s, then pulse 0→80→0→80→0
      setTimeout(() => {
        [0, 80, 0, 80, 0].forEach((v, i) => {
          setTimeout(() => {
            send('OutputCmd', {
              DeviceIndex: 0,
              FeatureIndex: 0,
              Command: { Vibrate: { Value: v } }
            });
          }, i * 300);
        });
        // Fade out after pulse
        setTimeout(() => {
          [60, 40, 20, 10, 0].forEach((v, i) => {
            setTimeout(() => {
              send('OutputCmd', {
                DeviceIndex: 0,
                FeatureIndex: 0,
                Command: { Vibrate: { Value: v } }
              });
              if (v === 0) ws.close();
            }, i * 400);
          });
        }, 2000);
      }, 3000);
    }
  }
});
```

#### Pattern building blocks

| Goal | How |
|------|-----|
| **Ramp** | Loop values from 0 → target in steps (e.g. 10, 20, 30…) with `setTimeout` spacing |
| **Wave** | Loop values back and forth (e.g. 0→100→0→100) |
| **Pulse** | Sharp 0→max→0 transitions with short intervals |
| **Hold steady** | Send the same value every ~3s in a `setInterval` |
| **Fade out** | Descending values (80, 60, 40, 20, 0) with spacing |
| **Pattern string** | Encode as `"value,hold_ms"` pairs: e.g. `"25,1000\|50,500\|75,200\|100,200\|75,200\|50,500\|25,1000"` → parse and schedule |

### Protocol reference (all you need)

Messages are JSON arrays. The key fields:

**Handshake:**
```json
[{"RequestServerInfo":{"Id":1,"ClientName":"AnyName","ProtocolVersionMajor":4,"ProtocolVersionMinor":0}}]
```

**List devices:**
```json
[{"RequestDeviceList":{"Id":2}}]
```

**Vibrate:**
```json
[{"OutputCmd":{"Id":3,"DeviceIndex":0,"FeatureIndex":0,"Command":{"Vibrate":{"Value":70}}}}]
```

**Stop (value = 0):**
```json
[{"OutputCmd":{"Id":4,"DeviceIndex":0,"FeatureIndex":0,"Command":{"Vibrate":{"Value":0}}}}]
```

---

## Agent Rules

- Always stop (Value: 0) after a timed session unless the user says otherwise
- Use `DeviceIndex: 0` unless the user specifies a different device
- Intiface Central must be running before calling any commands — remind the user if it fails
- The `ws` module (`require('ws')`) is available in `skills/intiface-direct/node_modules/ws` if you need to write temporary pattern scripts
- When writing temporary scripts, keep the WebSocket open while the pattern plays, then close it when done

---

## Supported Brands

Lovense · Kiiroo · We-Vibe · Satisfyer · The Handy · OSR-2/SR-6 · and [700+ more](https://iostindex.com)

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `connection refused` | Open Intiface Central and click Start Server |
| Device not found | Click Start Scanning in Intiface Central, power cycle the toy |
| Handshake fails | Make sure ProtocolVersionMajor/Minor are set (v4) |
| `Error: unknown variant` | Wrong message type — use `OutputCmd` not `VibrateCmd` |
| `missing field` | Check field names — `ProtocolVersionMajor` not `MessageVersion` |
| Remote can't connect | Use `INTIFACE_WS_URL=ws://<LAN-IP>:12345` (check firewall) |
