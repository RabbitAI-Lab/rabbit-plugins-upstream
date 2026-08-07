#!/usr/bin/env node

import crypto from 'node:crypto';
import { spawn } from 'node:child_process';
import { constants as fsConstants } from 'node:fs';
import {
  access,
  chmod,
  mkdir,
  open,
  readFile,
  realpath,
  rename,
  stat,
  writeFile,
} from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';

const TARGET_PLUGIN_VERSION = '1.3.0';
const EXPECTED_CAPABILITIES = Object.freeze([
  'control_wss_v1',
  'gateway_tunnel_v1',
  'long_wss_v1',
  'runtime_boot_identity_v1',
]);
const AUTOMATIC_RESTART_MAX_ATTEMPTS = 1;

function parseArgs(argv) {
  const [operation, ...tokens] = argv;
  const values = new Map();
  for (let index = 0; index < tokens.length; index += 1) {
    const token = tokens[index];
    if (!token.startsWith('--')) throw new Error(`Unexpected argument: ${token}`);
    const value = tokens[index + 1];
    if (!value || value.startsWith('--')) throw new Error(`Missing value for ${token}`);
    values.set(token, value);
    index += 1;
  }
  return { operation, values };
}

function requiredString(value, field, maxLength = 2048) {
  if (typeof value !== 'string' || value.trim().length === 0 || value.length > maxLength) {
    const error = new Error(`${field} must be a non-empty string`);
    error.code = 'REQUEST_INVALID';
    throw error;
  }
  return value.trim();
}

function safeSetupRunId(value) {
  const setupRunId = requiredString(value, 'setupRunId', 160);
  if (!/^[A-Za-z0-9_-]+$/u.test(setupRunId)) {
    const error = new Error('setupRunId contains unsupported characters');
    error.code = 'REQUEST_INVALID';
    throw error;
  }
  return setupRunId;
}

function stateDir(values) {
  return path.resolve(
    values.get('--state-dir') ??
      process.env.OPENCLAW_STATE_DIR ??
      path.join(os.homedir(), '.openclaw'),
  );
}

function pluginStateDirectory(root) {
  return path.join(root, 'plugins', 'clawtopics-link');
}

function planPath(root, setupRunId) {
  return path.join(pluginStateDirectory(root), 'gateway-restart-plans', `${setupRunId}.json`);
}

function canonicalJson(value) {
  if (value === null || typeof value !== 'object') return JSON.stringify(value);
  if (Array.isArray(value)) return `[${value.map(canonicalJson).join(',')}]`;
  return `{${Object.keys(value)
    .sort()
    .map((key) => `${JSON.stringify(key)}:${canonicalJson(value[key])}`)
    .join(',')}}`;
}

function sha256Base64Url(value) {
  return crypto.createHash('sha256').update(value).digest('base64url');
}

function sanitizeText(value, limit = 1200) {
  const normalized = String(value ?? '')
    .replace(/\u001b\[[0-9;]*m/gu, '')
    .replace(/[\r\n\t]+/gu, ' ')
    .replace(/\s{2,}/gu, ' ')
    .replace(/(Bearer\s+)[A-Za-z0-9._~-]+/giu, '$1[REDACTED]')
    .trim();
  return normalized.length <= limit ? normalized : `${normalized.slice(0, limit)}…`;
}

function extractLastJsonValue(text) {
  const source = String(text ?? '').trim();
  if (!source) return null;
  try {
    return JSON.parse(source);
  } catch {
    // Continue with line and brace scanning for noisy CLIs.
  }
  const lines = source.split(/\r?\n/u).map((line) => line.trim()).filter(Boolean).reverse();
  for (const line of lines) {
    try {
      return JSON.parse(line);
    } catch {
      // Continue.
    }
  }
  const first = source.indexOf('{');
  const last = source.lastIndexOf('}');
  if (first >= 0 && last > first) {
    try {
      return JSON.parse(source.slice(first, last + 1));
    } catch {
      return null;
    }
  }
  return null;
}

async function runCommand({ executable, args, timeoutMs = 20_000 }) {
  return new Promise((resolve, reject) => {
    let stdout = '';
    let stderr = '';
    let finished = false;
    let timedOut = false;
    const child = spawn(executable, args, {
      shell: false,
      stdio: ['ignore', 'pipe', 'pipe'],
      env: { ...process.env, NO_COLOR: '1' },
    });
    const append = (current, chunk) => {
      const combined = current + Buffer.from(chunk).toString('utf8');
      return Buffer.byteLength(combined, 'utf8') <= 256 * 1024
        ? combined
        : combined.slice(-256 * 1024);
    };
    child.stdout?.on('data', (chunk) => {
      stdout = append(stdout, chunk);
    });
    child.stderr?.on('data', (chunk) => {
      stderr = append(stderr, chunk);
    });
    const timer = setTimeout(() => {
      timedOut = true;
      child.kill('SIGTERM');
      setTimeout(() => child.kill('SIGKILL'), 1200).unref();
    }, timeoutMs);
    timer.unref();
    const settle = (callback) => {
      if (finished) return;
      finished = true;
      clearTimeout(timer);
      callback();
    };
    child.once('error', (error) =>
      settle(() =>
        reject(
          Object.assign(error, {
            stdout,
            stderr,
            timedOut,
          }),
        ),
      ),
    );
    child.once('close', (exitCode, signal) =>
      settle(() => {
        const result = { exitCode, signal, timedOut, stdout, stderr };
        if (exitCode === 0 && !timedOut) resolve(result);
        else {
          reject(
            Object.assign(
              new Error(
                timedOut
                  ? `Command timed out after ${timeoutMs}ms`
                  : `Command exited with code ${exitCode ?? 'unknown'}`,
              ),
              result,
            ),
          );
        }
      }),
    );
  });
}

async function readJson(filePath, code) {
  try {
    await access(filePath, fsConstants.R_OK);
    return JSON.parse(await readFile(filePath, 'utf8'));
  } catch {
    const error = new Error(`Required JSON file is unavailable: ${path.basename(filePath)}`);
    error.code = code;
    throw error;
  }
}

async function atomicWriteJson(filePath, value) {
  const directory = path.dirname(filePath);
  await mkdir(directory, { recursive: true, mode: 0o700 });
  await chmod(directory, 0o700).catch(() => undefined);
  const temporary = `${filePath}.${process.pid}.${crypto.randomUUID()}.tmp`;
  await writeFile(temporary, `${JSON.stringify(value, null, 2)}\n`, {
    encoding: 'utf8',
    mode: 0o600,
    flag: 'wx',
  });
  await chmod(temporary, 0o600).catch(() => undefined);
  await rename(temporary, filePath);
  await chmod(filePath, 0o600).catch(() => undefined);
}

async function updatePlan(filePath, patch) {
  const current = await readJson(filePath, 'RESTART_PLAN_UNAVAILABLE');
  const next = { ...current, ...patch, updatedAt: Date.now() };
  await atomicWriteJson(filePath, next);
  return next;
}

function nestedString(value, keys) {
  if (!value || typeof value !== 'object') return null;
  for (const [key, child] of Object.entries(value)) {
    if (keys.includes(key) && typeof child === 'string') return child;
    const nested = nestedString(child, keys);
    if (nested) return nested;
  }
  return null;
}

async function resolvePluginDirectory({ root, openclawBin, requestedPluginDir }) {
  const inspectResult = await runCommand({
    executable: openclawBin,
    args: ['plugins', 'inspect', 'clawtopics-link', '--json'],
    timeoutMs: 25_000,
  });
  const inspect = extractLastJsonValue(inspectResult.stdout);
  const plugin = inspect?.plugin;
  if (
    !plugin ||
    plugin.id !== 'clawtopics-link' ||
    plugin.version !== TARGET_PLUGIN_VERSION ||
    plugin.enabled !== true ||
    plugin.status !== 'loaded' ||
    plugin.dependencyStatus?.requiredInstalled !== true
  ) {
    const error = new Error('OpenClaw inspect did not prove the exact loaded Plugin 1.3.0');
    error.code = 'PLUGIN_COLD_INSPECT_INVALID';
    throw error;
  }
  const inspectedRoot = requiredString(plugin.rootDir, 'plugin.rootDir', 4096);
  if (!path.isAbsolute(inspectedRoot)) {
    const error = new Error('OpenClaw inspect returned a non-absolute Plugin root');
    error.code = 'PLUGIN_ROOT_INVALID';
    throw error;
  }
  let stateRoot;
  let pluginRoot;
  try {
    [stateRoot, pluginRoot] = await Promise.all([realpath(root), realpath(inspectedRoot)]);
  } catch {
    const error = new Error('OpenClaw inspect Plugin root is unavailable');
    error.code = 'PLUGIN_ROOT_UNAVAILABLE';
    throw error;
  }
  const relativePluginRoot = path.relative(stateRoot, pluginRoot);
  if (
    relativePluginRoot === '' ||
    relativePluginRoot === '..' ||
    relativePluginRoot.startsWith(`..${path.sep}`) ||
    path.isAbsolute(relativePluginRoot)
  ) {
    const error = new Error('OpenClaw inspect Plugin root escapes the state directory');
    error.code = 'PLUGIN_ROOT_OUTSIDE_STATE_DIR';
    throw error;
  }
  if (requestedPluginDir) {
    let requestedRoot;
    try {
      requestedRoot = await realpath(path.resolve(requestedPluginDir));
    } catch {
      const error = new Error('Requested Plugin root is unavailable');
      error.code = 'PLUGIN_ROOT_UNAVAILABLE';
      throw error;
    }
    if (requestedRoot !== pluginRoot) {
      const error = new Error('Requested Plugin root does not match OpenClaw inspect');
      error.code = 'PLUGIN_ROOT_MISMATCH';
      throw error;
    }
  }
  return { pluginDir: pluginRoot, inspect };
}

async function prepare(values) {
  const setupRunId = safeSetupRunId(values.get('--setup-run-id'));
  const root = stateDir(values);
  const openclawBin = values.get('--openclaw-bin') ?? 'openclaw';
  const { pluginDir, inspect } = await resolvePluginDirectory({
    root,
    openclawBin,
    requestedPluginDir: values.get('--plugin-dir'),
  });
  const packageFile = path.join(pluginDir, 'package.json');
  const manifestFile = path.join(pluginDir, 'openclaw.plugin.json');
  const identityFile = path.join(pluginStateDirectory(root), 'identity.json');
  const runtimeStatusFile = path.join(pluginStateDirectory(root), 'runtime-status.json');
  const [packageJson, manifest, identity] = await Promise.all([
    readJson(packageFile, 'PLUGIN_PACKAGE_JSON_INVALID'),
    readJson(manifestFile, 'PLUGIN_MANIFEST_INVALID'),
    readJson(identityFile, 'CONNECTOR_IDENTITY_UNREADABLE'),
  ]);
  if (
    packageJson.name !== '@clawtopics/openclaw-link' ||
    packageJson.version !== TARGET_PLUGIN_VERSION
  ) {
    const error = new Error('Persistent Plugin package is not the fixed 1.3.0 release');
    error.code = 'PLUGIN_DISK_VERSION_MISMATCH';
    throw error;
  }
  if (manifest.id !== 'clawtopics-link' || manifest.version !== TARGET_PLUGIN_VERSION) {
    const error = new Error('Plugin manifest id or version does not match 1.3.0');
    error.code = 'PLUGIN_MANIFEST_MISMATCH';
    throw error;
  }
  if (manifest.activation?.onStartup !== true) {
    const error = new Error('Plugin activation.onStartup must be true');
    error.code = 'PLUGIN_ON_STARTUP_DISABLED';
    throw error;
  }
  const entries = Array.isArray(packageJson.openclaw?.runtimeExtensions)
    ? packageJson.openclaw.runtimeExtensions
    : packageJson.openclaw?.extensions;
  if (!Array.isArray(entries) || entries.length === 0) {
    const error = new Error('Plugin has no runtime extension entry');
    error.code = 'PLUGIN_RUNTIME_ENTRY_MISSING';
    throw error;
  }
  const runtimeFiles = [];
  for (const entry of [...new Set(entries)]) {
    if (typeof entry !== 'string' || !entry.trim()) continue;
    const filePath = path.resolve(pluginDir, entry);
    if (!filePath.startsWith(`${pluginDir}${path.sep}`)) {
      const error = new Error('Plugin runtime entry escapes the package directory');
      error.code = 'PLUGIN_RUNTIME_ENTRY_INVALID';
      throw error;
    }
    const bytes = await readFile(filePath);
    runtimeFiles.push({ entry, sha256: sha256Base64Url(bytes) });
  }
  if (runtimeFiles.length === 0) {
    const error = new Error('Plugin runtime entries are unreadable');
    error.code = 'PLUGIN_RUNTIME_ENTRY_UNREADABLE';
    throw error;
  }
  if (
    typeof identity.installationId !== 'string' ||
    typeof identity.connectorId !== 'string' ||
    !identity.connectorSigningPrivateJwk
  ) {
    const error = new Error('Connector identity or durable signing credential is missing');
    error.code = 'CONNECTOR_IDENTITY_INCOMPLETE';
    throw error;
  }
  const identityMode = (await stat(identityFile)).mode & 0o777;
  if ((identityMode & 0o022) !== 0) {
    const error = new Error('Connector identity is group/world writable');
    error.code = 'CONNECTOR_IDENTITY_PERMISSIONS_UNSAFE';
    throw error;
  }
  const inspectVersion = nestedString(inspect, ['installedVersion', 'version']);
  if (inspectVersion && inspectVersion !== TARGET_PLUGIN_VERSION) {
    const error = new Error('OpenClaw cold registry reports another Plugin version');
    error.code = 'PLUGIN_COLD_INSPECT_VERSION_MISMATCH';
    throw error;
  }
  await runCommand({
    executable: openclawBin,
    args: ['config', 'validate', '--json'],
    timeoutMs: 25_000,
  });
  const configResult = await runCommand({
    executable: openclawBin,
    args: ['config', 'get', 'plugins.entries.clawtopics-link', '--json'],
    timeoutMs: 25_000,
  });
  const config = extractLastJsonValue(configResult.stdout);
  const controlApiBaseUrl = nestedString(config, ['controlApiBaseUrl']);
  if (!controlApiBaseUrl || !/^https?:\/\//u.test(controlApiBaseUrl)) {
    const error = new Error('Plugin controlApiBaseUrl is missing or invalid');
    error.code = 'PLUGIN_CONFIG_INCOMPLETE';
    throw error;
  }
  let previousRuntimeBootId = null;
  try {
    const runtimeStatus = await readJson(runtimeStatusFile, 'RUNTIME_STATUS_UNAVAILABLE');
    previousRuntimeBootId =
      typeof runtimeStatus.runtimeBootId === 'string' ? runtimeStatus.runtimeBootId : null;
  } catch {
    previousRuntimeBootId = null;
  }
  const now = Date.now();
  const plan = {
    schemaVersion: 1,
    state: 'PRE_RESTART_READY',
    setupRunId,
    installationId: identity.installationId,
    connectorId: identity.connectorId,
    targetPluginVersion: TARGET_PLUGIN_VERSION,
    previousRuntimeBootId,
    expectedCapabilities: [...EXPECTED_CAPABILITIES],
    observationTimeoutSeconds: 360,
    automaticRestartAttemptCount: 0,
    automaticRestartMaxAttempts: AUTOMATIC_RESTART_MAX_ATTEMPTS,
    noAdditionalAutomaticRestart: true,
    noReEnrollment: true,
    noRePairing: true,
    preflight: {
      packageSha256: sha256Base64Url(await readFile(packageFile)),
      manifestSha256: sha256Base64Url(await readFile(manifestFile)),
      runtimeFiles,
      identityMode: identityMode.toString(8).padStart(3, '0'),
      configValidated: true,
      controlApiOrigin: new URL(controlApiBaseUrl).origin,
    },
    createdAt: now,
    updatedAt: now,
  };
  plan.restartPlanFingerprint = sha256Base64Url(canonicalJson(plan));
  await atomicWriteJson(planPath(root, setupRunId), plan);
  process.stdout.write(
    `${JSON.stringify({
      ok: true,
      state: plan.state,
      setupRunId,
      targetPluginVersion: TARGET_PLUGIN_VERSION,
      previousRuntimeBootId,
      expectedCapabilities: plan.expectedCapabilities,
      restartPlanFingerprint: plan.restartPlanFingerprint,
      automaticRestartAttemptCount: 0,
      automaticRestartMaxAttempts: 1,
    })}\nCLAWTOPICS_PRE_RESTART_READY\n`,
  );
}

const ACCEPTED_WORDS = new Set([
  'ok',
  'accepted',
  'scheduled',
  'deferred',
  'coalesced',
  'immediate',
  'restarting',
  'in_progress',
]);

function restartStatus(value) {
  if (!value || typeof value !== 'object') return null;
  const candidates = [
    value.status,
    value.state,
    value.result,
    value.payload?.status,
    value.payload?.state,
    value.restart?.status,
    value.restart?.state,
  ];
  return candidates.find((item) => typeof item === 'string')?.toLowerCase() ?? null;
}

function classifyRestartError(error) {
  const combined = sanitizeText(
    `${error?.stdout ?? ''}\n${error?.stderr ?? ''}\n${
      error instanceof Error ? error.message : String(error)
    }`,
  );
  if (
    error?.timedOut ||
    /timed out|timeout|ETIMEDOUT|ECONNRESET|socket hang up|connection closed/iu.test(combined)
  ) {
    return {
      kind: 'unknown',
      code: 'GATEWAY_RESTART_RESULT_UNKNOWN',
      message: 'Restart result was not received; observe Presence without retrying.',
    };
  }
  return {
    kind: 'explicit_failure',
    code: /unauthorized|forbidden|operator\.admin|scope/iu.test(combined)
      ? 'GATEWAY_RESTART_NOT_AUTHORIZED'
      : 'GATEWAY_RESTART_COMMAND_FAILED',
    message: 'The single safe Gateway restart command failed.',
  };
}

async function claimSingleAttempt(filePath) {
  const lockPath = `${filePath}.attempt.lock`;
  let handle;
  try {
    handle = await open(lockPath, 'wx', 0o600);
    await handle.writeFile(`${Date.now()}\n`, 'utf8');
  } catch (error) {
    if (error?.code === 'EEXIST') {
      const duplicate = new Error('The only automatic restart attempt was already claimed');
      duplicate.code = 'AUTOMATIC_RESTART_LIMIT_REACHED';
      throw duplicate;
    }
    throw error;
  } finally {
    await handle?.close().catch(() => undefined);
  }
  const plan = await readJson(filePath, 'RESTART_PLAN_UNAVAILABLE');
  if (plan.state !== 'PRE_RESTART_READY' || plan.automaticRestartAttemptCount !== 0) {
    const duplicate = new Error('Restart Plan is not eligible for an automatic attempt');
    duplicate.code = 'AUTOMATIC_RESTART_LIMIT_REACHED';
    throw duplicate;
  }
  return updatePlan(filePath, {
    state: 'AUTO_GATEWAY_RESTART_ATTEMPTING',
    automaticRestartAttemptCount: 1,
    automaticRestartAttemptedAt: Date.now(),
  });
}

async function execute(values) {
  const setupRunId = safeSetupRunId(values.get('--setup-run-id'));
  const root = stateDir(values);
  const openclawBin = values.get('--openclaw-bin') ?? 'openclaw';
  const filePath = planPath(root, setupRunId);
  const existing = await readJson(filePath, 'RESTART_PLAN_UNAVAILABLE');
  if ((existing.automaticRestartAttemptCount ?? 0) >= 1) {
    const marker =
      existing.state === 'MANUAL_GATEWAY_RESTART_REQUIRED'
        ? 'MANUAL_GATEWAY_RESTART_REQUIRED'
        : 'CLAWTOPICS_WAITING_FOR_FRESH_GATEWAY';
    process.stdout.write(
      `${JSON.stringify({
        ok: existing.state !== 'MANUAL_GATEWAY_RESTART_REQUIRED',
        idempotent: true,
        state: existing.state,
        automaticRestartAttemptCount: 1,
        automaticRestartMaxAttempts: 1,
        noAdditionalAutomaticRestart: true,
      })}\n${marker}\n`,
    );
    return;
  }
  await claimSingleAttempt(filePath);
  const restartRequestedAt = Date.now();
  const observationDeadlineAt = restartRequestedAt + 360_000;
  await updatePlan(filePath, { restartRequestedAt, observationDeadlineAt });
  let result;
  try {
    const command = await runCommand({
      executable: openclawBin,
      args: ['gateway', 'restart', '--safe', '--json'],
      timeoutMs: 30_000,
    });
    const payload = extractLastJsonValue(`${command.stdout}\n${command.stderr}`);
    const status = restartStatus(payload);
    const accepted =
      payload?.ok === true ||
      (status !== null && ACCEPTED_WORDS.has(status)) ||
      (command.exitCode === 0 && payload?.ok !== false);
    result = accepted
      ? { kind: 'accepted', code: 'AUTO_GATEWAY_RESTART_ACCEPTED', status }
      : {
          kind: 'explicit_failure',
          code: 'GATEWAY_RESTART_REQUEST_REJECTED',
          message: 'OpenClaw did not accept the restart request.',
        };
  } catch (error) {
    result = classifyRestartError(error);
  }
  if (result.kind === 'accepted' || result.kind === 'unknown') {
    await updatePlan(filePath, {
      state: 'WAITING_FOR_FRESH_GATEWAY',
      restartRequestResult: result.kind,
      restartRequestedAt,
      observationDeadlineAt,
      lastErrorCode: result.kind === 'unknown' ? result.code : null,
    });
    process.stdout.write(
      `${JSON.stringify({
        ok: true,
        state: 'WAITING_FOR_FRESH_GATEWAY',
        code: result.code,
        automaticRestartAttemptCount: 1,
        automaticRestartMaxAttempts: 1,
        noAdditionalAutomaticRestart: true,
        observationDeadlineAt,
      })}\nCLAWTOPICS_WAITING_FOR_FRESH_GATEWAY\n`,
    );
    return;
  }
  await updatePlan(filePath, {
    state: 'MANUAL_GATEWAY_RESTART_REQUIRED',
    restartRequestResult: 'failed',
    lastErrorCode: result.code,
    manualAction: {
      required: true,
      code: 'MANUAL_GATEWAY_RESTART_REQUIRED',
      primaryAction: {
        type: 'resume_after_manual_restart',
        label: '我已重启，继续检查',
      },
    },
  });
  process.stdout.write(
    `${JSON.stringify({
      ok: false,
      state: 'MANUAL_GATEWAY_RESTART_REQUIRED',
      code: result.code,
      message: result.message,
      automaticRestartAttemptCount: 1,
      automaticRestartMaxAttempts: 1,
      noAdditionalAutomaticRestart: true,
    })}\nMANUAL_GATEWAY_RESTART_REQUIRED\n`,
  );
  process.exitCode = 1;
}

async function main() {
  const { operation, values } = parseArgs(process.argv.slice(2));
  if (operation === 'prepare') return prepare(values);
  if (operation === 'execute') return execute(values);
  throw Object.assign(new Error('Use prepare or execute'), { code: 'REQUEST_INVALID' });
}

main().catch((error) => {
  const code = typeof error?.code === 'string' ? error.code : 'GATEWAY_RESTART_SKILL_FAILED';
  process.stderr.write(
    `${JSON.stringify({
      ok: false,
      code,
      message: sanitizeText(error instanceof Error ? error.message : String(error)),
    })}\nPLUGIN_PRE_RESTART_FAILED\n`,
  );
  process.exitCode = 1;
});
