#!/usr/bin/env node
/**
 * lock.js — File-based lock for Bidding Hunter idempotency.
 *
 * Prevents concurrent pipeline runs. Stale locks (>2 hours) are broken.
 */

const fs = require('fs');
const path = require('path');

const LOCK_TIMEOUT_MS = 2 * 60 * 60 * 1000; // 2 hours
const LOCK_FILENAME = '.bidding-hunter.lock';

function lockPath(config) {
  const base = config.database?.path || '~/.bidding-hunter/data.db';
  const resolved = resolvePath(base);
  return path.join(path.dirname(resolved), LOCK_FILENAME);
}

function acquire(config) {
  const file = lockPath(config);
  fs.mkdirSync(path.dirname(file), { recursive: true });

  try {
    // Try to create lock file exclusively
    const fd = fs.openSync(file, 'wx');
    fs.writeFileSync(fd, JSON.stringify({
      pid: process.pid,
      startedAt: new Date().toISOString(),
    }));
    fs.closeSync(fd);
    return true;
  } catch (error) {
    if (error.code !== 'EEXIST') throw error;

    // Lock exists — check if stale
    try {
      const stat = fs.statSync(file);
      const age = Date.now() - stat.mtimeMs;
      if (age > LOCK_TIMEOUT_MS) {
        // Stale lock — break it
        console.error('[bidding-hunter] Breaking stale lock (>2 hours)');
        fs.unlinkSync(file);
        return acquire(config); // Retry
      }
      throw new Error('Another bidding-hunter process is already running. ' +
        `Lock file: ${file}. Wait or remove manually if stuck.`);
    } catch (e) {
      if (e.code === 'ENOENT') return acquire(config); // Race condition retry
      throw e;
    }
  }
}

function release(config) {
  const file = lockPath(config);
  try {
    fs.unlinkSync(file);
  } catch {
    // Already gone — fine
  }
}

function isLocked(config) {
  const file = lockPath(config);
  try {
    const stat = fs.statSync(file);
    return Date.now() - stat.mtimeMs <= LOCK_TIMEOUT_MS;
  } catch {
    return false;
  }
}

function resolvePath(p) {
  if (p.startsWith('~')) {
    const home = process.env.HOME || path.join('/home', process.env.USER || 'user');
    p = path.join(home, p.slice(1));
  }
  return path.resolve(p);
}

module.exports = { acquire, release, isLocked };
