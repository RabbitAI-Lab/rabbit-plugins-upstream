#!/usr/bin/env node
const { execSync } = require('child_process');
const path = require('path');

const skillDir = path.resolve(__dirname, '..');
const indexPath = path.join(skillDir, 'index.js');

try {
  const out = execSync(`node -e "const s=require('${indexPath.replace(/\\/g, '\\\\')}'); console.log(Object.keys(s).sort().join(','))"`, {
    cwd: skillDir,
    encoding: 'utf8',
    stdio: ['pipe', 'pipe', 'pipe'],
  });
  console.log('exports ok:', out.trim());
} catch (e) {
  console.error('import check failed:', e.message || e.stdout || e.stderr);
  process.exit(1);
}
