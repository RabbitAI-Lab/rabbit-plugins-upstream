#!/usr/bin/env node

/**
 * cybernetic-thinking — skill installer
 *
 * UX (mirrors `npx impeccable skills install`):
 *   1. Scan the machine for known AI coding agents.
 *   2. Print a clear list — detected agents are marked, undetected ones greyed out.
 *   3. If stdout is a TTY, prompt the user to confirm / select / supply a custom path.
 *      If not a TTY (CI, piped), fall back to installing for all detected agents.
 *   4. Link the skill into each selected agent's skill directory (junction on Windows,
 *      symlink elsewhere). Supports a custom --path for non-standard layouts.
 */

const fs = require('fs');
const path = require('path');
const os = require('os');
const readline = require('readline');

const pkg = require(path.join(__dirname, '..', 'package.json'));
const skillName = pkg.name;
const skillVersion = pkg.version;
const skillDir = path.join(__dirname, '..');

// ─────────────────────────────────────────────────────────────────────────────
// Agent registry
// ─────────────────────────────────────────────────────────────────────────────

const agents = [
  {
    name: 'Kilo',
    slug: 'kilo',
    paths: [
      { location: 'global', dir: path.join(os.homedir(), '.config', 'kilo', 'skills') },
      { location: 'local',  dir: path.join(process.cwd(), '.kilo', 'agent') }
    ]
  },
  {
    name: 'Claude Code',
    slug: 'claude-code',
    paths: [
      { location: 'global', dir: path.join(os.homedir(), '.claude', 'plugins', 'custom-skills') },
      { location: 'local',  dir: path.join(process.cwd(), '.claude') }
    ]
  },
  {
    name: 'Aider',
    slug: 'aider',
    paths: [
      { location: 'global', dir: path.join(os.homedir(), '.aider', 'skills') },
      { location: 'local',  dir: path.join(process.cwd(), '.aider', 'skills') }
    ]
  },
  {
    name: 'Cursor',
    slug: 'cursor',
    paths: [
      { location: 'local', dir: path.join(process.cwd(), '.cursor', 'rules') }
    ]
  },
  {
    name: 'OpenAI Codex',
    slug: 'openai-codex',
    paths: [
      { location: 'global', dir: path.join(os.homedir(), '.codex', 'skills') }
    ]
  },
  {
    name: 'GitHub Copilot',
    slug: 'github-copilot',
    paths: [
      { location: 'global', dir: path.join(os.homedir(), '.copilot', 'skills') }
    ]
  },
  {
    name: 'Windsurf',
    slug: 'windsurf',
    paths: [
      { location: 'global', dir: path.join(os.homedir(), '.windsurf', 'skills') }
    ]
  },
  {
    name: 'Zed',
    slug: 'zed',
    paths: [
      { location: 'global', dir: path.join(os.homedir(), '.zed', 'skills') }
    ]
  }
];

// ─────────────────────────────────────────────────────────────────────────────
// Helpers
// ─────────────────────────────────────────────────────────────────────────────

function dirExists(dir) {
  try {
    return fs.statSync(dir).isDirectory();
  } catch {
    return false;
  }
}

function isTTY() {
  return process.stdin.isTTY === true && process.stdout.isTTY === true;
}

function linkSkill(targetDir, agentName, force) {
  const dest = path.join(targetDir, skillName);
  if (fs.existsSync(dest) || fs.existsSync(dest + '.lnk')) {
    if (!force) {
      console.log(`  [skip] ${agentName}: already linked at ${dest}`);
      return 'skipped';
    }
    try {
      fs.rmSync(dest, { recursive: true, force: true });
    } catch (err) {
      console.log(`  [fail] ${agentName}: could not remove existing ${dest} (${err.message})`);
      return 'failed';
    }
  }
  try {
    fs.mkdirSync(targetDir, { recursive: true });
    // 'junction' works on Windows without admin rights; harmless elsewhere.
    fs.symlinkSync(skillDir, dest, 'junction');
    console.log(`  [ok]   ${agentName}: linked to ${dest}`);
    return 'installed';
  } catch (err) {
    console.log(`  [fail] ${agentName}: could not link to ${dest} (${err.message})`);
    console.log(`         try manually: cp -r "${skillDir}" "${dest}"`);
    return 'failed';
  }
}

function prompt(question) {
  return new Promise(resolve => {
    const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
    rl.question(question, ans => { rl.close(); resolve((ans || '').trim()); });
  });
}

// ─────────────────────────────────────────────────────────────────────────────
// Display
// ─────────────────────────────────────────────────────────────────────────────

function printHeader() {
  console.log(`${skillName} v${skillVersion} — skill installer`);
  console.log(`Source: ${skillDir}`);
  console.log('');
}

function printHelp() {
  console.log(`Usage: npx ${skillName} install [options]

Scans for installed AI coding agents and links this skill into their skill
directories. Runs interactively when stdout is a TTY; otherwise installs for
all detected agents (CI-friendly).

Options:
  --agents, -a <list>   Comma-separated agent slugs to install for
                        (e.g. -a kilo,claude-code). Skips interactive prompt.
  --path <dir>          Install into a custom directory instead of agent defaults.
                        Useful for non-standard layouts or unsupported agents.
  --global, -g          Only install to global (home) paths.
  --local, -l           Only install to project-local (cwd) paths.
  --yes, -y             Skip confirmation prompts. Implied when not a TTY.
  --force, -f           Overwrite existing links.
  --help, -h            Show this help message.

Examples:
  npx ${skillName} install
  npx ${skillName} install -a kilo,claude-code -y
  npx ${skillName} install --path ~/my-agent/skills
  npx ${skillName} install -g --force
`);
}

function printAgentScan(detectedAgents, scope) {
  console.log('Scanning for installed AI agents...');
  console.log('');
  for (const a of agents) {
    const inScope = a.paths.filter(p => {
      if (scope === 'global') return p.location === 'global';
      if (scope === 'local')  return p.location === 'local';
      return true;
    });
    const found = inScope.filter(p => dirExists(p.dir));
    const isDetected = found.length > 0;
    const marker = isDetected ? '[√]' : '[ ]';
    const where = found.map(p => relHome(p.dir)).join(', ');
    const tail = isDetected ? `  → ${where}` : '';
    console.log(`  ${marker} ${a.slug.padEnd(16)} ${a.name}${tail}`);
  }
  console.log('');
}

function relHome(p) {
  const home = os.homedir();
  if (p.startsWith(home)) return '~' + p.slice(home.length).replace(/\\/g, '/');
  return p.replace(/\\/g, '/');
}

// ─────────────────────────────────────────────────────────────────────────────
// Install logic
// ─────────────────────────────────────────────────────────────────────────────

function scopeFilter(scope) {
  return p => {
    if (scope === 'global') return p.location === 'global';
    if (scope === 'local')  return p.location === 'local';
    return true;
  };
}

function installForAgents(targetAgents, scope, force) {
  let installed = 0, skipped = 0, failed = 0;
  for (const agent of targetAgents) {
    const paths = agent.paths.filter(scopeFilter(scope));
    if (paths.length === 0) {
      console.log(`  [skip] ${agent.name}: no paths in scope '${scope}'`);
      skipped++;
      continue;
    }
    for (const { dir } of paths) {
      if (!dirExists(dir)) {
        // For explicitly selected agents, create the directory.
        try {
          fs.mkdirSync(dir, { recursive: true });
        } catch {
          console.log(`  [skip] ${agent.name}: cannot create ${dir}`);
          skipped++;
          continue;
        }
      }
      const result = linkSkill(dir, agent.name, force);
      if (result === 'installed') installed++;
      else if (result === 'skipped') skipped++;
      else failed++;
    }
  }
  return { installed, skipped, failed };
}

function installToCustomPath(customDir, force) {
  console.log(`Installing to custom path: ${customDir}`);
  console.log('');
  const result = linkSkill(customDir, 'custom', force);
  return {
    installed: result === 'installed' ? 1 : 0,
    skipped:   result === 'skipped'   ? 1 : 0,
    failed:    result === 'failed'    ? 1 : 0
  };
}

async function interactiveSelect(detectedAgents, scope) {
  // Returns the list of agents the user wants to install for.
  if (detectedAgents.length === 0) {
    console.log('No agents detected on this machine.');
    console.log('You can:');
    console.log('  - install for a specific agent:    npx ' + skillName + ' install -a kilo');
    console.log('  - install to a custom directory:   npx ' + skillName + ' install --path <dir>');
    console.log('  - list all agents and pick:        npx ' + skillName + ' install -a all');
    console.log('');
    const all = await prompt('Install for ALL known agents (creates their dirs)? [y/N] ');
    if (all.toLowerCase() === 'y' || all.toLowerCase() === 'yes') {
      return agents.slice();
    }
    return [];
  }

  console.log(`Detected ${detectedAgents.length} agent(s).`);
  console.log('');
  console.log('  [enter]  install for detected agents (default)');
  console.log('  [a]      install for ALL known agents');
  console.log('  [s]      select from a list');
  console.log('  [n]      abort');
  const ans = await prompt('Choose: ');

  if (ans === '' || ans.toLowerCase() === 'y') return detectedAgents.slice();
  if (ans.toLowerCase() === 'a') return agents.slice();
  if (ans.toLowerCase() === 'n') return null;
  if (ans.toLowerCase() === 's') {
    console.log('');
    agents.forEach((a, i) => {
      const isDet = detectedAgents.includes(a);
      const marker = isDet ? '√' : ' ';
      console.log(`  ${i + 1}. [${marker}] ${a.slug.padEnd(16)} ${a.name}`);
    });
    console.log('  (comma-separated numbers, or blank for detected-only)');
    const sel = await prompt('Pick: ');
    if (sel === '') return detectedAgents.slice();
    const picked = sel.split(',')
      .map(s => parseInt(s.trim(), 10) - 1)
      .filter(i => i >= 0 && i < agents.length)
      .map(i => agents[i]);
    return picked.length > 0 ? picked : detectedAgents.slice();
  }
  return detectedAgents.slice();
}

// ─────────────────────────────────────────────────────────────────────────────
// Main
// ─────────────────────────────────────────────────────────────────────────────

async function main() {
  const args = process.argv.slice(2);

  if (args.includes('--help') || args.includes('-h')) {
    printHelp();
    return;
  }

  // Parse args
  const selectedSlugs = [];
  let scope = 'all';
  let force = false;
  let autoYes = !isTTY();
  let customPath = null;

  for (let i = 0; i < args.length; i++) {
    const arg = args[i];
    if ((arg === '--agents' || arg === '-a') && i + 1 < args.length) {
      const raw = args[++i];
      raw.split(',').forEach(a => {
        const slug = a.trim().toLowerCase().replace(/\s+/g, '-');
        if (slug && !selectedSlugs.includes(slug)) selectedSlugs.push(slug);
      });
    } else if (arg === '--path' && i + 1 < args.length) {
      customPath = path.resolve(args[++i]);
    } else if (arg === '--global' || arg === '-g') {
      scope = 'global';
    } else if (arg === '--local' || arg === '-l' || arg === '--project') {
      scope = 'local';
    } else if (arg === '--all') {
      scope = 'all';
    } else if (arg === '--force' || arg === '-f') {
      force = true;
    } else if (arg === '--yes' || arg === '-y') {
      autoYes = true;
    } else {
      console.log(`Unknown option: ${arg}  (use --help)`);
      process.exit(1);
    }
  }

  printHeader();

  // Case 1: custom path — bypass agent selection entirely.
  if (customPath) {
    const summary = installToCustomPath(customPath, force);
    printSummary(summary, 'Done.');
    return;
  }

  // Case 2: --agents all (explicit override)
  const wantAllAgents = selectedSlugs.includes('all');

  // Scan
  printAgentScan(agents, scope);

  let targetAgents;

  if (wantAllAgents) {
    targetAgents = agents.slice();
  } else if (selectedSlugs.length > 0) {
    targetAgents = agents.filter(a => selectedSlugs.includes(a.slug));
    if (targetAgents.length === 0) {
      console.log('No matching agents. Available slugs:');
      agents.forEach(a => console.log(`  ${a.slug.padEnd(16)} ${a.name}`));
      process.exit(1);
    }
  } else {
    // Auto-detect
    const detected = agents.filter(a =>
      a.paths.filter(scopeFilter(scope)).some(p => dirExists(p.dir))
    );

    if (isTTY() && !autoYes) {
      const choice = await interactiveSelect(detected, scope);
      if (choice === null) {
        console.log('Aborted.');
        process.exit(0);
      }
      if (choice.length === 0) {
        console.log('Nothing to install. Use --agents or --path to specify a target.');
        process.exit(0);
      }
      targetAgents = choice;
    } else {
      // Non-interactive: install for detected agents only.
      targetAgents = detected;
      if (targetAgents.length === 0) {
        console.log('No agents detected and not a TTY — cannot prompt.');
        console.log('Specify agents explicitly:  npx ' + skillName + ' install -a kilo,claude-code');
        console.log('Or install to a custom path: npx ' + skillName + ' install --path <dir>');
        process.exit(0);
      }
    }
  }

  // Confirm
  console.log(`Will install for: ${targetAgents.map(a => a.name).join(', ')}`);
  console.log(`Scope: ${scope}    Force: ${force ? 'yes' : 'no'}`);
  console.log('');

  if (isTTY() && !autoYes) {
    const confirm = await prompt('Proceed? [Y/n] ');
    if (confirm.toLowerCase() === 'n') {
      console.log('Aborted.');
      process.exit(0);
    }
  }

  const summary = installForAgents(targetAgents, scope, force);
  printSummary(summary, 'Done.');
}

function printSummary({ installed, skipped, failed }, tail) {
  console.log('');
  console.log(`${tail} installed: ${installed}, skipped: ${skipped}, failed: ${failed}`);
  if (installed > 0) {
    console.log('Verify with:  pwsh init.ps1   (or  powershell -ExecutionPolicy Bypass -File init.ps1)');
  }
  if (failed > 0) process.exit(1);
}

main().catch(err => {
  console.error('Installer error:', err);
  process.exit(1);
});
