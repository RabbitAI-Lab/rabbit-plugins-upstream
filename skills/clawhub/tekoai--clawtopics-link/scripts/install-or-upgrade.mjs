#!/usr/bin/env node

import { spawn } from 'node:child_process';
import { createHash } from 'node:crypto';
import { access, mkdir, open, readFile, rename, rm, stat } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { pathToFileURL } from 'node:url';

export const PLUGIN_VERSION = '1.3.0';
export const PLUGIN_ID = 'clawtopics-link';
export const PLUGIN_PACKAGE = '@clawtopics/openclaw-link';
export const CONTROL_API_BASE_URL = 'https://openclaw.tekoai.com/api';
export const ARTIFACT_NAME = `clawtopics-openclaw-link-${PLUGIN_VERSION}.tgz`;
export const ARTIFACT_URL =
  `https://github.com/TekoAI/clawtopics-openclaw-link/releases/download/` +
  `v${PLUGIN_VERSION}/${ARTIFACT_NAME}`;
export const ARTIFACT_SHA256 = 'e0ec1052729eb1e505b9511641490319331b02b4360747301fdb57abf99d2728';

const MAX_ARTIFACT_BYTES = 10 * 1024 * 1024;
const COMMAND_TIMEOUT_MS = 25_000;
const INSTALL_TIMEOUT_MS = 180_000;

class InstallError extends Error {
  constructor(message, marker = 'PLUGIN_PREINSTALL_REQUIRED') {
    super(message);
    this.marker = marker;
  }
}

function safeStage(stage, details = {}) {
  process.stderr.write(
    `${JSON.stringify({ source: 'clawtopics-link-installer', stage, ...details })}\n`,
  );
}

export function resolveStateDir(environment = process.env) {
  return path.resolve(
    environment.OPENCLAW_STATE_DIR ??
      environment.OPENCLAW_HOME ??
      path.join(os.homedir(), '.openclaw'),
  );
}

async function writableDirectory(directory) {
  try {
    await mkdir(directory, { recursive: true, mode: 0o700 });
    const probe = path.join(directory, `.write-${process.pid}-${Date.now()}`);
    const handle = await open(probe, 'wx', 0o600);
    await handle.close();
    await rm(probe, { force: true });
    return true;
  } catch {
    return false;
  }
}

export async function selectCacheDirectory({
  cwd = process.cwd(),
  tmpDir = process.env.TMPDIR,
  fallback = '/tmp',
} = {}) {
  const candidates = [
    path.join(cwd, '.clawtopics-plugin-cache'),
    ...(tmpDir ? [path.join(tmpDir, 'clawtopics-plugin-cache')] : []),
    ...(fallback ? [path.join(fallback, 'clawtopics-plugin-cache')] : []),
  ];
  for (const candidate of [...new Set(candidates.map((value) => path.resolve(value)))]) {
    if (await writableDirectory(candidate)) return candidate;
  }
  throw new InstallError('No writable bounded plugin cache', 'PLUGIN_LOCAL_CACHE_UNAVAILABLE');
}

export async function sha256File(filePath) {
  const bytes = await readFile(filePath);
  return createHash('sha256').update(bytes).digest('hex');
}

async function optionalSha256(filePath) {
  try {
    return await sha256File(filePath);
  } catch (error) {
    if (error?.code === 'ENOENT') return null;
    throw error;
  }
}

export async function runCommand(command, args, options = {}) {
  const timeoutMs = options.timeoutMs ?? COMMAND_TIMEOUT_MS;
  return await new Promise((resolve, reject) => {
    const child = spawn(command, args, {
      cwd: options.cwd,
      env: options.env ?? process.env,
      stdio: ['ignore', 'pipe', 'pipe'],
    });
    let stdout = '';
    let stderr = '';
    let timedOut = false;
    const timer = setTimeout(() => {
      timedOut = true;
      child.kill('SIGTERM');
      setTimeout(() => child.kill('SIGKILL'), 1_000).unref();
    }, timeoutMs);
    child.stdout.on('data', (chunk) => {
      stdout += chunk.toString();
    });
    child.stderr.on('data', (chunk) => {
      stderr += chunk.toString();
    });
    child.on('error', (error) => {
      clearTimeout(timer);
      reject(error);
    });
    child.on('close', (code, signal) => {
      clearTimeout(timer);
      if (code === 0 && !timedOut) {
        resolve({ stdout, stderr });
        return;
      }
      const error = new Error(
        timedOut
          ? `bounded command timed out: ${args.slice(0, 2).join(' ')}`
          : `bounded command failed: ${args.slice(0, 2).join(' ')} (${code ?? signal})`,
      );
      error.stdout = stdout;
      error.stderr = stderr;
      error.timedOut = timedOut;
      reject(error);
    });
  });
}

async function downloadArtifact(targetPath, fetchImpl = fetch) {
  if ((await optionalSha256(targetPath)) === ARTIFACT_SHA256) return targetPath;
  const partPath = `${targetPath}.part`;
  await rm(partPath, { force: true });
  let lastError;
  for (let attempt = 1; attempt <= 3; attempt += 1) {
    try {
      const response = await fetchImpl(ARTIFACT_URL, {
        redirect: 'follow',
        signal: AbortSignal.timeout(30_000),
      });
      if (!response.ok) throw new Error(`download returned HTTP ${response.status}`);
      const bytes = Buffer.from(await response.arrayBuffer());
      if (bytes.length === 0 || bytes.length > MAX_ARTIFACT_BYTES) {
        throw new Error('downloaded artifact size is outside bounds');
      }
      const handle = await open(partPath, 'w', 0o600);
      try {
        await handle.writeFile(bytes);
        await handle.sync();
      } finally {
        await handle.close();
      }
      if ((await sha256File(partPath)) !== ARTIFACT_SHA256) {
        throw new Error('downloaded artifact checksum mismatch');
      }
      await rename(partPath, targetPath);
      return targetPath;
    } catch (error) {
      lastError = error;
      await rm(partPath, { force: true });
    }
  }
  throw new InstallError(`Fixed plugin download failed: ${lastError?.message ?? 'unknown'}`);
}

function parseJsonOutput(output) {
  try {
    const value = JSON.parse(output.trim());
    if (value && typeof value === 'object') return value;
  } catch {
    // Fall through for CLIs that prefix their JSON with diagnostics.
  }
  for (let start = 0; start < output.length; start += 1) {
    const opening = output[start];
    if (opening !== '{' && opening !== '[') continue;
    const stack = [];
    let inString = false;
    let escaped = false;
    for (let index = start; index < output.length; index += 1) {
      const character = output[index];
      if (inString) {
        if (escaped) escaped = false;
        else if (character === '\\') escaped = true;
        else if (character === '"') inString = false;
        continue;
      }
      if (character === '"') {
        inString = true;
        continue;
      }
      if (character === '{') stack.push('}');
      else if (character === '[') stack.push(']');
      else if (character === '}' || character === ']') {
        if (stack.pop() !== character) break;
        if (stack.length === 0) {
          try {
            const value = JSON.parse(output.slice(start, index + 1));
            if (value && typeof value === 'object') return value;
          } catch {
            break;
          }
        }
      }
    }
  }
  return null;
}

function installedPluginRecord(payload) {
  const plugins = Array.isArray(payload?.plugins) ? payload.plugins : [];
  return (
    plugins.find(
      (plugin) =>
        plugin &&
        typeof plugin === 'object' &&
        plugin.id === PLUGIN_ID &&
        plugin.version === PLUGIN_VERSION &&
        plugin.status === 'loaded' &&
        plugin.enabled === true &&
        plugin.dependencyStatus?.requiredInstalled === true,
    ) ?? null
  );
}

async function confirmInstalledPlugin(openclawBin, runner) {
  const result = await runner(openclawBin, ['plugins', 'list', '--json']);
  return installedPluginRecord(parseJsonOutput(result.stdout));
}

function parseVersion(output) {
  const match = output.match(/\b(\d{4})\.(\d+)\.(\d+)\b/u);
  return match ? match.slice(1, 4).map(Number) : null;
}

function supportedHostVersion(version) {
  if (!version) return false;
  const [year, month, patch] = version;
  return year === 2026 && month === 7 && patch >= 1;
}

export async function inspectArtifact(artifactPath, runner = runCommand) {
  const digest = await sha256File(artifactPath);
  if (digest !== ARTIFACT_SHA256) {
    throw new InstallError('Fixed plugin artifact checksum mismatch');
  }
  const packageResult = await runner('tar', ['-xOf', artifactPath, 'package/package.json']);
  const manifestResult = await runner('tar', [
    '-xOf',
    artifactPath,
    'package/openclaw.plugin.json',
  ]);
  const packageJson = JSON.parse(packageResult.stdout);
  const manifest = JSON.parse(manifestResult.stdout);
  if (
    packageJson.name !== PLUGIN_PACKAGE ||
    packageJson.version !== PLUGIN_VERSION ||
    manifest.id !== PLUGIN_ID ||
    manifest.version !== PLUGIN_VERSION
  ) {
    throw new InstallError('Fixed plugin package metadata mismatch');
  }
  return { digest, packageJson, manifest };
}

async function runtimeMarker(openclawBin, runner) {
  for (let attempt = 0; attempt < 2; attempt += 1) {
    try {
      const result = await runner(openclawBin, [PLUGIN_ID, 'status', '--json']);
      const status = parseJsonOutput(result.stdout);
      const runtimeVersion = status?.runtime?.pluginVersion ?? status?.pluginVersion;
      if (runtimeVersion === PLUGIN_VERSION) return 'CLAWTOPICS_PLUGIN_RUNTIME_CURRENT';
    } catch {
      // A cold runtime is expected after replacing plugin code.
    }
  }
  return 'CLAWTOPICS_PLUGIN_RESTART_REQUIRED';
}

export async function installOrUpgrade({
  artifactPath,
  stateDir = resolveStateDir(),
  openclawBin = process.env.OPENCLAW_BIN ?? 'openclaw',
  runner = runCommand,
  artifactInspector = inspectArtifact,
  artifactDownloader = downloadArtifact,
  cacheSelector = selectCacheDirectory,
} = {}) {
  const version = await runner(openclawBin, ['--version']);
  if (!supportedHostVersion(parseVersion(`${version.stdout}\n${version.stderr}`))) {
    throw new InstallError('OpenClaw host version is outside the supported range');
  }

  const cacheDir = artifactPath ? path.dirname(artifactPath) : await cacheSelector();
  const fixedArtifact =
    artifactPath ?? (await artifactDownloader(path.join(cacheDir, ARTIFACT_NAME)));
  await artifactInspector(fixedArtifact, runner);

  const identityPath = path.join(stateDir, 'plugins', PLUGIN_ID, 'identity.json');
  const identityBefore = await optionalSha256(identityPath);
  safeStage('artifact_verified', { version: PLUGIN_VERSION });
  let installCommandError = null;
  try {
    await runner(openclawBin, ['plugins', 'install', `npm-pack:${fixedArtifact}`, '--force'], {
      timeoutMs: INSTALL_TIMEOUT_MS,
    });
  } catch (error) {
    installCommandError = error;
  }
  const installedPlugin = await confirmInstalledPlugin(openclawBin, runner);
  if (installedPlugin === null) {
    throw new InstallError(
      installCommandError === null
        ? 'Plugin install completed without an exact loaded Plugin record'
        : 'Plugin install command failed and no exact loaded Plugin record was found',
    );
  }
  if (installCommandError !== null) {
    safeStage('plugin_install_confirmed_after_cli_warning', {
      version: PLUGIN_VERSION,
      status: 'loaded',
    });
  }
  const identityAfter = await optionalSha256(identityPath);
  if (identityBefore !== null && identityAfter !== identityBefore) {
    throw new InstallError(
      'Connector identity changed during plugin replacement',
      'PLUGIN_INSTALL_POLICY_DENIED',
    );
  }
  safeStage('plugin_replaced', { identityPreserved: identityBefore !== null });

  try {
    await runner(openclawBin, [
      'config',
      'set',
      `plugins.entries.${PLUGIN_ID}.config.controlApiBaseUrl`,
      JSON.stringify(CONTROL_API_BASE_URL),
      '--strict-json',
    ]);
  } catch {
    safeStage('config_deferred', { defaultControlApiBaseUrl: true });
  }
  await runner(openclawBin, ['plugins', 'enable', PLUGIN_ID]);
  try {
    await runner(openclawBin, [PLUGIN_ID, 'reconnect', '--json']);
  } catch {
    safeStage('plugin_reconnect_deferred');
  }
  return await runtimeMarker(openclawBin, runner);
}

async function main() {
  try {
    const marker = await installOrUpgrade();
    process.stdout.write(`${marker}\n`);
  } catch (error) {
    const marker = error instanceof InstallError ? error.marker : 'PLUGIN_PREINSTALL_REQUIRED';
    safeStage('failed', { errorType: error?.constructor?.name ?? 'Error' });
    process.stdout.write(`${marker}\n`);
    process.exitCode = 1;
  }
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  await main();
}
