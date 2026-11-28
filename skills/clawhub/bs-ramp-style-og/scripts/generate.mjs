#!/usr/bin/env node

import { createHash, randomUUID } from 'node:crypto';
import {
  closeSync,
  existsSync,
  fsyncSync,
  linkSync,
  mkdirSync,
  openSync,
  readFileSync,
  renameSync,
  statSync,
  unlinkSync,
  writeFileSync,
} from 'node:fs';
import { isIP } from 'node:net';
import { hostname } from 'node:os';
import { dirname, extname, resolve } from 'node:path';
import {
  inspectRasterBytes,
  MIME_BY_RASTER_FORMAT,
  PRESET_DIMENSIONS,
} from './raster.mjs';
import {
  normalizeImageSize,
  normalizeQuality,
  resolveProvider,
  skillryGenerate,
} from './lib/skillry-media.mjs';

const TEXT_ENDPOINT = 'openai/gpt-image-2';
const EDIT_ENDPOINT = 'openai/gpt-image-2/edit';
const QUEUE_ORIGIN = 'https://queue.fal.run';
const ALLOWED_SIZES = new Set([
  'auto',
  'square_hd',
  'square',
  'portrait_4_3',
  'portrait_16_9',
  'landscape_4_3',
  'landscape_16_9',
]);
const ALLOWED_QUALITIES = new Set(['auto', 'low', 'medium', 'high']);
const ALLOWED_FORMATS = new Set(['webp', 'png', 'jpeg']);
const REFERENCE_MIME_BY_EXTENSION = new Map([
  ['.png', 'image/png'],
  ['.jpg', 'image/jpeg'],
  ['.jpeg', 'image/jpeg'],
  ['.webp', 'image/webp'],
]);
const SINGLE_VALUE_OPTIONS = new Set([
  '--provider',
  '--prompt-file',
  '--output',
  '--task',
  '--size',
  '--quality',
  '--format',
  '--poll-seconds',
  '--max-wait-seconds',
  '--adopt-request-id',
]);
const MAX_REFERENCE_BYTES = 20 * 1024 * 1024;
const MAX_INLINE_REFERENCE_BYTES = 64 * 1024 * 1024;
const MAX_DOWNLOAD_BYTES = 32 * 1024 * 1024;
const SUBMISSION_TIMEOUT_MS = 120_000;
const QUEUE_REQUEST_TIMEOUT_MS = 30_000;
const MEDIA_TIMEOUT_MS = 120_000;

function usage() {
  return `Usage:
  node scripts/generate.mjs \\
    --prompt-file /absolute/path/prompt.txt \\
    --output /absolute/path/artwork.webp \\
    --task /absolute/path/artwork.fal-task.json \\
    [--reference /absolute/path/input.png] \\
    [--provider auto|skillry|fal] [--size landscape_16_9] [--quality low] [--format webp] \\
    [--adopt-request-id REQUEST_ID]

Repeat --reference for up to 16 authorized images. References may be local
PNG, JPEG, or WebP files, HTTPS URLs, or image data URIs.

Run the exact same command again to resume the same saved request. The script
never submits a replacement while the task record exists.

If submission became uncertain before a request ID was saved, inspect FAL
history. Only after locating the matching original task, rerun with
--adopt-request-id to attach that request to the existing task record.
`;
}

function parseArgs(argv) {
  const options = { references: [] };
  const seenSingletons = new Set();
  for (let index = 0; index < argv.length; index += 1) {
    const token = argv[index];
    if (token === '--help' || token === '-h') {
      if (options.help) throw new Error('Help flag was provided more than once.');
      options.help = true;
      continue;
    }
    if (token !== '--reference' && !SINGLE_VALUE_OPTIONS.has(token)) {
      throw new Error(`Unknown option: ${token}`);
    }
    const value = argv[index + 1];
    if (!value || value.startsWith('--')) {
      throw new Error(`Missing value for ${token}.`);
    }
    if (token === '--reference') {
      options.references.push(value);
    } else {
      if (seenSingletons.has(token)) throw new Error(`Duplicate option: ${token}`);
      seenSingletons.add(token);
      options[token.slice(2)] = value;
    }
    index += 1;
  }
  return options;
}

function requireOption(options, name) {
  const value = options[name];
  if (!value) throw new Error(`Missing required option --${name}.`);
  return value;
}

function parseTiming(options) {
  const pollSeconds = Number(options['poll-seconds'] ?? 4);
  const maxWaitSeconds = Number(options['max-wait-seconds'] ?? 600);
  if (!Number.isInteger(pollSeconds) || pollSeconds < 1 || pollSeconds > 60) {
    throw new Error('--poll-seconds must be an integer between 1 and 60.');
  }
  if (
    !Number.isInteger(maxWaitSeconds) ||
    maxWaitSeconds < 1 ||
    maxWaitSeconds > 3600
  ) {
    throw new Error('--max-wait-seconds must be an integer between 1 and 3600.');
  }
  return { pollSeconds, maxWaitSeconds };
}

function sha256(value) {
  return createHash('sha256').update(value).digest('hex');
}

function parseJson(text, label) {
  try {
    return JSON.parse(text);
  } catch {
    throw new Error(`${label} did not return valid JSON.`);
  }
}

function compactError(value) {
  if (!value) return null;
  if (typeof value === 'string') {
    return value.replace(/\s+/g, ' ').trim().slice(0, 800);
  }
  if (typeof value?.message === 'string') {
    return value.message.replace(/\s+/g, ' ').trim().slice(0, 800);
  }
  return JSON.stringify(value).replace(/\s+/g, ' ').trim().slice(0, 800);
}

function payloadError(payload) {
  return compactError(
    payload?.error ?? payload?.error_message ?? payload?.error_type
  );
}

function syncDirectoryBestEffort(path) {
  let descriptor;
  try {
    descriptor = openSync(path, 'r');
    fsyncSync(descriptor);
  } catch (error) {
    if (!['EINVAL', 'EISDIR', 'EPERM', 'ENOTSUP', 'EBADF'].includes(error?.code)) {
      throw error;
    }
  } finally {
    if (descriptor !== undefined) closeSync(descriptor);
  }
}

function writeBytesExclusiveDurable(path, bytes) {
  mkdirSync(dirname(path), { recursive: true });
  let descriptor;
  try {
    descriptor = openSync(path, 'wx', 0o600);
    writeFileSync(descriptor, bytes);
    fsyncSync(descriptor);
  } finally {
    if (descriptor !== undefined) closeSync(descriptor);
  }
  syncDirectoryBestEffort(dirname(path));
}

function writeJsonExclusive(path, value) {
  try {
    writeBytesExclusiveDurable(
      path,
      Buffer.from(`${JSON.stringify(value, null, 2)}\n`, 'utf8')
    );
  } catch (error) {
    if (error?.code === 'EEXIST') {
      throw new Error(
        `Task record already exists: ${path}. No request was submitted by this process; rerun to resume or inspect the saved submission state.`
      );
    }
    throw error;
  }
}

function writeJsonAtomic(path, value) {
  mkdirSync(dirname(path), { recursive: true });
  const temporary = `${path}.${randomUUID()}.tmp`;
  try {
    writeBytesExclusiveDurable(
      temporary,
      Buffer.from(`${JSON.stringify(value, null, 2)}\n`, 'utf8')
    );
    renameSync(temporary, path);
    syncDirectoryBestEffort(dirname(path));
  } catch (error) {
    if (existsSync(temporary)) unlinkSync(temporary);
    throw error;
  }
}

function probeWritableOutputDirectory(outputPath) {
  const directory = dirname(outputPath);
  mkdirSync(directory, { recursive: true });
  const probe = resolve(directory, `.wonky-doodle-write-probe-${randomUUID()}`);
  writeBytesExclusiveDurable(probe, Buffer.alloc(0));
  unlinkSync(probe);
  syncDirectoryBestEffort(directory);
}

function processIsAlive(pid) {
  if (!Number.isInteger(pid) || pid <= 0) return false;
  try {
    process.kill(pid, 0);
    return true;
  } catch (error) {
    if (error?.code === 'EPERM') return true;
    if (error?.code === 'ESRCH') return false;
    throw error;
  }
}

function acquireTaskLock(taskPath) {
  const lockPath = `${taskPath}.lock`;
  const token = randomUUID();
  const localHostname = hostname();
  for (let attempt = 0; attempt < 3; attempt += 1) {
    const lock = {
      schemaVersion: 1,
      token,
      pid: process.pid,
      hostname: localHostname,
      taskPath,
      createdAt: new Date().toISOString(),
    };
    try {
      writeBytesExclusiveDurable(
        lockPath,
        Buffer.from(`${JSON.stringify(lock, null, 2)}\n`, 'utf8')
      );
      return { lockPath, token };
    } catch (error) {
      if (error?.code !== 'EEXIST') throw error;
    }

    let existing;
    try {
      existing = parseJson(readFileSync(lockPath, 'utf8'), 'Task lock');
    } catch (error) {
      throw new Error(
        `${error.message} Invalid lock evidence is preserved at ${lockPath}; inspect it before manual recovery.`
      );
    }
    if (existing.hostname !== localHostname) {
      throw new Error(
        `Task is locked by PID ${existing.pid ?? 'unknown'} on host ${existing.hostname ?? 'unknown'}. Cross-host locks are never removed automatically.`
      );
    }
    if (processIsAlive(existing.pid)) {
      throw new Error(
        `Task is already running in PID ${existing.pid}. This process will not poll or write the same task concurrently.`
      );
    }

    const stamp = String(existing.createdAt ?? 'unknown').replace(/[^0-9A-Za-z.-]/g, '-');
    const staleToken = String(existing.token ?? randomUUID())
      .replace(/[^0-9A-Za-z.-]/g, '-')
      .slice(0, 160);
    const stalePath = `${lockPath}.stale-${stamp}-${staleToken}`;
    try {
      renameSync(lockPath, stalePath);
      syncDirectoryBestEffort(dirname(lockPath));
    } catch (error) {
      if (error?.code === 'ENOENT') continue;
      throw error;
    }
  }
  throw new Error(`Could not acquire the task lock after three attempts: ${lockPath}`);
}

function releaseTaskLock(lock) {
  if (!existsSync(lock.lockPath)) return;
  const existing = parseJson(readFileSync(lock.lockPath, 'utf8'), 'Task lock');
  if (existing.token !== lock.token) {
    throw new Error(
      `Task lock token changed unexpectedly; lock is preserved at ${lock.lockPath}.`
    );
  }
  unlinkSync(lock.lockPath);
  syncDirectoryBestEffort(dirname(lock.lockPath));
}

function requireFalKey() {
  const key = process.env.FAL_KEY;
  if (!key) {
    throw new Error(
      'FAL_KEY is not set. Set it in the local environment and do not paste it into a prompt or task file.'
    );
  }
  return key;
}

function authHeaders(key) {
  return { Authorization: `Key ${key}` };
}

function submissionHeaders(key) {
  return {
    ...authHeaders(key),
    'Content-Type': 'application/json',
    'X-Fal-No-Retry': '1',
    'x-app-fal-disable-fallback': 'true',
  };
}

async function fetchJson(url, init, label, timeoutMs) {
  let response;
  try {
    response = await fetch(url, {
      ...init,
      redirect: 'error',
      signal: AbortSignal.timeout(timeoutMs),
    });
  } catch (error) {
    throw new Error(`${label} failed without retry: ${error.message}`);
  }
  const text = await response.text();
  if (!response.ok) {
    throw new Error(
      `${label} failed with HTTP ${response.status}; no retry was attempted. ${text
        .replace(/\s+/g, ' ')
        .trim()
        .slice(0, 800)}`
    );
  }
  return parseJson(text, label);
}

function normalizeRequestId(value) {
  const requestId = String(value ?? '').trim();
  if (!/^[A-Za-z0-9_-]{8,160}$/.test(requestId)) {
    throw new Error('FAL request ID has an unexpected format.');
  }
  return requestId;
}

function queueUrls(endpoint, requestId) {
  const encoded = encodeURIComponent(requestId);
  const base = `${QUEUE_ORIGIN}/${endpoint}/requests/${encoded}`;
  return {
    statusUrl: `${base}/status`,
    responseUrl: base,
  };
}

function validateStoredQueueUrls(state) {
  const expected = queueUrls(state.endpoint, state.requestId);
  for (const [field, expectedValue] of Object.entries(expected)) {
    let actual;
    try {
      actual = new URL(state[field]);
    } catch {
      throw new Error(`Task record ${field} is not a valid URL.`);
    }
    if (
      actual.origin !== QUEUE_ORIGIN ||
      actual.username ||
      actual.password ||
      actual.search ||
      actual.hash ||
      actual.toString() !== new URL(expectedValue).toString()
    ) {
      throw new Error(`Task record ${field} does not match its request and endpoint.`);
    }
  }
}

function assertPublicHostname(hostname, label) {
  const normalized = hostname.toLowerCase();
  if (
    normalized === 'localhost' ||
    normalized.endsWith('.localhost') ||
    normalized.endsWith('.local') ||
    normalized.endsWith('.internal') ||
    isIP(normalized) !== 0
  ) {
    throw new Error(`${label} must use a public hostname.`);
  }
}

function validateMediaUrl(value) {
  const url = new URL(value);
  if (
    url.protocol !== 'https:' ||
    url.username ||
    url.password ||
    url.port
  ) {
    throw new Error('FAL media URL must be an uncredentialed public HTTPS URL.');
  }
  assertPublicHostname(url.hostname, 'FAL media URL');
  return url.toString();
}

function referenceFromBytes(bytes, claimedMime, label) {
  if (bytes.length > MAX_REFERENCE_BYTES) {
    throw new Error(`${label} exceeds the 20 MB reference limit.`);
  }
  const metadata = inspectRasterBytes(bytes, { maxBytes: MAX_REFERENCE_BYTES });
  const actualMime = MIME_BY_RASTER_FORMAT.get(metadata.format);
  if (claimedMime && claimedMime.toLowerCase() !== actualMime) {
    throw new Error(`${label} claims ${claimedMime} but contains ${actualMime}.`);
  }
  return {
    value: `data:${actualMime};base64,${bytes.toString('base64')}`,
    inlineBytes: bytes.length,
  };
}

function normalizeReference(value) {
  if (value.startsWith('data:')) {
    const match =
      /^data:(image\/(?:png|jpeg|webp));base64,([A-Za-z0-9+/]*={0,2})$/i.exec(
        value
      );
    if (!match || !match[2] || match[2].length % 4 !== 0) {
      throw new Error('Image data URI must contain canonical base64 PNG, JPEG, or WebP data.');
    }
    const bytes = Buffer.from(match[2], 'base64');
    if (bytes.toString('base64') !== match[2]) {
      throw new Error('Image data URI contains invalid or non-canonical base64.');
    }
    return referenceFromBytes(bytes, match[1].toLowerCase(), 'Image data URI');
  }

  const looksLikeWindowsPath = /^[a-z]:[\\/]/i.test(value);
  if (!looksLikeWindowsPath && /^[a-z][a-z0-9+.-]*:/i.test(value)) {
    const url = new URL(value);
    if (
      url.protocol !== 'https:' ||
      url.username ||
      url.password ||
      url.port ||
      value.length > 4096
    ) {
      throw new Error('Reference URLs must be uncredentialed HTTPS URLs under 4096 characters.');
    }
    assertPublicHostname(url.hostname, 'Reference URL');
    return { value: url.toString(), inlineBytes: 0 };
  }

  const path = resolve(value);
  const extension = extname(path).toLowerCase();
  const claimedMime = REFERENCE_MIME_BY_EXTENSION.get(extension);
  if (!claimedMime) {
    throw new Error(`Unsupported local reference type: ${extension || 'no extension'}.`);
  }
  const metadata = statSync(path);
  if (!metadata.isFile()) throw new Error(`Reference is not a regular file: ${path}`);
  return referenceFromBytes(readFileSync(path), claimedMime, `Local reference ${path}`);
}

function validateOutputExtension(path, format) {
  const extension = extname(path).toLowerCase();
  const valid =
    (format === 'webp' && extension === '.webp') ||
    (format === 'png' && extension === '.png') ||
    (format === 'jpeg' && ['.jpg', '.jpeg'].includes(extension));
  if (!valid) {
    throw new Error(
      `Output extension ${extension || '(none)'} does not match format ${format}.`
    );
  }
}

function buildRequestedInputs(options) {
  const promptPath = resolve(requireOption(options, 'prompt-file'));
  const outputPath = resolve(requireOption(options, 'output'));
  const prompt = readFileSync(promptPath, 'utf8').trim();
  if (!prompt) throw new Error('Prompt file is empty.');
  if (prompt.length > 50_000) throw new Error('Prompt exceeds the 50,000-character limit.');
  if (options.references.length > 16) {
    throw new Error('No more than 16 reference images are allowed.');
  }

  const normalizedReferences = options.references.map(normalizeReference);
  const totalInlineBytes = normalizedReferences.reduce(
    (sum, reference) => sum + reference.inlineBytes,
    0
  );
  if (totalInlineBytes > MAX_INLINE_REFERENCE_BYTES) {
    throw new Error('Inline reference images exceed the 64 MB combined safety limit.');
  }
  const imageUrls = normalizedReferences.map((reference) => reference.value);
  const endpoint = imageUrls.length > 0 ? EDIT_ENDPOINT : TEXT_ENDPOINT;
  const imageSize =
    options.size ?? (imageUrls.length > 0 ? 'auto' : 'landscape_16_9');
  const quality = options.quality ?? 'low';
  const format = options.format ?? 'webp';
  if (!ALLOWED_SIZES.has(imageSize)) {
    throw new Error(`Unsupported --size value: ${imageSize}.`);
  }
  if (!ALLOWED_QUALITIES.has(quality)) {
    throw new Error(`Unsupported --quality value: ${quality}.`);
  }
  if (!ALLOWED_FORMATS.has(format)) {
    throw new Error(`Unsupported --format value: ${format}.`);
  }
  validateOutputExtension(outputPath, format);

  return {
    providerOption: options.provider ?? null,
    rawReferences: options.references,
    prompt,
    imageUrls,
    endpoint,
    outputPath,
    promptSha256: sha256(prompt),
    referencesSha256: sha256(
      JSON.stringify(imageUrls.map((reference) => sha256(reference)))
    ),
    inputSummary: {
      image_size: imageSize,
      quality,
      num_images: 1,
      output_format: format,
      reference_count: imageUrls.length,
    },
  };
}

function loadState(taskPath) {
  const state = parseJson(readFileSync(taskPath, 'utf8'), 'Task record');
  if (
    state.schemaVersion !== 1 ||
    ![TEXT_ENDPOINT, EDIT_ENDPOINT].includes(state.endpoint)
  ) {
    throw new Error('Task record schema or endpoint does not match this Skill.');
  }
  if (state.provider === 'skillry') return state;
  if (['SUBMITTING', 'SUBMISSION_UNKNOWN'].includes(state.status)) return state;
  if (!state.requestId || !state.statusUrl || !state.responseUrl) {
    throw new Error('Task record is missing its FAL request identifiers.');
  }
  state.requestId = normalizeRequestId(state.requestId);
  validateStoredQueueUrls(state);
  if (state.status === 'COMPLETED' && state.error) {
    throw new Error('Completed task record still contains an error and requires review.');
  }
  return state;
}

function assertSameRequest(state, requested) {
  const mismatches = [];
  if (state.endpoint !== requested.endpoint) mismatches.push('endpoint');
  if (state.outputPath !== requested.outputPath) mismatches.push('output path');
  if (state.promptSha256 !== requested.promptSha256) mismatches.push('prompt');
  if (state.referencesSha256 !== requested.referencesSha256) mismatches.push('references');
  for (const key of [
    'image_size',
    'quality',
    'num_images',
    'output_format',
    'reference_count',
  ]) {
    if (state.input?.[key] !== requested.inputSummary[key]) mismatches.push(key);
  }
  if (mismatches.length > 0) {
    throw new Error(
      `Saved task does not match the requested ${mismatches.join(', ')}. Keep this task record and request explicit approval before using a new task path for another paid generation.`
    );
  }
}

async function submitTask(taskPath, requested, key) {
  if (existsSync(requested.outputPath)) {
    throw new Error(`Refusing to overwrite existing output: ${requested.outputPath}`);
  }
  probeWritableOutputDirectory(requested.outputPath);

  const now = new Date().toISOString();
  const intent = {
    schemaVersion: 1,
    endpoint: requested.endpoint,
    outputPath: requested.outputPath,
    promptSha256: requested.promptSha256,
    referencesSha256: requested.referencesSha256,
    input: requested.inputSummary,
    status: 'SUBMITTING',
    submissionMayHaveStarted: false,
    createdAt: now,
    updatedAt: now,
  };
  writeJsonExclusive(taskPath, intent);

  intent.submissionMayHaveStarted = true;
  intent.updatedAt = new Date().toISOString();
  writeJsonAtomic(taskPath, intent);

  const input = {
    prompt: requested.prompt,
    image_size: requested.inputSummary.image_size,
    quality: requested.inputSummary.quality,
    num_images: 1,
    output_format: requested.inputSummary.output_format,
    ...(requested.imageUrls.length > 0
      ? { image_urls: requested.imageUrls }
      : {}),
  };

  let submitted;
  try {
    submitted = await fetchJson(
      `${QUEUE_ORIGIN}/${requested.endpoint}`,
      {
        method: 'POST',
        headers: submissionHeaders(key),
        body: JSON.stringify(input),
      },
      'FAL submission',
      SUBMISSION_TIMEOUT_MS
    );
  } catch (error) {
    intent.status = 'SUBMISSION_UNKNOWN';
    intent.error = compactError(error);
    intent.updatedAt = new Date().toISOString();
    writeJsonAtomic(taskPath, intent);
    throw new Error(
      `${error.message}. The submission tombstone is preserved and blocks another POST. Inspect FAL history before taking any further paid action.`
    );
  }

  let requestId;
  try {
    requestId = normalizeRequestId(submitted.request_id);
  } catch (error) {
    intent.status = 'SUBMISSION_UNKNOWN';
    intent.error = compactError(error);
    intent.updatedAt = new Date().toISOString();
    writeJsonAtomic(taskPath, intent);
    throw new Error(
      'FAL submission returned without a usable request ID. The tombstone is preserved and blocks another POST; inspect FAL history.'
    );
  }

  const urls = queueUrls(requested.endpoint, requestId);
  const state = {
    ...intent,
    requestId,
    ...urls,
    status: 'SUBMITTED',
    updatedAt: new Date().toISOString(),
  };
  delete state.error;
  const submitError = payloadError(submitted);
  if (submitError) {
    state.providerStatus = 'SUBMISSION_RESPONSE_ERROR';
    state.status = 'FAILED';
    state.error = submitError;
  }
  writeJsonAtomic(taskPath, state);
  if (submitError) {
    throw new Error(
      `FAL submission returned request ${requestId} with an error: ${submitError}. No replacement will be submitted automatically.`
    );
  }
  process.stdout.write(`Saved FAL request ${requestId} to ${taskPath}.\n`);
  return state;
}

function adoptRequest(state, taskPath, requestIdValue) {
  if (!['SUBMITTING', 'SUBMISSION_UNKNOWN'].includes(state.status)) {
    throw new Error(
      '--adopt-request-id is only valid for an uncertain submission tombstone.'
    );
  }
  const requestId = normalizeRequestId(requestIdValue);
  Object.assign(state, queueUrls(state.endpoint, requestId), {
    requestId,
    status: 'SUBMITTED',
    adoptedAt: new Date().toISOString(),
  });
  state.updatedAt = state.adoptedAt;
  delete state.error;
  writeJsonAtomic(taskPath, state);
  process.stdout.write(`Adopted existing FAL request ${requestId}.\n`);
  return state;
}

function findImages(payload) {
  for (const candidate of [
    payload?.images,
    payload?.data?.images,
    payload?.payload?.images,
  ]) {
    if (Array.isArray(candidate)) return candidate;
  }
  return [];
}

function verifyRasterAgainstTask(bytes, state, remoteImage = null) {
  const metadata = inspectRasterBytes(bytes, { maxBytes: MAX_DOWNLOAD_BYTES });
  const expectedMime = MIME_BY_RASTER_FORMAT.get(state.input.output_format);
  const actualMime = MIME_BY_RASTER_FORMAT.get(metadata.format);
  if (actualMime !== expectedMime) {
    throw new Error(`Downloaded image contains ${actualMime}, expected ${expectedMime}.`);
  }
  const expectedDimensions = PRESET_DIMENSIONS.get(state.input.image_size);
  if (
    expectedDimensions &&
    (metadata.width !== expectedDimensions.width ||
      metadata.height !== expectedDimensions.height)
  ) {
    throw new Error(
      `Downloaded image is ${metadata.width}x${metadata.height}, expected ${expectedDimensions.width}x${expectedDimensions.height}.`
    );
  }
  if (
    Number.isInteger(remoteImage?.width) &&
    Number.isInteger(remoteImage?.height) &&
    (remoteImage.width !== metadata.width || remoteImage.height !== metadata.height)
  ) {
    throw new Error('FAL result metadata does not match the downloaded raster dimensions.');
  }
  return metadata;
}

function verifyPersistedOutput(path, state) {
  const bytes = readFileSync(path);
  if (sha256(bytes) !== state.resultSha256) {
    throw new Error(`Persisted output digest does not match the task record: ${path}`);
  }
  const metadata = verifyRasterAgainstTask(bytes, state);
  if (
    state.resultWidth !== metadata.width ||
    state.resultHeight !== metadata.height ||
    state.resultFormat !== metadata.format ||
    state.resultBytes !== metadata.bytes
  ) {
    throw new Error(`Persisted output metadata does not match the task record: ${path}`);
  }
  return metadata;
}

function finalizeLocalResult(state, taskPath, temporaryPath) {
  if (existsSync(state.outputPath)) {
    if (!state.resultSha256) {
      throw new Error(
        `Output exists without a persisted result digest: ${state.outputPath}. Inspect it manually; the script will not overwrite it.`
      );
    }
    verifyPersistedOutput(state.outputPath, state);
    if (existsSync(temporaryPath)) {
      verifyPersistedOutput(temporaryPath, state);
      unlinkSync(temporaryPath);
      syncDirectoryBestEffort(dirname(temporaryPath));
    }
    state.status = 'COMPLETED';
    delete state.temporaryOutputPath;
    delete state.error;
    state.updatedAt = new Date().toISOString();
    writeJsonAtomic(taskPath, state);
    process.stdout.write(`Recovered completed output: ${state.outputPath}\n`);
    return true;
  }

  if (!state.resultSha256 || !existsSync(temporaryPath)) return false;
  verifyPersistedOutput(temporaryPath, state);
  linkSync(temporaryPath, state.outputPath);
  syncDirectoryBestEffort(dirname(state.outputPath));
  unlinkSync(temporaryPath);
  syncDirectoryBestEffort(dirname(state.outputPath));
  state.status = 'COMPLETED';
  delete state.temporaryOutputPath;
  delete state.error;
  state.updatedAt = new Date().toISOString();
  writeJsonAtomic(taskPath, state);
  process.stdout.write(`Recovered downloaded output: ${state.outputPath}\n`);
  return true;
}

async function readResponseWithLimit(response, limit) {
  const contentLength = Number(response.headers.get('content-length') ?? 0);
  if (Number.isFinite(contentLength) && contentLength > limit) {
    throw new Error(`Media response exceeds the ${limit}-byte download limit.`);
  }
  if (!response.body) throw new Error('Media response has no body.');
  const reader = response.body.getReader();
  const chunks = [];
  let total = 0;
  while (true) {
    const { done, value } = await reader.read();
    if (done) break;
    total += value.byteLength;
    if (total > limit) {
      await reader.cancel();
      throw new Error(`Media response exceeds the ${limit}-byte download limit.`);
    }
    chunks.push(Buffer.from(value));
  }
  return Buffer.concat(chunks, total);
}

async function downloadResult(state, taskPath, key) {
  const temporaryPath =
    state.temporaryOutputPath ?? `${state.outputPath}.${state.requestId}.part`;
  if (finalizeLocalResult(state, taskPath, temporaryPath)) return;

  const activeKey = key ?? requireFalKey();
  const result = await fetchJson(
    state.responseUrl,
    { headers: authHeaders(activeKey) },
    'FAL result',
    QUEUE_REQUEST_TIMEOUT_MS
  );
  const resultError = payloadError(result);
  if (resultError) {
    state.status = 'FAILED';
    state.error = resultError;
    state.updatedAt = new Date().toISOString();
    writeJsonAtomic(taskPath, state);
    throw new Error(
      `FAL result contains an error: ${resultError}. The task record is preserved; do not submit a replacement without approval.`
    );
  }

  const images = findImages(result);
  if (images.length !== 1 || !images[0]?.url) {
    throw new Error(`FAL result must contain exactly one image; found ${images.length}.`);
  }
  const image = images[0];
  const expectedMime = MIME_BY_RASTER_FORMAT.get(state.input.output_format);
  if (image.content_type && image.content_type.toLowerCase() !== expectedMime) {
    throw new Error(
      `FAL result reports ${image.content_type}, expected ${expectedMime}.`
    );
  }
  if (existsSync(state.outputPath)) {
    throw new Error(`Refusing to overwrite existing output: ${state.outputPath}`);
  }

  const mediaUrl = validateMediaUrl(image.url);
  let response;
  try {
    response = await fetch(mediaUrl, {
      redirect: 'error',
      signal: AbortSignal.timeout(MEDIA_TIMEOUT_MS),
    });
  } catch (error) {
    throw new Error(
      `Media download failed without retry: ${error.message}. Rerun the same command to resume this request.`
    );
  }
  if (!response.ok) {
    throw new Error(
      `Media download failed with HTTP ${response.status}. Rerun the same command to resume this request.`
    );
  }
  const contentType = (response.headers.get('content-type') ?? '')
    .split(';', 1)[0]
    .trim()
    .toLowerCase();
  if (contentType !== expectedMime) {
    throw new Error(
      `Unexpected media content type ${contentType || 'missing'}; expected ${expectedMime}.`
    );
  }

  const bytes = await readResponseWithLimit(response, MAX_DOWNLOAD_BYTES);
  const metadata = verifyRasterAgainstTask(bytes, state, image);
  const resultSha256 = sha256(bytes);
  if (existsSync(temporaryPath)) {
    const existing = readFileSync(temporaryPath);
    if (sha256(existing) !== resultSha256) {
      throw new Error(
        `Temporary output already exists with different content: ${temporaryPath}`
      );
    }
    verifyRasterAgainstTask(existing, state, image);
  } else {
    writeBytesExclusiveDurable(temporaryPath, bytes);
  }

  Object.assign(state, {
    status: 'RESULT_DOWNLOADED',
    resultSha256,
    resultBytes: metadata.bytes,
    resultContentType: contentType,
    resultFormat: metadata.format,
    resultWidth: metadata.width,
    resultHeight: metadata.height,
    temporaryOutputPath: temporaryPath,
    updatedAt: new Date().toISOString(),
  });
  delete state.error;
  writeJsonAtomic(taskPath, state);
  finalizeLocalResult(state, taskPath, temporaryPath);
}

async function pollTask(state, taskPath, key, timing) {
  if (['FAILED', 'CANCELLED'].includes(state.status)) {
    throw new Error(
      `Saved task ended as ${state.status}. It will not be replaced automatically.`
    );
  }
  if (['READY', 'RESULT_DOWNLOADED', 'COMPLETED'].includes(state.status)) {
    await downloadResult(state, taskPath, key);
    return;
  }

  const activeKey = key ?? requireFalKey();
  const deadline = Date.now() + timing.maxWaitSeconds * 1000;
  while (true) {
    const remaining = deadline - Date.now();
    if (remaining <= 0) {
      throw new Error(
        `Polling stopped after ${timing.maxWaitSeconds} seconds. Rerun the same command to resume request ${state.requestId}; no replacement was submitted.`
      );
    }
    const status = await fetchJson(
      state.statusUrl,
      { headers: authHeaders(activeKey) },
      'FAL status',
      Math.min(QUEUE_REQUEST_TIMEOUT_MS, remaining)
    );
    const statusError = payloadError(status);
    state.providerStatus = status.status ?? 'UNKNOWN';
    state.updatedAt = new Date().toISOString();
    if (statusError) {
      state.status = 'FAILED';
      state.error = statusError;
      writeJsonAtomic(taskPath, state);
      throw new Error(
        `FAL task reported an error: ${statusError}. The task record is preserved; do not submit a replacement without approval.`
      );
    }
    delete state.error;
    if (state.providerStatus === 'COMPLETED') state.status = 'READY';
    else if (['FAILED', 'CANCELLED'].includes(state.providerStatus)) {
      state.status = state.providerStatus;
    } else {
      state.status = state.providerStatus;
    }
    writeJsonAtomic(taskPath, state);

    if (state.status === 'READY') {
      await downloadResult(state, taskPath, activeKey);
      return;
    }
    if (['FAILED', 'CANCELLED'].includes(state.status)) {
      throw new Error(
        `FAL task ended as ${state.status}. The task record is preserved; do not submit a replacement without approval.`
      );
    }
    const sleepMs = Math.min(
      timing.pollSeconds * 1000,
      Math.max(0, deadline - Date.now())
    );
    if (sleepMs <= 0) continue;
    process.stdout.write(`FAL request ${state.requestId}: ${state.providerStatus}.\n`);
    await new Promise((resolveWait) => setTimeout(resolveWait, sleepMs));
  }
}


async function runSkillryTask(taskPath, requested, existingState = null) {
  const requestId = existingState?.requestId || randomUUID();
  const now = new Date().toISOString();
  const state = existingState
    ? { ...existingState, status: 'SUBMITTING', updatedAt: now }
    : {
        schemaVersion: 1,
        provider: 'skillry',
        endpoint: requested.endpoint,
        requestId,
        outputPath: requested.outputPath,
        promptSha256: requested.promptSha256,
        referencesSha256: requested.referencesSha256,
        input: requested.inputSummary,
        status: 'SUBMITTING',
        createdAt: now,
        updatedAt: now,
      };
  delete state.error;
  writeJsonAtomic(taskPath, state);
  const norm = normalizeImageSize(requested.inputSummary.image_size, 'gpt-image-2');
  const expectedDims = PRESET_DIMENSIONS.get(requested.inputSummary.image_size);
  const format = requested.inputSummary.output_format;
  const expectedMime = MIME_BY_RASTER_FORMAT.get(format);
  try {
    const res = await skillryGenerate({
      model: 'gpt-image-2',
      prompt: requested.prompt,
      size: norm.apiSize,
      quality: normalizeQuality(requested.inputSummary.quality),
      references: requested.rawReferences,
      targetFormat: format,
      targetWidth: expectedDims?.width ?? norm.targetWidth,
      targetHeight: expectedDims?.height ?? norm.targetHeight,
      requestId,
      stepLabel: 'generate',
      onTick: (st) => process.stdout.write(`Skillry request ${requestId}: ${st.status}.\n`),
    });
    const metadata = verifyRasterAgainstTask(res.bytes, state);
    const resultSha256 = sha256(res.bytes);
    const temporaryPath = `${requested.outputPath}.${requestId}.part`;
    writeBytesExclusiveDurable(temporaryPath, res.bytes);
    Object.assign(state, {
      runId: res.runId,
      jobId: res.jobId,
      points: res.points,
      status: 'RESULT_DOWNLOADED',
      resultSha256,
      resultBytes: metadata.bytes,
      resultContentType: expectedMime,
      resultFormat: metadata.format,
      resultWidth: metadata.width,
      resultHeight: metadata.height,
      temporaryOutputPath: temporaryPath,
      updatedAt: new Date().toISOString(),
    });
    delete state.error;
    delete state.approvalUrl;
    writeJsonAtomic(taskPath, state);
    finalizeLocalResult(state, taskPath, temporaryPath);
  } catch (error) {
    if (error.code === 'budget_pending') {
      state.status = 'AWAITING_BUDGET_APPROVAL';
      if (error.runId) state.runId = error.runId;
      if (error.approvalUrl) state.approvalUrl = error.approvalUrl;
    } else {
      state.status = error.terminal ? 'FAILED' : 'SUBMISSION_UNKNOWN';
    }
    state.error = compactError(error);
    state.updatedAt = new Date().toISOString();
    writeJsonAtomic(taskPath, state);
    throw error;
  }
}

async function main() {
  const options = parseArgs(process.argv.slice(2));
  if (options.help) {
    process.stdout.write(usage());
    return;
  }
  const timing = parseTiming(options);
  const taskPath = resolve(requireOption(options, 'task'));
  const requested = buildRequestedInputs(options);
  if (taskPath === requested.outputPath) {
    throw new Error('The task record and generated image must use different paths.');
  }
  const lock = acquireTaskLock(taskPath);
  try {
    let state;
    let key = null;
    if (existsSync(taskPath)) {
      state = loadState(taskPath);
      assertSameRequest(state, requested);
      const savedProvider = state.provider || 'fal';
      const chosenProvider = requested.providerOption ? resolveProvider(requested.providerOption) : savedProvider;
      if (chosenProvider !== savedProvider) {
        throw new Error(`Saved task uses provider "${savedProvider}", cannot switch to "${chosenProvider}" on the same task path.`);
      }
      if (savedProvider === 'skillry') {
        if (state.status === 'COMPLETED' && existsSync(requested.outputPath)) {
          verifyPersistedOutput(requested.outputPath, state);
          process.stdout.write(`Output already exists: ${requested.outputPath}\n`);
          return;
        }
        if (state.temporaryOutputPath && finalizeLocalResult(state, taskPath, state.temporaryOutputPath)) {
          return;
        }
        if (state.status === 'AWAITING_BUDGET_APPROVAL') {
          await runSkillryTask(taskPath, requested, state);
          return;
        }
        throw new Error(`Saved Skillry task is ${state.status}. Use a new task path after review rather than resubmitting automatically.`);
      }
      if (options['adopt-request-id']) {
        state = adoptRequest(state, taskPath, options['adopt-request-id']);
      } else if (['SUBMITTING', 'SUBMISSION_UNKNOWN'].includes(state.status)) {
        throw new Error(
          `Saved task is ${state.status}. This path will never submit again automatically. Inspect FAL history, then adopt the matching original request ID or use a new task path only after explicit approval.`
        );
      }
      await pollTask(state, taskPath, key, timing);
    } else {
      const chosenProvider = resolveProvider(requested.providerOption);
      if (chosenProvider === 'skillry') {
        if (existsSync(requested.outputPath)) {
          throw new Error(`Refusing to overwrite existing output: ${requested.outputPath}`);
        }
        probeWritableOutputDirectory(requested.outputPath);
        await runSkillryTask(taskPath, requested);
        return;
      }
      if (options['adopt-request-id']) {
        throw new Error('--adopt-request-id requires an existing uncertain task record.');
      }
      key = requireFalKey();
      state = await submitTask(taskPath, requested, key);
      await pollTask(state, taskPath, key, timing);
    }
  } finally {
    releaseTaskLock(lock);
  }
}

main().catch((error) => {
  process.stderr.write(`${error.message}\n`);
  process.exitCode = 1;
});
