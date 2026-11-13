#!/usr/bin/env node
/**
 * verify-gep.js — Quick verification that GEP prompt was captured.
 */
const fs = require('fs');
const path = require('path');
const WORKSPACE = process.env.WORKSPACE_ROOT || process.cwd();
const outFile = process.argv[2] || path.join(WORKSPACE, 'memory/evolution/last_run_stdout.txt');

if (!fs.existsSync(outFile)) { console.error('File not found:', outFile); process.exit(1); }

const raw = fs.readFileSync(outFile, 'utf-8');
const gepStart = raw.indexOf('GEP');
const gepEnd = raw.indexOf('Evolver finished.');
if (gepStart === -1) { console.error('No GEP prompt found'); process.exit(1); }

const gep = raw.slice(gepStart, gepEnd > gepStart ? gepEnd : undefined).trim();
const cycleMatch = gep.match(/Cycle #(\d+)/);
const geneMatch = gep.match(/Selected Gene "([^"]+)"/);

console.log('GEP prompt found:', gep.length, 'bytes');
console.log('Cycle:', cycleMatch ? cycleMatch[1] : 'unknown');
console.log('Gene:', geneMatch ? geneMatch[1] : 'unknown');
console.log('Status: OK');
