#!/usr/bin/env node
/**
 * config.js — Configuration loader for Bidding Hunter.
 *
 * Loads and validates config from YAML files, with env var substitution.
 * Merge order: default → ~/.bidding-hunter/config.yaml → --config path
 */

const fs = require('fs');
const path = require('path');
const yaml = require('yaml');

/**
 * Resolve ~ and relative paths to absolute.
 */
function resolvePath(p) {
  if (!p) return p;
  if (p.startsWith('~')) {
    p = path.join(process.env.HOME || `/home/${process.env.USER || 'user'}`, p.slice(1));
  }
  return path.resolve(p);
}

/**
 * Substitute ${ENV_VAR} patterns in a string.
 */
function substituteEnv(value) {
  if (typeof value !== 'string') return value;
  return value.replace(/\$\{(\w+)\}/g, (_, name) => process.env[name] || '');
}

/**
 * Deep-substitute env vars in an object.
 */
function deepSubstitute(obj) {
  if (!obj || typeof obj !== 'object') return obj;
  if (Array.isArray(obj)) return obj.map(deepSubstitute);
  const result = {};
  for (const [key, value] of Object.entries(obj)) {
    if (typeof value === 'string') {
      result[key] = substituteEnv(value);
    } else if (typeof value === 'object' && value !== null) {
      result[key] = deepSubstitute(value);
    } else {
      result[key] = value;
    }
  }
  return result;
}

/**
 * Deep merge two objects. b overrides a.
 */
function deepMerge(a, b) {
  if (!b || typeof b !== 'object') return b !== undefined ? b : a;
  if (!a || typeof a !== 'object') return b;
  const result = { ...a };
  for (const [key, val] of Object.entries(b)) {
    if (val === undefined) continue;
    if (typeof val === 'object' && val !== null && !Array.isArray(val) && typeof result[key] === 'object' && result[key] !== null) {
      result[key] = deepMerge(result[key], val);
    } else {
      result[key] = val;
    }
  }
  return result;
}

/**
 * Load and merge configuration from multiple sources.
 * @param {string} [customPath] - Optional path to user config file
 * @returns {object} Merged configuration
 */
function loadConfig(customPath) {
  // 1. Load default config (bundled with package)
  const defaultPath = path.join(__dirname, '..', 'config', 'default.yaml');
  let config = {};
  if (fs.existsSync(defaultPath)) {
    config = yaml.parse(fs.readFileSync(defaultPath, 'utf8'));
  }

  // 2. Load user config from standard location
  const userPath = customPath || resolvePath('~/.bidding-hunter/config.yaml');
  if (fs.existsSync(userPath)) {
    const userConfig = yaml.parse(fs.readFileSync(userPath, 'utf8'));
    config = deepMerge(config, userConfig);
  }

  // 3. Substitute environment variables
  config = deepSubstitute(config);

  // 4. Resolve paths
  config = resolveConfigPaths(config);

  return config;
}

/**
 * Resolve ~ and relative paths in the config object.
 */
function resolveConfigPaths(config) {
  const copy = { ...config };

  if (copy.database?.path) {
    copy.database.path = resolvePath(copy.database.path);
  }
  if (copy.scan?.results_dir) {
    copy.scan.results_dir = resolvePath(copy.scan.results_dir);
  }
  if (copy.logging?.file) {
    copy.logging.file = resolvePath(copy.logging.file);
  }
  if (copy.platforms?.custom_paths) {
    copy.platforms.custom_paths = copy.platforms.custom_paths.map(resolvePath);
  }

  // Normalize retry_stairs: accept both snake_case (config YAML) and camelCase (code)
  if (copy.scan?.retry_stairs) {
    copy.scan.retry_stairs = copy.scan.retry_stairs.map(s => ({
      timeout: s.timeout,
      waitUntil: s.waitUntil || s.wait_until || 'domcontentloaded',
    }));
  }

  return copy;
}

/**
 * Validate config against the JSON Schema.
 * Returns { valid: boolean, errors: string[] }.
 * Soft validation — warns but doesn't throw.
 */
function validateConfig(config) {
  const errors = [];

  // Required sections
  if (!config.matching) {
    errors.push('Missing required section: matching');
  } else {
    if (!config.matching.tiers || Object.keys(config.matching.tiers).length === 0) {
      errors.push('matching.tiers is required and must have at least one tier');
    }
    for (const [key, tier] of Object.entries(config.matching.tiers || {})) {
      if (!tier.keywords || tier.keywords.length === 0) {
        errors.push(`matching.tiers.${key}.keywords is required`);
      }
    }
  }

  // Validation of platform.enabled
  if (config.platforms?.enabled && !Array.isArray(config.platforms.enabled)) {
    errors.push('platforms.enabled must be an array');
  }

  // Scan config
  if (config.scan) {
    if (config.scan.date_window !== undefined && (config.scan.date_window < 1 || config.scan.date_window > 30)) {
      errors.push('scan.date_window must be between 1 and 30');
    }
    if (config.scan.concurrency !== undefined && (config.scan.concurrency < 1 || config.scan.concurrency > 10)) {
      errors.push('scan.concurrency must be between 1 and 10');
    }
  }

  return { valid: errors.length === 0, errors };
}

module.exports = {
  loadConfig,
  resolvePath,
  substituteEnv,
  deepMerge,
  validateConfig,
};
