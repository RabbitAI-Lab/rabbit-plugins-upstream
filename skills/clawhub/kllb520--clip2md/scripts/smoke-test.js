#!/usr/bin/env node

const assert = require('assert');
const { spawnSync } = require('child_process');
const fs = require('fs');
const http = require('http');
const os = require('os');
const path = require('path');

const skillDir = path.resolve(__dirname, '..');
const cli = path.join(skillDir, 'scripts', 'clip2md.js');
const home = fs.mkdtempSync(path.join(os.tmpdir(), 'clip2md-skill-'));
const cleanupDirs = [home];
let server;
let baseUrl;
let waitHits = 0;
const sockets = new Set();

function task(overrides = {}) {
  return {
    id: 42,
    url: 'https://example.com/article',
    status: 'SUCCESS',
    title: 'Example Article',
    note_markdown_content: '# Example',
    asset_count: 2,
    asset_ready_count: 2,
    asset_pending_count: 0,
    asset_failed_count: 0,
    content_version: 1,
    note_content_version: 1,
    created_at: new Date().toISOString(),
    updated_at: new Date().toISOString(),
    ...overrides,
  };
}

function send(res, statusCode, body, headers = {}) {
  res.writeHead(statusCode, { 'content-type': 'application/json', connection: 'close', ...headers });
  res.end(JSON.stringify(body));
}

function createServer() {
  return http.createServer((req, res) => {
    if (req.headers.authorization !== 'Bearer test-token') {
      send(res, 401, { detail: 'invalid token' });
      return;
    }

    if (req.method === 'GET' && req.url === '/api/v1/auth/me') {
      send(res, 200, { daily_quota: 3, permanent_quota: 7 });
      return;
    }

    if (req.method === 'POST' && req.url === '/api/v1/tasks') {
      send(res, 200, task({
        id: 100,
        status: 'PENDING',
        title: null,
        note_markdown_content: null,
        asset_ready_count: 0,
        asset_pending_count: 2,
      }));
      return;
    }

    if (req.method === 'GET' && req.url === '/api/v1/tasks/100') {
      send(res, 200, task({ id: 100 }));
      return;
    }

    if (req.method === 'GET' && req.url === '/api/v1/tasks/101') {
      send(res, 200, task({
        id: 101,
        status: 'FAILED_AUTH_EXPIRED',
        error_msg: '账号授权失效',
        error_category: 'auth',
        note_markdown_content: null,
      }));
      return;
    }

    if (req.method === 'GET' && req.url === '/api/v1/tasks/102') {
      send(res, 200, task({ id: 102, status: 'PAUSED_BY_SERVICE' }));
      return;
    }

    if (req.method === 'GET' && req.url === '/api/v1/tasks/103') {
      send(res, 200, task({ id: 103, status: 'PROCESSING', note_markdown_content: null }));
      return;
    }

    if (req.method === 'GET' && req.url === '/api/v1/tasks/104') {
      waitHits += 1;
      send(res, 200, task({
        id: 104,
        status: waitHits >= 2 ? 'SUCCESS' : 'PROCESSING',
        note_markdown_content: waitHits >= 2 ? '# Done' : null,
      }));
      return;
    }

    send(res, 404, { detail: 'not found' });
  });
}

function run(args, extraEnv = {}) {
  const result = spawnSync(process.execPath, [cli, ...args], {
    cwd: skillDir,
    env: {
      ...process.env,
      HOME: home,
      CLIP2MD_API_BASE: baseUrl,
      ...extraEnv,
    },
    encoding: 'utf8',
    timeout: 10000,
  });
  if (result.error) {
    result.stderr = `${result.stderr || ''}\n${result.error.message} while running: ${args.join(' ')}`;
  }
  return result;
}

function parseJsonOutput(result) {
  const output = result.stdout.trim() || result.stderr.trim();
  return JSON.parse(output);
}

async function listen() {
  server = createServer();
  server.on('connection', (socket) => {
    sockets.add(socket);
    socket.on('close', () => sockets.delete(socket));
  });
  await new Promise((resolve) => server.listen(0, '127.0.0.1', resolve));
  const address = server.address();
  baseUrl = `http://127.0.0.1:${address.port}/api/v1`;
}

async function close() {
  if (server) {
    for (const socket of sockets) {
      socket.destroy();
    }
    await new Promise((resolve) => server.close(resolve));
  }
  for (const dir of cleanupDirs) {
    fs.rmSync(dir, { recursive: true, force: true });
  }
}

(async () => {
  try {
    await listen();

    let result = run(['quota', '--json']);
    assert.strictEqual(result.status, 1);
    assert.match(result.stderr, /未配置 token/);

    result = run(['config', 'test-token', '--json']);
    assert.strictEqual(result.status, 0, result.stderr);
    const configFile = path.join(home, '.clip2md', 'config.json');
    assert.strictEqual((fs.statSync(path.dirname(configFile)).mode & 0o777), 0o700);
    assert.strictEqual((fs.statSync(configFile).mode & 0o777), 0o600);
    assert.doesNotMatch(result.stdout + result.stderr, /test-token/);

    result = run(['quota', '--json']);
    assert.strictEqual(result.status, 0, result.stderr);
    assert.deepStrictEqual(parseJsonOutput(result), {
      ok: true,
      daily_quota: 3,
      permanent_quota: 7,
    });

    result = run(['clip', 'https://example.com/article', '--json']);
    assert.strictEqual(result.status, 0, result.stderr);
    const clip = parseJsonOutput(result);
    assert.strictEqual(clip.task.id, 100);
    assert.strictEqual(clip.task.status, 'PENDING');
    assert.strictEqual(clip.quota.daily_quota, 3);

    result = run(['status', '100', '--json']);
    assert.strictEqual(result.status, 0, result.stderr);
    assert.strictEqual(parseJsonOutput(result).task.markdown_ready, true);

    result = run(['status', '101', '--json']);
    assert.strictEqual(result.status, 2);
    assert.strictEqual(parseJsonOutput(result).task.status_kind, 'failure');

    result = run(['status', '102', '--json']);
    assert.strictEqual(result.status, 4);
    assert.strictEqual(parseJsonOutput(result).task.status_kind, 'unknown');

    result = run(['wait', '104', '--timeout', '3', '--interval', '1', '--json']);
    assert.strictEqual(result.status, 0, result.stderr);
    assert.strictEqual(parseJsonOutput(result).outcome, 'success');

    const started = Date.now();
    result = run(['wait', '103', '--timeout', '1', '--interval', '5', '--json']);
    const elapsed = Date.now() - started;
    assert.strictEqual(result.status, 3);
    assert.strictEqual(parseJsonOutput(result).outcome, 'timeout');
    assert(elapsed < 2500, `wait exceeded timeout guard: ${elapsed}ms`);

    const missingTokenHome = fs.mkdtempSync(path.join(os.tmpdir(), 'clip2md-missing-token-'));
    cleanupDirs.push(missingTokenHome);
    result = run(['status', '100', '--json'], { HOME: missingTokenHome });
    assert.strictEqual(result.status, 1);
    assert.match(result.stderr, /未配置 token/);

    const invalidTokenHome = fs.mkdtempSync(path.join(os.tmpdir(), 'clip2md-bad-token-'));
    cleanupDirs.push(invalidTokenHome);
    result = run(['config', 'bad-token', '--json'], { HOME: invalidTokenHome });
    assert.strictEqual(result.status, 0, result.stderr);
    result = run(['status', '100', '--json'], { HOME: invalidTokenHome });
    assert.strictEqual(result.status, 1);
    const invalidTokenError = parseJsonOutput(result);
    assert.strictEqual(invalidTokenError.error.status, 401);
    assert.doesNotMatch(result.stdout + result.stderr, /bad-token/);

    console.log('clip2md smoke tests passed');
  } finally {
    await close();
  }
})().catch((error) => {
  console.error(error);
  process.exit(1);
});
