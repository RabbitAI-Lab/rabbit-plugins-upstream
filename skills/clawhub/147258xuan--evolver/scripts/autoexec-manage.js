#!/usr/bin/env node
/**
 * autoexec-manage.js — Start/stop/status for evolver autoexec daemon (V2 self-learning loop).
 *
 * Usage:
 *   node skills/evolver/scripts/autoexec-manage.js status   # check daemon + material health
 *   node skills/evolver/scripts/autoexec-manage.js start    # start daemon (session dirs auto-set)
 *   node skills/evolver/scripts/autoexec-manage.js stop     # stop daemon (removes lock)
 *
 * Requires config at ~/.evomap/autoexec/config.json with allowedRoots.
 */

const { execSync, spawn } = require('child_process');
const fs = require('fs');
const path = require('path');
const os = require('os');

const HOME = os.homedir();
const AUTOEXEC_DIR = path.join(HOME, '.evomap', 'autoexec');
const LOCK = path.join(AUTOEXEC_DIR, 'autoexec.lock');
const SESSION_DIRS = path.join(process.cwd(), 'memory', 'evolution');

function log(msg) { console.log(`[autoexec-manage] ${msg}`); }

function isRunning() {
  try {
    const out = execSync('Get-CimInstance Win32_Process -Filter "Name=\'node.exe\'" | Select-Object -ExpandProperty CommandLine', { encoding: 'utf-8', shell: 'powershell' });
    return out.includes('evolver.js autoexec');
  } catch { return false; }
}

function main() {
  const cmd = process.argv[2] || 'status';

  if (cmd === 'status') {
    const running = isRunning();
    const hasLock = fs.existsSync(LOCK);
    const hasConfig = fs.existsSync(path.join(AUTOEXEC_DIR, 'config.json'));
    log(`daemon running: ${running}`);
    log(`lock present: ${hasLock}`);
    log(`config present: ${hasConfig}`);
    log(`session dirs: ${SESSION_DIRS}`);
    if (hasConfig) {
      const cfg = JSON.parse(fs.readFileSync(path.join(AUTOEXEC_DIR, 'config.json'), 'utf-8'));
      log(`allowedRoots: ${JSON.stringify(cfg.allowedRoots)}`);
    }
    return;
  }

  if (cmd === 'start') {
    if (isRunning()) { log('already running'); return; }
    if (fs.existsSync(LOCK)) { fs.unlinkSync(LOCK); log('removed stale lock'); }
    log('starting autoexec daemon...');
    const child = spawn('powershell', ['-NoProfile', '-Command',
      `$env:EVOLVER_SESSION_DIRS='${SESSION_DIRS}'; evolver autoexec`], {
      detached: true, stdio: 'ignore', shell: false,
    });
    child.unref();
    log('started (detached). check `node autoexec-manage.js status` in a few seconds.');
    return;
  }

  if (cmd === 'stop') {
    try {
      const out = execSync('Get-CimInstance Win32_Process -Filter "Name=\'node.exe\'" | Where-Object { $_.CommandLine -match \'evolver.js autoexec\' } | ForEach-Object { $_.ProcessId }', { encoding: 'utf-8', shell: 'powershell' });
      const pids = out.trim().split(/\s+/).filter(Boolean);
      for (const pid of pids) {
        execSync(`Stop-Process -Id ${pid} -Force`, { shell: 'powershell' });
        log(`killed pid ${pid}`);
      }
    } catch { log('no daemon process found'); }
    if (fs.existsSync(LOCK)) { fs.unlinkSync(LOCK); log('removed lock'); }
    return;
  }

  log(`unknown command: ${cmd} (use status|start|stop)`);
}

main();
