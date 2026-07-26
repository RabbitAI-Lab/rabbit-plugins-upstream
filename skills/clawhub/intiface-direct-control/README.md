# Intiface Direct — Buttplug v4 Device Control

## What you need
1. Intiface Central — free app from https://intiface.com/central/
2. Node.js
3. A BLE toy (700+ brands supported)

## Quick Start
1. Open Intiface Central → Start Server
2. Click Start Scanning → power on your device
3. `node connector.cjs list` — see devices
4. `node connector.cjs vibrate 0 0 70` — vibrate at 70%
5. `node connector.cjs stop 0` — stop

## CLI Commands
- `node connector.cjs list`
- `node connector.cjs vibrate <device> <feature> <value>`
- `node connector.cjs stop <device>`

## Env Vars
- `INTIFACE_WS_URL` — WebSocket URL (default: ws://localhost:12345)
