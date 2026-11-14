#!/usr/bin/env node
/**
 * evolve-cycle.js — V2 material-driven evolution cycle.
 *
 * Usage: node skills/evolver/scripts/evolve-cycle.js [--distill]
 *
 * Flow (evolver >= 2.0.23):
 *   1. Find latest session transcript in memory/evolution/
 *   2. `evolver ingest` the transcript -> material with extracted signals
 *   3. Either `evolver distill` (no runner needed) or `evolver cycle --repo`
 *   4. Prints summary with gene/capsule result
 */

const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const WORKSPACE = process.env.WORKSPACE_ROOT || process.cwd();
const EVOLUTION_DIR = path.join(WORKSPACE, 'memory', 'evolution');

function log(msg) { console.log(`[evolve-cycle] ${msg}`); }

function run(cmd, opts = {}) {
  return execSync(cmd, { cwd: WORKSPACE, encoding: 'utf-8', stdio: ['ignore', 'pipe', 'pipe'], ...opts });
}

function main() {
  const wantDistill = process.argv.includes('--distill');
  log('Starting V2 evolution cycle (material-driven)...');

  // Find latest transcript material in evolution dir
  const candidates = fs.existsSync(EVOLUTION_DIR)
    ? fs.readdirSync(EVOLUTION_DIR).filter((f) => /\.(transcript|chat|messages)\.jsonl?$/i.test(f))
    : [];
  if (candidates.length === 0) {
    log('ERROR: no *.transcript.jsonl found in memory/evolution — create one first (OpenAI messages format).');
    process.exit(1);
  }
  candidates.sort((a, b) => fs.statSync(path.join(EVOLUTION_DIR, b)).mtimeMs - fs.statSync(path.join(EVOLUTION_DIR, a)).mtimeMs);
  const transcript = path.join(EVOLUTION_DIR, candidates[0]);
  log(`Material source: ${path.basename(transcript)}`);

  // Step 1: ingest (dry-run first to show signals)
  log('Step 1: evolver ingest --dry-run ...');
  try {
    const out = run(`evolver ingest "${transcript}" --dry-run`);
    process.stdout.write(out);
  } catch (e) {
    log(`ingest --dry-run failed: ${e.message}`);
    process.exit(1);
  }

  log('Step 2: evolver ingest (record material) ...');
  try {
    const out = run(`evolver ingest "${transcript}"`);
    process.stdout.write(out);
  } catch (e) {
    log(`ingest failed (maybe unchanged since last ingest): ${e.message}`);
  }

  if (wantDistill) {
    log('Step 3: evolver distill ...');
    // Distill requires explicit category/signals/strategy; a generic fallback:
    const cat = 'optimize';
    const sigs = 'deprecated_cli,breaking_change,migration_required';
    const strategy = 'When a CLI command is reported as a deprecated V1 shim with no compatibility action, stop retrying it and switch to the V2 material-driven flow: ingest session logs as materials, then distill or cycle. Verify command availability with --help before relying on it.';
    try {
      const out = run(`evolver distill --category "${cat}" --signals "${sigs}" --strategy "${strategy}"`);
      process.stdout.write(out);
    } catch (e) {
      log(`distill failed: ${e.message}`);
      process.exit(1);
    }
  } else {
    log('Step 3: evolver cycle --repo (requires runner support; generic-chat materials are refused) ...');
    try {
      const out = run(`evolver cycle --repo "${WORKSPACE}" --limit 1`);
      process.stdout.write(out);
    } catch (e) {
      log(`cycle failed (expected for generic-chat materials without a runner): ${e.message}`);
      log('Hint: use --distill for generic-chat materials, or ingest a claude-code/codex/gemini session log.');
      process.exit(1);
    }
  }

  log('Done.');
}

main();
