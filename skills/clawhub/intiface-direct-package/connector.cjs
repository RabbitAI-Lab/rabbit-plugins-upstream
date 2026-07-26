#!/usr/bin/env node
/**
 * Intiface Direct Connector — Buttplug v4 WebSocket Client
 *
 * Connects directly to Intiface Central using the Buttplug v4 protocol.
 * Bypasses unstable third-party MCP bridges.
 *
 * Usage:
 *   node connector.cjs                                  # localhost:12345
 *   INTIFACE_WS_URL=ws://192.168.0.13:12345 node connector.cjs  # remote
 *   node connector.cjs list                             # list devices
 *   node connector.cjs vibrate 0 0 70                   # vibrate once
 *   node connector.cjs loop 0 0 25                      # continuous vibration (every 3s)
 *   node connector.cjs loop 0 0 25 5                    # continuous vibration (every 5s)
 *   node connector.cjs stop 0                           # stop device 0
 */

const WebSocket = require('ws');

const WS_URL = process.env.INTIFACE_WS_URL || 'ws://localhost:12345';
const ws = new WebSocket(WS_URL);
let mid = 1;
let devices = {};

function sendMsg(type, params = {}) {
  const id = mid++;
  params.Id = id;
  ws.send(JSON.stringify([{[type]: params}]));
  return id;
}

const cmd = process.argv[2];
const deviceIndex = parseInt(process.argv[3] || '0');
const featureIndex = parseInt(process.argv[4] || '0');
const value = parseInt(process.argv[5] || '0');
const intervalSec = parseFloat(process.argv[6] || '3');

ws.on('open', () => {
  sendMsg('RequestServerInfo', {
    ClientName: 'OpenClaw',
    ProtocolVersionMajor: 4,
    ProtocolVersionMinor: 0
  });
});

ws.on('message', (raw) => {
  const txt = raw.toString();
  try {
    const msgs = JSON.parse(txt);
    if (!Array.isArray(msgs)) return;
    for (const m of msgs) {
      if (m.ServerInfo) {
        if (cmd === 'list' || !cmd) {
          sendMsg('RequestDeviceList');
        } else if (cmd === 'vibrate') {
          sendMsg('OutputCmd', {
            DeviceIndex: deviceIndex,
            FeatureIndex: featureIndex,
            Command: { Vibrate: { Value: value } }
          });
          console.log('Vibrate ' + deviceIndex + ':' + featureIndex + ' @ ' + value + ' (once)');
          setTimeout(() => ws.close(), 500);
        } else if (cmd === 'loop') {
          console.log('Continuous vibration on ' + deviceIndex + ':' + featureIndex + ' @ ' + value + ' (every ' + intervalSec + 's)');
          console.log('Send "stop ' + deviceIndex + '" or Ctrl+C to end');
          const loop = () => {
            sendMsg('OutputCmd', {
              DeviceIndex: deviceIndex,
              FeatureIndex: featureIndex,
              Command: { Vibrate: { Value: value } }
            });
          };
          loop();
          setInterval(loop, intervalSec * 1000);
        } else if (cmd === 'stop') {
          sendMsg('OutputCmd', {
            DeviceIndex: deviceIndex,
            FeatureIndex: 0,
            Command: { Vibrate: { Value: 0 } }
          });
          console.log('Stopped device ' + deviceIndex);
          setTimeout(() => ws.close(), 500);
        } else {
          console.log('Unknown command:', cmd);
          ws.close();
        }
      }
      else if (m.DeviceList) {
        devices = m.DeviceList.Devices || {};
        const keys = Object.keys(devices);
        console.log('Devices connected: ' + keys.length);
        for (const k of keys) {
          const d = devices[k];
          const features = Object.values(d.DeviceFeatures || {}).map(f =>
            Object.keys(f.Output || {}).join(',')
          ).filter(Boolean).join(', ') || 'none';
          console.log('  [' + d.DeviceIndex + '] ' + d.DeviceName + ' (features: ' + features + ')');
        }
        ws.close();
      }
      else if (m.Ok) {
        if (cmd !== 'loop') {
          console.log('Command acknowledged (id: ' + m.Ok.Id + ')');
        }
      }
      else if (m.Error) {
        console.error('Error:', m.Error.ErrorMessage);
      }
    }
  } catch(e) {}
});

ws.on('error', (e) => {
  console.error('Connection failed:', e.message);
  process.exit(1);
});

ws.on('close', () => {
  if (cmd === 'loop') {
    console.log('Connection closed — loop ended');
  }
  process.exit(0);
});

// Timeout for non-loop commands
if (cmd !== 'loop') {
  setTimeout(() => { console.error('Timed out'); process.exit(1); }, 8000);
}
