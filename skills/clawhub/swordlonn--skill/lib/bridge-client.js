/**
 * Client-side bridge injection script.
 * 
 * This script is injected into the WatchItAI web page running in a WebView/browser.
 * It creates the window.watchItAINative object that the Host page uses to interact
 * with the native system, communicating via WebSocket with the bridge server.
 */

const BRIDGE_URL = "ws://localhost:8765/bridge";

let ws = null;
let messageId = 0;
const pendingRequests = new Map();
let connectionPromise = null;

function connect() {
  if (connectionPromise) return connectionPromise;

  connectionPromise = new Promise((resolve, reject) => {
    try {
      ws = new WebSocket(BRIDGE_URL);
    } catch (e) {
      connectionPromise = null;
      reject(e);
      return;
    }

    ws.onopen = () => {
      console.log("[WatchItAI Bridge] Connected");
      resolve(ws);
    };

    ws.onclose = () => {
      console.log("[WatchItAI Bridge] Disconnected");
      connectionPromise = null;
      ws = null;
      // reject all pending
      for (const [id, req] of pendingRequests) {
        req.reject(new Error("Bridge disconnected"));
      }
      pendingRequests.clear();
    };

    ws.onerror = (err) => {
      console.error("[WatchItAI Bridge] Error:", err);
      if (connectionPromise) {
        reject(err);
        connectionPromise = null;
      }
    };

    ws.onmessage = (event) => {
      try {
        const msg = JSON.parse(event.data);
        if (msg.type === "response" && msg.data?.id) {
          const req = pendingRequests.get(msg.data.id);
          if (req) {
            pendingRequests.delete(msg.data.id);
            if (msg.data.error) {
              req.reject(new Error(msg.data.error));
            } else {
              req.resolve(msg.data.result);
            }
          }
        } else if (msg.type === "controlStarted") {
          if (window.watchItAINative?._onControlStarted) {
            window.watchItAINative._onControlStarted.forEach((cb) => cb());
          }
        } else if (msg.type === "controlEnded") {
          if (window.watchItAINative?._onControlEnded) {
            window.watchItAINative._onControlEnded.forEach((cb) => cb());
          }
        }
      } catch (e) {
        console.warn("[WatchItAI Bridge] Invalid message:", e);
      }
    };
  });

  return connectionPromise;
}

async function sendMessage(type, data = {}) {
  await connect();
  const id = ++messageId;
  return new Promise((resolve, reject) => {
    pendingRequests.set(id, { resolve, reject });
    ws.send(JSON.stringify({ id, type, data }));

    setTimeout(() => {
      if (pendingRequests.has(id)) {
        pendingRequests.delete(id);
        reject(new Error("Bridge request timeout"));
      }
    }, 10000);
  });
}

const watchItAINative = {
  controlMouse: async (params) => {
    return sendMessage("controlMouse", params);
  },

  controlKey: async (params) => {
    return sendMessage("controlKey", params);
  },

  controlWheel: async (params) => {
    return sendMessage("controlWheel", params);
  },

  getScreenSources: async () => {
    const result = await sendMessage("getScreenSources");
    return result.sources || [];
  },

  showNotification: (title, body) => {
    sendMessage("showNotification", { title, body }).catch(console.warn);
  },

  onControlStarted: (callback) => {
    if (!watchItAINative._onControlStarted) {
      watchItAINative._onControlStarted = [];
    }
    watchItAINative._onControlStarted.push(callback);
  },

  onControlEnded: (callback) => {
    if (!watchItAINative._onControlEnded) {
      watchItAINative._onControlEnded = [];
    }
    watchItAINative._onControlEnded.push(callback);
  },

  getWindowId: () => {
    return "watchitai-bridge";
  },

  // Permission query: check if required permissions are granted
  getPermissions: async () => {
    return sendMessage("getPermissions");
  },

  // Convenience: check if remote control is likely to work
  canControl: async () => {
    try {
      const result = await sendMessage("getPermissions");
      const perms = result?.permissions || [];
      const screenOk = perms.find((p) => p.name === "screen-recording")?.granted !== false;
      const accessOk = perms.find((p) => p.name === "accessibility")?.granted !== false;
      return screenOk && accessOk;
    } catch {
      return false;
    }
  },

  _isBridge: true,
  _bridgeUrl: BRIDGE_URL,
};

window.watchItAINative = watchItAINative;
window.dispatchEvent(new Event("watchItAINativeReady"));

console.log("[WatchItAI Bridge] Native bridge injected into window.watchItAINative");

export default watchItAINative;
