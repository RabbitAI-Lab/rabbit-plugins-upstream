// Shared Skillry API media adapter with FAL/Codex-friendly provider resolution.
// Zero external npm dependencies; pure Node built-ins (ESM).
import { createHash, randomUUID } from 'node:crypto';
import { spawnSync } from 'node:child_process';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';

export const ROUTERBASE_GPT_IMAGE_SIZES = [
  '1024x1024',
  '1024x1536',
  '1536x1024',
  '1024x2048',
  '2048x1024',
  '688x2048',
  '2048x688',
  '880x2048',
  '2048x880',
  '1152x2048',
  '2048x1152',
  '1360x2048',
  '2048x1360',
  '1536x2048',
  '2048x1536',
  '2048x2048',
  '2160x3840',
  '3840x2160',
];

const ROUTERBASE_PARSED_SIZES = ROUTERBASE_GPT_IMAGE_SIZES.map((label) => {
  const [w, h] = label.split('x').map(Number);
  return { label, w, h, ratio: w / h, area: w * h };
});

const PRESET_TO_ROUTERBASE = new Map([
  ['auto', '2048x1152'],
  ['landscape_16_9', '2048x1152'],
  ['portrait_16_9', '1152x2048'],
  ['landscape_4_3', '2048x1536'],
  ['portrait_4_3', '1536x2048'],
  ['square_hd', '1024x1024'],
  ['square', '1024x1024'],
  ['landscape_3_2', '1536x1024'],
  ['portrait_3_2', '1024x1536'],
]);

const MIME_BY_FORMAT = {
  png: 'image/png',
  jpeg: 'image/jpeg',
  jpg: 'image/jpeg',
  webp: 'image/webp',
};

const FORMAT_BY_MIME = {
  'image/png': 'png',
  'image/jpeg': 'jpeg',
  'image/jpg': 'jpeg',
  'image/webp': 'webp',
};

const PRIVATE_HOST_PATTERNS = [
  /^localhost$/i,
  /\.localhost$/i,
  /\.local$/i,
  /\.internal$/i,
  /^127\./,
  /^10\./,
  /^192\.168\./,
  /^169\.254\./,
  /^172\.(1[6-9]|2\d|3[01])\./,
  /^\[?::1\]?$/,
];

const UUID_PATTERN = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;
const NANOS_PER_CREDIT = 15_000_000;

export function getBaseUrl() {
  return String(
    process.env.SKILLRY_BASE_URL ||
      process.env.SKILLRY_API_BASE_URL ||
      process.env.SKILLRY_URL ||
      'https://skillry.dev'
  )
    .trim()
    .replace(/\/+$/, '');
}

export function getSkillryApiKey() {
  return String(process.env.SKILLRY_API_KEY || '').trim();
}

export function isCodexClient() {
  return Boolean(process.env.CODEX_THREAD_ID || process.env.CODEX_SESSION_ID);
}

function splitCommandTokens(raw) {
  const tokens = [];
  const re = /"([^"]*)"|'([^']*)'|(\S+)/g;
  let m;
  while ((m = re.exec(raw)) !== null) {
    tokens.push(m[1] ?? m[2] ?? m[3]);
  }
  return tokens;
}

let cachedCliLookup = null;
export function findSkillryCli() {
  const override = String(process.env.SKILLRY_CLI_BIN || '').trim();
  if (override) {
    const tokens = splitCommandTokens(override);
    if (tokens.length > 0) {
      return { bin: tokens[0], prefixArgs: tokens.slice(1) };
    }
  }
  if (cachedCliLookup && cachedCliLookup.key === (process.env.PATH || '')) {
    return cachedCliLookup.value;
  }
  const probe = spawnSync('skillry', ['--version'], {
    stdio: 'ignore',
    timeout: 4000,
  });
  const value = probe.status === 0 ? { bin: 'skillry', prefixArgs: [] } : null;
  cachedCliLookup = { key: process.env.PATH || '', value };
  return value;
}

export function hasSkillryAuth() {
  return Boolean(getSkillryApiKey() || findSkillryCli());
}

export function normalizeBudgetPoints(value) {
  const num = Number(value);
  if (!Number.isFinite(num) || num <= 0 || num > 1_000_000) {
    throw new Error(`Invalid Skillry budget points: ${value}`);
  }
  if (Math.round(num * NANOS_PER_CREDIT) / NANOS_PER_CREDIT === num) {
    return num;
  }
  const rounded = Number(num.toFixed(7));
  if (!Number.isFinite(rounded) || rounded <= 0) {
    throw new Error(`Invalid Skillry budget points after rounding: ${value}`);
  }
  return rounded;
}

export function formatQuoteDisplay(quote) {
  const points = Number(quote?.points);
  const priceKind = String(quote?.price_kind || quote?.priceKind || 'fixed');
  if (priceKind === 'usage_cap') {
    return {
      kind: 'usage_cap',
      maxPoints: points,
      userMessage: `up to ${points} credits (the approved ceiling can be charged if supplier usage is unavailable)`,
    };
  }
  return {
    kind: 'estimate',
    estimatedPoints: points,
    userMessage: `estimated ${points} credits`,
  };
}

export function resolveProvider(requested, opts = {}) {
  const {
    allowCodex = false,
    allowElevenLabs = false,
    allowHeygen = false,
    allowHost = false,
  } = opts;
  const allowed = new Set(['skillry', 'fal']);
  if (allowCodex) allowed.add('codex');
  if (allowHost) allowed.add('host');
  if (allowElevenLabs) allowed.add('elevenlabs');
  if (allowHeygen) allowed.add('heygen');

  const raw = requested ? String(requested).trim().toLowerCase() : 'auto';
  if (raw && raw !== 'auto') {
    if (!allowed.has(raw)) {
      throw new Error(
        `Unsupported --provider "${requested}". Allowed values: ${[...allowed].join(', ')}.`
      );
    }
    return raw;
  }

  if (allowCodex && isCodexClient()) {
    return allowHost ? 'host' : 'codex';
  }
  if (hasSkillryAuth()) {
    return 'skillry';
  }
  if (String(process.env.FAL_KEY || '').trim()) {
    return 'fal';
  }
  if (
    allowElevenLabs &&
    String(process.env.ELEVENLABS_API_KEY || process.env.XI_API_KEY || '').trim()
  ) {
    return 'elevenlabs';
  }
  if (allowHeygen && String(process.env.HEYGEN_API_KEY || '').trim()) {
    return 'heygen';
  }
  return 'skillry';
}

export function normalizeQuality(q) {
  const val = String(q || '')
    .trim()
    .toLowerCase();
  if (val === 'low' || val === 'medium' || val === 'high') return val;
  return 'medium';
}

export function normalizeImageSize(inputSize, model = 'gpt-image-2') {
  if (!inputSize || inputSize === 'auto') {
    return { apiSize: '2048x1152', targetWidth: null, targetHeight: null };
  }
  if (typeof inputSize === 'string') {
    const preset = PRESET_TO_ROUTERBASE.get(inputSize);
    if (preset) {
      return { apiSize: preset, targetWidth: null, targetHeight: null };
    }
    const aspectMatch = /^(\d+):(\d+)$/.exec(inputSize.trim());
    if (aspectMatch) {
      const aw = Number(aspectMatch[1]);
      const ah = Number(aspectMatch[2]);
      return pickClosestRouterbaseSize(aw / ah, 0, 0, model, false);
    }
    const dimMatch = /^(\d+)\s*[xX]\s*(\d+)$/.exec(inputSize.trim());
    if (dimMatch) {
      const w = Number(dimMatch[1]);
      const h = Number(dimMatch[2]);
      return normalizeExplicitDims(w, h, model);
    }
  } else if (
    typeof inputSize === 'object' &&
    Number.isInteger(inputSize.width) &&
    Number.isInteger(inputSize.height)
  ) {
    return normalizeExplicitDims(inputSize.width, inputSize.height, model);
  }
  throw new Error(`Unsupported image size specification: ${JSON.stringify(inputSize)}`);
}

function normalizeExplicitDims(w, h, model) {
  const exact = `${w}x${h}`;
  if (ROUTERBASE_GPT_IMAGE_SIZES.includes(exact)) {
    return { apiSize: exact, targetWidth: null, targetHeight: null };
  }
  if (w === 2560 && h === 1440 && model === 'gpt-image-2') {
    return { apiSize: '2048x1152', targetWidth: 2560, targetHeight: 1440 };
  }
  return pickClosestRouterbaseSize(w / h, w, h, model, true);
}

function pickClosestRouterbaseSize(targetRatio, w, h, model, setTarget) {
  const sorted = [...ROUTERBASE_PARSED_SIZES].sort(
    (a, b) => Math.abs(a.ratio - targetRatio) - Math.abs(b.ratio - targetRatio)
  );
  const bestDiff = Math.abs(sorted[0].ratio - targetRatio);
  const aspectGroup = sorted.filter(
    (item) => Math.abs(item.ratio - targetRatio) <= bestDiff + 0.02
  );
  let chosen;
  if (w > 0 && h > 0) {
    const covering = aspectGroup.filter((item) => item.w >= w && item.h >= h);
    if (covering.length > 0) {
      covering.sort((a, b) => a.area - b.area);
      chosen = covering[0];
    } else {
      aspectGroup.sort((a, b) => b.area - a.area);
      chosen = aspectGroup[0];
    }
  } else {
    aspectGroup.sort((a, b) => a.area - b.area);
    chosen = aspectGroup[Math.min(1, aspectGroup.length - 1)] || aspectGroup[0];
  }
  if (w === 2560 && h === 1440 && model === 'gpt-image-2.5-flare') {
    return { apiSize: '3840x2160', targetWidth: 2560, targetHeight: 1440 };
  }
  return {
    apiSize: chosen.label,
    targetWidth: setTarget ? w : null,
    targetHeight: setTarget ? h : null,
  };
}

export function inspectImageFormat(bytes) {
  if (!Buffer.isBuffer(bytes)) bytes = Buffer.from(bytes);
  if (
    bytes.length >= 8 &&
    bytes[0] === 0x89 &&
    bytes[1] === 0x50 &&
    bytes[2] === 0x4e &&
    bytes[3] === 0x47 &&
    bytes[4] === 0x0d &&
    bytes[5] === 0x0a &&
    bytes[6] === 0x1a &&
    bytes[7] === 0x0a
  ) {
    return 'png';
  }
  if (bytes.length >= 3 && bytes[0] === 0xff && bytes[1] === 0xd8 && bytes[2] === 0xff) {
    return 'jpeg';
  }
  if (
    bytes.length >= 12 &&
    bytes.subarray(0, 4).toString('ascii') === 'RIFF' &&
    bytes.subarray(8, 12).toString('ascii') === 'WEBP'
  ) {
    return 'webp';
  }
  return null;
}

export function inspectImageDimensions(bytes) {
  const fmt = inspectImageFormat(bytes);
  if (fmt === 'png' && bytes.length >= 24) {
    return {
      format: 'png',
      width: bytes.readUInt32BE(16),
      height: bytes.readUInt32BE(20),
    };
  }
  if (fmt === 'jpeg') {
    let i = 2;
    while (i + 9 < bytes.length) {
      if (bytes[i] !== 0xff) break;
      const marker = bytes[i + 1];
      if (marker === 0xd8 || marker === 0xd9) {
        i += 2;
        continue;
      }
      const len = bytes.readUInt16BE(i + 2);
      if (
        (marker >= 0xc0 && marker <= 0xc3) ||
        (marker >= 0xc5 && marker <= 0xc7) ||
        (marker >= 0xc9 && marker <= 0xcb) ||
        (marker >= 0xcd && marker <= 0xcf)
      ) {
        return {
          format: 'jpeg',
          height: bytes.readUInt16BE(i + 5),
          width: bytes.readUInt16BE(i + 7),
        };
      }
      i += 2 + len;
    }
  }
  if (fmt === 'webp' && bytes.length >= 30) {
    const chunk = bytes.subarray(12, 16).toString('ascii');
    if (chunk === 'VP8X' && bytes.length >= 30) {
      const w = 1 + (bytes[24] | (bytes[25] << 8) | (bytes[26] << 16));
      const h = 1 + (bytes[27] | (bytes[28] << 8) | (bytes[29] << 16));
      return { format: 'webp', width: w, height: h };
    }
    if (chunk === 'VP8 ' && bytes.length >= 30) {
      return {
        format: 'webp',
        width: bytes.readUInt16LE(26) & 0x3fff,
        height: bytes.readUInt16LE(28) & 0x3fff,
      };
    }
    if (chunk === 'VP8L' && bytes.length >= 25) {
      const bits = bytes.readUInt32LE(21);
      return {
        format: 'webp',
        width: (bits & 0x3fff) + 1,
        height: ((bits >> 14) & 0x3fff) + 1,
      };
    }
  }
  return { format: fmt, width: null, height: null };
}

export function convertOrResizeImage(bytes, { targetFormat, targetWidth, targetHeight } = {}) {
  const buf = Buffer.isBuffer(bytes) ? bytes : Buffer.from(bytes);
  const desiredFmt = targetFormat === 'jpg' ? 'jpeg' : targetFormat || null;
  const info = inspectImageDimensions(buf);
  const srcFmt = info.format;
  const needsResize =
    Boolean(targetWidth && targetHeight) &&
    (info.width !== targetWidth || info.height !== targetHeight);
  const needsConvert = Boolean(desiredFmt && srcFmt !== desiredFmt);
  if (!needsResize && !needsConvert) {
    return buf;
  }

  const outFmt = desiredFmt || srcFmt || 'png';
  const tmpDir = fs.mkdtempSync(path.join(os.tmpdir(), 'skillry-img-'));
  try {
    const inExt = srcFmt === 'jpeg' ? 'jpg' : srcFmt || 'png';
    const outExt = outFmt === 'jpeg' ? 'jpg' : outFmt;
    const inFile = path.join(tmpDir, `in.${inExt}`);
    const outFile = path.join(tmpDir, `out.${outExt}`);
    fs.writeFileSync(inFile, buf);

    const vf =
      targetWidth && targetHeight
        ? `scale=${targetWidth}:${targetHeight}:force_original_aspect_ratio=increase:flags=lanczos,crop=${targetWidth}:${targetHeight}`
        : null;

    const ffArgs = ['-v', 'error', '-y', '-i', inFile];
    if (vf) ffArgs.push('-vf', vf);
    if (outFmt === 'webp') ffArgs.push('-c:v', 'libwebp', '-quality', '90');
    else if (outFmt === 'jpeg') ffArgs.push('-q:v', '2');
    ffArgs.push(outFile);

    const ff = spawnSync('ffmpeg', ffArgs, { encoding: 'utf8', timeout: 60000 });
    if (ff.status === 0 && fs.existsSync(outFile)) {
      const result = fs.readFileSync(outFile);
      const actual = inspectImageFormat(result);
      if (!desiredFmt || actual === outFmt) return result;
    }

    if (outFmt === 'webp') {
      const intermediatePng = path.join(tmpDir, 'mid.png');
      let sourceForWebp = inFile;
      if (vf || (srcFmt !== 'png' && srcFmt !== 'jpeg')) {
        const ffPng = spawnSync(
          'ffmpeg',
          ['-v', 'error', '-y', '-i', inFile, ...(vf ? ['-vf', vf] : []), intermediatePng],
          { encoding: 'utf8', timeout: 60000 }
        );
        if (ffPng.status === 0 && fs.existsSync(intermediatePng)) {
          sourceForWebp = intermediatePng;
        }
      }
      const cw = spawnSync('cwebp', ['-quiet', '-q', '90', sourceForWebp, '-o', outFile], {
        encoding: 'utf8',
        timeout: 60000,
      });
      if (cw.status === 0 && fs.existsSync(outFile)) {
        return fs.readFileSync(outFile);
      }
    }

    const pyScript = [
      'import sys',
      'from PIL import Image, ImageOps',
      'src, dst, fmt, w, h = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]), int(sys.argv[5])',
      'im = Image.open(src)',
      'if w > 0 and h > 0: im = ImageOps.fit(im, (w, h), method=Image.Resampling.LANCZOS)',
      'if fmt == "jpeg" and im.mode in ("RGBA", "P", "LA"): im = im.convert("RGB")',
      'save_fmt = "JPEG" if fmt == "jpeg" else fmt.upper()',
      'im.save(dst, save_fmt, quality=90)',
    ].join('\n');
    const py = spawnSync(
      'python3',
      ['-c', pyScript, inFile, outFile, outFmt, String(targetWidth || 0), String(targetHeight || 0)],
      { encoding: 'utf8', timeout: 60000 }
    );
    if (py.status === 0 && fs.existsSync(outFile)) {
      return fs.readFileSync(outFile);
    }

    if (!vf && outFmt !== 'webp' && process.platform === 'darwin') {
      const sipsFmt = outFmt === 'jpeg' ? 'jpeg' : 'png';
      const sp = spawnSync('sips', ['-s', 'format', sipsFmt, inFile, '--out', outFile], {
        encoding: 'utf8',
        timeout: 60000,
      });
      if (sp.status === 0 && fs.existsSync(outFile)) {
        return fs.readFileSync(outFile);
      }
    }

    throw new Error(
      `Failed to convert or resize image to ${outFmt}${vf ? ` (${targetWidth}x${targetHeight})` : ''}. Install ffmpeg or Pillow.`
    );
  } finally {
    fs.rmSync(tmpDir, { recursive: true, force: true });
  }
}

function assertSafeExternalUrl(rawUrl) {
  const url = new URL(rawUrl);
  if (url.protocol !== 'https:' || url.username || url.password) {
    throw new Error(`External media URL must use credential-free HTTPS: ${rawUrl}`);
  }
  const host = url.hostname.toLowerCase();
  if (PRIVATE_HOST_PATTERNS.some((p) => p.test(host))) {
    throw new Error(`Refusing private or loopback URL: ${url.hostname}`);
  }
  return url;
}

async function resolveReferenceBytes(ref, maxEdge) {
  let buf;
  let mime;
  if (Buffer.isBuffer(ref)) {
    buf = ref;
  } else if (typeof ref === 'string') {
    const trimmed = ref.trim();
    const dataMatch = /^data:(image\/(?:png|jpeg|jpg|webp));base64,(.+)$/is.exec(trimmed);
    if (dataMatch) {
      mime = dataMatch[1].toLowerCase() === 'image/jpg' ? 'image/jpeg' : dataMatch[1].toLowerCase();
      buf = Buffer.from(dataMatch[2], 'base64');
    } else if (/^https?:\/\//i.test(trimmed)) {
      const safeUrl = assertSafeExternalUrl(trimmed);
      const res = await fetch(safeUrl, { signal: AbortSignal.timeout(60000) });
      if (!res.ok) {
        throw new Error(`Reference URL download failed (${res.status}): ${safeUrl.origin}`);
      }
      buf = Buffer.from(await res.arrayBuffer());
      const ct = String(res.headers.get('content-type') || '').split(';')[0].trim().toLowerCase();
      mime = ct === 'image/jpg' ? 'image/jpeg' : ct;
    } else {
      const absPath = path.resolve(trimmed);
      buf = fs.readFileSync(absPath);
    }
  } else {
    throw new Error('Reference input must be a file path, data URI, HTTPS URL, or Buffer.');
  }

  let dims = inspectImageDimensions(buf);
  let fmt = dims.format || FORMAT_BY_MIME[mime] || null;
  if (!fmt) {
    throw new Error('Unsupported reference image format; expected PNG, JPEG, or WebP.');
  }
  mime = MIME_BY_FORMAT[fmt];

  if (maxEdge && dims.width && dims.height && Math.max(dims.width, dims.height) > maxEdge) {
    const scale = maxEdge / Math.max(dims.width, dims.height);
    const nw = Math.max(16, Math.round(dims.width * scale));
    const nh = Math.max(16, Math.round(dims.height * scale));
    buf = convertOrResizeImage(buf, { targetFormat: fmt, targetWidth: nw, targetHeight: nh });
    dims = inspectImageDimensions(buf);
  } else if (maxEdge && (!dims.width || !dims.height)) {
    const tmpDir = fs.mkdtempSync(path.join(os.tmpdir(), 'skillry-ref-'));
    try {
      const ext = fmt === 'jpeg' ? 'jpg' : fmt;
      const srcFile = path.join(tmpDir, `ref.${ext}`);
      const dstFile = path.join(tmpDir, 'scaled.png');
      fs.writeFileSync(srcFile, buf);
      const ff = spawnSync(
        'ffmpeg',
        [
          '-v',
          'error',
          '-y',
          '-i',
          srcFile,
          '-vf',
          `scale='min(${maxEdge},iw)':'min(${maxEdge},ih)':force_original_aspect_ratio=decrease`,
          dstFile,
        ],
        { timeout: 60000 }
      );
      if (ff.status === 0 && fs.existsSync(dstFile)) {
        buf = fs.readFileSync(dstFile);
        mime = 'image/png';
        fmt = 'png';
      }
    } finally {
      fs.rmSync(tmpDir, { recursive: true, force: true });
    }
  }

  if (buf.length > 20 * 1024 * 1024) {
    buf = convertOrResizeImage(buf, {
      targetFormat: 'jpeg',
      targetWidth: dims.width && maxEdge ? Math.min(dims.width, maxEdge) : undefined,
      targetHeight: dims.height && maxEdge ? Math.min(dims.height, maxEdge) : undefined,
    });
    mime = 'image/jpeg';
    fmt = 'jpeg';
  }

  return { bytes: buf, mime, format: fmt };
}

async function apiRequest(baseUrl, apiKey, endpoint, init = {}) {
  const headers = new Headers(init.headers || {});
  headers.set('Authorization', `Bearer ${apiKey}`);
  const res = await fetch(`${baseUrl}${endpoint}`, {
    ...init,
    headers,
    signal: init.signal || AbortSignal.timeout(120000),
  });
  const text = await res.text();
  let data = null;
  try {
    data = text ? JSON.parse(text) : {};
  } catch {
    data = { raw: text };
  }
  if (!res.ok) {
    const errObj = typeof data?.error === 'object' && data.error ? data.error : null;
    const code =
      (typeof data?.error === 'string' && data.error) ||
      errObj?.code ||
      `http_${res.status}`;
    const detail =
      errObj?.message || data?.message || (typeof text === 'string' ? text.slice(0, 300) : '');
    const err = new Error(
      `Skillry API ${endpoint} failed (${res.status} ${code})${detail ? `: ${detail}` : ''}`
    );
    err.status = res.status;
    err.code = code;
    throw err;
  }
  return data;
}

function buildMediaPayload(spec, refIds) {
  const payload = { model: spec.model };
  if (spec.prompt) payload.prompt = String(spec.prompt).trim();
  if (spec.text !== undefined) payload.text = String(spec.text);
  if (spec.size) payload.size = spec.size;
  if (spec.quality) payload.quality = spec.quality;
  if (spec.resolution) payload.resolution = spec.resolution;
  if (spec.aspectRatio || spec.aspect_ratio) {
    payload.aspect_ratio = spec.aspectRatio || spec.aspect_ratio;
  }
  if (spec.duration !== undefined) payload.duration = Number(spec.duration);
  if (spec.voiceId || spec.voice_id) payload.voice_id = spec.voiceId || spec.voice_id;
  if (spec.languageCode || spec.language_code) {
    payload.language_code = spec.languageCode || spec.language_code;
  }
  // FAL eleven-v4 rejects speed !== 1, so only include speed when explicitly requested on another model.
  if (spec.speed !== undefined && spec.model !== 'eleven-v4') {
    payload.speed = Number(spec.speed);
  }
  if (spec.stability !== undefined) payload.stability = Number(spec.stability);
  if (spec.similarityBoost !== undefined || spec.similarity_boost !== undefined) {
    payload.similarity_boost = Number(spec.similarityBoost ?? spec.similarity_boost);
  }
  if (spec.promptInfluence !== undefined || spec.prompt_influence !== undefined) {
    payload.prompt_influence = Number(spec.promptInfluence ?? spec.prompt_influence);
  }
  if (spec.loop !== undefined) {
    payload.loop = Boolean(spec.loop);
  }
  if (spec.generateAudio !== undefined || spec.generate_audio !== undefined) {
    payload.generate_audio = Boolean(spec.generateAudio ?? spec.generate_audio);
  }
  if (refIds.length === 1) payload.reference_id = refIds[0];
  else if (refIds.length > 1) payload.reference_ids = refIds;
  return payload;
}

async function uploadHttpReferences(baseUrl, apiKey, refs, maxEdge) {
  const refIds = [];
  for (const ref of refs) {
    if (typeof ref === 'string' && UUID_PATTERN.test(ref.trim())) {
      refIds.push(ref.trim());
      continue;
    }
    const prepared = await resolveReferenceBytes(ref, maxEdge);
    const uploaded = await apiRequest(baseUrl, apiKey, '/api/cli/image-references', {
      method: 'POST',
      headers: { 'Content-Type': prepared.mime },
      body: prepared.bytes,
    });
    refIds.push(uploaded.id);
  }
  return refIds;
}

function appendCliMediaFlags(cliArgs, spec, tmpDir) {
  if (spec.prompt) {
    const pf = path.join(tmpDir, 'prompt.txt');
    fs.writeFileSync(pf, String(spec.prompt).trim(), 'utf8');
    cliArgs.push('--prompt-file', pf);
  }
  if (spec.text !== undefined) {
    const tf = path.join(tmpDir, 'text.txt');
    fs.writeFileSync(tf, String(spec.text), 'utf8');
    cliArgs.push('--text-file', tf);
  }
  if (spec.size) cliArgs.push('--size', String(spec.size));
  if (spec.quality) cliArgs.push('--quality', String(spec.quality));
  if (spec.resolution) cliArgs.push('--resolution', String(spec.resolution));
  if (spec.aspectRatio || spec.aspect_ratio) {
    cliArgs.push('--aspect-ratio', String(spec.aspectRatio || spec.aspect_ratio));
  }
  if (spec.duration !== undefined) cliArgs.push('--duration', String(spec.duration));
  if (spec.voiceId || spec.voice_id) cliArgs.push('--voice-id', String(spec.voiceId || spec.voice_id));
  if (spec.languageCode || spec.language_code) {
    cliArgs.push('--language-code', String(spec.languageCode || spec.language_code));
  }
  if (spec.speed !== undefined && spec.model !== 'eleven-v4') {
    cliArgs.push('--speed', String(spec.speed));
  }
  if (spec.stability !== undefined) cliArgs.push('--stability', String(spec.stability));
  if (spec.similarityBoost !== undefined || spec.similarity_boost !== undefined) {
    cliArgs.push('--similarity-boost', String(spec.similarityBoost ?? spec.similarity_boost));
  }
  if (spec.promptInfluence !== undefined || spec.prompt_influence !== undefined) {
    cliArgs.push('--prompt-influence', String(spec.promptInfluence ?? spec.prompt_influence));
  }
  if (spec.loop !== undefined) cliArgs.push('--loop', String(Boolean(spec.loop)));
  if (spec.generateAudio !== undefined || spec.generate_audio !== undefined) {
    cliArgs.push('--generate-audio', String(Boolean(spec.generateAudio ?? spec.generate_audio)));
  }
  if (spec.skillSlug) {
    cliArgs.push('--skill', String(spec.skillSlug));
  }
}

async function appendCliReferences(cliArgs, refs, maxEdge, tmpDir) {
  for (let i = 0; i < refs.length; i += 1) {
    const prepared = await resolveReferenceBytes(refs[i], maxEdge);
    const ext = prepared.format === 'jpeg' ? 'jpg' : prepared.format;
    const rf = path.join(tmpDir, `ref-${i + 1}.${ext}`);
    fs.writeFileSync(rf, prepared.bytes);
    cliArgs.push('--reference', rf);
  }
}

function defaultCachePath(requestId, model) {
  const dir = path.join(os.tmpdir(), 'skillry-cli-cache');
  fs.mkdirSync(dir, { recursive: true });
  const ext =
    model?.startsWith('seedance') || model === 'minimax-h3'
      ? 'mp4'
      : model?.startsWith('eleven') || model?.startsWith('heygen')
        ? 'mp3'
        : 'bin';
  return path.join(dir, `${requestId}.${ext}`);
}

/**
 * Request a free, read-only Skillry media quote before asking the user to approve spending.
 * Never creates a run or submits a paid task.
 */
export async function skillryQuote(spec) {
  if (!spec?.model) throw new Error('skillryQuote requires model.');
  const baseUrl = getBaseUrl();
  const apiKey = getSkillryApiKey();
  const refs = spec.references || spec.referenceFiles || [];
  const maxEdge = 4096;
  const runId = spec.runId || String(process.env.SKILLRY_RUN_ID || '').trim() || null;

  if (apiKey) {
    const refIds = await uploadHttpReferences(baseUrl, apiKey, refs, maxEdge);
    const payload = buildMediaPayload(spec, refIds);
    const headers = {
      'Content-Type': 'application/json',
      ...(runId ? { 'X-Skillry-Run-ID': runId } : {}),
      ...(runId && spec.stepLabel ? { 'X-Skillry-Step': encodeURIComponent(spec.stepLabel) } : {}),
    };
    const quote = await apiRequest(baseUrl, apiKey, '/v1/media/quotes', {
      method: 'POST',
      headers,
      body: JSON.stringify(payload),
    });
    const points = normalizeBudgetPoints(quote.points);
    const priceKind = String(quote.price_kind || 'fixed');
    return {
      mode: 'http',
      baseUrl,
      model: spec.model,
      provider: quote.provider || null,
      priceKind,
      points,
      usd: quote.usd ?? null,
      quoteToken: quote.quote_token || null,
      referenceIds: refIds,
      display: formatQuoteDisplay({ points, price_kind: priceKind }),
    };
  }

  const cli = findSkillryCli();
  if (!cli) {
    throw new Error(
      'Skillry auth is not configured. Choose an option: (1) connect Skillry MCP, run `skillry login`, or set SKILLRY_API_KEY; (2) in Codex, use Codex built-in image_gen for image steps; (3) pass --provider fal with FAL_KEY.'
    );
  }

  const tmpDir = fs.mkdtempSync(path.join(os.tmpdir(), 'skillry-quote-'));
  try {
    const cliArgs = [
      ...cli.prefixArgs,
      'media',
      '--base-url',
      baseUrl,
      '--model',
      spec.model,
      '--quote-only',
    ];
    appendCliMediaFlags(cliArgs, spec, tmpDir);
    if (runId) {
      cliArgs.push('--run-id', runId);
      if (spec.stepLabel) cliArgs.push('--step', spec.stepLabel);
    }
    await appendCliReferences(cliArgs, refs, maxEdge, tmpDir);
    const res = spawnSync(cli.bin, cliArgs, {
      encoding: 'utf8',
      timeout: 120000,
    });
    if (res.status !== 0) {
      const detail = (res.stderr || res.stdout || '').trim().slice(0, 600);
      throw new Error(`skillry CLI media --quote-only exited ${res.status}: ${detail}`);
    }
    const jsonMatch = (res.stdout || '').match(/\{[\s\S]*\}\s*$/);
    if (!jsonMatch) {
      throw new Error('skillry CLI media --quote-only did not output JSON.');
    }
    const quote = JSON.parse(jsonMatch[0]);
    const points = normalizeBudgetPoints(quote.points);
    const priceKind = String(quote.price_kind || 'fixed');
    return {
      mode: 'cli',
      baseUrl,
      model: spec.model,
      provider: quote.provider || null,
      priceKind,
      points,
      usd: quote.usd ?? null,
      quoteToken: quote.quote_token || null,
      referenceIds: [],
      display: formatQuoteDisplay({ points, price_kind: priceKind }),
    };
  } finally {
    fs.rmSync(tmpDir, { recursive: true, force: true });
  }
}

/**
 * Create a budgeted Skillry run (runId) after the user confirms the plan and total
 * credits in chat. Approved immediately by the server (no browser confirmation page).
 */
export async function skillryStartRun({
  runId = randomUUID(),
  name,
  budgetPoints,
  plan,
  skillSlug,
}) {
  const apiKey = getSkillryApiKey();
  if (!apiKey) {
    throw new Error('SKILLRY_API_KEY is required for skillryStartRun over HTTP.');
  }
  const baseUrl = getBaseUrl();
  const budget = normalizeBudgetPoints(budgetPoints);
  const approval = await apiRequest(baseUrl, apiKey, '/api/relay/runs', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      id: runId,
      name: name || 'Skillry media run',
      budget_points: budget,
      plan: plan || `Run Skillry media workflow with a maximum of ${budget} credits.`,
      ...(skillSlug ? { skill_slug: skillSlug } : {}),
    }),
  });
  return {
    runId,
    status: String(approval.status || 'unknown'),
    budgetPoints: budget,
    raw: approval,
  };
}

// An exclusive link makes a complete receipt visible to concurrent invocations at once.
function persistOnce(file, data) {
  const staging = file + '.' + randomUUID();
  fs.writeFileSync(staging, JSON.stringify(data), { flag: 'wx', mode: 0o600 });
  try {
    fs.linkSync(staging, file);
    return true;
  } catch (error) {
    if (error.code === 'EEXIST') return false;
    throw error;
  } finally {
    fs.unlinkSync(staging);
  }
}

function getSavedRequestId(directory, key) {
  const file = path.join(directory, key + '.request');
  if (!fs.existsSync(file)) persistOnce(file, { requestId: randomUUID() });
  return JSON.parse(fs.readFileSync(file, 'utf8')).requestId;
}

async function requireConfirmedRun(spec) {
  const quote = await skillryQuote(spec);
  const error = new Error('Skillry quote: ' + quote.display.userMessage +
    '. Show the full plan and budget to the user. After confirmation, create a run with start_skill_run or skillry run start, then pass its ID using SKILLRY_RUN_ID.');
  error.code = 'budget_pending';
  error.budget = quote.points;
  throw error;
}

export async function skillrySubmit(spec) {
  if (!spec?.model) throw new Error('skillrySubmit requires model.');
  const baseUrl = getBaseUrl();
  const apiKey = getSkillryApiKey();
  const refs = spec.references || spec.referenceFiles || [];
  const maxEdge = 4096;
  const runId = spec.runId || String(process.env.SKILLRY_RUN_ID || '').trim() || null;
  const fingerprint = sha256Hex(JSON.stringify({
    input: buildMediaPayload(spec, []),
    references: refs.map((ref) => Buffer.isBuffer(ref) ? sha256Hex(ref) : String(ref)),
    step: spec.stepLabel || null,
  }));
  const receiptDirectory = path.join(os.tmpdir(), 'skillry-run-receipts');
  fs.mkdirSync(receiptDirectory, { recursive: true, mode: 0o700 });
  const receiptKey = sha256Hex(JSON.stringify({
    baseUrl, runId, fingerprint, output: spec.outputPath || spec.cliOutputPath || null,
  }));
  const requestId = spec.requestId || getSavedRequestId(receiptDirectory, receiptKey);
  if (!UUID_PATTERN.test(requestId)) throw new Error('A valid Skillry request UUID is required.');

  if (apiKey) {
    const marker = path.join(receiptDirectory, sha256Hex(baseUrl + '/' + requestId) + '.submitted-v2');
    if (fs.existsSync(marker)) {
      const saved = JSON.parse(fs.readFileSync(marker, 'utf8'));
      if (saved.fingerprint !== fingerprint || (runId && saved.runId !== runId))
        throw new Error('This request ID belongs to a different Skillry specification or run.');
    }
    // Recovery comes before uploads and quotes, including jobs created by older adapters.
    try {
      const job = await apiRequest(baseUrl, apiKey,
        '/v1/media/jobs?request_id=' + encodeURIComponent(requestId));
      if (!job.id || job.model !== spec.model)
        throw new Error('The stored job does not match the requested model.');
      return {
        mode: 'http', baseUrl, runId, requestId, jobId: job.id, status: job.status,
        charged: job.charged ?? null, points: job.points ?? null,
        settlement_basis: job.settlement_basis ?? null,
      };
    } catch (error) {
      if (error.status !== 404) throw error;
      if (fs.existsSync(marker))
        throw new Error('The original submission is unconfirmed. Look up request ' + requestId + ' without resubmitting.');
    }
    if (!runId) await requireConfirmedRun(spec);
    const refIds = await uploadHttpReferences(baseUrl, apiKey, refs, maxEdge);
    const payload = buildMediaPayload(spec, refIds);
    const headers = {
      'Content-Type': 'application/json',
      'X-Skillry-Run-ID': runId,
      ...(spec.stepLabel ? { 'X-Skillry-Step': encodeURIComponent(spec.stepLabel) } : {}),
    };
    const quote =
      spec.quoteToken && spec.approvedPoints !== undefined
        ? {
            quote_token: spec.quoteToken,
            points: normalizeBudgetPoints(spec.approvedPoints),
          }
        : await apiRequest(baseUrl, apiKey, '/v1/media/quotes', {
            method: 'POST',
            headers,
            body: JSON.stringify(payload),
          });
    if (!persistOnce(marker, { runId, fingerprint }))
      throw new Error('This request is already being submitted. Check request ' + requestId + '.');
    const job = await apiRequest(baseUrl, apiKey, '/v1/media/jobs', {
      method: 'POST',
      headers: { ...headers, 'Idempotency-Key': requestId },
      body: JSON.stringify({
        ...payload,
        quote_token: quote.quote_token,
        max_points: quote.points,
      }),
    });
    return {
      mode: 'http',
      baseUrl,
      runId,
      requestId,
      jobId: job.id,
      status: job.status || 'accepted',
      points: quote.points ?? null,
    };
  }

  const cli = findSkillryCli();
  if (!cli) {
    throw new Error(
      'Skillry auth is not configured. Choose an option: (1) connect Skillry MCP, run `skillry login`, or set SKILLRY_API_KEY; (2) in Codex, use Codex built-in image_gen for image steps; (3) pass --provider fal with FAL_KEY.'
    );
  }

  if (!runId) await requireConfirmedRun(spec);
  const tmpDir = fs.mkdtempSync(path.join(os.tmpdir(), 'skillry-cli-'));
  const cacheOutputPath = path.resolve(spec.cliOutputPath || defaultCachePath(requestId, spec.model));
  fs.mkdirSync(path.dirname(cacheOutputPath), { recursive: true });
  try {
    const cliArgs = [
      ...cli.prefixArgs,
      'media',
      '--base-url',
      baseUrl,
      '--model',
      spec.model,
      '--output',
      cacheOutputPath,
      '--request-id',
      requestId,
    ];
    appendCliMediaFlags(cliArgs, spec, tmpDir);
    cliArgs.push('--json', '--run-id', runId);
    if (spec.stepLabel) cliArgs.push('--step', spec.stepLabel);
    // CLI recovery fingerprints reference paths. Keep paths stable across process restarts.
    const referenceDir = path.join(receiptDirectory, requestId + '-refs');
    fs.mkdirSync(referenceDir, { recursive: true, mode: 0o700 });
    await appendCliReferences(cliArgs, refs, maxEdge, referenceDir);
    const res = spawnSync(cli.bin, cliArgs, {
      encoding: 'utf8',
      timeout: 20 * 60 * 1000,
    });
    if (res.status !== 0 || !fs.existsSync(cacheOutputPath)) {
      const detail = (res.stderr || res.stdout || '').trim().slice(0, 600);
      throw new Error(`skillry CLI media exited ${res.status}: ${detail}`);
    }
    const parsed = JSON.parse(res.stdout.trim());
    if (parsed.requestId !== requestId || !UUID_PATTERN.test(parsed.id))
      throw new Error('The CLI did not return the expected job receipt. Check request ' + requestId + '.');
    return {
      mode: 'cli', baseUrl, runId, requestId, jobId: parsed.id,
      status: 'succeeded', points: parsed.points ?? null, charged: parsed.charged ?? null,
      settlement_basis: parsed.settlement_basis ?? null,
      cachedOutputPath: cacheOutputPath,
    };
  } finally {
    fs.rmSync(tmpDir, { recursive: true, force: true });
  }
}

export async function skillryStatus(handle) {
  if (handle.mode === 'cli') {
    const ok = handle.cachedOutputPath && fs.existsSync(handle.cachedOutputPath);
    return {
      status: ok ? 'succeeded' : 'failed',
      checkAfterSeconds: 0,
      error: ok ? null : `Missing cached CLI output at ${handle.cachedOutputPath}`,
      points: handle.points ?? null,
      charged: handle.charged ?? null,
      settlement_basis: handle.settlement_basis ?? null,
    };
  }
  const apiKey = getSkillryApiKey();
  if (!apiKey) {
    throw new Error('SKILLRY_API_KEY is required to poll an HTTP Skillry media job.');
  }
  const baseUrl = handle.baseUrl || getBaseUrl();
  const q = handle.jobId
    ? `id=${encodeURIComponent(handle.jobId)}`
    : `request_id=${encodeURIComponent(handle.requestId)}`;
  const data = await apiRequest(baseUrl, apiKey, `/v1/media/jobs?${q}`);
  const rawStatus = String(data.status || 'unknown').toLowerCase();
  if (rawStatus === 'completed' || data.download) {
    return {
      status: 'succeeded',
      checkAfterSeconds: 0,
      error: null,
      points: data.points ?? handle.points ?? null,
      charged: data.charged ?? null,
      settlement_basis: data.settlement_basis ?? null,
      jobId: data.id || handle.jobId,
    };
  }
  if (['failed', 'cancelled', 'error', 'expired', 'rejected'].includes(rawStatus)) {
    return {
      status: 'failed',
      checkAfterSeconds: 0,
      error: data.error || `Provider stopped with status ${data.status}`,
      points: data.points ?? null,
    };
  }
  return {
    status: rawStatus === 'accepted' ? 'queued' : 'running',
    checkAfterSeconds: Number(data.check_after_seconds) || 4,
    error: null,
    jobId: data.id || handle.jobId,
  };
}

export async function skillryDownload(handle) {
  if (handle.mode === 'cli') {
    if (!handle.cachedOutputPath || !fs.existsSync(handle.cachedOutputPath)) {
      throw new Error(`CLI output file not found: ${handle.cachedOutputPath}`);
    }
    return fs.readFileSync(handle.cachedOutputPath);
  }
  const apiKey = getSkillryApiKey();
  if (!apiKey) {
    throw new Error('SKILLRY_API_KEY is required to download an HTTP Skillry media result.');
  }
  const baseUrl = handle.baseUrl || getBaseUrl();
  const idParam = handle.jobId
    ? `id=${encodeURIComponent(handle.jobId)}`
    : `request_id=${encodeURIComponent(handle.requestId)}`;
  const res = await fetch(`${baseUrl}/v1/media/jobs?${idParam}&download=1`, {
    headers: { Authorization: `Bearer ${apiKey}` },
    signal: AbortSignal.timeout(120000),
  });
  if (!res.ok) {
    const errText = await res.text().catch(() => '');
    throw new Error(`Skillry media download failed (${res.status}): ${errText.slice(0, 300)}`);
  }
  const ct = String(res.headers.get('content-type') || '').toLowerCase();
  if (ct.includes('application/json')) {
    const body = await res.json();
    const outUrl =
      (Array.isArray(body.outputs) && body.outputs[0]) ||
      body.url ||
      body.output_url ||
      body.images?.[0]?.url ||
      body.video?.url ||
      body.audio?.url;
    if (!outUrl) {
      throw new Error('Skillry download JSON contained no output URL.');
    }
    const safeUrl = assertSafeExternalUrl(outUrl);
    // External CDN download must NOT include the Skillry Authorization header.
    const cdnRes = await fetch(safeUrl, { signal: AbortSignal.timeout(180000) });
    if (!cdnRes.ok) {
      throw new Error(`External media download failed (${cdnRes.status}).`);
    }
    return Buffer.from(await cdnRes.arrayBuffer());
  }
  return Buffer.from(await res.arrayBuffer());
}

export async function skillryPollUntilDone(
  handle,
  { timeoutMs = 15 * 60 * 1000, onTick } = {}
) {
  if (handle.mode === 'cli') return handle;
  const deadline = Date.now() + timeoutMs;
  for (;;) {
    const st = await skillryStatus(handle);
    if (onTick) onTick(st);
    if (st.status === 'succeeded') {
      return {
        ...handle,
        jobId: st.jobId || handle.jobId,
        points: st.points,
        charged: st.charged ?? null,
        settlement_basis: st.settlement_basis ?? null,
      };
    }
    if (st.status === 'failed') {
      const err = new Error(st.error || 'Skillry media job failed.');
      err.terminal = true;
      throw err;
    }
    const remaining = deadline - Date.now();
    if (remaining <= 0) {
      throw new Error(
        `Timed out waiting for Skillry job ${handle.jobId || handle.requestId}; rerun to resume without paying again.`
      );
    }
    const waitMs = Math.min(remaining, Math.max(2000, Math.min(30000, (st.checkAfterSeconds || 4) * 1000)));
    await new Promise((r) => setTimeout(r, waitMs));
  }
}

export async function skillryGenerate(spec) {
  const handle = await skillrySubmit(spec);
  const done = await skillryPollUntilDone(handle, { onTick: spec.onTick });
  let bytes = await skillryDownload(done);

  if (spec.targetFormat || (spec.targetWidth && spec.targetHeight)) {
    bytes = convertOrResizeImage(bytes, {
      targetFormat: spec.targetFormat,
      targetWidth: spec.targetWidth,
      targetHeight: spec.targetHeight,
    });
  }

  if (spec.outputPath) {
    const outPath = path.resolve(spec.outputPath);
    fs.mkdirSync(path.dirname(outPath), { recursive: true });
    const tmpOut = `${outPath}.${process.pid}.tmp`;
    fs.writeFileSync(tmpOut, bytes);
    fs.renameSync(tmpOut, outPath);
  }

  return {
    ...done,
    bytes,
    outputPath: spec.outputPath ? path.resolve(spec.outputPath) : null,
  };
}

export function applyAudioSpeed(bytes, speed) {
  const spd = Number(speed);
  if (!Number.isFinite(spd) || Math.abs(spd - 1) < 0.01) return Buffer.from(bytes);
  const clamped = Math.max(0.5, Math.min(2.0, spd));
  const tmpDir = fs.mkdtempSync(path.join(os.tmpdir(), 'skillry-spd-'));
  try {
    const inFile = path.join(tmpDir, 'in.mp3');
    const outFile = path.join(tmpDir, 'out.mp3');
    fs.writeFileSync(inFile, bytes);
    const r = spawnSync(
      'ffmpeg',
      ['-v', 'error', '-y', '-i', inFile, '-filter:a', `atempo=${clamped}`, '-codec:a', 'libmp3lame', '-b:a', '192k', outFile],
      { timeout: 60000 }
    );
    if (r.status === 0 && fs.existsSync(outFile)) {
      return fs.readFileSync(outFile);
    }
    return Buffer.from(bytes);
  } finally {
    fs.rmSync(tmpDir, { recursive: true, force: true });
  }
}

export function sha256Hex(input) {
  return createHash('sha256').update(input).digest('hex');
}
