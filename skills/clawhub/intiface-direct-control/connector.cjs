#!/usr/bin/env node
/**
 * Intiface Direct Connector — Buttplug v4 WebSocket Client
 * 
 * Connects directly to Intiface Central using the Buttplug v4 protocol.
 * Bypasses unstable third-party MCP bridges.
 *
 * Usage:
 *   node connector.cjs                          # localhost:12345
 *   INTIFACE_WS_URL=ws://192.168.0.13:12345 node connector.cjs  # remote
 *   node connector.cjs list                     # list devices
 *   node connector.cjs vibrate 0 0 70           # vibrate device 0, feature 0, value 70
 *   node connector.cjs stop 0                   # stop device 0
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
          setTimeout(() => ws.close(), 500);
        } else if (cmd === 'stop') {
          sendMsg('OutputCmd', {
            DeviceIndex: deviceIndex,
            FeatureIndex: 0,
            Command: { Vibrate: { Value: 0 } }
          });
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
        console.log('Command acknowledged (id: ' + m.Ok.Id + ')');
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

ws.on('close', () => process.exit(0));

setTimeout(() => { console.error('Timed out'); process.exit(1); }, 8000);
