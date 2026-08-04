import { captureScreen, getScreenSize, killAllChildProcesses } from "./screen.js";
import { moveMouse, mouseDown, mouseUp, clickMouse, scrollMouse, getMousePosition } from "./mouse.js";
import { keyDown, keyUp, keyPress, typeText } from "./keyboard.js";
import { showNotification } from "./notify.js";
import { IS_MACOS } from "./platform.js";
import { info, warn, error, generateToken, sanitizeNumber, sanitizeString } from "./utils.js";
import { getApiBase, getDomain } from "./config.js";

const QUALITY_PRESETS = {
  low: { quality: 50, maxWidth: 640 },
  medium: { quality: 70, maxWidth: 1280 },
  high: { quality: 85, maxWidth: 1920 },
};

let daemonState = {
  running: false,
  fps: 15,
  permission: "view",
  quality: "high",
  qualitySettings: QUALITY_PRESETS.high,
  duration: 30,
  viewers: new Map(),
  captureTimer: null,
  peer: null,
  peerId: null,
  sessionId: null,
  sessionToken: null,
  shareUrl: null,
};

class ReconnectManager {
  constructor(maxAttempts = 10, baseDelay = 1000) {
    this.maxAttempts = maxAttempts;
    this.baseDelay = baseDelay;
    this.attempts = 0;
  }

  async wait() {
    if (this.attempts >= this.maxAttempts) {
      throw new Error("Max reconnect attempts reached");
    }

    const delay = Math.min(this.baseDelay * Math.pow(2, this.attempts), 30000);
    info(`[daemon] Reconnecting in ${delay}ms (attempt ${this.attempts + 1}/${this.maxAttempts})`);
    await new Promise(r => setTimeout(r, delay));
    this.attempts++;
  }

  reset() {
    this.attempts = 0;
  }
}

const reconnectManager = new ReconnectManager();

function getPeerConfig() {
  const domain = getDomain();
  return {
    host: domain,
    port: 443,
    path: "/peerjs/myapp",
    secure: true,
    key: "watchitai",
    config: {
      iceServers: [{ urls: "stun:stun.l.google.com:19302" }],
    },
    debug: 1,
  };
}

async function createSession(duration, permission) {
  const apiBase = getApiBase();
  const response = await fetch(`${apiBase}/sessions`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      duration,
      permission,
      audio: false,
    }),
  });

  if (!response.ok) {
    throw new Error(`Failed to create session: ${response.status}`);
  }

  return await response.json();
}

async function registerHost(sessionId, token, peerId) {
  const apiBase = getApiBase();
  const response = await fetch(
    `${apiBase}/sessions/${encodeURIComponent(sessionId)}/register`,
    {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ token, peerId }),
    }
  );

  if (!response.ok) {
    throw new Error(`Failed to register host: ${response.status}`);
  }

  return await response.json();
}

async function handleControlMessage(peerId, data) {
  if (daemonState.permission !== "control") {
    return;
  }

  if (!data || !data.type) {
    return;
  }

  const type = sanitizeString(data.type, 50);

  try {
    switch (type) {
      case "mouseMove": {
        const x = sanitizeNumber(data.x, 0, 10000);
        const y = sanitizeNumber(data.y, 0, 10000);
        await moveMouse(x, y);
        break;
      }
      case "mouseDown": {
        const button = sanitizeString(data.button, 10) || "left";
        await mouseDown(button);
        break;
      }
      case "mouseUp": {
        const button = sanitizeString(data.button, 10) || "left";
        await mouseUp(button);
        break;
      }
      case "mouseClick": {
        const button = sanitizeString(data.button, 10) || "left";
        await clickMouse(button);
        break;
      }
      case "mouseScroll": {
        const deltaX = sanitizeNumber(data.deltaX, -100, 100);
        const deltaY = sanitizeNumber(data.deltaY, -100, 100);
        await scrollMouse(deltaX, deltaY);
        break;
      }
      case "keyDown": {
        const key = sanitizeString(data.key, 50);
        const modifiers = data.modifiers || [];
        await keyDown(key, modifiers);
        break;
      }
      case "keyUp": {
        const key = sanitizeString(data.key, 50);
        const modifiers = data.modifiers || [];
        await keyUp(key, modifiers);
        break;
      }
      case "keyPress": {
        const key = sanitizeString(data.key, 50);
        const modifiers = data.modifiers || [];
        await keyPress(key, modifiers);
        break;
      }
      case "typeText": {
        const text = sanitizeString(data.text, 1000);
        if (text) {
          await typeText(text);
        }
        break;
      }
    }
  } catch (e) {
    error("[daemon] Control command failed:", e.message);
  }
}

async function startScreenCapture() {
  if (daemonState.captureTimer) {
    clearTimeout(daemonState.captureTimer);
    daemonState.captureTimer = null;
  }

  const interval = Math.round(1000 / daemonState.fps);
  let lastCaptureTime = 0;
  const { quality, maxWidth } = daemonState.qualitySettings;

  const captureLoop = async () => {
    if (!daemonState.running) return;

    const now = Date.now();
    const elapsed = now - lastCaptureTime;

    if (elapsed >= interval) {
      try {
        const buffer = await captureScreen(null, { quality, maxWidth });
        const dataUrl = `data:image/jpeg;base64,${buffer.toString("base64")}`;
        const frameData = {
          type: "screenFrame",
          dataUrl,
          timestamp: now,
        };

        for (const [viewerPeerId, conn] of daemonState.viewers) {
          try {
            if (conn.open) {
              conn.send(frameData);
            }
          } catch (e) {
            // ignore
          }
        }

        lastCaptureTime = now;
      } catch (e) {
        warn("[daemon] Capture failed:", e.message);
      }
    }

    if (daemonState.running) {
      const nextDelay = Math.max(0, interval - (Date.now() - now));
      daemonState.captureTimer = setTimeout(captureLoop, nextDelay);
    }
  };

  captureLoop();
  info(`[daemon] Screen capture started at ${daemonState.fps}fps (quality: ${daemonState.quality})`);
}

function stopScreenCapture() {
  daemonState.running = false;
  if (daemonState.captureTimer) {
    clearTimeout(daemonState.captureTimer);
    daemonState.captureTimer = null;
  }
  info("[daemon] Screen capture stopped");
}

function setupPeerHandlers(session) {
  const peer = daemonState.peer;

  peer.on("open", async (id) => {
    daemonState.peerId = id;
    info(`[daemon] Peer connected: ${id}`);

    try {
      await registerHost(session.id, session.token, id);
      info("[daemon] Host registered successfully");
      reconnectManager.reset();
    } catch (e) {
      error("[daemon] Failed to register host:", e.message);
    }

    daemonState.running = true;
    startScreenCapture();

    try {
      await showNotification(
        "WatchItAI",
        `Screen sharing started. ${daemonState.viewers.size} viewer(s).`
      );
    } catch (e) {
      // ignore
    }
  });

  peer.on("connection", (conn) => {
    const viewerPeerId = conn.peer;
    daemonState.viewers.set(viewerPeerId, conn);
    info(`[daemon] Viewer connected: ${viewerPeerId}`);

    conn.on("open", () => {
      try {
        conn.send({
          type: "session-info",
          permission: daemonState.permission,
          audio: false,
          quality: daemonState.quality,
          fps: daemonState.fps,
        });
      } catch (e) {}
    });

    conn.on("data", (data) => {
      handleControlMessage(viewerPeerId, data);
    });

    conn.on("close", () => {
      daemonState.viewers.delete(viewerPeerId);
      info(`[daemon] Viewer disconnected: ${viewerPeerId}`);
    });

    conn.on("error", (err) => {
      warn(`[daemon] Connection error: ${err.message}`);
      daemonState.viewers.delete(viewerPeerId);
    });
  });

  peer.on("call", (call) => {
    const callerPeerId = call.peer;
    info(`[daemon] Incoming call from: ${callerPeerId}`);
    
    call.on("stream", () => {
      info(`[daemon] Call stream established: ${callerPeerId}`);
    });

    call.on("close", () => {
      info(`[daemon] Call ended: ${callerPeerId}`);
    });
  });

  peer.on("disconnected", async () => {
    warn("[daemon] Peer disconnected");
    stopScreenCapture();

    try {
      await handleReconnect();
    } catch (e) {
      error("[daemon] Reconnect failed:", e.message);
      stopDaemon();
    }
  });

  peer.on("error", (err) => {
    error("[daemon] Peer error:", err.message || err.type);
  });

  peer.on("close", () => {
    info("[daemon] Peer connection closed");
    stopScreenCapture();
  });
}

async function handleReconnect() {
  await reconnectManager.wait();
  
  info("[daemon] Attempting to reconnect...");
  if (daemonState.peer) {
    try {
      daemonState.peer.reconnect();
    } catch (e) {
      warn("[daemon] peer.reconnect() not available, creating new peer");
      await createNewPeer();
    }
  } else {
    await createNewPeer();
  }
  
  daemonState.running = true;
  startScreenCapture();
}

async function createNewPeer() {
  const peerjs = await import("peerjs");
  const Peer = peerjs.default || peerjs.Peer || peerjs;
  const peerConfig = getPeerConfig();
  daemonState.peer = new Peer(peerConfig);
  
  const session = {
    id: daemonState.sessionId,
    token: daemonState.sessionToken,
  };
  setupPeerHandlers(session);
}

async function startDaemon(options = {}) {
  if (daemonState.running) {
    return {
      sessionId: daemonState.sessionId,
      shareUrl: daemonState.shareUrl,
      peerId: daemonState.peerId,
    };
  }

  daemonState.fps = options.fps || 15;
  daemonState.permission = options.permission || "view";
  daemonState.quality = options.quality || "high";
  daemonState.duration = options.duration || 30;
  daemonState.qualitySettings = QUALITY_PRESETS[daemonState.quality] || QUALITY_PRESETS.high;

  info("[daemon] Starting daemon mode...");
  info(`[daemon] FPS: ${daemonState.fps}, Permission: ${daemonState.permission}, Quality: ${daemonState.quality}`);

  try {
    const session = await createSession(daemonState.duration, daemonState.permission);
    daemonState.sessionId = session.id;
    daemonState.sessionToken = session.token;
    daemonState.shareUrl = session.shareUrl;

    info(`[daemon] Session created: ${session.id}`);
    info(`[daemon] Share URL: ${session.shareUrl}`);

    const peerjs = await import("peerjs");
    const Peer = peerjs.default || peerjs.Peer || peerjs;
    const peerConfig = getPeerConfig();
    daemonState.peer = new Peer(peerConfig);

    setupPeerHandlers(session);

    return {
      sessionId: daemonState.sessionId,
      shareUrl: daemonState.shareUrl,
      peerId: null,
    };
  } catch (e) {
    error("[daemon] Failed to start:", e.message);
    throw e;
  }
}

function stopDaemon() {
  info("[daemon] Stopping daemon...");
  
  daemonState.running = false;
  
  if (daemonState.captureTimer) {
    clearTimeout(daemonState.captureTimer);
    daemonState.captureTimer = null;
  }

  for (const [peerId, conn] of daemonState.viewers) {
    try {
      conn.close();
    } catch (e) {}
  }
  daemonState.viewers.clear();

  if (daemonState.peer) {
    try {
      daemonState.peer.destroy();
    } catch (e) {}
    daemonState.peer = null;
  }

  killAllChildProcesses();

  daemonState.peerId = null;
  daemonState.sessionId = null;
  daemonState.sessionToken = null;
  daemonState.shareUrl = null;

  info("[daemon] Daemon stopped");
}

function getDaemonStatus() {
  return {
    running: daemonState.running,
    fps: daemonState.fps,
    permission: daemonState.permission,
    quality: daemonState.quality,
    viewers: daemonState.viewers.size,
    peerId: daemonState.peerId,
    sessionId: daemonState.sessionId,
    shareUrl: daemonState.shareUrl,
  };
}

export {
  startDaemon,
  stopDaemon,
  getDaemonStatus,
  ReconnectManager,
};

export default {
  startDaemon,
  stopDaemon,
  getDaemonStatus,
};
