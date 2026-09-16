#!/usr/bin/env node
/**
 * Cloudflare Drop — Temporary Account API Deploy Script
 *
 * Usage: node deploy.mjs <static-folder-path> --accept-terms --claim-url-file <path>
 *
 * Dependencies: Node.js only (crypto, fs, path)
 */

import { createHash } from "node:crypto";
import {
  closeSync,
  lstatSync,
  openSync,
  readFileSync,
  readdirSync,
  rmSync,
  writeFileSync,
} from "node:fs";
import { extname, join } from "node:path";

const API_BASE = "https://api.cloudflare.com/client/v4";
const MAX_FILES = 1_000;
const MAX_WORKER_SCRIPT_BYTES = 2 * 1024 * 1024;

// --- Proof-of-Work Solver ---

function sha256(value) {
  return createHash("sha256").update(value).digest();
}

function solvePreviewChallenge({ challengeToken, seed, k, g }) {
  const seedBytes = Buffer.from(seed, "base64url");
  if (seedBytes.length !== 32) throw new Error("seed must decode to 32 bytes");
  if (!Number.isInteger(k) || k <= 0) throw new Error("k must be positive");
  if (!Number.isInteger(g) || g <= 0) throw new Error("g must be positive");
  if (k * g > 64_000_000) throw new Error("k * g must not exceed 64,000,000");

  const checkpoints = [];
  let hash = sha256(seedBytes);
  checkpoints.push(hash);

  for (let segment = 0; segment < k; segment++) {
    for (let iteration = 0; iteration < g; iteration++) {
      hash = sha256(hash);
    }
    checkpoints.push(hash);
  }

  return {
    challengeToken,
    solution: {
      checkpoints: Buffer.concat(checkpoints).toString("base64"),
    },
  };
}

// --- API Helpers ---

async function apiPost(path, body, token = null) {
  const headers = { "Content-Type": "application/json" };
  if (token) headers["Authorization"] = `Bearer ${token}`;

  const res = await fetch(`${API_BASE}${path}`, {
    method: "POST",
    headers,
    body: JSON.stringify(body),
  });

  return parseApiResponse(res);
}

async function apiPut(path, body, token, isFormData = false) {
  const headers = { "Authorization": `Bearer ${token}` };

  let requestBody;
  if (isFormData) {
    requestBody = body; // FormData object
  } else {
    headers["Content-Type"] = "application/json";
    requestBody = JSON.stringify(body);
  }

  const res = await fetch(`${API_BASE}${path}`, {
    method: "PUT",
    headers,
    body: requestBody,
  });

  return parseApiResponse(res);
}

async function apiGet(path, token) {
  const res = await fetch(`${API_BASE}${path}`, {
    headers: { "Authorization": `Bearer ${token}` },
  });

  return parseApiResponse(res);
}

async function parseApiResponse(res) {
  let json;
  try {
    json = await res.json();
  } catch {
    throw new Error(`API ${res.status} returned a non-JSON response`);
  }

  if (!res.ok || !json.success) {
    throw new Error(`API ${res.status}: ${JSON.stringify(json.errors ?? [])}`);
  }
  return json.result;
}

// --- Static Site → Worker ---

function getMimeType(ext) {
  const types = {
    ".html": "text/html",
    ".css": "text/css",
    ".js": "application/javascript",
    ".json": "application/json",
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".gif": "image/gif",
    ".svg": "image/svg+xml",
    ".ico": "image/x-icon",
    ".woff": "font/woff",
    ".woff2": "font/woff2",
    ".ttf": "font/ttf",
    ".txt": "text/plain",
    ".xml": "application/xml",
    ".webp": "image/webp",
    ".mp4": "video/mp4",
    ".webm": "video/webm",
  };
  return types[ext] || "application/octet-stream";
}

function collectFiles(dirPath, basePath = "") {
  const files = [];
  const entries = readdirSync(dirPath);

  for (const entry of entries) {
    const fullPath = join(dirPath, entry);
    const relPath = join(basePath, entry);
    const stat = lstatSync(fullPath);

    if (stat.isSymbolicLink()) {
      throw new Error(`Symlinks are not allowed in the static directory: ${fullPath}`);
    }

    if (stat.isDirectory()) {
      files.push(...collectFiles(fullPath, relPath));
    } else if (stat.isFile()) {
      const content = readFileSync(fullPath);
      const ext = extname(entry);
      files.push({
        path: "/" + relPath.replace(/\\/g, "/"),
        content: content.toString("base64"),
        mimeType: getMimeType(ext),
      });
    } else {
      throw new Error(`Only regular files are allowed in the static directory: ${fullPath}`);
    }
  }

  return files;
}

function generateWorkerScript(files) {
  const assetsMap = {};
  for (const file of files) {
    assetsMap[file.path] = {
      b: file.content,
      m: file.mimeType,
    };
  }

  const assetsJson = JSON.stringify(assetsMap);

  return `const A=${assetsJson};export default{async fetch(r){const u=new URL(r.url);let p=u.pathname;if(p==="/"||p==="")p="/index.html";let a=A[p];if(!a&&!p.includes("."))a=A[p+".html"];if(!a)return new Response("404",{status:404});const h={"Content-Type":a.m};const body=Uint8Array.from(atob(a.b),c=>c.charCodeAt(0));return new Response(body,{headers:h})}};`;
}

function prepareStaticSite(staticDir) {
  const root = lstatSync(staticDir);
  if (!root.isDirectory()) {
    throw new Error(`Static path must be a directory: ${staticDir}`);
  }

  const files = collectFiles(staticDir);
  if (files.length === 0) {
    throw new Error("Static directory is empty");
  }
  if (files.length > MAX_FILES) {
    throw new Error(`Static directory exceeds the ${MAX_FILES}-file limit`);
  }
  if (!files.some((file) => file.path === "/index.html")) {
    throw new Error("Static directory must contain index.html at its root");
  }

  const workerScript = generateWorkerScript(files);
  const workerScriptBytes = Buffer.byteLength(workerScript);
  if (workerScriptBytes > MAX_WORKER_SCRIPT_BYTES) {
    throw new Error(
      `Generated Worker is ${workerScriptBytes} bytes; limit is ${MAX_WORKER_SCRIPT_BYTES} bytes`
    );
  }

  return { files, workerScript, workerScriptBytes };
}

function openClaimFile(claimFile) {
  try {
    return openSync(claimFile, "wx", 0o600);
  } catch (error) {
    throw new Error(`Cannot create claim URL file: ${error.message}`);
  }
}

// --- Main Deploy Flow ---

async function deploy(staticDir, claimFile) {
  console.log("🚀 Cloudflare Drop Deploy (Temporary Account API)");
  console.log(`📁 Static directory: ${staticDir}\n`);

  const { files, workerScript, workerScriptBytes } = prepareStaticSite(staticDir);
  const claimFileDescriptor = openClaimFile(claimFile);
  let claimFileWritten = false;

  try {

  // Step 1: Request challenge
  console.log("⏳ Step 1/4: Requesting proof-of-work challenge...");
  const challenge = await apiPost("/provisioning/previews/challenge", {});
  console.log(`   Challenge received (k=${challenge.k}, g=${challenge.g})`);

  // Step 2: Solve challenge
  console.log("⏳ Step 2/4: Solving proof-of-work...");
  const solution = solvePreviewChallenge(challenge);
  console.log("   Challenge solved!");

  // Step 3: Create temporary account
  console.log("⏳ Step 3/4: Creating temporary account...");
  const account = await apiPost("/provisioning/previews", {
    termsOfService: "https://www.cloudflare.com/terms/",
    privacyPolicy: "https://www.cloudflare.com/privacypolicy/",
    acceptTermsOfService: "yes",
    ...solution,
  });

  const accountId = account.account.id;
  const apiToken = account.account.apiToken;
  const claimUrl = account.claim.url;

  writeFileSync(claimFileDescriptor, `${claimUrl}\n`);
  claimFileWritten = true;
  closeSync(claimFileDescriptor);

  console.log(`   Account created: ${account.account.name}`);
  console.log(`   Claim URL written to: ${claimFile}`);
  console.log(`   Expires: ${account.claim.expiresAt}\n`);

  // Step 4: Deploy static site
  console.log("⏳ Step 4/4: Deploying static site...");

  console.log(`   Collected ${files.length} files (${workerScriptBytes} bytes generated)`);

  // Upload worker
  const formData = new FormData();
  formData.append(
    "metadata",
    new Blob([
      JSON.stringify({
        main_module: "worker.mjs",
        compatibility_date: new Date().toISOString().slice(0, 10),
      }),
    ], { type: "application/json" })
  );
  formData.append("worker.mjs", new Blob([workerScript], { type: "application/javascript+module" }), "worker.mjs");

  const scriptName = "site-" + Date.now().toString(36);
  await apiPut(`/accounts/${accountId}/workers/scripts/${scriptName}`, formData, apiToken, true);

  // Script uploads are not automatically exposed on workers.dev.
  await apiPost(
    `/accounts/${accountId}/workers/scripts/${scriptName}/subdomain`,
    { enabled: true },
    apiToken
  );

  // Get subdomain
  const subdomain = await apiGet(`/accounts/${accountId}/workers/subdomain`, apiToken);
  const liveUrl = `https://${scriptName}.${subdomain.subdomain}.workers.dev`;

  console.log("\n✅ Deploy complete!");
  console.log(`\n🌐 Live URL: ${liveUrl}`);
  console.log(`🔐 Claim URL file: ${claimFile}`);
  console.log(`⏰ Expires in 60 minutes (claim to keep permanently)\n`);

  return { liveUrl, claimFile };
  } finally {
    if (!claimFileWritten) {
      closeSync(claimFileDescriptor);
      rmSync(claimFile, { force: true });
    }
  }
}

// --- Entry Point ---

function parseArgs(args) {
  let staticDir;
  let acceptedTerms = false;
  let claimFile;

  for (let index = 0; index < args.length; index += 1) {
    const arg = args[index];
    if (arg === "--accept-terms") {
      acceptedTerms = true;
    } else if (arg === "--claim-url-file") {
      claimFile = args[++index];
      if (!claimFile) {
        throw new Error("--claim-url-file requires a path");
      }
    } else if (arg.startsWith("-")) {
      throw new Error(`Unknown option: ${arg}`);
    } else if (staticDir) {
      throw new Error("Only one static directory may be provided");
    } else {
      staticDir = arg;
    }
  }

  if (!staticDir) {
    throw new Error("A static directory is required");
  }
  if (!acceptedTerms) {
    throw new Error(
      "Explicit Terms and Privacy Policy acceptance is required; pass --accept-terms after user confirmation"
    );
  }
  if (!claimFile) {
    throw new Error("A private claim URL file is required; pass --claim-url-file <path>");
  }

  return { staticDir, claimFile };
}

try {
  const { staticDir, claimFile } = parseArgs(process.argv.slice(2));
  deploy(staticDir, claimFile).catch(err => {
    console.error(`\n❌ Deploy failed: ${err.message}`);
    process.exit(1);
  });
} catch (error) {
  console.error(`Error: ${error.message}`);
  process.exit(1);
}
