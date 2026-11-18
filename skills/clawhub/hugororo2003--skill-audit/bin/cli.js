#!/usr/bin/env node
'use strict';
const fs = require('fs');
const path = require('path');
const { auditFile, findSkillMd } = require('../src/audit');
const { toMarkdown, toHtml } = require('../src/report');
const args = process.argv.slice(2);
const flags = {};
const targets = [];
for (let i = 0; i < args.length; i++) {
  if (args[i] === '--json' || args[i] === '--html' || args[i] === '--md') flags[args[i]] = args[++i];
  else if (args[i] === '--out') flags.out = args[++i];
  else if (args[i] === '-h' || args[i] === '--help') { console.log('usage: skill-audit <path> [--out dir] [--json f] [--html f] [--md f]'); process.exit(0); }
  else targets.push(args[i]);
}
if (!targets.length) { console.error('skill-audit: give me a SKILL.md path or a directory'); process.exit(2); }
let bad = 0;
for (const t of targets) {
  const file = findSkillMd(t);
  if (!file) { console.error('no SKILL.md found under ' + t); bad++; continue; }
  const res = auditFile(file);
  if (flags.out) fs.mkdirSync(flags.out, { recursive: true });
  const base = path.join(flags.out || '.', (res.skill.name || 'skill') + '.report');
  if (flags.json) fs.writeFileSync(flags.json, JSON.stringify(res, null, 2));
  else if (flags.out) fs.writeFileSync(base + '.json', JSON.stringify(res, null, 2));
  if (flags.html) fs.writeFileSync(flags.html, toHtml(res));
  else if (flags.out) fs.writeFileSync(base + '.html', toHtml(res));
  if (flags.md) fs.writeFileSync(flags.md, toMarkdown(res));
  console.log(toMarkdown(res));
  const hasCritical = res.findings.some(f => !f.pass && f.severity === 'critical');
  if (hasCritical) bad++;
}
process.exit(bad ? 1 : 0);