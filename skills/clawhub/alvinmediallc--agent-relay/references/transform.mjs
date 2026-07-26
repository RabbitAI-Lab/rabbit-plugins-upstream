/**
 * Agent Relay — Hook Transform: Attachment Downloader
 *
 * Copy this file to your OpenClaw hooks/transforms/ directory (as .mjs).
 * Updates the agent's message to include downloaded file paths.
 *
 * Payload shape from Agent Relay push webhook:
 *   { source, agentName, message: { id, text, createdAt, attachment?: { url, type, name } } }
 *
 * Setup:
 *   1. Place this file at: ~/.openclaw/hooks/transforms/agent-relay.mjs
 *   2. Set MEDIA_ROOT below to your preferred download location
 *   3. Configure hooks.mappings to reference this transform (see hooks-config.json)
 */
import fs from "node:fs";
import path from "node:path";
import { randomUUID } from "node:crypto";

// --- CONFIGURATION ---
const MEDIA_ROOT = "<YOUR_WORKSPACE>/skills/agent-relay/media";
// Example: /home/agent/workspace/skills/agent-relay/media

/**
 * Build message envelope for text-only messages (no attachment).
 */
function buildPlainMessage(msg) {
  return [
    `--- Message from User via Relay (${msg.id || ""}) ---`,
    msg.text || "(no text)",
    "--- End relay ---",
    "",
    "Process this as a full agent turn. Reply via:",
    '  <YOUR_WORKSPACE>/skills/agent-relay/scripts/relay send "<reply>"',
    "",
    "ETIQUETTE: Short (1-3 lines), direct, no fluff, no sign-offs.",
  ].join("\n");
}

/**
 * @param ctx — hook context { payload, headers, path, url }
 * @returns null to skip, or override object to merge into agent action
 */
export default async function transform(ctx) {
  const msg = ctx?.payload?.message;
  if (!msg) return null;

  const att = msg.attachment;
  if (!att || !att.url || !att.type) {
    return { message: buildPlainMessage(msg) };
  }

  // Ensure media directory exists
  fs.mkdirSync(MEDIA_ROOT, { recursive: true });

  // Per-message subdirectory
  const msgDir = path.join(MEDIA_ROOT, msg.id || randomUUID());
  fs.mkdirSync(msgDir, { recursive: true });

  // Sanitise filename
  const rawName = att.name || "attachment";
  const safeName = rawName.replace(/[^a-zA-Z0-9._-]/g, "_");
  const dest = path.join(msgDir, safeName);

  let downloaded = false;
  let localPath = "";

  try {
    const resp = await fetch(att.url, { signal: AbortSignal.timeout(30000) });
    if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
    const buffer = Buffer.from(await resp.arrayBuffer());
    fs.writeFileSync(dest, buffer);
    downloaded = true;
    localPath = dest;
  } catch (_err) {
    // Retry once with shorter timeout (URL may be time-limited)
    try {
      const resp2 = await fetch(att.url, { signal: AbortSignal.timeout(15000) });
      if (resp2.ok) {
        const buffer = Buffer.from(await resp2.arrayBuffer());
        fs.writeFileSync(dest, buffer);
        downloaded = true;
        localPath = dest;
      }
    } catch (_) {
      // Download failed
    }
  }

  const parts = [];
  if (msg.text) parts.push(msg.text);

  if (downloaded) {
    const sizeKB = (fs.statSync(dest).size / 1024).toFixed(1);
    const isImage = /^image\//.test(att.type);

    if (isImage) {
      parts.push(`[Image attached: ${safeName} (${sizeKB} KB)]`);
      parts.push(`Local path: ${localPath}`);
      parts.push("Read the local path to view the image.");
    } else {
      parts.push(`[File attached: ${safeName} (${att.type}, ${sizeKB} KB)]`);
      parts.push(`Local path: ${localPath}`);
      parts.push("Read the local path to inspect this file.");
    }
  } else {
    parts.push(`[Attachment: ${safeName} (${att.type}) — download failed, URL expired]`);
  }

  return {
    message: [
      `--- Message from User via Relay (${msg.id || ""}) ---`,
      parts.join("\n"),
      "--- End relay ---",
      "",
      "Process this as a full agent turn. Reply via:",
      '  <YOUR_WORKSPACE>/skills/agent-relay/scripts/relay send "<reply>"',
      "",
      "ETIQUETTE: Short (1-3 lines), direct, no fluff, no sign-offs.",
    ].join("\n"),
  };
}
