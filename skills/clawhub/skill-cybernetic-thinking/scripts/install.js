#!/usr/bin/env node

/**
 * cybernetic-thinking — skill installer
 *
 * UX mirrors `npx impeccable skills install` using @clack/prompts:
 *   1. Scan for known AI coding agents.
 *   2. Show detected agents with paths.
 *   3. Prompt: detected-only or customize selection.
 *   4. Prompt: project or global install location.
 *   5. Link the skill into each selected agent's skills directory.
 *
 * Non-interactive fallback (CI, piped stdin): installs for all detected
 * agents at global scope.
 *
 * Flags (for scripting / CI):
 *   --agents, -a <slugs>   Comma-separated agent slugs (skip prompts)
 *   --path <dir>           Install into a custom directory
 *   --global, -g           Global scope only
 *   --local, -l            Project scope only
 *   --yes, -y              Skip prompts (use detected agents)
 *   --force, -f            Overwrite existing links
 *   --help, -h             Show help
 */

const fs = require('fs');
const path = require('path');
const os = require('os');

const pkg = require(path.join(__dirname, '..', 'package.json'));
const skillName = pkg.name;
const skillDir = path.join(__dirname, '..');

// ─────────────────────────────────────────────────────────────────────────────
// Agent registry
// Detection: ~/.<root> (global) or ./.<root> (project)
// Install:   ~/.<root>/skills/<skillName> or ./.<root>/skills/<skillName>
// ─────────────────────────────────────────────────────────────────────────────

const agents = [
  { name: 'Claude Code',    slug: 'claude',   root: '.claude'   },
  { name: 'Codex CLI',      slug: 'codex',    root: '.codex'    },
  { name: 'Cursor',         slug: 'cursor',   root: '.cursor'   },
  { name: 'Gemini CLI',     slug: 'gemini',   root: '.gemini'   },
  { name: 'GitHub Copilot', slug: 'copilot',  root: '.github'   },
  { name: 'Kilo',           slug: 'kilo',     root: '.kilo'     },
  { name: 'Aider',          slug: 'aider',    root: '.aider'    },
  { name: 'Windsurf',       slug: 'windsurf', root: '.windsurf' },
  { name: 'Zed',            slug: 'zed',      root: '.zed'      },
];

const SKILL_SUBDIR = 'skills';

// ─────────────────────────────────────────────────────────────────────────────
// Helpers
// ─────────────────────────────────────────────────────────────────────────────

function dirExists(p) {
  try { return fs.statSync(p).isDirectory(); } catch { return false; }
}

function isTTY() {
  return process.stdin.isTTY === true && process.stdout.isTTY === true;
}

function relHome(p) {
  const home = os.homedir();
  if (p === home) return '~';
  if (p.startsWith(home)) return '~' + p.slice(home.length).replace(/\\/g, '/');
  return p.replace(/\\/g, '/');
}

function globalDetect(a)  { return path.join(os.homedir(), a.root); }
function globalInstall(a)  { return path.join(os.homedir(), a.root, SKILL_SUBDIR); }
function projectDetect(a)  { return path.join(process.cwd(), a.root); }
function projectInstall(a) { return path.join(process.cwd(), a.root, SKILL_SUBDIR); }

function detectAll() {
  const found = [];
  for (const a of agents) {
    if (dirExists(globalDetect(a)))  found.push({ agent: a, scope: 'global',  dir: globalDetect(a) });
    if (dirExists(projectDetect(a))) found.push({ agent: a, scope: 'project', dir: projectDetect(a) });
  }
  return found;
}

function linkSkill(targetParentDir, force) {
  const dest = path.join(targetParentDir, skillName);
  const label = relHome(targetParentDir);
  if (fs.existsSync(dest)) {
    if (!force) { console.log(`  [skip] ${label} (already linked)`); return 'skipped'; }
    try { fs.rmSync(dest, { recursive: true, force: true }); } catch (e) {
      console.log(`  [fail] ${label} (${e.message})`); return 'failed';
    }
  }
  try {
    fs.mkdirSync(targetParentDir, { recursive: true });
    fs.symlinkSync(skillDir, dest, 'junction');
    console.log(`  [ok]   ${label}`);
    return 'installed';
  } catch (e) {
    console.log(`  [fail] ${label} (${e.message})`);
    console.log(`         try manually: cp -r "${skillDir}" "${dest}"`);
    return 'failed';
  }
}

function doInstall(targetAgents, scope, force) {
  let installed = 0, skipped = 0, failed = 0;
  for (const a of targetAgents) {
    const dirs = [];
    if (scope === 'global' || scope === 'all')  dirs.push(globalInstall(a));
    if (scope === 'project' || scope === 'all') dirs.push(projectInstall(a));
    for (const d of dirs) {
      const r = linkSkill(d, force);
      if (r === 'installed') installed++; else if (r === 'skipped') skipped++; else failed++;
    }
  }
  return { installed, skipped, failed };
}

// ─────────────────────────────────────────────────────────────────────────────
// Help
// ─────────────────────────────────────────────────────────────────────────────

function printHelp() {
  console.log(`Usage: npx ${skillName} install [options]

Scans for installed AI coding agents and links this skill into their skills
directories. Runs interactively when stdin is a TTY; otherwise installs for all
detected agents at global scope (CI-friendly).

Options:
  --agents, -a <list>   Comma-separated agent slugs (e.g. -a claude,codex)
  --path <dir>          Install into a custom directory
  --global, -g          Global scope only
  --local, -l           Project scope only
  --yes, -y             Skip prompts (use detected agents)
  --force, -f           Overwrite existing links
  --help, -h            Show this help message

Examples:
  npx ${skillName} install
  npx ${skillName} install -a claude,codex
  npx ${skillName} install --path ~/my-agent/skills
  npx ${skillName} install -g --force
`);
}

// ─────────────────────────────────────────────────────────────────────────────
// Non-interactive install
// ─────────────────────────────────────────────────────────────────────────────

function nonInteractive({ selectedAgents, scope, customPath, force }) {
  if (customPath) {
    console.log(`Installing to custom path: ${customPath}`);
    const r = linkSkill(customPath, force);
    return {
      installed: r === 'installed' ? 1 : 0,
      skipped:   r === 'skipped'   ? 1 : 0,
      failed:    r === 'failed'    ? 1 : 0,
    };
  }

  let target;
  if (selectedAgents && selectedAgents.length > 0) {
    target = selectedAgents;
  } else {
    const detected = detectAll();
    const effectiveScope = scope === 'all' ? 'global' : scope;
    target = [...new Set(detected.filter(d => d.scope === effectiveScope).map(d => d.agent))];
  }

  if (target.length === 0) {
    console.log('No agents detected.');
    console.log(`Specify agents with: npx ${skillName} install -a claude,codex`);
    console.log(`Or a custom path:    npx ${skillName} install --path <dir>`);
    return { installed: 0, skipped: 0, failed: 0 };
  }

  const effectiveScope = scope === 'all' ? 'global' : scope;
  console.log(`Installing for: ${target.map(a => a.name).join(', ')}`);
  console.log(`Scope: ${effectiveScope}`);
  console.log('');
  return doInstall(target, effectiveScope, force);
}

// ─────────────────────────────────────────────────────────────────────────────
// Interactive install (clack TUI — mirrors impeccable UX)
// ─────────────────────────────────────────────────────────────────────────────

async function interactive({ force }) {
  const clack = require('@clack/prompts');

  clack.intro(`${skillName} install`);

  // 1. Detect
  const detected = detectAll();
  const detectedAgents = [...new Set(detected.map(d => d.agent))];

  if (detected.length > 0) {
    const lines = detected.map(d => `  ${d.agent.name.padEnd(16)} ${relHome(d.dir)}`).join('\n');
    console.log(`\n◇ Detected agents\n${lines}\n`);
  } else {
    console.log('\n◇ No agents detected on this machine.\n');
  }

  // No agents detected — offer all or abort
  if (detectedAgents.length === 0) {
    const proceed = await clack.select({
      message: 'No agents detected. Install for all known agents?',
      options: [
        { value: 'all',    label: 'Yes, install for all (creates their dirs)' },
        { value: 'abort',  label: 'Abort' },
      ],
    });
    if (clack.isCancel(proceed) || proceed === 'abort') {
      clack.cancel('Aborted');
      process.exit(0);
    }
    const location = await clack.select({
      message: 'Install location',
      options: [
        { value: 'project', label: `Project (${process.cwd()})` },
        { value: 'global',  label: 'Global (~)' },
      ],
    });
    if (clack.isCancel(location)) { clack.cancel('Aborted'); process.exit(0); }
    console.log('');
    const r = doInstall(agents, location, force);
    clack.outro(`Done! installed: ${r.installed}, skipped: ${r.skipped}, failed: ${r.failed}`);
    if (r.failed > 0) process.exit(1);
    return;
  }

  // 2. Detected only or customize?
  const mode = await clack.select({
    message: 'Install for detected agents only, or add more?',
    options: [
      { value: 'detected', label: `Detected only (${detectedAgents.map(a => a.slug).join(', ')})` },
      { value: 'custom',   label: 'Customize...' },
    ],
  });
  if (clack.isCancel(mode)) { clack.cancel('Aborted'); process.exit(0); }

  // 3. Select agents (if customize)
  let targetAgents;
  if (mode === 'custom') {
    const opts = agents.map(a => ({
      value: a.slug,
      label: a.name,
      hint: a.slug,
    }));
    const picked = await clack.multiselect({
      message: 'Select agents',
      options: opts,
      required: true,
    });
    if (clack.isCancel(picked)) { clack.cancel('Aborted'); process.exit(0); }
    targetAgents = agents.filter(a => picked.includes(a.slug));
  } else {
    targetAgents = detectedAgents;
  }

  // 4. Install location
  const location = await clack.select({
    message: 'Install location',
    options: [
      { value: 'project', label: `Project (${process.cwd()})` },
      { value: 'global',  label: 'Global (~)' },
    ],
  });
  if (clack.isCancel(location)) { clack.cancel('Aborted'); process.exit(0); }

  // 5. Install
  console.log('');
  const r = doInstall(targetAgents, location, force);
  clack.outro(`Done! installed: ${r.installed}, skipped: ${r.skipped}, failed: ${r.failed}`);
  if (r.failed > 0) process.exit(1);
}

// ─────────────────────────────────────────────────────────────────────────────
// Arg parsing
// ─────────────────────────────────────────────────────────────────────────────

function parseArgs(argv) {
  const positional = [];
  const opts = { agents: null, path: null, scope: 'all', force: false, yes: false, help: false };
  let i = 0;
  while (i < argv.length) {
    const a = argv[i];
    if (a === '--agents' || a === '-a') {
      opts.agents = (argv[++i] || '').split(',').map(s => s.trim().toLowerCase()).filter(Boolean);
      i++;
    } else if (a === '--path') {
      opts.path = path.resolve(argv[++i]);
      i++;
    } else if (a === '--global' || a === '-g') {
      opts.scope = 'global'; i++;
    } else if (a === '--local' || a === '-l' || a === '--project') {
      opts.scope = 'project'; i++;
    } else if (a === '--all') {
      opts.scope = 'all'; i++;
    } else if (a === '--force' || a === '-f') {
      opts.force = true; i++;
    } else if (a === '--yes' || a === '-y') {
      opts.yes = true; i++;
    } else if (a === '--help' || a === '-h') {
      opts.help = true; i++;
    } else if (!a.startsWith('-')) {
      positional.push(a); i++;
    } else {
      console.log(`Unknown option: ${a}  (use --help)`);
      process.exit(1);
    }
  }
  return { positional, opts };
}

// ─────────────────────────────────────────────────────────────────────────────
// Main
// ─────────────────────────────────────────────────────────────────────────────

async function main() {
  const { positional, opts } = parseArgs(process.argv.slice(2));

  if (opts.help) { printHelp(); return; }

  // Subcommand: accept 'install' or none
  const subcommand = positional[0];
  if (subcommand && subcommand !== 'install') {
    console.log(`Unknown subcommand: ${subcommand}  (use --help)`);
    process.exit(1);
  }

  // Custom path: bypass everything
  if (opts.path) {
    const r = nonInteractive({ customPath: opts.path, force: opts.force });
    console.log(`\nDone! installed: ${r.installed}, skipped: ${r.skipped}, failed: ${r.failed}`);
    if (r.failed > 0) process.exit(1);
    return;
  }

  // Explicit --agents: non-interactive
  if (opts.agents) {
    const selected = agents.filter(a => opts.agents.includes(a.slug));
    if (selected.length === 0) {
      console.log('No matching agents. Available slugs:');
      agents.forEach(a => console.log(`  ${a.slug.padEnd(12)} ${a.name}`));
      process.exit(1);
    }
    const scope = opts.scope === 'all' ? 'global' : opts.scope;
    const r = nonInteractive({ selectedAgents: selected, scope, force: opts.force });
    console.log(`\nDone! installed: ${r.installed}, skipped: ${r.skipped}, failed: ${r.failed}`);
    if (r.failed > 0) process.exit(1);
    return;
  }

  // Interactive vs non-interactive
  if (isTTY() && !opts.yes) {
    await interactive({ force: opts.force });
  } else {
    const r = nonInteractive({ scope: opts.scope, force: opts.force });
    console.log(`\nDone! installed: ${r.installed}, skipped: ${r.skipped}, failed: ${r.failed}`);
    if (r.failed > 0) process.exit(1);
  }
}

main().catch(err => { console.error('Installer error:', err); process.exit(1); });
