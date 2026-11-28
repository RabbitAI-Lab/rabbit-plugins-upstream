#!/usr/bin/env node
/**
 * Launcher tests for bin/yotta-present.js (no external dependencies).
 *
 * Checks: version, help, command resolution, installer delegation and an
 * MCP initialize round-trip over stdio.
 */
'use strict';
const assert = require('assert');
const path = require('path');
const { spawn, spawnSync } = require('child_process');

const ROOT = path.join(__dirname, '..');
const LAUNCHER = path.join(ROOT, 'bin', 'yotta-present.js');
const pkg = require(path.join(ROOT, 'package.json'));

let checks = 0;
function check(name, fn) {
  fn();
  checks += 1;
  process.stdout.write('ok - ' + name + '\n');
}

function run(args) {
  return spawnSync(process.execPath, [LAUNCHER].concat(args), {
    cwd: ROOT,
    encoding: 'utf8',
    timeout: 30000,
  });
}

function initializeRoundTrip() {
  return new Promise(function (resolve, reject) {
    const child = spawn(process.execPath, [LAUNCHER], { cwd: ROOT, stdio: ['pipe', 'pipe', 'pipe'] });
    let out = '';
    let err = '';
    const timer = setTimeout(function () {
      child.kill();
      reject(new Error('MCP initialize timed out; stderr=' + err));
    }, 30000);
    child.stdout.on('data', function (chunk) {
      out += chunk.toString('utf8');
      const line = out.split(/\r?\n/).filter(Boolean)[0];
      if (!line) return;
      clearTimeout(timer);
      child.kill();
      try {
        resolve(JSON.parse(line));
      } catch (error) {
        reject(new Error('invalid JSON from server: ' + line));
      }
    });
    child.stderr.on('data', function (chunk) { err += chunk.toString('utf8'); });
    child.on('error', function (error) {
      clearTimeout(timer);
      reject(error);
    });
    child.stdin.write(JSON.stringify({
      jsonrpc: '2.0',
      id: 1,
      method: 'initialize',
      params: {
        protocolVersion: '2025-11-25',
        capabilities: {},
        clientInfo: { name: 'launcher-test', version: '1' },
      },
    }) + '\n');
  });
}

async function main() {
  check('--version prints package version', function () {
    const result = run(['--version']);
    assert.strictEqual(result.status, 0, result.stderr);
    assert.strictEqual(result.stdout.trim(), pkg.version);
  });

  check('--help documents MCP start and install modes', function () {
    const result = run(['--help']);
    assert.strictEqual(result.status, 0, result.stderr);
    assert.ok(/stdio MCP server/.test(result.stdout), result.stdout);
    assert.ok(/--agent/.test(result.stdout), result.stdout);
  });

  check('--print-command resolves the Python server script', function () {
    const result = run(['--print-command']);
    assert.strictEqual(result.status, 0, result.stderr);
    assert.ok(/yotta_present_mcp\.py/.test(result.stdout), result.stdout);
    assert.ok(/\S+\s+\S+yotta_present_mcp\.py/.test(result.stdout), result.stdout);
  });

  check('install flags delegate to the installer', function () {
    const result = run(['--list']);
    assert.strictEqual(result.status, 0, result.stderr);
    assert.ok(result.stdout.trim().length > 0, 'installer produced no output');
  });

  await (async function () {
    const response = await initializeRoundTrip();
    check('MCP initialize returns the server identity', function () {
      assert.ok(response.result, JSON.stringify(response));
      assert.strictEqual(response.result.serverInfo.name, 'yotta-present');
      assert.strictEqual(response.result.serverInfo.version, pkg.version);
    });
  }());

  process.stdout.write('bin launcher: ' + checks + ' checks passed\n');
}

main().catch(function (error) {
  process.stderr.write('bin launcher FAILED: ' + (error && error.stack || error) + '\n');
  process.exit(1);
});
