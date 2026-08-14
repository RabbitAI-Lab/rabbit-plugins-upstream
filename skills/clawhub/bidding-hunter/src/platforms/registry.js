#!/usr/bin/env node
/**
 * registry.js — Platform adapter registry for Bidding Hunter.
 *
 * Auto-discovers and validates platform adapters from:
 *   1. src/platforms/*.js (built-in)
 *   2. ~/.bidding-hunter/platforms/*.js (user-defined)
 *   3. config.platforms.custom_paths (additional paths)
 */

const fs = require('fs');
const path = require('path');

function loadAll(config) {
  const adapters = {};
  const seen = new Set();

  // 1. Load built-in adapters
  const builtinDir = __dirname;
  const builtinFiles = fs.readdirSync(builtinDir)
    .filter(f => f.endsWith('.js') && f !== 'registry.js' && f !== 'base.js');

  for (const file of builtinFiles) {
    try {
      const adapter = require(path.join(builtinDir, file));
      if (isValidAdapter(adapter)) {
        const id = adapter.meta.id;
        adapters[id] = adapter;
        seen.add(id);
      }
    } catch (error) {
      console.error(`[registry] Failed to load built-in adapter ${file}: ${error.message}`);
    }
  }

  // 2. Load user-defined adapters
  const userDir = path.join(process.env.HOME || '/tmp', '.bidding-hunter', 'platforms');
  if (fs.existsSync(userDir)) {
    const userFiles = fs.readdirSync(userDir).filter(f => f.endsWith('.js'));
    for (const file of userFiles) {
      try {
        const adapter = require(path.join(userDir, file));
        if (isValidAdapter(adapter) && !seen.has(adapter.meta.id)) {
          adapters[adapter.meta.id] = adapter;
          seen.add(adapter.meta.id);
        }
      } catch (error) {
        console.error(`[registry] Failed to load user adapter ${file}: ${error.message}`);
      }
    }
  }

  // 3. Load custom paths from config
  const customPaths = config?.platforms?.custom_paths || [];
  for (const p of customPaths) {
    if (fs.existsSync(p) && p.endsWith('.js')) {
      try {
        const adapter = require(path.resolve(p));
        if (isValidAdapter(adapter) && !seen.has(adapter.meta.id)) {
          adapters[adapter.meta.id] = adapter;
          seen.add(adapter.meta.id);
        }
      } catch (error) {
        console.error(`[registry] Failed to load custom adapter ${p}: ${error.message}`);
      }
    }
  }

  return adapters;
}

/**
 * Get a specific adapter by ID.
 */
function get(config, id) {
  const all = loadAll(config);
  return all[id] || null;
}

/**
 * List all available adapter IDs and names.
 */
function list(config) {
  const all = loadAll(config);
  return Object.entries(all).map(([id, adapter]) => ({
    id,
    name: adapter.meta.name,
    version: adapter.meta.version,
    url: adapter.meta.url,
  }));
}

/**
 * Validate that an adapter conforms to the required interface.
 */
function isValidAdapter(adapter) {
  if (!adapter || !adapter.meta) {
    console.error('[registry] Adapter missing meta');
    return false;
  }
  const required = ['id', 'name', 'version'];
  for (const field of required) {
    if (!adapter.meta[field]) {
      console.error(`[registry] Adapter missing meta.${field}`);
      return false;
    }
  }
  if (typeof adapter.scan !== 'function') {
    console.error(`[registry] Adapter '${adapter.meta.id}' missing scan() method`);
    return false;
  }
  return true;
}

/**
 * Find a transformDetailUrl function for a given URL.
 * Checks all loaded adapters for a transformDetailUrl method
 * and returns the first transformed URL that differs from the input.
 */
function findTransformDetailUrl(config, url) {
  const adapters = loadAll(config);
  for (const adapter of Object.values(adapters)) {
    if (typeof adapter.transformDetailUrl === 'function') {
      const transformed = adapter.transformDetailUrl(url);
      if (transformed !== url) return transformed;
    }
  }
  return url;
}

module.exports = { loadAll, get, list, isValidAdapter, findTransformDetailUrl };
