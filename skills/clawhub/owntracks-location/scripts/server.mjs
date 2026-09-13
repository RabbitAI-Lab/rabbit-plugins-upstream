#!/usr/bin/env node
/**
 * OwnTracks HTTP webhook receiver (Node.js, zero deps).
 *
 * Every endpoint that can return location data requires a bearer token, so there
 * is no unauthenticated path to the trail. The token lives in the OS keychain
 * when one is available and in a 0600 file otherwise (with a printed warning).
 *
 *   node server.mjs                 start the receiver
 *   node server.mjs --set-token     store a token (stdin, or generated)
 *   node server.mjs --show-token    print the resolved token (for phone setup)
 *   node server.mjs --revoke        clear the token from keychain AND file
 *   node server.mjs --purge-data    delete the stored location trail
 */
import { createServer } from "http";
import {
  mkdirSync, writeFileSync, readFileSync, existsSync, chmodSync, statSync, rmSync,
} from "fs";
import { spawnSync } from "child_process";
import { randomBytes, timingSafeEqual } from "crypto";
import { join, dirname } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const PORT = parseInt(process.env.OWNTRACKS_PORT || "18793", 10);
const BIND = process.env.OWNTRACKS_BIND || "127.0.0.1";
const DATA_DIR = process.env.OWNTRACKS_DATA || join(__dirname, "data");
const RETENTION_DAYS = parseInt(process.env.OWNTRACKS_RETENTION_DAYS ?? "7", 10);
const MAX_POINTS = parseInt(process.env.OWNTRACKS_MAX_POINTS ?? "500", 10);
const STORE_SSID = process.env.OWNTRACKS_STORE_SSID === "1";
const LOG_COORDS = process.env.OWNTRACKS_LOG_COORDS === "1";

const KEYCHAIN_SERVICE = "owntracks-location";
const KEYCHAIN_ACCOUNT = "receiver-token";

const historyFile = join(DATA_DIR, "history.json");
const latestFile = join(DATA_DIR, "latest.json");
const tokenFile = join(DATA_DIR, "token");

// ---------------------------------------------------------------- storage ---

function ensureDataDir() {
  mkdirSync(DATA_DIR, { recursive: true, mode: 0o700 });
  chmodSync(DATA_DIR, 0o700);
}

function writePrivate(file, text) {
  writeFileSync(file, text, { mode: 0o600 });
  chmodSync(file, 0o600); // writeFileSync only applies mode on creation
}

function loadHistory() {
  try {
    if (existsSync(historyFile)) return JSON.parse(readFileSync(historyFile, "utf-8"));
  } catch {}
  return [];
}

/** Drop points older than the retention window, then cap the count. 0 = unlimited. */
function prune(history) {
  let out = history;
  if (RETENTION_DAYS > 0) {
    const cutoff = Date.now() / 1000 - RETENTION_DAYS * 86400;
    out = out.filter(e => (typeof e.tst === "number" ? e.tst >= cutoff : true));
  }
  if (MAX_POINTS > 0) out = out.slice(-MAX_POINTS);
  return out;
}

function saveHistory(h) {
  writePrivate(historyFile, JSON.stringify(prune(h), null, 2));
}

// ---------------------------------------------------------------- keychain ---

function keychainStore(token) {
  if (process.platform === "darwin") {
    const r = spawnSync("security", [
      "add-generic-password", "-U", "-s", KEYCHAIN_SERVICE, "-a", KEYCHAIN_ACCOUNT, "-w", token,
    ], { stdio: "ignore" });
    return !r.error && r.status === 0;
  }
  const r = spawnSync("secret-tool", [
    "store", "--label=OwnTracks receiver token", "service", KEYCHAIN_SERVICE, "account", KEYCHAIN_ACCOUNT,
  ], { input: token, stdio: ["pipe", "ignore", "ignore"] });
  return !r.error && r.status === 0;
}

function keychainRead() {
  if (process.platform === "darwin") {
    const r = spawnSync("security", [
      "find-generic-password", "-s", KEYCHAIN_SERVICE, "-a", KEYCHAIN_ACCOUNT, "-w",
    ], { encoding: "utf-8" });
    return !r.error && r.status === 0 ? r.stdout.trim() : "";
  }
  const r = spawnSync("secret-tool", [
    "lookup", "service", KEYCHAIN_SERVICE, "account", KEYCHAIN_ACCOUNT,
  ], { encoding: "utf-8" });
  return !r.error && r.status === 0 ? r.stdout.trim() : "";
}

function keychainClear() {
  if (process.platform === "darwin") {
    const r = spawnSync("security", [
      "delete-generic-password", "-s", KEYCHAIN_SERVICE, "-a", KEYCHAIN_ACCOUNT,
    ], { stdio: "ignore" });
    return !r.error && r.status === 0;
  }
  const r = spawnSync("secret-tool", [
    "clear", "service", KEYCHAIN_SERVICE, "account", KEYCHAIN_ACCOUNT,
  ], { stdio: "ignore" });
  return !r.error && r.status === 0;
}

function fileTokenRead() {
  if (!existsSync(tokenFile)) return "";
  if (statSync(tokenFile).mode & 0o077) {
    console.error(`⚠️  ${tokenFile} was group/world readable — tightening to 0600.`);
    chmodSync(tokenFile, 0o600);
  }
  return readFileSync(tokenFile, "utf-8").trim();
}

/** env → keychain → 0600 file. */
function resolveToken() {
  return (process.env.OWNTRACKS_SECRET || "").trim() || keychainRead() || fileTokenRead();
}

// ------------------------------------------------------------------- auth ---

/** OwnTracks sends HTTP Basic; curl and the agent send Bearer. Accept both. */
function presentedToken(req) {
  const h = req.headers["authorization"] || "";
  if (h.startsWith("Bearer ")) return h.slice(7).trim();
  if (h.startsWith("Basic ")) {
    const decoded = Buffer.from(h.slice(6).trim(), "base64").toString("utf-8");
    const i = decoded.indexOf(":");
    return i === -1 ? "" : decoded.slice(i + 1);
  }
  return "";
}

function authorized(req, token) {
  const a = Buffer.from(presentedToken(req));
  const b = Buffer.from(token);
  return a.length === b.length && timingSafeEqual(a, b);
}

// -------------------------------------------------------------- sub-commands ---

const flags = new Set(process.argv.slice(2));

if (flags.has("--set-token")) {
  ensureDataDir();
  let token = "";
  if (!process.stdin.isTTY) {
    try { token = readFileSync(0, "utf-8").trim(); } catch {}
  }
  if (!token) {
    token = randomBytes(32).toString("hex");
    console.log("No token on stdin — generated one.");
  }
  if (keychainStore(token)) {
    console.log("🔐 Token stored in the OS keychain.");
  } else {
    writePrivate(tokenFile, token + "\n");
    console.log(`⚠️  WARNING: no OS keychain available (install libsecret's secret-tool on Linux).`);
    console.log(`⚠️  The token was written to ${tokenFile} as a plain 0600 file instead.`);
    console.log(`⚠️  Anyone who can read that file, or run as this user, can read your location.`);
  }
  console.log(`Token: ${token}`);
  console.log("Put it in OwnTracks → Preferences → Connection → Authentication as the PASSWORD.");
  process.exit(0);
}

if (flags.has("--show-token")) {
  const token = resolveToken();
  if (!token) { console.error("No token configured. Run: node server.mjs --set-token"); process.exit(1); }
  console.log(token);
  process.exit(0);
}

if (flags.has("--revoke") || flags.has("--logout")) {
  const inKeychain = keychainClear();
  const hadFile = existsSync(tokenFile);
  if (hadFile) rmSync(tokenFile, { force: true });
  console.log(`🔓 Keychain entry: ${inKeychain ? "cleared" : "none found"}`);
  console.log(`🔓 Token file:     ${hadFile ? "deleted" : "none found"}`);
  if (process.env.OWNTRACKS_SECRET) {
    console.log("⚠️  OWNTRACKS_SECRET is still set in this environment — unset it and remove it from any systemd unit.");
  }
  console.log("");
  console.log("This receiver is self-hosted: there is no vendor account to revoke. Finish the");
  console.log("revocation on the phone — OwnTracks → Preferences → Connection: clear the URL and");
  console.log("the Authentication password, so the device stops sending.");
  console.log("OwnTracks HTTP mode reference: https://owntracks.org/booklet/features/http/");
  console.log("Then restart the receiver so it reloads (it refuses to start with no token).");
  console.log("The location trail is NOT deleted by --revoke. To erase it: node server.mjs --purge-data");
  process.exit(0);
}

if (flags.has("--purge-data")) {
  let removed = 0;
  for (const f of [latestFile, historyFile]) {
    if (existsSync(f)) { rmSync(f, { force: true }); removed++; console.log(`🗑️  Deleted ${f}`); }
  }
  if (!removed) console.log("Nothing to delete — no location data stored.");
  console.log("Named places in places.sqlite are untouched (use: node places.mjs remove <name>).");
  process.exit(0);
}

// ----------------------------------------------------------------- server ---

ensureDataDir();

const TOKEN = resolveToken();
if (!TOKEN) {
  console.error("✋ No token configured, so every endpoint would be open to anyone who can reach");
  console.error("   the port. Refusing to start. Create one with:");
  console.error("     node scripts/server.mjs --set-token");
  process.exit(1);
}

const isLoopback = BIND === "127.0.0.1" || BIND === "::1" || BIND === "localhost";
if (!isLoopback) {
  console.warn(`⚠️  Binding to ${BIND}, not loopback: this listener is reachable from the network.`);
  console.warn("⚠️  Plain HTTP means the token and your coordinates cross the wire in clear text.");
  console.warn("⚠️  Put it behind Tailscale, a WireGuard tunnel or a TLS reverse proxy, and firewall the port.");
}

// Trim anything already past the retention window before serving a single request.
saveHistory(loadHistory());

function readBody(req) {
  return new Promise((resolve, reject) => {
    const chunks = [];
    let size = 0;
    req.on("data", c => {
      size += c.length;
      if (size > 64 * 1024) { reject(new Error("body too large")); req.destroy(); return; }
      chunks.push(c);
    });
    req.on("end", () => {
      try { resolve(JSON.parse(Buffer.concat(chunks).toString())); }
      catch (e) { reject(e); }
    });
    req.on("error", reject);
  });
}

const server = createServer(async (req, res) => {
  const url = new URL(req.url, `http://localhost:${PORT}`);

  // Liveness only — carries no location data, so it stays open.
  if (url.pathname === "/health") {
    res.writeHead(200);
    return res.end("ok");
  }

  if (!authorized(req, TOKEN)) {
    res.writeHead(401, { "content-type": "application/json", "www-authenticate": "Bearer" });
    return res.end(JSON.stringify({ error: "unauthorized" }));
  }

  if (req.method === "POST" && (url.pathname === "/" || url.pathname === "/owntracks")) {
    try {
      const body = await readBody(req);
      if (body._type !== "location") {
        res.writeHead(200, { "content-type": "application/json" });
        return res.end("[]");
      }

      const entry = {
        lat: body.lat,
        lon: body.lon,
        acc: body.acc ?? null,
        alt: body.alt ?? null,
        vel: body.vel ?? null,
        batt: body.batt ?? null,
        tst: body.tst,
        updated: new Date().toISOString(),
      };
      // The wifi network name is not needed to answer "where am I?", so it is
      // dropped unless you ask for it.
      if (STORE_SSID) entry.ssid = body.SSID ?? null;

      writePrivate(latestFile, JSON.stringify(entry, null, 2));

      const history = loadHistory();
      history.push(entry);
      saveHistory(history);

      // Logs are a second copy of the trail, usually unretained. Coordinates are opt-in.
      console.log(LOG_COORDS
        ? `📍 ${entry.lat}, ${entry.lon} (acc: ${entry.acc}m, batt: ${entry.batt}%)`
        : `📍 location update stored (acc: ${entry.acc}m)`);

      res.writeHead(200, { "content-type": "application/json" });
      return res.end("[]");
    } catch (e) {
      console.error("Parse error:", e.message);
      res.writeHead(400, { "content-type": "application/json" });
      return res.end(JSON.stringify({ error: "bad request" }));
    }
  }

  if (req.method === "GET" && url.pathname === "/latest") {
    if (existsSync(latestFile)) {
      res.writeHead(200, { "content-type": "application/json" });
      return res.end(readFileSync(latestFile, "utf-8"));
    }
    res.writeHead(404, { "content-type": "application/json" });
    return res.end(JSON.stringify({ error: "no location yet" }));
  }

  if (req.method === "GET" && url.pathname === "/history") {
    const history = loadHistory();
    const limit = parseInt(url.searchParams.get("limit") || "50", 10);
    res.writeHead(200, { "content-type": "application/json" });
    return res.end(JSON.stringify(history.slice(-limit)));
  }

  res.writeHead(404, { "content-type": "application/json" });
  res.end(JSON.stringify({ error: "not found" }));
});

server.listen(PORT, BIND, () => {
  console.log(`🛰️  OwnTracks receiver listening on http://${BIND}:${PORT} (token required)`);
  console.log(`    Retention: ${RETENTION_DAYS > 0 ? RETENTION_DAYS + " days" : "unlimited"}, ` +
              `max ${MAX_POINTS > 0 ? MAX_POINTS : "unlimited"} points, ` +
              `SSID capture ${STORE_SSID ? "ON" : "off"}`);
});
