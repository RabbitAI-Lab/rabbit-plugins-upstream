#!/usr/bin/env node
/**
 * Evolver Skill — Run EvoMap evolution cycles
 */

const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const WORKSPACE = process.env.WORKSPACE_ROOT || process.cwd();
const EVOLUTION_DIR = path.join(WORKSPACE, 'memory', 'evolution');

function runCycle() {
  const outFile = path.join(EVOLUTION_DIR, 'last_run_stdout.txt');
  fs.mkdirSync(EVOLUTION_DIR, { recursive: true });

  try {
    execSync(`evolver run > '${outFile}' 2>&1`, {
      cwd: WORKSPACE,
      timeout: 120_000,
      stdio: 'inherit'
    });
  } catch (e) {
    if (!fs.existsSync(outFile) || fs.statSync(outFile).size === 0) {
      console.error(`[evolver] run failed: ${e.message}`);
      process.exit(1);
    }
  }

  const raw = fs.readFileSync(outFile, 'utf-8');
  console.log('[evolver] Cycle output saved to', outFile);
  return raw;
}

function verify() {
  const outFile = process.argv[2] || path.join(EVOLUTION_DIR, 'last_run_stdout.txt');
  if (!fs.existsSync(outFile)) {
    console.error('File not found:', outFile);
    process.exit(1);
  }
  const raw = fs.readFileSync(outFile, 'utf-8');
  const gepStart = raw.indexOf('GEP');
  const gepEnd = raw.indexOf('Evolver finished.');
  if (gepStart === -1) {
    console.error('No GEP prompt found');
    process.exit(1);
  }
  const gep = raw.slice(gepStart, gepEnd > gepStart ? gepEnd : undefined).trim();
  const cycleMatch = gep.match(/Cycle #(\d+)/);
  const geneMatch = gep.match(/Selected Gene "([^"]+)"/);
  console.log('GEP prompt found:', gep.length, 'bytes');
  console.log('Cycle:', cycleMatch ? cycleMatch[1] : 'unknown');
  console.log('Gene:', geneMatch ? geneMatch[1] : 'unknown');
  console.log('Status: OK');
}

const cmd = process.argv[2];
if (cmd === 'verify') {
  verify();
} else if (!cmd || cmd === 'run') {
  runCycle();
} else {
  console.log('Usage: node index.js [run|verify] [file]');
}
