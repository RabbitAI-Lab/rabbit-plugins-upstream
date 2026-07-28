'use strict';

const os = require('node:os');
const path = require('node:path');
const fs = require('node:fs');
const crypto = require('node:crypto');

/**
 * Local credential store for JGY phone-login tokens.
 *
 * Layout (master design §8.2 / skill plan §6):
 *   ~/.jinguyuan/               dir 0700
 *     jgy-auth.json             file 0600, atomic write
 *     device-id                 file 0600, stable per install
 *
 * MVP uses the file fallback (no OS keychain dependency). The verification code is never stored;
 * the full phone is never stored (only a display mask). Writes are atomic (temp file + rename).
 *
 * The base directory is overridable via JGY_HOME (used by tests) so nothing touches the real home.
 */

const CRED_VERSION = 1;

function baseDir() {
  return process.env.JGY_HOME || path.join(os.homedir(), '.jinguyuan');
}

function credPath() {
  return path.join(baseDir(), 'jgy-auth.json');
}

function deviceIdPath() {
  return path.join(baseDir(), 'device-id');
}

function ensureDir() {
  const dir = baseDir();
  fs.mkdirSync(dir, { recursive: true, mode: 0o700 });
  // mkdir mode is subject to umask; enforce 0700 explicitly.
  try { fs.chmodSync(dir, 0o700); } catch { /* best effort on non-POSIX */ }
  return dir;
}

function atomicWrite(file, contents) {
  ensureDir();
  const tmp = `${file}.${process.pid}.${crypto.randomBytes(6).toString('hex')}.tmp`;
  fs.writeFileSync(tmp, contents, { mode: 0o600 });
  try { fs.chmodSync(tmp, 0o600); } catch { /* best effort */ }
  fs.renameSync(tmp, file);
  try { fs.chmodSync(file, 0o600); } catch { /* best effort */ }
}

/**
 * Stable, non-personal per-install device id. Created on first use and reused thereafter, so it
 * survives logout (which only clears jgy-auth.json). Never derived from user data.
 */
function getOrCreateDeviceId() {
  const file = deviceIdPath();
  try {
    const existing = fs.readFileSync(file, 'utf8').trim();
    if (existing) return existing;
  } catch { /* not created yet */ }
  const id = `dev_${crypto.randomBytes(16).toString('hex')}`;
  atomicWrite(file, id);
  return id;
}

function read() {
  try {
    const raw = fs.readFileSync(credPath(), 'utf8');
    const parsed = JSON.parse(raw);
    if (!parsed || parsed.version !== CRED_VERSION) return null;
    return parsed;
  } catch {
    return null;
  }
}

function write(creds) {
  const payload = { version: CRED_VERSION, updated_at: new Date().toISOString(), ...creds };
  atomicWrite(credPath(), JSON.stringify(payload));
  return payload;
}

function clear() {
  try { fs.rmSync(credPath(), { force: true }); } catch { /* already gone */ }
}

/** Test/introspection helper: current file mode as octal string (e.g. "600"), or null. */
function fileMode(file = credPath()) {
  try {
    return (fs.statSync(file).mode & 0o777).toString(8);
  } catch {
    return null;
  }
}

module.exports = {
  CRED_VERSION,
  baseDir,
  credPath,
  deviceIdPath,
  getOrCreateDeviceId,
  read,
  write,
  clear,
  fileMode,
};
