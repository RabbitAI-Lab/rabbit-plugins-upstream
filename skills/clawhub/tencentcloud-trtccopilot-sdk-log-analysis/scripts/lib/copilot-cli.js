import { spawnSync } from 'node:child_process';

const REGISTRY = 'https://mirrors.tencent.com/npm';
const PACKAGE = '@tencent/trtccopilot-cli';

function commandExists(bin, env) {
  const probe = spawnSync(bin, ['--version'], { encoding: 'utf-8', env });
  return !probe.error && probe.status === 0;
}

// Resolve how to invoke the trtccopilot CLI:
// 1. A global `trtccopilot` already on PATH (after `npm i -g`).
// 2. npx fallback pinned to the Tencent internal registry.
export function resolveCopilotCommand({ env = process.env } = {}) {
  if (commandExists('trtccopilot', env)) {
    return { mode: 'global', command: 'trtccopilot', prefixArgs: [] };
  }
  return { mode: 'npx', command: 'npx', prefixArgs: ['--yes', '--registry', REGISTRY, PACKAGE] };
}

// Call an agent-accessible API through the CLI: `<cmd> api call <method> <path> [--data <json>]`.
// Returns the parsed JSON body. Throws on spawn error, non-zero exit, or unparseable output.
export function callApi(method, apiPath, { data, env = process.env, timeoutMs } = {}) {
  const resolved = resolveCopilotCommand({ env });
  const args = [...resolved.prefixArgs, 'api', 'call', method, apiPath];
  if (data != null) {
    args.push('--data', typeof data === 'string' ? data : JSON.stringify(data));
  }

  const result = spawnSync(resolved.command, args, {
    env,
    encoding: 'utf-8',
    timeout: timeoutMs,
    maxBuffer: 64 * 1024 * 1024,
  });

  if (result.error) {
    throw new Error(`trtccopilot call failed (${resolved.mode}): ${result.error.message}`);
  }
  const stdout = (result.stdout || '').trim();
  const stderr = (result.stderr || '').trim();
  if (result.status !== 0) {
    const details = [stderr, stdout].filter(Boolean).join('\n').trim();
    throw new Error(`trtccopilot ${method} ${apiPath} failed (exit ${result.status}): ${details}`);
  }
  // The CLI prints a non-JSON banner (e.g. "HTTP 404 ...") on backend errors.
  if (!stdout.startsWith('{') && !stdout.startsWith('[')) {
    throw new Error(`trtccopilot ${method} ${apiPath} returned non-JSON output: ${stdout || '(empty)'}`);
  }
  try {
    return JSON.parse(stdout);
  } catch (err) {
    throw new Error(`trtccopilot ${method} ${apiPath} produced invalid JSON: ${err.message}`);
  }
}
