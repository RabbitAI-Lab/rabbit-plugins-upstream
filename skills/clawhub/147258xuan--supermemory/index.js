#!/usr/bin/env node
/**
 * SuperMemory Skill — AI memory compression engine
 * Wrapper around supermemory.py
 */

const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const SKILL_DIR = __dirname;
const PYTHON_SCRIPT = path.join(SKILL_DIR, 'supermemory.py');

function runPy(args) {
  try {
    const out = execSync(`python3 "${PYTHON_SCRIPT}" ${args}`, {
      timeout: 30000,
      encoding: 'utf8'
    });
    return out.trim();
  } catch (e) {
    return e.stdout || e.message;
  }
}

function add(content) {
  if (!content) {
    console.error('Usage: supermemory add <content>');
    process.exit(1);
  }
  console.log(runPy(`add "${content.replace(/"/g, '\\"')}"`));
}

function list() {
  console.log(runPy('list'));
}

function search(query) {
  if (!query) {
    console.error('Usage: supermemory search <query>');
    process.exit(1);
  }
  console.log(runPy(`search "${query.replace(/"/g, '\\"')}"`));
}

function pin(id) {
  if (!id) {
    console.error('Usage: supermemory pin <id>');
    process.exit(1);
  }
  console.log(runPy(`pin ${id}`));
}

function stats() {
  console.log(runPy('stats'));
}

module.exports = { add, list, search, pin, stats, runPy };

if (require.main === module) {
  const cmd = process.argv[2];
  if (cmd === 'add') add(process.argv[3]);
  else if (cmd === 'list') list();
  else if (cmd === 'search') search(process.argv[3]);
  else if (cmd === 'pin') pin(process.argv[3]);
  else if (cmd === 'stats') stats();
  else {
    console.log('Usage: node index.js <add|list|search|pin|stats> [args]');
    process.exit(1);
  }
}
