'use strict';

/**
 * Anonymous claim storage for the queue-to-lottery flow.
 *
 * Each slug (e.g. a queue ticket id) maps to a claim record that holds a
 * claim_token and arbitrary state.  Data is persisted as a single JSON file
 * under ~/.jinguyuan/ with atomic writes (.tmp → rename) and 0600 permissions.
 */

const crypto = require('node:crypto');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');

const STORE_DIR = path.join(os.homedir(), '.jinguyuan');
const STORE_PATH = path.join(STORE_DIR, 'anonymous-claims.json');

// ── internal helpers ──────────────────────────────────────────────

function ensureDir() {
  if (!fs.existsSync(STORE_DIR)) {
    fs.mkdirSync(STORE_DIR, { recursive: true, mode: 0o700 });
  }
}

function loadAll() {
  ensureDir();
  try {
    const raw = fs.readFileSync(STORE_PATH, 'utf8');
    return JSON.parse(raw);
  } catch (e) {
    if (e.code === 'ENOENT') return {};
    throw e;
  }
}

function saveAll(data) {
  ensureDir();
  const tmp = `${STORE_PATH}.tmp`;
  fs.writeFileSync(tmp, JSON.stringify(data, null, 2), { mode: 0o600 });
  fs.renameSync(tmp, STORE_PATH);
}

function generateClaimToken() {
  return `jgy_claim_${crypto.randomBytes(32).toString('base64url')}`;
}

// ── public API ────────────────────────────────────────────────────

function getOrCreateClaim(slug) {
  const all = loadAll();
  const existing = all[slug];
  if (existing && existing.claim_token) return existing;

  const value = {
    claim_token: generateClaimToken(),
    state: 'prepared',
    created_at: new Date().toISOString(),
  };
  all[slug] = value;
  saveAll(all);
  return value;
}

function getAllClaims() {
  return loadAll();
}

function saveClaim(claim) {
  if (!claim || !claim.slug) return null;
  const all = loadAll();
  all[claim.slug] = { ...all[claim.slug], ...claim };
  saveAll(all);
  return all[claim.slug];
}

function updateClaim(slug, updates) {
  const all = loadAll();
  if (!all[slug]) return null;
  Object.assign(all[slug], updates);
  saveAll(all);
  return all[slug];
}

function getClaimByToken(claimToken) {
  if (!claimToken) return null;
  const all = loadAll();
  for (const slug of Object.keys(all)) {
    if (all[slug].claim_token === claimToken) return { slug, ...all[slug] };
  }
  return null;
}

function removeClaim(slug) {
  const all = loadAll();
  if (!all[slug]) return false;
  delete all[slug];
  saveAll(all);
  return true;
}

module.exports = { getOrCreateClaim, getAllClaims, saveClaim, getClaimByToken, updateClaim, removeClaim };
