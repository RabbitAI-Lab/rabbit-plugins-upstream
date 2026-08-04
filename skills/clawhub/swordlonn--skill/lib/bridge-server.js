/**
 * WatchItAI Bridge Server
 *
 * Local HTTP + WebSocket server that bridges the WatchItAI web frontend
 * with native system capabilities (mouse, keyboard, screen capture, notifications).
 *
 * The frontend injects window.watchItAINative via WebSocket messaging.
 */

import http from "http";
import https from "https";
import { WebSocketServer } from "ws";
import express from "express";
import * as fs from "fs";
import * as path from "path";
import { fileURLToPath } from "url";
import { exec } from "child_process";
import { getPlatformName, getOSInfo, IS_MACOS } from "./platform.js";
import { generateToken, validateToken, info, warn, error } from "./utils.js";
import { loadConfig } from "./config.js";

// 启动速度优化：mouse/keyboard/screen/notify/permissions 改为按需加载
// 这样在 ws 连接尚未建立前，不加载重型模块
const moduleCache = {};
async function loadMouse() {
  if (!moduleCache.mouse) {
    moduleCache.mouse = await import("./mouse.js");
  }
  return moduleCache.mouse;
}
async function loadKeyboard() {
  if (!moduleCache.keyboard) {
    moduleCache.keyboard = await import("./keyboard.js");
  }
  return moduleCache.keyboard;
}
async function loadScreen() {
  if (!moduleCache.screen) {
    moduleCache.screen = await import("./screen.js");
  }
  return moduleCache.screen;
}
async function loadNotify() {
  if (!moduleCache.notify) {
    moduleCache.notify = await import("./notify.js");
  }
  return moduleCache.notify;
}
async function loadPermissions() {
  if (!moduleCache.permissions) {
    moduleCache.permissions = await import("./permissions.js");
  }
  return moduleCache.permissions;
}

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

let server = null;
let wss = null;
let activeClients = new Set();
let controlCallbacks = { started: null, ended: null };
let screenShareInterval = null;
let screenShareTimer = null;
let screenShareBusy = false;
let screenShareStopped = false;
let caffeinateProcess = null;
let bridgeToken = null;

// Cache permission states to avoid repeated checks
let permissionCache = {
  screenRecording: null,
  accessibility: null,
  lastCheck: 0,
};
const PERMISSION_CACHE_TTL = 60000;

// ============================================================
// Authentication
// ============================================================
export function getBridgeToken() {
  if (!bridgeToken) {
    bridgeToken = generateToken(32);
  }
  return bridgeToken;
}

export function setBridgeToken(token) {
  bridgeToken = token;
}

function authenticateConnection(ws, request) {
  const urlParams = new URLSearchParams(request.url.slice(request.url.indexOf("?") + 1));
  const token = urlParams.get("token");
  
  if (!bridgeToken) {
    bridgeToken = generateToken(32);
  }
  
  if (!token || !validateToken(token, bridgeToken)) {
    ws.close(1008, "Unauthorized: Invalid or missing token");
    return false;
  }
  
  ws.isAuthenticated = true;
  return true;
}

// ============================================================
// Permission guards
// ============================================================
async function refreshPermissionCache() {
  const now = Date.now();
  if (now - permissionCache.lastCheck < PERMISSION_CACHE_TTL) return;

  if (IS_MACOS) {
    // 启动速度优化：两个权限检查并行
    const { hasScreenRecordingPermission, hasAccessibilityPermission } = await loadPermissions();
    const [sr, acc] = await Promise.all([
      hasScreenRecordingPermission(),
      hasAccessibilityPermission(),
    ]);
    permissionCache.screenRecording = sr;
    permissionCache.accessibility = acc;
  } else {
    // Linux/Windows: assume granted (tool availability checked separately)
    permissionCache.screenRecording = true;
    permissionCache.accessibility = true;
  }
  permissionCache.lastCheck = now;
}

function requireScreenRecording() {
  const sr = permissionCache.screenRecording;
  if (sr === false) {
    throw new Error(
      "Screen Recording permission is missing. Run 'bash run.sh preflight' to fix.",
    );
  }
  if (sr && sr.reason === "display-asleep") {
    throw new Error(
      "Display is asleep. Wake up your screen to enable screen sharing.",
    );
  }
}

function requireAccessibility() {
  if (permissionCache.accessibility === false) {
    throw new Error(
      "Accessibility permission is missing. Run 'bash run.sh preflight' to fix.",
    );
  }
}

function createBridgeMessage(type, data = {}) {
  return JSON.stringify({ type, data, ts: Date.now() });
}

async function handleBridgeMessage(ws, message) {
  let parsed;
  try {
    parsed = JSON.parse(message);
  } catch (e) {
    console.warn("[bridge] Invalid message format");
    return;
  }

  const { id, type, data } = parsed;
  const respond = (result, error = null) => {
    ws.send(
      createBridgeMessage("response", {
        id,
        result,
        error,
      }),
    );
  };

  try {
    // Refresh permission cache if stale
    await refreshPermissionCache();

    switch (type) {
      case "ping":
        respond({ pong: true, platform: getPlatformName() });
        break;

      case "getPlatformInfo":
        respond(getOSInfo());
        break;

      case "getPermissions": {
        const { checkAllPermissions } = await loadPermissions();
        const perms = await checkAllPermissions();
        respond({ permissions: perms });
        break;
      }

      case "controlMouse": {
        requireAccessibility();
        const { action, button, x, y } = data;
        const { moveMouse, mouseDown, mouseUp, clickMouse } = await loadMouse();
        if (action === "move") {
          await moveMouse(x, y);
        } else if (action === "down") {
          await mouseDown(button);
        } else if (action === "up") {
          await mouseUp(button);
        } else if (action === "click") {
          await clickMouse(button);
        }
        respond({ success: true });
        break;
      }

      case "controlKey": {
        requireAccessibility();
        const { action, key, modifiers } = data;
        const { keyDown, keyUp, keyPress } = await loadKeyboard();
        if (action === "down") {
          await keyDown(key, modifiers);
        } else if (action === "up") {
          await keyUp(key, modifiers);
        } else if (action === "press") {
          await keyPress(key, modifiers);
        }
        respond({ success: true });
        break;
      }

      case "controlWheel": {
        requireAccessibility();
        const { deltaX, deltaY } = data;
        const { scrollMouse } = await loadMouse();
        await scrollMouse(deltaX, deltaY);
        respond({ success: true });
        break;
      }

      case "typeText": {
        requireAccessibility();
        const { text } = data;
        const { typeText } = await loadKeyboard();
        await typeText(text);
        respond({ success: true });
        break;
      }

      case "getScreenSources": {
        requireScreenRecording();
        const { getScreenSources } = await loadScreen();
        const sources = await getScreenSources();
        respond({ sources });
        break;
      }

      case "getScreenSize": {
        const { getScreenSize } = await loadScreen();
        respond(await getScreenSize());
        break;
      }

      case "captureScreen": {
        requireScreenRecording();
        const { captureScreen } = await loadScreen();
        const buffer = await captureScreen(data?.displayId);
        respond({
          dataUrl: `data:image/png;base64,${buffer.toString("base64")}`,
          timestamp: Date.now(),
        });
        break;
      }

      case "startScreenShare": {
        requireScreenRecording();
        const fps = data?.fps || 15;
        const interval = Math.round(1000 / fps);

        // Stop any existing share
        screenShareStopped = true;
        if (screenShareTimer) {
          clearTimeout(screenShareTimer);
          screenShareTimer = null;
        }
        if (screenShareInterval) {
          clearInterval(screenShareInterval);
          screenShareInterval = null;
        }

        console.log(`[bridge] Starting screen share at ${fps} FPS (interval: ${interval}ms)`);

        if (IS_MACOS && !caffeinateProcess) {
          caffeinateProcess = exec("caffeinate -i -d -s");
          caffeinateProcess.on("exit", () => {
            caffeinateProcess = null;
          });
          console.log("[bridge] Started caffeinate to prevent display sleep");
        }

        const { captureScreen } = await loadScreen();
        screenShareStopped = false;
        screenShareBusy = false;

        const sendFrame = async () => {
          if (screenShareStopped) return;
          // Skip if previous frame still capturing (prevents concurrent spawns)
          if (screenShareBusy) {
            scheduleNextFrame();
            return;
          }
          screenShareBusy = true;
          try {
            const buffer = await captureScreen(data?.displayId);
            const dataUrl = `data:image/png;base64,${buffer.toString("base64")}`;
            broadcast("screenShareFrame", { dataUrl, timestamp: Date.now() });
          } catch (e) {
            console.warn("[bridge] Screen capture failed during share:", e.message);
          } finally {
            screenShareBusy = false;
          }
          scheduleNextFrame();
        };

        const scheduleNextFrame = () => {
          if (screenShareStopped) return;
          screenShareTimer = setTimeout(sendFrame, interval);
        };

        await sendFrame();
        console.log("[bridge] First frame sent");

        respond({ success: true, fps, interval });
        break;
      }

      case "stopScreenShare": {
        const wasActive = !screenShareStopped || screenShareTimer;
        screenShareStopped = true;
        if (screenShareTimer) {
          clearTimeout(screenShareTimer);
          screenShareTimer = null;
        }
        if (screenShareInterval) {
          clearInterval(screenShareInterval);
          screenShareInterval = null;
        }
        if (wasActive) {
          if (caffeinateProcess) {
            caffeinateProcess.kill();
            caffeinateProcess = null;
            console.log("[bridge] Stopped caffeinate");
          }
          console.log("[bridge] Screen share stopped");
          broadcast("screenShareStopped", { ts: Date.now() });
        } else {
          console.log("[bridge] stopScreenShare called but no screen share was active");
        }
        console.log("[bridge] Active clients:", activeClients.size);
        respond({ success: true, wasActive });
        break;
      }

      case "showNotification": {
        const { title, body } = data;
        const { showNotification } = await loadNotify();
        await showNotification(title, body);
        respond({ success: true });
        break;
      }

      case "showAlert": {
        const { title, message } = data;
        const { showAlert } = await loadNotify();
        await showAlert(title, message);
        respond({ success: true });
        break;
      }

      case "wakeDisplay": {
        const { wakeDisplay } = await loadPermissions();
        const result = await wakeDisplay();
        if (result.success) {
          // 唤醒成功后刷新权限缓存
          permissionCache.lastCheck = 0;
          await refreshPermissionCache();
          respond({ success: true, method: result.method });
        } else {
          // 自动唤醒失败，发送系统通知提醒用户
          const { showNotification } = await loadNotify();
          await showNotification(
            "WatchItAI 远程唤醒",
            "有人在远端请求查看您的屏幕，请点击此通知或移动鼠标唤醒屏幕"
          );
          respond({
            success: false,
            reason: result.reason,
            hint: result.hint,
            notified: true,
          });
        }
        break;
      }

      case "getMousePosition": {
        requireAccessibility();
        const { getMousePosition } = await loadMouse();
        const pos = await getMousePosition();
        respond(pos);
        break;
      }

      case "control.start": {
        // Verify both permissions before allowing remote control
        await refreshPermissionCache();
        requireAccessibility();
        requireScreenRecording();
        broadcast("controlStarted", { ts: Date.now() });
        if (controlCallbacks.started) controlCallbacks.started();
        respond({ success: true });
        break;
      }

      case "control.end": {
        broadcast("controlEnded", { ts: Date.now() });
        if (controlCallbacks.ended) controlCallbacks.ended();
        respond({ success: true });
        break;
      }

      default:
        respond(null, `Unknown message type: ${type}`);
    }
  } catch (err) {
        error(`[bridge] Error handling ${type}:`, err.message);
        respond(null, err.message);
      }
}

function broadcast(type, data = {}) {
  const msg = createBridgeMessage(type, data);
  for (const client of activeClients) {
    if (client.readyState === 1) {
      client.send(msg);
    }
  }
}

function onControlStarted(callback) {
  controlCallbacks.started = callback;
}

function onControlEnded(callback) {
  controlCallbacks.ended = callback;
}

export function startBridgeServer(port = 8765, options = {}) {
  return new Promise(async (resolve, reject) => {
    if (server) {
      resolve({ port, server, wss });
      return;
    }

    if (!options.skipPermissionCheck) {
      try {
        // 启动速度优化：按需加载 permissions 模块
        const { checkAllPermissions, formatPermissions } = await loadPermissions();
        const perms = await checkAllPermissions();
        info(formatPermissions(perms));

        const missing = perms.filter((p) => p.granted === false);
        if (missing.length > 0) {
          warn(`\n⚠️  ${missing.length} permission(s) missing!`);
          warn("   Some features (screen capture / remote control) may not work.");
          if (IS_MACOS) {
            warn("   Run 'bash run.sh preflight' to request permissions.\n");
          }
        } else {
          info("\n✅ All permissions granted.\n");
        }

        await refreshPermissionCache();
      } catch (e) {
        warn("[bridge] Permission check failed:", e.message);
      }
    }

    const app = express();

    app.use(express.json());

    app.get("/health", (req, res) => {
      res.json({ status: "ok", platform: getPlatformName() });
    });

    app.get("/token", (req, res) => {
      res.json({ token: getBridgeToken() });
    });

    // ---- Serve local host page ----
    app.get("/", (req, res) => {
      const htmlPath = path.join(__dirname, "local-host.html");
      if (fs.existsSync(htmlPath)) {
        res.sendFile(htmlPath);
      } else {
        res.status(404).send("Local host page not found");
      }
    });

    // ---- Create session via server-side API call (no browser CSRF needed) ----
    // Used by AI tools / CLI to create a session directly without browser involvement.
    app.post("/create-session", async (req, res) => {
      const config = loadConfig();
      const { duration = 30, permission = "view", audio = false } = req.body || {};
      const sessionBody = JSON.stringify({ duration, permission, audio });
      const apiBase = `https://${config.domain}`;

      async function makeSessionRequest(rejectUnauthorized) {
        return new Promise((resolve, reject) => {
          const url = new URL(`${apiBase}/api/sessions`);
          const proxyReq = https.request(
            {
              hostname: url.hostname,
              port: url.port || 443,
              path: url.pathname,
              method: "POST",
              headers: {
                "Content-Type": "application/json",
                "Content-Length": Buffer.byteLength(sessionBody),
                "X-Forwarded-Host": url.hostname,
                "X-Forwarded-Proto": "https",
              },
              rejectUnauthorized,
            },
            (proxyRes) => {
              let data = "";
              proxyRes.on("data", (chunk) => (data += chunk));
              proxyRes.on("end", () => {
                try {
                  resolve(JSON.parse(data));
                } catch (e) {
                  reject(new Error("Failed to parse session response: " + data));
                }
              });
            },
          );
          proxyReq.on("error", reject);
          // 优化：添加 10s 超时，避免长时间卡住
          proxyReq.setTimeout(10000, () => {
            proxyReq.destroy(new Error("Session creation timeout (10s)"));
          });
          proxyReq.write(sessionBody);
          proxyReq.end();
        });
      }

      function buildLocalUrl(result) {
        const localUrl = new URL(`http://localhost:${port}/`);
        localUrl.searchParams.set("sessionId", result.id);
        localUrl.searchParams.set("token", result.token);
        localUrl.searchParams.set("bridgeToken", getBridgeToken());
        localUrl.searchParams.set("shareUrl", result.shareUrl || "");
        localUrl.searchParams.set("duration", String(duration));
        localUrl.searchParams.set("permission", permission);
        if (audio) localUrl.searchParams.set("audio", "true");
        localUrl.searchParams.set("autoStart", "true");
        localUrl.searchParams.set("silent", "true");
        if (result.peerServerConfig) {
          localUrl.searchParams.set("peerConfig", JSON.stringify(result.peerServerConfig));
        }
        return localUrl.toString();
      }

      try {
        const result = await makeSessionRequest(true);
        res.json({
          success: true,
          session: result,
          localUrl: buildLocalUrl(result),
          shareUrl: result.shareUrl,
        });
      } catch (err) {
        // Retry with TLS verification disabled if cert error
        if (err.code === "UNABLE_TO_GET_ISSUER_CERT_LOCALLY" ||
            err.code === "CERT_HAS_EXPIRED" ||
            err.code === "DEPTH_ZERO_SELF_SIGNED_CERT" ||
            err.message.includes("certificate")) {
          try {
            const result = await makeSessionRequest(false);
            res.json({
              success: true,
              session: result,
              localUrl: buildLocalUrl(result),
              shareUrl: result.shareUrl,
              tlsWarning: "Certificate verification was disabled for this request",
            });
          } catch (retryErr) {
            res.status(502).json({ error: "Failed to create session: " + retryErr.message });
          }
        } else {
          res.status(502).json({ error: "Failed to create session: " + err.message });
        }
      }
    });

    // ---- API proxy to watchitai.net ----
    // Proxies /api/* requests to https://watchitai.net/api/* so the local-host.html
    // page (served from localhost) can call the API without CORS or CSRF cookie issues.
    const API_UPSTREAM = `https://${(loadConfig?.() || {}).domain || "watchitai.net"}`;

    app.all("/api/*", async (req, res) => {
      const apiPath = req.params[0]; // everything after /api/
      const upstreamUrl = `${API_UPSTREAM}/api/${apiPath}`;

      try {
        const url = new URL(upstreamUrl);
        // Append query string from original request
        if (req.url.includes("?")) {
          url.search = req.url.slice(req.url.indexOf("?"));
        }
        const options = {
          hostname: url.hostname,
          port: url.port || 443,
          path: url.pathname + url.search,
          method: req.method,
          headers: {
            "Content-Type": req.get("Content-Type") || "application/json",
            "X-Forwarded-Host": url.hostname,
            "X-Forwarded-Proto": "https",
          },
          rejectUnauthorized: true,
        };

        const proxyReq = https.request(options, (proxyRes) => {
          // Forward set-cookie headers so CSRF cookie works
          const cookies = proxyRes.headers["set-cookie"];
          if (cookies) {
            cookies.forEach((c) => {
              // Rewrite cookie domain to localhost and remove Secure flag
              const rewritten = c.replace(/Domain=[^;]+;?/gi, "").replace(/Secure;?/gi, "");
              res.append("Set-Cookie", rewritten);
            });
          }
          res.status(proxyRes.statusCode);
          res.set("Content-Type", proxyRes.headers["content-type"] || "application/json");
          proxyRes.pipe(res);
        });

        proxyReq.on("error", (err) => {
          console.error("[bridge] API proxy error:", err.message);
          if (!res.headersSent) {
            res.status(502).json({ error: "API proxy error: " + err.message });
          }
        });

        if (req.body && Object.keys(req.body).length > 0) {
          proxyReq.write(JSON.stringify(req.body));
        }
        proxyReq.end();
      } catch (err) {
        console.error("[bridge] API proxy setup error:", err.message);
        res.status(500).json({ error: "API proxy setup error: " + err.message });
      }
    });

    // ---- PeerJS HTTP proxy (avoids CORS from localhost to watchitai.net) ----
    // Proxies /peerjs/* HTTP requests to https://<domain>/peerjs/*
    app.all("/peerjs/*", async (req, res) => {
      const config = loadConfig();
      const domain = config.domain || "watchitai.net";
      const peerPath = req.params[0];
      const queryString = req.url.includes("?") ? req.url.slice(req.url.indexOf("?")) : "";
      const upstreamPath = `/peerjs/${peerPath}${queryString}`;

      const options = {
        hostname: domain,
        port: 443,
        path: upstreamPath,
        method: req.method,
        headers: {
          "Host": domain,
          "Origin": `https://${domain}`,
        },
        rejectUnauthorized: true,
      };

      const proxyReq = https.request(options, (proxyRes) => {
        res.status(proxyRes.statusCode);
        for (const [key, value] of Object.entries(proxyRes.headers)) {
          res.set(key, value);
        }
        proxyRes.pipe(res);
      });

      proxyReq.on("error", (err) => {
        console.error("[bridge] PeerJS HTTP proxy error:", err.message);
        if (!res.headersSent) {
          res.status(502).json({ error: "PeerJS proxy error: " + err.message });
        }
      });

      if (req.body && Object.keys(req.body).length > 0) {
        proxyReq.write(JSON.stringify(req.body));
      }
      proxyReq.end();
    });

    app.get("/permissions", async (req, res) => {
      try {
        const { checkAllPermissions } = await loadPermissions();
        const perms = await checkAllPermissions();
        res.json({
          platform: getPlatformName(),
          permissions: perms,
          cached: {
            screenRecording: permissionCache.screenRecording,
            accessibility: permissionCache.accessibility,
          },
        });
      } catch (e) {
        res.status(500).json({ error: e.message });
      }
    });

    app.get("/screenshot", async (req, res) => {
      try {
        const { captureScreen } = await loadScreen();
        const buffer = await captureScreen();
        res.set("Content-Type", "image/png");
        res.send(buffer);
      } catch (e) {
        res.status(500).json({ error: e.message });
      }
    });

    app.post("/notify", async (req, res) => {
      try {
        const { title, body } = req.body;
        const { showNotification } = await loadNotify();
        await showNotification(title || "WatchItAI", body || "");
        res.json({ success: true });
      } catch (e) {
        res.status(500).json({ error: e.message });
      }
    });

    server = http.createServer(app);

    // Create WSS without binding to server — we handle upgrade manually
    // This prevents WSS from throwing unhandled errors on EADDRINUSE
    wss = new WebSocketServer({ noServer: true });

    // Handle WebSocket upgrade requests manually
    server.on("upgrade", (request, socket, head) => {
      if (request.url.startsWith("/bridge")) {
        wss.handleUpgrade(request, socket, head, (ws, req) => {
          if (authenticateConnection(ws, req)) {
            wss.emit("connection", ws, request);
          }
        });
      } else if (request.url.startsWith("/peerjs")) {
        // Proxy PeerJS WebSocket to wss://<domain>/peerjs/*
        const config = loadConfig();
        const domain = config.domain || "watchitai.net";
        const upstreamUrl = new URL(request.url, `https://${domain}`);

        const proxyReq = https.request({
          hostname: domain,
          port: 443,
          path: upstreamUrl.pathname + upstreamUrl.search,
          method: "GET",
          headers: {
            "Host": domain,
            "Origin": `https://${domain}`,
            "Connection": "Upgrade",
            "Upgrade": "websocket",
            "Sec-WebSocket-Key": request.headers["sec-websocket-key"],
            "Sec-WebSocket-Version": request.headers["sec-websocket-version"],
            "Sec-WebSocket-Protocol": request.headers["sec-websocket-protocol"],
            "Sec-WebSocket-Extensions": request.headers["sec-websocket-extensions"],
          },
          rejectUnauthorized: true,
        });

        proxyReq.on("upgrade", (proxyRes, proxySocket, proxyHead) => {
          // Forward the 101 response headers to the client
          let responseLines = ["HTTP/1.1 101 Switching Protocols"];
          for (const [key, value] of Object.entries(proxyRes.headers)) {
            responseLines.push(`${key}: ${value}`);
          }
          responseLines.push("", "");
          socket.write(responseLines.join("\r\n"));
          if (proxyHead.length) socket.write(proxyHead);

          // Pipe bidirectionally between client and upstream
          proxySocket.pipe(socket);
          socket.pipe(proxySocket);

          proxySocket.on("error", () => { try { socket.destroy(); } catch (e) {} });
          socket.on("error", () => { try { proxySocket.destroy(); } catch (e) {} });
          proxySocket.on("close", () => { try { socket.end(); } catch (e) {} });
          socket.on("close", () => { try { proxySocket.end(); } catch (e) {} });
        });

        proxyReq.on("error", (err) => {
          console.error("[bridge] PeerJS WS proxy error:", err.message);
          try { socket.destroy(); } catch (e) {}
        });

        proxyReq.on("response", () => {
          // Non-101 response from upstream — connection failed
          try { socket.destroy(); } catch (e) {}
        });

        proxyReq.end();
      } else {
        socket.destroy();
      }
    });

    // Register error handler BEFORE listen so EADDRINUSE is caught by the Promise
    server.on("error", (err) => {
      console.error("[bridge] Server error:", err.message);
      // Clean up partial state so a new attempt can be made
      server = null;
      wss = null;
      reject(err);
    });

    wss.on("connection", (ws) => {
      info("[bridge] Client connected");
      activeClients.add(ws);

      ws.send(createBridgeMessage("connected", { platform: getPlatformName() }));

      ws.on("message", (data) => {
        handleBridgeMessage(ws, data.toString());
      });

      ws.on("close", () => {
        info("[bridge] Client disconnected");
        activeClients.delete(ws);
      });

      ws.on("error", (err) => {
        error("[bridge] WebSocket error:", err.message);
        activeClients.delete(ws);
      });
    });

    server.listen(port, () => {
      info(`[bridge] Bridge server listening on ws://localhost:${port}/bridge`);
      console.log(`[bridge] HTTP API on http://localhost:${port}`);
      console.log(`[bridge] Local host page on http://localhost:${port}/`);
      resolve({ port, server, wss });
    });
  });
}

export function stopBridgeServer() {
  screenShareStopped = true;
  if (screenShareTimer) {
    clearTimeout(screenShareTimer);
    screenShareTimer = null;
  }
  if (screenShareInterval) {
    clearInterval(screenShareInterval);
    screenShareInterval = null;
  }
  if (moduleCache.screen) {
    try {
      moduleCache.screen.killAllChildProcesses();
    } catch (e) {
      // ignore
    }
  }
  if (wss) {
    wss.close();
    wss = null;
  }
  if (server) {
    server.close();
    server = null;
  }
  activeClients.clear();
  info("[bridge] Bridge server stopped");
}

export function getBridgeStatus() {
  return {
    running: !!server,
    port: server?.address()?.port || null,
    clients: activeClients.size,
    platform: getPlatformName(),
  };
}

export default {
  startBridgeServer,
  stopBridgeServer,
  getBridgeStatus,
  onControlStarted,
  onControlEnded,
  broadcast,
};
