#!/usr/bin/env node
/**
 * detect-cli-changes.js — Detect changes in evolver CLI flags and subcommands.
 *
 * Compares current --help output against a stored baseline and reports
 * new, removed, or changed flags/subcommands.
 *
 * Usage: node skills/evolver/scripts/detect-cli-changes.js [--update]
 */

const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const WORKSPACE = process.env.WORKSPACE_ROOT || process.cwd();
const EVOLUTION_DIR = path.join(WORKSPACE, 'memory', 'evolution');
const BASELINE_FILE = path.join(EVOLUTION_DIR, 'cli_features.json');

function log(msg) { console.log(`[detect-cli] ${msg}`); }

function parseHelpOutput(output) {
  const subcommands = [];
  const flags = new Set();
  const deprecated = new Set();

  // Extract subcommands from usage line
  const usageMatch = output.match(/Usage:.*?\[(run\|[^\]]+)\]/);
  if (usageMatch) {
    const cmds = usageMatch[1].split('|').map(s => s.trim()).filter(Boolean);
    subcommands.push(...cmds);
  }

  // Extract flags from help text
  const flagRegex = /-\s+(-{1,2}[a-zA-Z][a-zA-Z0-9-]*)(?:\s+\[?[^\]]*\]?)?/g;
  let match;
  while ((match = flagRegex.exec(output)) !== null) {
    const flag = match[1];
    if (output.includes('deprecated') || output.includes('removed')) {
      // Check context for deprecation
      const context = output.slice(Math.max(0, match.index - 50), match.index + 50);
      if (context.includes('deprecated') || context.includes('removed')) {
        deprecated.add(flag);
      }
    }
    flags.add(flag);
  }

  // Extract version
  const versionMatch = output.match(/"evolver_version":\s*"([^"]+)"/);
  const version = versionMatch ? versionMatch[1] : 'unknown';

  // Extract GEP version
  const gepMatch = output.match(/GEP.*?v([\d.]+)\s*(STRICT)?/i);
  const gepVersion = gepMatch ? `v${gepMatch[1]}${gepMatch[2] || ''}` : 'unknown';

  return {
    subcommands,
    flags: Array.from(flags),
    deprecated: Array.from(deprecated),
    version,
    gepVersion,
  };
}

function loadBaseline() {
  if (!fs.existsSync(BASELINE_FILE)) {
    return null;
  }
  try {
    return JSON.parse(fs.readFileSync(BASELINE_FILE, 'utf8'));
  } catch (e) {
    return null;
  }
}

function saveBaseline(data) {
  fs.mkdirSync(EVOLUTION_DIR, { recursive: true });
  fs.writeFileSync(BASELINE_FILE, JSON.stringify(data, null, 2));
  log(`Baseline saved to ${BASELINE_FILE}`);
}

function compare(current, baseline) {
  if (!baseline) {
    return {
      is_new_install: true,
      changes: [],
      summary: 'No baseline found. Created new baseline.',
    };
  }

  const changes = [];

  // Check new subcommands
  for (const cmd of current.subcommands) {
    if (!baseline.subcommands.includes(cmd)) {
      changes.push({ type: 'new_subcommand', item: cmd });
    }
  }

  // Check removed subcommands
  for (const cmd of baseline.subcommands) {
    if (!current.subcommands.includes(cmd)) {
      changes.push({ type: 'removed_subcommand', item: cmd });
    }
  }

  // Check new flags
  for (const flag of current.flags) {
    if (!baseline.flags.includes(flag)) {
      changes.push({ type: 'new_flag', item: flag });
    }
  }

  // Check removed flags
  for (const flag of baseline.flags) {
    if (!current.flags.includes(flag) && !current.deprecated.includes(flag)) {
      changes.push({ type: 'removed_flag', item: flag });
    }
  }

  // Check deprecated flags
  for (const flag of current.deprecated) {
    if (!baseline.deprecated.includes(flag)) {
      changes.push({ type: 'newly_deprecated', item: flag });
    }
  }

  // Version changes
  if (current.version !== baseline.version) {
    changes.push({ type: 'version_change', from: baseline.version, to: current.version });
  }

  if (current.gepVersion !== baseline.gepVersion) {
    changes.push({ type: 'gep_version_change', from: baseline.gepVersion, to: current.gepVersion });
  }

  return {
    is_new_install: false,
    changes,
    summary: changes.length === 0 ? 'No changes detected.' : `${changes.length} change(s) detected.`,
  };
}

function main() {
  const updateBaseline = process.argv.includes('--update');

  log('Fetching current CLI help...');
  let helpOutput;
  try {
    helpOutput = execSync('evolver --help', { encoding: 'utf8', timeout: 10000 });
  } catch (err) {
    // Some CLIs write help to stderr or return non-zero
    helpOutput = err.stdout || err.stderr || '';
  }

  if (!helpOutput) {
    log('ERROR: Could not fetch evolver --help output');
    process.exit(1);
  }

  const current = parseHelpOutput(helpOutput);
  const baseline = loadBaseline();
  const comparison = compare(current, baseline);

  log(comparison.summary);

  if (comparison.changes.length > 0) {
    console.log('\nChanges detected:');
    for (const change of comparison.changes) {
      console.log(`  [${change.type}] ${change.item}${change.from ? ` (${change.from} -> ${change.to})` : ''}`);
    }
    console.log('\nAction required: Review skill scripts for compatibility.');
  }

  if (updateBaseline || !baseline) {
    const dataToSave = {
      detected_at: new Date().toISOString(),
      ...current,
    };
    saveBaseline(dataToSave);
  }

  // Output JSON for machine consumption
  console.log('\n' + JSON.stringify({
    current,
    baseline: baseline || { note: 'no baseline' },
    comparison,
  }, null, 2));
}

main();
