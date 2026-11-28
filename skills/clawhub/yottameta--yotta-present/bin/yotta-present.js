#!/usr/bin/env node
/**
 * yotta-present launcher.
 *
 * Default: start the stdio MCP server (scripts/yotta_present_mcp.py).
 * Install flags: delegate to bin/install.js.
 */
'use strict';
const { spawn, spawnSync } = require('child_process');
const path = require('path');

const PKG_ROOT = path.join(__dirname, '..');
const SERVER = path.join(PKG_ROOT, 'scripts', 'yotta_present_mcp.py');
const INSTALL_FLAGS = [
  '--agent', '--dir', '--list', '-l', '-g', '--global', '--dry-run', '--yes',
];

const HELP = [
  'yotta-present - presentation layer for AI output',
  '',
  'Usage:',
  '  npx -y @yottameta/yotta-present                     start the stdio MCP server',
  '  npx -y @yottameta/yotta-present --agent <name>      install to an agent default dir',
  '  npx -y @yottameta/yotta-present --dir <path>        install to a custom dir',
  '  npx -y @yottameta/yotta-present --list              list agent -> default dir',
  '  npx -y @yottameta/yotta-present --version           print the package version',
  '  npx -y @yottameta/yotta-present --print-command     print the resolved Python command',
  '',
  'The MCP server needs Python 3.8+. Set YOTTA_PRESENT_PYTHON to choose an interpreter.',
].join('\n');

function isInstallRequest(args) {
  return args.some(function (item) {
    if (INSTALL_FLAGS.indexOf(item) !== -1) return true;
    return item.indexOf('--agent=') === 0 || item.indexOf('--dir=') === 0;
  });
}

function pythonCandidates() {
  const candidates = [];
  if (process.env.YOTTA_PRESENT_PYTHON) candidates.push(process.env.YOTTA_PRESENT_PYTHON);
  candidates.push('python3', 'python', 'py');
  return candidates;
}

function findPython() {
  const candidates = pythonCandidates();
  for (let i = 0; i < candidates.length; i++) {
    try {
      const result = spawnSync(candidates[i], ['--version'], { encoding: 'utf8', timeout: 5000 });
      if (result.status === 0) return candidates[i];
    } catch (error) {
      // Try the next candidate.
    }
  }
  return candidates[candidates.length - 1];
}

function main() {
  const args = process.argv.slice(2);
  if (args.indexOf('--version') !== -1 || args.indexOf('-v') !== -1) {
    process.stdout.write(require(path.join(PKG_ROOT, 'package.json')).version + '\n');
    return;
  }
  if (args.indexOf('--help') !== -1 || args.indexOf('-h') !== -1) {
    process.stdout.write(HELP + '\n');
    return;
  }
  if (args.indexOf('--print-command') !== -1) {
    const resolved = findPython();
    process.stdout.write(resolved + ' ' + SERVER + '\n');
    return;
  }
  if (isInstallRequest(args)) {
    require(path.join(__dirname, 'install.js'));
    return;
  }
  const python = findPython();
  const child = spawn(python, [SERVER].concat(args), { stdio: 'inherit' });
  child.on('exit', function (code) { process.exit(code || 0); });
  child.on('error', function (error) {
    process.stderr.write('yotta-present: cannot start Python MCP server: ' + error.message + '\n');
    process.exit(1);
  });
}

main();
