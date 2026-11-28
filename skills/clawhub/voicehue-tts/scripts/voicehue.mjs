#!/usr/bin/env node
/**
 * VoiceHue TTS Skill CLI — zero-dependency Node.js 18+ helper for AI agents.
 *
 * Security & scope:
 * - Connects exclusively to https://voicehue.com/v1/... (and https://api.voicehue.com
 *   for signed completed job audio downloads — no third-party hosts).
 * - Reads only VOICEHUE_API_KEY from process.env (or `.env.local` / `.env` inside
 *   the current working directory if unset in process.env); never prints or logs it.
 * - Reads and writes files strictly inside the current working directory.
 * - Uses only Node.js built-ins (no npm packages, no shell execution, no deletions).
 */
import crypto from "node:crypto";
import {realpathSync} from "node:fs";
import fs from "node:fs/promises";
import path from "node:path";
import {fileURLToPath} from "node:url";

const DEFAULT_ORIGIN = "https://voicehue.com";
const DEFAULT_MODEL = "voicehue-tts";
const SYNC_MAX_CHARS = 5_000;
const JOB_MAX_CHARS = 20_000;
const POLL_INTERVAL_MS = 5_000;
const MAX_POLL_ATTEMPTS = 72; // up to 6 minutes
const FAST_TIMEOUT_MS = 30_000;
const SPEECH_TIMEOUT_MS = 185_000;   // Matches server UPSTREAM_TIMEOUT_MS (170s) + margin
const DIALOGUE_TIMEOUT_MS = 310_000; // Matches server DIALOGUE_UPSTREAM_TIMEOUT_MS (280s) + margin
const STUDIO_TIMEOUT_MS = 165_000;   // Matches server proxyStudio timeout (150s) + margin
const MAX_RETRIES = 2;

const BOOLEAN_FLAGS = new Set(["wait", "json", "help", "auto", "strip-markdown", "raw"]);

const HELP = `VoiceHue TTS CLI (https://voicehue.com/developers#agent-skill)

Usage:
  node <SKILL_DIR>/scripts/voicehue.mjs check    [--json]
  node <SKILL_DIR>/scripts/voicehue.mjs voices   [--language <code>] [--tier standard|premium] [--gender female|male] [--tag <tag>] [--query <text>] [--limit <n>] [--json]
  node <SKILL_DIR>/scripts/voicehue.mjs usage    [--json]
  node <SKILL_DIR>/scripts/voicehue.mjs speak    --voice <id> (--text <str> | --text-file <path>) --out <path> [--speed 0.5..2] [--format mp3|wav] [--pronunciations <json-path>] [--strip-markdown | --raw] [--auto] [--idempotency-key <key>]
  node <SKILL_DIR>/scripts/voicehue.mjs dialogue (--blocks-file <json-path> | --script-file <txt-path> --voices "Host=vh-ethan,Guest=vh-mia") --out <path> [--format mp3|wav] [--pronunciations <json-path>] [--pause-ms <n>] [--idempotency-key <key>]
  node <SKILL_DIR>/scripts/voicehue.mjs job      --voice <id> (--text <str> | --text-file <path>) [--out <path>] [--speed 0.5..2] [--format mp3|wav] [--pronunciations <json-path>] [--strip-markdown | --raw] [--callback-url <https-url>] [--idempotency-key <key>] [--wait]
  node <SKILL_DIR>/scripts/voicehue.mjs job      --id <job-uuid> [--out <path>] [--wait]
  node <SKILL_DIR>/scripts/voicehue.mjs studio   --payload-file <json-path> [--json]

Environment:
  VOICEHUE_API_KEY   Required for all commands except "voices" (and optional for "check").
                     Read from process.env, or fallback to VOICEHUE_API_KEY in ./.env.local or ./.env.
                     Create free at https://voicehue.com/dashboard/keys
`;

/** Ensures a user-supplied file path resolves inside the workspace root (prevents path traversal). */
export function resolveWorkspacePath(cwd, targetPath) {
  if (!targetPath || typeof targetPath !== "string") {
    throw new Error("A file path inside the current working directory is required.");
  }
  const root = path.resolve(cwd);
  const resolved = path.resolve(root, targetPath);
  const rel = path.relative(root, resolved);
  if (rel.startsWith("..") || path.isAbsolute(rel)) {
    throw new Error(`Path "${targetPath}" must stay inside the current working directory (${root}).`);
  }
  return resolved;
}

/** Matches regional queries like zh-CN / en-US against base-language voices like zh / en too. */
export function languageMatches(voiceLang, queryLang) {
  if (!queryLang) return true;
  const v = String(voiceLang || "").toLowerCase().replace("_", "-");
  const q = String(queryLang || "").trim().toLowerCase().replace("_", "-");
  if (!q) return true;
  return v.startsWith(q) || (!v.includes("-") && q.startsWith(v + "-"));
}

/** Strips Markdown syntax, code blocks, URLs, and HTML so docs sound natural when spoken. */
export function stripMarkdownForSpeech(raw) {
  let text = String(raw || "").replace(/\r\n/g, "\n");
  // Drop YAML frontmatter at top of file
  text = text.replace(/^---\n[\s\S]*?\n---\n?/, "");
  // Drop fenced code blocks (``` or ~~~, including indented blocks inside lists)
  text = text.replace(/^[ \t]*(?:```|~~~)[^\n]*\n[\s\S]*?^[ \t]*(?:```|~~~)[ \t]*$/gm, "");
  // Drop HTML comments and inline HTML tags
  text = text.replace(/<!--[\s\S]*?-->/g, "");
  text = text.replace(/<\/?[A-Za-z][A-Za-z0-9-]*(?:\s+[^>]*)?>/g, "");
  // Drop Markdown images ![alt](url) and empty badge links [](url); keep link text from [label](url)
  text = text.replace(/!\[[^\]]*\]\([^)]*\)/g, "");
  text = text.replace(/\[\s*\]\([^)]*\)/g, "");
  text = text.replace(/\[([^\]]+)\]\([^)]*\)/g, "$1");
  // Drop reference link definitions like [id]: https://...
  text = text.replace(/^\s*\[[^\]]+\]:\s+\S+.*$/gm, "");
  // Drop bare HTTP(S) URLs so they are not spelled out letter by letter
  text = text.replace(/https?:\/\/[^\s)>\]]+/g, "");
  // Drop horizontal rules and table delimiter lines
  text = text.replace(/^\s*(?:[-*_]\s*){3,}$/gm, "");
  text = text.replace(/^\s*\|?(?:\s*:?-{3,}:?\s*\|)+\s*:?-{3,}:?\s*\|?\s*$/gm, "");
  // Convert Markdown table rows into readable comma-separated lines
  text = text.replace(/^\s*\|(.+)\|\s*$/gm, (_, inner) =>
    inner
      .split("|")
      .map((cell) => cell.trim())
      .filter(Boolean)
      .join(", ")
  );
  // Strip heading markers, blockquotes, and bullet/numbered list prefixes
  text = text.replace(/^\s{0,3}#{1,6}\s+/gm, "");
  text = text.replace(/^\s*>\s?/gm, "");
  text = text.replace(/^\s*(?:[-*+]|\d+\.)\s+/gm, "");
  // Strip inline emphasis and code backticks while preserving the words inside
  text = text.replace(/`([^`]+)`/g, "$1");
  text = text.replace(/(\*\*|__)(.*?)\1/g, "$2");
  text = text.replace(/~~(.*?)~~/g, "$1");
  text = text.replace(/(?<!\*)\*([^*\n]+)\*(?!\*)/g, "$1");
  // Collapse excess whitespace and blank lines
  text = text.replace(/[ \t]+/g, " ").replace(/[ \t]*\n[ \t]*/g, "\n").replace(/\n{3,}/g, "\n\n");
  return text.trim();
}

/** Parses a human-readable `Speaker: line` script (supports both `:` and `：`) into dialogue blocks. */
export function parseDialogueScript(scriptText, voiceMap, defaultPauseMs = 400) {
  const normalizedMap = new Map();
  for (const [k, v] of Object.entries(voiceMap || {})) {
    if (k && v) normalizedMap.set(k.trim().toLowerCase(), String(v).trim());
  }
  const lines = String(scriptText || "").replace(/\r\n/g, "\n").split("\n");
  const blocks = [];
  const missingSpeakers = new Set();

  for (const rawLine of lines) {
    const line = rawLine.trim();
    if (!line || line.startsWith("#") || line.startsWith("//")) continue;
    // Match `Speaker: text`, `Speaker：text`, `**Speaker**: text`, or `**Speaker:** text`
    // Ignore URL schemes (`https://`) and timestamps (`10:30`) so continuation lines are not misparsed as speakers.
    const m = line.match(/^(\*\*|__)?([^:\uff1a\n]{1,40}?)\1?\s*([:\uff1a])\s*(.+)$/);
    const looksLikeUrlOrTime =
      Boolean(m) &&
      m[3] === ":" &&
      (m[4].startsWith("//") || (/\d$/.test(m[2]) && /^\d/.test(m[4])));
    if (m && !looksLikeUrlOrTime) {
      const marker = m[1] || "";
      const speaker = m[2].trim();
      let input = m[4].trim();
      if (marker && input.startsWith(marker)) {
        input = input.slice(marker.length).trim();
      }
      if (!input) continue;
      const voice = normalizedMap.get(speaker.toLowerCase());
      if (!voice) {
        missingSpeakers.add(speaker);
        continue;
      }
      blocks.push({speaker, voice, input, pause_ms: defaultPauseMs});
    } else if (blocks.length > 0) {
      // Continuation line belongs to the previous speaker
      blocks[blocks.length - 1].input += " " + line;
    } else {
      throw new Error(
        `Could not parse dialogue line "${line.slice(0, 60)}". Expected format: "Speaker: spoken line".`
      );
    }
  }

  if (missingSpeakers.size > 0) {
    throw new Error(
      `Unmapped speaker(s) in script: ${[...missingSpeakers].join(", ")}. Pass --voices "Speaker1=vh-ethan,Speaker2=vh-mia".`
    );
  }
  if (blocks.length === 0) {
    throw new Error("Script file did not contain any `Speaker: line` dialogue turns.");
  }
  return blocks;
}

/** Parses `--voices "Host=vh-ethan,Guest=vh-mia"` into `{Host: "vh-ethan", Guest: "vh-mia"}`. */
export function parseVoiceMapArg(raw) {
  const map = {};
  if (typeof raw !== "string" || !raw.trim()) return map;
  for (const pair of raw.split(",")) {
    const idx = pair.indexOf("=");
    if (idx <= 0) continue;
    const speaker = pair.slice(0, idx).trim();
    const voice = pair.slice(idx + 1).trim();
    if (speaker && voice) map[speaker] = voice;
  }
  return map;
}

/** Pure-JS duration estimator for WAV (exact RIFF byteRate) and MP3 (MPEG frame scan). */
export function estimateAudioDurationSeconds(bytes, format) {
  if (!(bytes instanceof Uint8Array) || bytes.byteLength < 4) return null;
  if (format === "wav" && bytes.byteLength > 44) {
    const view = new DataView(bytes.buffer, bytes.byteOffset, bytes.byteLength);
    const riff = String.fromCharCode(bytes[0], bytes[1], bytes[2], bytes[3]);
    if (riff === "RIFF") {
      const byteRate = view.getUint32(28, true);
      if (byteRate > 0) {
        return Math.round(((bytes.byteLength - 44) / byteRate) * 10) / 10;
      }
    }
    return null;
  }

  // MP3: skip optional ID3v2 header, then walk valid MPEG Layer III frame headers
  let offset = 0;
  if (bytes.byteLength > 10 && bytes[0] === 0x49 && bytes[1] === 0x44 && bytes[2] === 0x33) {
    const tagSize =
      ((bytes[6] & 0x7f) << 21) | ((bytes[7] & 0x7f) << 14) | ((bytes[8] & 0x7f) << 7) | (bytes[9] & 0x7f);
    offset = 10 + tagSize;
  }
  const bitratesMpeg1L3 = [0, 32, 40, 48, 56, 64, 80, 96, 112, 128, 160, 192, 224, 256, 320, 0];
  const bitratesMpeg2L3 = [0, 8, 16, 24, 32, 40, 48, 56, 64, 80, 96, 112, 128, 144, 160, 0];
  const sampleRates = {
    3: [44100, 48000, 32000], // MPEG 1
    2: [22050, 24000, 16000], // MPEG 2
    0: [11025, 12000, 8000]   // MPEG 2.5
  };

  let totalSec = 0;
  let frames = 0;
  while (offset + 4 <= bytes.byteLength) {
    if (bytes[offset] !== 0xff || (bytes[offset + 1] & 0xe0) !== 0xe0) {
      offset++;
      continue;
    }
    const ver = (bytes[offset + 1] >> 3) & 0x03;
    const layer = (bytes[offset + 1] >> 1) & 0x03;
    const brIdx = (bytes[offset + 2] >> 4) & 0x0f;
    const srIdx = (bytes[offset + 2] >> 2) & 0x03;
    const pad = (bytes[offset + 2] >> 1) & 0x01;
    if (ver === 1 || layer !== 1 || brIdx === 0 || brIdx === 15 || srIdx === 3) {
      offset++;
      continue;
    }
    const sr = sampleRates[ver]?.[srIdx];
    const brKbps = ver === 3 ? bitratesMpeg1L3[brIdx] : bitratesMpeg2L3[brIdx];
    if (!sr || !brKbps) {
      offset++;
      continue;
    }
    const samples = ver === 3 ? 1152 : 576;
    const frameLen = Math.floor(((samples / 8) * brKbps * 1000) / sr) + pad;
    if (frameLen < 24 || offset + frameLen > bytes.byteLength) break;
    totalSec += samples / sr;
    frames++;
    offset += frameLen;
  }
  if (frames > 0) return Math.round(totalSec * 10) / 10;
  return null;
}

/** Parses --flag value and --boolean flags into a simple object. */
export function parseArgs(argv) {
  const args = {_: []};
  for (let i = 0; i < argv.length; i++) {
    const token = argv[i];
    if (!token.startsWith("--")) {
      args._.push(token);
      continue;
    }
    const eq = token.indexOf("=");
    if (eq > 2) {
      args[token.slice(2, eq)] = token.slice(eq + 1);
      continue;
    }
    const key = token.slice(2);
    const next = argv[i + 1];
    if (BOOLEAN_FLAGS.has(key) || next === undefined || next.startsWith("--")) {
      args[key] = true;
    } else {
      args[key] = next;
      i++;
    }
  }
  return args;
}

function charCount(text) {
  return Array.from(text).length;
}

/** Extracts only VOICEHUE_API_KEY from a dotenv file inside cwd; ignores all other keys. */
function parseVoiceHueKeyFromDotenv(content) {
  for (const rawLine of content.replace(/\r\n/g, "\n").split("\n")) {
    const m = rawLine.match(/^\s*(?:export\s+)?VOICEHUE_API_KEY\s*=\s*(.+?)\s*$/);
    if (!m) continue;
    let val = m[1].trim();
    if (val.startsWith('"') || val.startsWith("'")) {
      const quote = val[0];
      const end = val.indexOf(quote, 1);
      if (end > 0) val = val.slice(1, end);
    } else {
      const commentIdx = val.search(/\s+#/);
      if (commentIdx !== -1) val = val.slice(0, commentIdx).trim();
    }
    if (val) return val;
  }
  return "";
}

/** Resolves VOICEHUE_API_KEY from process.env, falling back only to ./.env.local or ./.env inside cwd. */
export async function resolveApiKey(env, cwd) {
  const fromEnv = (env?.VOICEHUE_API_KEY || "").trim();
  if (fromEnv) return {key: fromEnv, source: "env"};
  if (cwd) {
    for (const file of [".env.local", ".env"]) {
      try {
        const candidate = resolveWorkspacePath(cwd, file);
        const content = await fs.readFile(candidate, "utf8");
        const found = parseVoiceHueKeyFromDotenv(content);
        if (found) return {key: found, source: file};
      } catch {
        // File does not exist or is unreadable; try next candidate
      }
    }
  }
  return {key: "", source: "none"};
}

async function requireKey(env, cwd) {
  const {key} = await resolveApiKey(env, cwd);
  if (!key) {
    throw new Error(
      "VOICEHUE_API_KEY is not set (checked environment, ./.env.local, and ./.env). Create a free API key at https://voicehue.com/dashboard/keys and export VOICEHUE_API_KEY before running this command."
    );
  }
  return key;
}

function resolveIdempotencyKey(raw) {
  if (typeof raw !== "string") return crypto.randomUUID();
  const key = raw.trim();
  if (!key || key.length > 120) {
    throw new Error("--idempotency-key must be a non-empty string of at most 120 characters.");
  }
  return key;
}

export function formatApiError(status, body) {
  const err = body && typeof body === "object" && body.error && typeof body.error === "object" ? body.error : {};
  const code = typeof err.code === "string" ? err.code : `http_${status}`;
  const msg = typeof err.message === "string" ? err.message : `Request failed with HTTP ${status}.`;
  const details = [];
  if (typeof err.operation_id === "string" && err.operation_id) details.push(`operation_id=${err.operation_id}`);
  if (typeof err.block === "number") details.push(`block=${err.block}`);
  if (typeof err.completed_blocks === "number") details.push(`completed_blocks=${err.completed_blocks}`);
  if (typeof err.limit === "number") details.push(`limit=${err.limit}`);
  if (typeof err.resets_at === "string" && err.resets_at) details.push(`resets_at=${err.resets_at}`);
  if (err.characters && typeof err.characters === "object") {
    const c = err.characters;
    if (typeof c.needed === "number" || typeof c.remaining === "number") {
      details.push(`characters(needed=${c.needed ?? "?"},remaining=${c.remaining ?? "?"})`);
    }
  }
  const hints = {
    invalid_api_key: "Verify VOICEHUE_API_KEY or generate a new key at https://voicehue.com/dashboard/keys.",
    insufficient_quota: "Run `usage` to inspect remaining daily/monthly characters and reset times.",
    voice_daily_limit:
      "This voice reached its per-voice daily cap. Switch to an uncapped standard voice (e.g. vh-mia, vh-ethan, vh-qinghe, vh-baichuan, vh-zhixia).",
    insufficient_credits:
      "Premium voices allow up to 200 chars/request on the daily free trial without credits. Choose a standard voice or shorten the text.",
    premium_trial_exhausted: "Today's free premium trial is used up. Choose a standard voice or wait until 00:00 UTC.",
    premium_daily_cap: "Today's premium daily cap (1/3 of monthly allowance) is reached; resets at 00:00 UTC. Standard voices are unaffected.",
    input_too_long: "Pass `--auto` on `speak` (or use `job`) for 5,001-20,000 characters, or split at paragraph boundaries.",
    too_many_blocks: "Free keys support up to 20 dialogue blocks (100 on pro). Merge adjacent turns or split into parts.",
    too_many_jobs: "Up to 5 open jobs are allowed per key. Wait for an existing job to finish before submitting another.",
    voice_not_found: "Run `voices` to fetch currently available voice IDs.",
    unsupported_format: "Retry with `--format mp3`.",
    duplicate_request: "This Idempotency-Key was already processed. Use a new key for a new request.",
    capacity_exhausted: "Today's provider capacity for this voice is full. Try another voice or wait until resets_at.",
    rate_limit_exceeded: "Wait a few seconds and retry with the same `--idempotency-key`.",
    rate_limited: "Wait a few seconds and retry.",
    concurrency_limit_exceeded: "Wait 1-2 seconds and retry with the same `--idempotency-key`.",
    price_confirmation_required: "Call Voice Studio `action: \"quote\"` first, then pass UUID `request_id` and `max_credits`.",
    voice_rights_confirmation_required: "Obtain explicit speaker/owner confirmation before setting `consent: true`."
  };
  const detailStr = details.length ? ` (${details.join(", ")})` : "";
  const hint = hints[code] ? ` Hint: ${hints[code]}` : "";
  return `VoiceHue API error [${code}] (HTTP ${status}): ${msg}${detailStr}${hint}`;
}

async function readJsonSafe(res) {
  const text = await res.text();
  try {
    return JSON.parse(text);
  } catch {
    return {error: {code: `http_${res.status}`, message: text.slice(0, 240) || `HTTP ${res.status}`}};
  }
}

const RETRYABLE_429_CODES = new Set(["rate_limit_exceeded", "rate_limited", "concurrency_limit_exceeded"]);

/** Fetch wrapper with request timeout and safe backoff retries on transient 5xx / RPM 429 (reusing Idempotency-Key). */
async function fetchWithRetry(fetchImpl, url, init, {timeoutMs, sleep, retries = MAX_RETRIES}) {
  let lastErr;
  for (let attempt = 0; attempt <= retries; attempt++) {
    const reqInit = {...init};
    if (typeof AbortSignal !== "undefined" && typeof AbortSignal.timeout === "function" && !reqInit.signal) {
      reqInit.signal = AbortSignal.timeout(timeoutMs);
    }
    try {
      const res = await fetchImpl(url, reqInit);
      if (res.ok || attempt === retries) return res;

      if (res.status === 502 || res.status === 503 || res.status === 504) {
        const retryAfter = Number(res.headers?.get?.("retry-after"));
        const delaySec = Number.isFinite(retryAfter) && retryAfter > 0 ? Math.min(15, retryAfter) : 2 * (attempt + 1);
        await sleep(delaySec * 1000);
        continue;
      }

      if (res.status === 429) {
        // Peek JSON body so we ONLY retry transient RPM/concurrency limits, never daily/monthly quota exhaustion.
        const body = await readJsonSafe(res);
        const code = body?.error?.code;
        if (RETRYABLE_429_CODES.has(code)) {
          const retryAfter = Number(res.headers?.get?.("retry-after"));
          const delaySec = Number.isFinite(retryAfter) && retryAfter > 0 ? Math.min(15, retryAfter) : 3 * (attempt + 1);
          await sleep(delaySec * 1000);
          continue;
        }
        // Return a synthetic Response carrying the already-parsed JSON body so caller reports exact error.
        return new Response(JSON.stringify(body), {status: res.status, headers: {"content-type": "application/json"}});
      }

      return res;
    } catch (err) {
      lastErr = err;
      // Never blindly retry a client-side request timeout (server may still be completing the original synthesis/mutation).
      if (err?.name === "TimeoutError" || err?.name === "AbortError") {
        throw new Error(
          `Request to ${url} timed out after ${Math.round(timeoutMs / 1000)}s. Do not blindly duplicate paid requests; check job/operation status or retry with the same Idempotency-Key.`
        );
      }
      if (attempt === retries) throw err;
      await sleep(2000 * (attempt + 1));
    }
  }
  throw lastErr || new Error("Network request failed.");
}

async function loadInputText(args, cwd) {
  let raw = "";
  let isMarkdownFile = false;
  if (typeof args.text === "string" && args.text.length > 0) {
    raw = args.text;
  } else if (typeof args["text-file"] === "string") {
    const filePath = resolveWorkspacePath(cwd, args["text-file"]);
    raw = await fs.readFile(filePath, "utf8");
    isMarkdownFile = /\.(?:md|mdx|markdown)$/i.test(filePath);
  } else {
    throw new Error("Provide either --text <string> or --text-file <workspace-path>.");
  }

  const shouldStrip = Boolean(args["strip-markdown"]) || (isMarkdownFile && !args.raw);
  const text = (shouldStrip ? stripMarkdownForSpeech(raw) : raw).trim();
  return {text, markdownStripped: shouldStrip};
}

async function loadOptionalPronunciations(args, cwd) {
  if (typeof args.pronunciations !== "string") return undefined;
  const filePath = resolveWorkspacePath(cwd, args.pronunciations);
  const parsed = JSON.parse(await fs.readFile(filePath, "utf8"));
  if (!Array.isArray(parsed)) {
    throw new Error("Pronunciations file must contain a JSON array of {\"from\",\"to\"} objects.");
  }
  return parsed;
}

async function writeAudioFile(cwd, outArg, bytes) {
  const dest = resolveWorkspacePath(cwd, outArg);
  await fs.mkdir(path.dirname(dest), {recursive: true});
  await fs.writeFile(dest, bytes);
  return dest;
}

async function cmdCheck(args, {cwd, env, fetchImpl, origin, stdout, sleep}) {
  const nodeVersion = process.version;
  const major = Number.parseInt(nodeVersion.replace(/^v/, "").split(".")[0], 10);
  const {key, source} = await resolveApiKey(env, cwd);

  let voicesCount = null;
  let apiReachable = false;
  try {
    const vRes = await fetchWithRetry(fetchImpl, `${origin}/v1/voices`, {method: "GET", headers: {Accept: "application/json"}}, {timeoutMs: FAST_TIMEOUT_MS, sleep, retries: 1});
    if (vRes.ok) {
      const payload = await vRes.json();
      voicesCount = Array.isArray(payload?.data) ? payload.data.length : 0;
      apiReachable = true;
    }
  } catch {
    apiReachable = false;
  }

  let usage = null;
  let authOk = false;
  let authError = null;
  if (key && apiReachable) {
    try {
      const uRes = await fetchWithRetry(
        fetchImpl,
        `${origin}/v1/usage`,
        {method: "GET", headers: {Authorization: `Bearer ${key}`, Accept: "application/json"}},
        {timeoutMs: FAST_TIMEOUT_MS, sleep, retries: 1}
      );
      if (uRes.ok) {
        usage = await uRes.json();
        authOk = true;
      } else {
        authError = formatApiError(uRes.status, await readJsonSafe(uRes));
      }
    } catch (err) {
      authError = err instanceof Error ? err.message : String(err);
    }
  }

  const report = {
    ok: major >= 18 && apiReachable && (!key || authOk),
    node: nodeVersion,
    api_reachable: apiReachable,
    voices_available: voicesCount,
    api_key_configured: Boolean(key),
    api_key_source: source,
    auth_ok: key ? authOk : null,
    ...(authError ? {auth_error: authError} : {}),
    ...(usage
      ? {
          plan: usage.key?.plan ?? "unknown",
          standard_daily_remaining: usage.standard?.daily?.remaining ?? null,
          standard_monthly_remaining: usage.standard?.monthly?.remaining ?? null,
          premium_remaining: usage.premium?.characters?.remaining ?? 0,
          premium_trial_remaining: usage.premium?.trial?.remaining ?? 0
        }
      : {})
  };

  if (args.json) {
    stdout.write(JSON.stringify(report, null, 2) + "\n");
    return;
  }
  const lines = [
    `Node.js:      ${nodeVersion} (${major >= 18 ? "ok" : "upgrade to 18+"})`,
    `VoiceHue API: ${apiReachable ? `reachable (${voicesCount} voices)` : "unreachable"}`,
    `API Key:      ${key ? `configured via ${source} (${authOk ? "valid" : "error: " + authError})` : "not set — create free at https://voicehue.com/dashboard/keys"}`
  ];
  if (usage) {
    const monthlyText =
      usage.standard?.monthly?.limit === null && usage.standard?.monthly?.remaining === null
        ? "unlimited"
        : `${usage.standard?.monthly?.remaining ?? "?"}/${usage.standard?.monthly?.limit ?? "?"}`;
    lines.push(
      `Plan & quota: ${usage.key?.plan ?? "unknown"} | daily ${usage.standard?.daily?.remaining ?? "?"}/${usage.standard?.daily?.limit ?? "?"} | monthly ${monthlyText} | premium trial ${usage.premium?.trial?.remaining ?? 0}/${usage.premium?.trial?.limit ?? 0}`
    );
  }
  stdout.write(lines.join("\n") + "\n");
}

async function cmdVoices(args, {fetchImpl, origin, stdout, sleep}) {
  const res = await fetchWithRetry(
    fetchImpl,
    `${origin}/v1/voices`,
    {method: "GET", headers: {Accept: "application/json"}},
    {timeoutMs: FAST_TIMEOUT_MS, sleep}
  );
  if (!res.ok) throw new Error(formatApiError(res.status, await readJsonSafe(res)));
  const payload = await res.json();
  const all = Array.isArray(payload?.data) ? payload.data : [];

  const lang = typeof args.language === "string" ? args.language : "";
  const tier = typeof args.tier === "string" ? args.tier.toLowerCase() : "";
  const gender = typeof args.gender === "string" ? args.gender.toLowerCase() : "";
  const tag = typeof args.tag === "string" ? args.tag.trim().toLowerCase() : "";
  const query = typeof args.query === "string" ? args.query.trim().toLowerCase() : "";
  const limit = Math.max(1, Math.min(200, Number.parseInt(String(args.limit || "30"), 10) || 30));

  let list = all.filter((v) => {
    if (lang && !languageMatches(v.language, lang)) return false;
    if (tier && String(v.tier || "").toLowerCase() !== tier) return false;
    if (gender && String(v.gender || "").toLowerCase() !== gender) return false;
    const tags = Array.isArray(v.tags) ? v.tags.map((t) => String(t).toLowerCase()) : [];
    if (tag && !tags.includes(tag)) return false;
    if (query) {
      const hay = [v.id, v.name, v.language, v.gender, v.tier, ...tags, v.description || "", v.description_zh || ""].join(" ").toLowerCase();
      if (!hay.includes(query)) return false;
    }
    return true;
  });

  // Sort standard voices ahead of premium voices so free-tier callers see usable voices first.
  list.sort((a, b) => Number(a.tier === "premium") - Number(b.tier === "premium"));
  const total = list.length;
  list = list.slice(0, limit);

  if (args.json) {
    stdout.write(JSON.stringify({total, shown: list.length, voices: list}, null, 2) + "\n");
    return;
  }
  stdout.write(`Found ${total} matching voice(s) (showing ${list.length}):\n`);
  for (const v of list) {
    const extras = [];
    if (v.tier === "premium" && v.char_rate !== undefined) extras.push(`char_rate=${v.char_rate}`);
    if (typeof v.daily_char_limit === "number" && v.daily_char_limit > 0) extras.push(`daily_cap=${v.daily_char_limit}`);
    if (Array.isArray(v.tags) && v.tags.length) extras.push(`tags=${v.tags.join(",")}`);
    const desc = v.description || v.description_zh || "";
    const meta = extras.length ? ` | ${extras.join(", ")}` : "";
    const note = desc ? ` — ${desc}` : "";
    stdout.write(`- ${v.id} | ${v.name} | ${v.language} | ${v.gender} | ${v.tier}${meta}${note}\n`);
  }
}

async function cmdUsage(args, {cwd, env, fetchImpl, origin, stdout, sleep}) {
  const key = await requireKey(env, cwd);
  const res = await fetchWithRetry(
    fetchImpl,
    `${origin}/v1/usage`,
    {method: "GET", headers: {Authorization: `Bearer ${key}`, Accept: "application/json"}},
    {timeoutMs: FAST_TIMEOUT_MS, sleep}
  );
  if (!res.ok) throw new Error(formatApiError(res.status, await readJsonSafe(res)));
  const u = await res.json();
  if (args.json) {
    stdout.write(JSON.stringify(u, null, 2) + "\n");
    return;
  }
  const day = u.standard?.daily || {};
  const month = u.standard?.monthly || {};
  const premChars = u.premium?.characters || {};
  const trial = u.premium?.trial || {};
  const monthlyLine =
    month.limit === null && month.remaining === null
      ? "Standard monthly: unlimited"
      : `Standard monthly: ${month.remaining ?? "?"} / ${month.limit ?? "?"} chars left`;
  stdout.write(
    [
      `Plan: ${u.key?.plan ?? "unknown"} (RPM: ${u.standard?.rpm ?? "?"})`,
      `Standard daily:   ${day.remaining ?? "?"} / ${day.limit ?? "?"} chars left (resets ${u.standard?.resets_at ?? "00:00 UTC"})`,
      monthlyLine,
      `Premium balance:  ${premChars.remaining ?? 0} chars left`,
      `Premium trial:    ${trial.remaining ?? 0} / ${trial.limit ?? 0} chars left today`
    ].join("\n") + "\n"
  );
}

async function cmdSpeak(args, ctx) {
  const {cwd, env, fetchImpl, origin, stdout, sleep} = ctx;
  const key = await requireKey(env, cwd);
  if (typeof args.voice !== "string" || !args.voice.trim()) {
    throw new Error("--voice <id> is required. Run `voices` first to pick an ID.");
  }
  if (typeof args.out !== "string" || !args.out.trim()) {
    throw new Error("--out <workspace-path> is required (for example: --out ./output/speech.mp3).");
  }
  resolveWorkspacePath(cwd, args.out);
  const {text, markdownStripped} = await loadInputText(args, cwd);
  const chars = charCount(text);
  if (!chars) throw new Error("Input text is empty.");
  if (chars > SYNC_MAX_CHARS) {
    if (args.auto) {
      if (chars > JOB_MAX_CHARS) {
        throw new Error(
          `Text is ${chars} characters (max single job limit is ${JOB_MAX_CHARS}). Split into chapters of at most ${JOB_MAX_CHARS} characters instead of truncating.`
        );
      }
      await cmdJob({...args, wait: true}, ctx);
      return;
    }
    throw new Error(
      `Text is ${chars} characters (sync limit is ${SYNC_MAX_CHARS}). Pass --auto (or use the "job" command) for up to ${JOB_MAX_CHARS} characters instead of truncating.`
    );
  }
  const format = args.format === "wav" ? "wav" : "mp3";
  const body = {model: DEFAULT_MODEL, input: text, voice: args.voice.trim(), response_format: format};
  if (args.speed !== undefined) {
    const speed = Number(args.speed);
    if (!Number.isFinite(speed) || speed < 0.5 || speed > 2) {
      throw new Error("--speed must be a number between 0.5 and 2.");
    }
    body.speed = speed;
  }
  const pronunciations = await loadOptionalPronunciations(args, cwd);
  if (pronunciations) body.pronunciations = pronunciations;

  const headers = {
    Authorization: `Bearer ${key}`,
    "Content-Type": "application/json",
    "Idempotency-Key": resolveIdempotencyKey(args["idempotency-key"])
  };

  const res = await fetchWithRetry(
    fetchImpl,
    `${origin}/v1/audio/speech`,
    {method: "POST", headers, body: JSON.stringify(body)},
    {timeoutMs: SPEECH_TIMEOUT_MS, sleep}
  );
  if (!res.ok) throw new Error(formatApiError(res.status, await readJsonSafe(res)));

  const bytes = new Uint8Array(await res.arrayBuffer());
  const dest = await writeAudioFile(cwd, args.out, bytes);
  const durationSeconds = estimateAudioDurationSeconds(bytes, format);
  const summary = {
    ok: true,
    file: path.relative(cwd, dest) || dest,
    voice: body.voice,
    characters: chars,
    duration_seconds: durationSeconds,
    format,
    speed: body.speed ?? 1,
    bytes: bytes.byteLength,
    markdown_stripped: markdownStripped,
    request_id: res.headers.get("x-voicehue-request-id") || null,
    pronunciations_count: pronunciations ? pronunciations.length : 0
  };
  stdout.write(JSON.stringify(summary, null, 2) + "\n");
}

async function cmdDialogue(args, {cwd, env, fetchImpl, origin, stdout, sleep}) {
  const key = await requireKey(env, cwd);
  if (typeof args.out !== "string" || !args.out.trim()) {
    throw new Error("--out <workspace-path> is required.");
  }
  resolveWorkspacePath(cwd, args.out);

  let raw = null;
  let blocks;
  if (typeof args["script-file"] === "string") {
    const scriptPath = resolveWorkspacePath(cwd, args["script-file"]);
    const scriptText = await fs.readFile(scriptPath, "utf8");
    const voiceMap = parseVoiceMapArg(args.voices);
    const defaultPause = Number.isFinite(Number(args["pause-ms"])) ? Math.max(0, Math.min(5000, Math.round(Number(args["pause-ms"])))) : 400;
    blocks = parseDialogueScript(scriptText, voiceMap, defaultPause);
  } else if (typeof args["blocks-file"] === "string") {
    const blocksPath = resolveWorkspacePath(cwd, args["blocks-file"]);
    raw = JSON.parse(await fs.readFile(blocksPath, "utf8"));
    const rawBlocks = Array.isArray(raw) ? raw : raw?.blocks;
    if (!Array.isArray(rawBlocks) || rawBlocks.length === 0) {
      throw new Error("Blocks file must be a JSON array of blocks or an object with a non-empty `blocks` array.");
    }
    // Accept `text` as a friendly alias for `input` so agents never trip over REST vs MCP field naming.
    blocks = rawBlocks.map((b) => {
      if (!b || typeof b !== "object") return b;
      if (typeof b.input === "string") return b;
      if (typeof b.text === "string") {
        const {text, ...rest} = b;
        return {...rest, input: text};
      }
      return b;
    });
  } else {
    throw new Error("Provide either --blocks-file <json-path> or --script-file <txt-path> with --voices.");
  }

  let totalChars = 0;
  for (const b of blocks) {
    if (typeof b?.input === "string") totalChars += charCount(b.input.trim());
  }
  if (totalChars === 0) throw new Error("Dialogue blocks contain no spoken text.");
  if (totalChars > SYNC_MAX_CHARS) {
    throw new Error(`Dialogue total is ${totalChars} characters (limit is ${SYNC_MAX_CHARS}). Split into multiple parts.`);
  }

  const format = args.format === "wav" || raw?.response_format === "wav" ? "wav" : "mp3";
  const body = {model: DEFAULT_MODEL, response_format: format, blocks};
  const pronunciations = (await loadOptionalPronunciations(args, cwd)) ?? (Array.isArray(raw?.pronunciations) ? raw.pronunciations : undefined);
  if (pronunciations) body.pronunciations = pronunciations;

  const headers = {
    Authorization: `Bearer ${key}`,
    "Content-Type": "application/json",
    "Idempotency-Key": resolveIdempotencyKey(args["idempotency-key"])
  };

  const res = await fetchWithRetry(
    fetchImpl,
    `${origin}/v1/audio/dialogue`,
    {method: "POST", headers, body: JSON.stringify(body)},
    {timeoutMs: DIALOGUE_TIMEOUT_MS, sleep}
  );
  if (!res.ok) throw new Error(formatApiError(res.status, await readJsonSafe(res)));

  const bytes = new Uint8Array(await res.arrayBuffer());
  const dest = await writeAudioFile(cwd, args.out, bytes);
  const headerDur = Number(res.headers.get("x-voicehue-duration"));
  const durationSeconds = Number.isFinite(headerDur) && headerDur > 0 ? headerDur : estimateAudioDurationSeconds(bytes, format);
  const summary = {
    ok: true,
    file: path.relative(cwd, dest) || dest,
    blocks: blocks.length,
    characters: totalChars,
    duration_seconds: durationSeconds,
    format,
    bytes: bytes.byteLength,
    request_id: res.headers.get("x-voicehue-request-id") || null
  };
  stdout.write(JSON.stringify(summary, null, 2) + "\n");
}

async function downloadJobAudio(job, args, {cwd, fetchImpl, origin, sleep}) {
  const url = job?.audio?.url;
  if (typeof url !== "string" || !url.startsWith("https://")) {
    throw new Error("Completed job does not carry an active audio download URL (file may have expired after 24 hours).");
  }
  // Enforce host allowlist: only download from VoiceHue origins (or the injected test origin).
  const parsed = new URL(url);
  const allowedOrigin = new URL(origin);
  const okHost =
    parsed.host === allowedOrigin.host ||
    parsed.hostname === "voicehue.com" ||
    parsed.hostname === "api.voicehue.com";
  if (!okHost) {
    throw new Error(`Refusing to download job audio from unexpected host: ${parsed.host}`);
  }
  const dl = await fetchWithRetry(fetchImpl, url, {method: "GET"}, {timeoutMs: SPEECH_TIMEOUT_MS, sleep});
  if (!dl.ok) throw new Error(`Failed to download completed job audio (HTTP ${dl.status}).`);
  const bytes = new Uint8Array(await dl.arrayBuffer());
  const dest = await writeAudioFile(cwd, args.out, bytes);
  const format = job?.response_format === "wav" ? "wav" : "mp3";
  return {
    file: path.relative(cwd, dest) || dest,
    bytes: bytes.byteLength,
    duration_seconds: estimateAudioDurationSeconds(bytes, format)
  };
}

async function cmdJob(args, {cwd, env, fetchImpl, origin, stdout, sleep}) {
  const key = await requireKey(env, cwd);
  if (typeof args.out === "string" && args.out.trim()) {
    resolveWorkspacePath(cwd, args.out);
  }
  let job;
  let markdownStripped = false;

  if (typeof args.id === "string" && args.id.trim()) {
    const res = await fetchWithRetry(
      fetchImpl,
      `${origin}/v1/audio/speech/jobs/${encodeURIComponent(args.id.trim())}`,
      {method: "GET", headers: {Authorization: `Bearer ${key}`, Accept: "application/json"}},
      {timeoutMs: FAST_TIMEOUT_MS, sleep}
    );
    if (!res.ok) throw new Error(formatApiError(res.status, await readJsonSafe(res)));
    job = await res.json();
  } else {
    if (typeof args.voice !== "string" || !args.voice.trim()) {
      throw new Error("Provide --id <job-uuid> to check an existing job, or --voice <id> with --text / --text-file to create one.");
    }
    const loaded = await loadInputText(args, cwd);
    const text = loaded.text;
    markdownStripped = loaded.markdownStripped;
    const chars = charCount(text);
    if (!chars) throw new Error("Input text is empty.");
    if (chars > JOB_MAX_CHARS) {
      throw new Error(`Text is ${chars} characters (job limit is ${JOB_MAX_CHARS}). Split into chapters of at most ${JOB_MAX_CHARS} characters.`);
    }
    const format = args.format === "wav" ? "wav" : "mp3";
    const body = {model: DEFAULT_MODEL, input: text, voice: args.voice.trim(), response_format: format};
    if (args.speed !== undefined) {
      const speed = Number(args.speed);
      if (!Number.isFinite(speed) || speed < 0.5 || speed > 2) throw new Error("--speed must be between 0.5 and 2.");
      body.speed = speed;
    }
    if (typeof args["callback-url"] === "string") body.callback_url = args["callback-url"];
    const pronunciations = await loadOptionalPronunciations(args, cwd);
    if (pronunciations) body.pronunciations = pronunciations;

    const res = await fetchWithRetry(
      fetchImpl,
      `${origin}/v1/audio/speech/jobs`,
      {
        method: "POST",
        headers: {
          Authorization: `Bearer ${key}`,
          "Content-Type": "application/json",
          "Idempotency-Key": resolveIdempotencyKey(args["idempotency-key"])
        },
        body: JSON.stringify(body)
      },
      {timeoutMs: FAST_TIMEOUT_MS, sleep}
    );
    if (!res.ok) throw new Error(formatApiError(res.status, await readJsonSafe(res)));
    job = await res.json();
  }

  if (args.wait && job && (job.status === "queued" || job.status === "processing")) {
    for (let attempt = 0; attempt < MAX_POLL_ATTEMPTS; attempt++) {
      await sleep(POLL_INTERVAL_MS);
      const pollRes = await fetchWithRetry(
        fetchImpl,
        `${origin}/v1/audio/speech/jobs/${encodeURIComponent(job.id)}`,
        {method: "GET", headers: {Authorization: `Bearer ${key}`, Accept: "application/json"}},
        {timeoutMs: FAST_TIMEOUT_MS, sleep}
      );
      if (!pollRes.ok) throw new Error(formatApiError(pollRes.status, await readJsonSafe(pollRes)));
      job = await pollRes.json();
      if (job.status === "completed" || job.status === "failed") break;
    }
  }

  if (job?.status === "failed") {
    throw new Error(formatApiError(500, {error: job.error || {code: "job_failed", message: "The long speech job failed."}}));
  }

  let saved = null;
  if (job?.status === "completed" && typeof args.out === "string" && args.out.trim()) {
    saved = await downloadJobAudio(job, args, {cwd, fetchImpl, origin, sleep});
  }
  const stillPending = Boolean(args.wait) && (job?.status === "queued" || job?.status === "processing");

  stdout.write(
    JSON.stringify(
      {
        ok: true,
        job_id: job?.id ?? null,
        status: job?.status ?? null,
        voice: job?.voice ?? null,
        characters: job?.characters ?? null,
        format: job?.response_format ?? "mp3",
        ...(markdownStripped ? {markdown_stripped: true} : {}),
        ...(saved ? {file: saved.file, bytes: saved.bytes, duration_seconds: saved.duration_seconds} : {}),
        ...(stillPending
          ? {
              note: `Job is still ${job.status} after polling. Resume later with: job --id ${job.id}${args.out ? ` --out ${args.out}` : ""} --wait`
            }
          : {}),
        expires_at: job?.expires_at ?? null
      },
      null,
      2
    ) + "\n"
  );
}

async function cmdStudio(args, {cwd, env, fetchImpl, origin, stdout, sleep}) {
  const key = await requireKey(env, cwd);
  if (typeof args["payload-file"] !== "string") {
    throw new Error("--payload-file <json-path> is required for `studio`.");
  }
  const filePath = resolveWorkspacePath(cwd, args["payload-file"]);
  const body = JSON.parse(await fs.readFile(filePath, "utf8"));
  if (!body || typeof body !== "object" || typeof body.action !== "string") {
    throw new Error("Voice Studio payload must be a JSON object with an `action` field.");
  }
  const res = await fetchWithRetry(
    fetchImpl,
    `${origin}/v1/voice-studio`,
    {
      method: "POST",
      headers: {Authorization: `Bearer ${key}`, "Content-Type": "application/json"},
      body: JSON.stringify(body)
    },
    {timeoutMs: STUDIO_TIMEOUT_MS, sleep, retries: 0} // Never auto-retry paid studio mutations blindly; use action: "operation"
  );
  const data = await readJsonSafe(res);
  if (!res.ok) throw new Error(formatApiError(res.status, data));
  stdout.write(JSON.stringify(data, null, 2) + "\n");
}

export async function runCli(argv, options = {}) {
  const cwd = options.cwd ?? process.cwd();
  const env = options.env ?? process.env;
  const fetchImpl = options.fetchImpl ?? globalThis.fetch;
  const origin = options.origin ?? DEFAULT_ORIGIN;
  const stdout = options.stdout ?? process.stdout;
  const sleep = options.sleep ?? ((ms) => new Promise((r) => setTimeout(r, ms)));

  const args = parseArgs(argv);
  const cmd = args._[0];
  if (!cmd || args.help || cmd === "help") {
    stdout.write(HELP);
    return 0;
  }

  const ctx = {cwd, env, fetchImpl, origin, stdout, sleep};
  switch (cmd) {
    case "check":
      await cmdCheck(args, ctx);
      return 0;
    case "voices":
      await cmdVoices(args, ctx);
      return 0;
    case "usage":
      await cmdUsage(args, ctx);
      return 0;
    case "speak":
      await cmdSpeak(args, ctx);
      return 0;
    case "dialogue":
      await cmdDialogue(args, ctx);
      return 0;
    case "job":
      await cmdJob(args, ctx);
      return 0;
    case "studio":
      await cmdStudio(args, ctx);
      return 0;
    default:
      throw new Error(`Unknown command "${cmd}". Run with --help to see available commands.`);
  }
}

function isMainModule() {
  if (!process.argv[1]) return false;
  try {
    return realpathSync(process.argv[1]) === realpathSync(fileURLToPath(import.meta.url));
  } catch {
    return path.resolve(process.argv[1]) === fileURLToPath(import.meta.url);
  }
}

if (isMainModule()) {
  runCli(process.argv.slice(2)).catch((err) => {
    process.stderr.write((err instanceof Error ? err.message : String(err)) + "\n");
    process.exitCode = 1;
  });
}
