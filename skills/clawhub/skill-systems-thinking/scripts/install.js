#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const os = require('os');

const pkg = require(path.join(__dirname, '..', 'package.json'));
const skillName = pkg.name;
const skillDir = path.join(__dirname, '..');

const agents = [
  {
    name: 'Kilo',
    slug: 'kilo',
    paths: [
      { location: 'global', dir: path.join(os.homedir(), '.config', 'kilo', 'skills') },
      { location: 'local', dir: path.join(process.cwd(), '.kilo', 'agent') }
    ]
  },
  {
    name: 'Claude Code',
    slug: 'claude-code',
    paths: [
      { location: 'global', dir: path.join(os.homedir(), '.claude', 'plugins', 'custom-skills') },
      { location: 'local', dir: path.join(process.cwd(), '.claude') }
    ]
  },
  {
    name: 'Aider',
    slug: 'aider',
    paths: [
      { location: 'global', dir: path.join(os.homedir(), '.aider', 'skills') },
      { location: 'local', dir: path.join(process.cwd(), '.aider', 'skills') }
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

function dirExists(dir) {
  try {
    return fs.statSync(dir).isDirectory();
  } catch {
    return false;
  }
}

function linkSkill(targetDir, agentName) {
  const dest = path.join(targetDir, skillName);
  if (fs.existsSync(dest)) {
    console.log(`[SKIP] ${agentName}: ${dest} already exists`);
    return false;
  }
  try {
    fs.mkdirSync(targetDir, { recursive: true });
    fs.symlinkSync(skillDir, dest, 'junction');
    console.log(`[OK] ${agentName}: linked to ${dest}`);
    return true;
  } catch (err) {
    console.log(`[FAIL] ${agentName}: could not link to ${dest} (${err.message})`);
    console.log(`       Try copying manually: cp -r ${skillDir} ${dest}`);
    return false;
  }
}

function showHelp() {
  console.log(`Usage: npx ${skillName} install [options]

Options:
  --agents, -a <list>      Comma-separated agent names to install for
                           (e.g. --agents kilo,claude-code)
  --global, -g             Install only to global (home directory) paths
  --local, --project, -l   Install only to project-local (cwd) paths
  --all                    Install to both global and project-local paths (default)
  --force, -f              Overwrite existing links
  --help, -h               Show this help message

Examples:
  npx ${skillName} install
  npx ${skillName} install --agents kilo,claude-code
  npx ${skillName} install --global --agents aider
  npx ${skillName} install --local --force
`);
}

function main() {
  const args = process.argv.slice(2);

  if (args.includes('--help') || args.includes('-h')) {
    showHelp();
    return;
  }

  const selectedAgents = [];
  let scope = 'all';
  let force = false;

  for (let i = 0; i < args.length; i++) {
    const arg = args[i];
    if ((arg === '--agents' || arg === '-a') && i + 1 < args.length) {
      const raw = args[++i];
      raw.split(',').forEach(a => {
        const slug = a.trim().toLowerCase().replace(/\s+/g, '-');
        selectedAgents.push(slug);
      });
    } else if (arg === '--global' || arg === '-g') {
      scope = 'global';
    } else if (arg === '--local' || arg === '--project' || arg === '-l') {
      scope = 'local';
    } else if (arg === '--all') {
      scope = 'all';
    } else if (arg === '--force' || arg === '-f') {
      force = true;
    }
  }

  const userSpecifiedAgents = selectedAgents.length > 0;

  let targetAgents;
  if (userSpecifiedAgents) {
    targetAgents = agents.filter(a => selectedAgents.includes(a.slug));
    if (targetAgents.length === 0) {
      console.log('No matching agents found. Available agents:');
      agents.forEach(a => console.log(`  ${a.slug.padEnd(20)} ${a.name}`));
      process.exit(1);
    }
  } else {
    // Auto-detect: only install for agents that have at least one existing directory
    const detected = [];
    const notDetected = [];
    for (const agent of agents) {
      const scopePaths = agent.paths.filter(p => {
        if (scope === 'global') return p.location === 'global';
        if (scope === 'local') return p.location === 'local';
        return true;
      });
      if (scopePaths.some(p => dirExists(p.dir))) {
        detected.push(agent);
      } else {
        notDetected.push(agent);
      }
    }
    targetAgents = detected;
    if (notDetected.length > 0) {
      console.log('Agents not detected:');
      notDetected.forEach(a => console.log(`  ${a.slug.padEnd(20)} ${a.name}`));
      console.log('Use --agents to install for them explicitly.');
      console.log('');
    }
    if (targetAgents.length === 0) {
      console.log('No agents detected on this machine.');
      console.log('Available agents:');
      agents.forEach(a => console.log(`  ${a.slug.padEnd(20)} ${a.name}`));
      console.log('');
      console.log('Use --agents to select specific agents, e.g.:');
      console.log(`  npx ${skillName} install --agents kilo,claude-code`);
      process.exit(0);
    }
  }

  console.log(`Installing ${skillName}...`);
  console.log(`Skill directory: ${skillDir}`);
  console.log(`Scope: ${scope}`);
  console.log(`Agents: ${targetAgents.map(a => a.name).join(', ')}`);
  console.log(`Force: ${force ? 'yes' : 'no'}`);
  console.log('');

  let installed = 0;
  let skipped = 0;
  let failed = 0;

  for (const agent of targetAgents) {
    const filteredPaths = agent.paths.filter(p => {
      if (scope === 'global') return p.location === 'global';
      if (scope === 'local') return p.location === 'local';
      return true;
    });

    for (const { dir } of filteredPaths) {
      if (!dirExists(dir)) {
        // When user explicitly specified agents, create missing directories
        if (userSpecifiedAgents) {
          try {
            fs.mkdirSync(dir, { recursive: true });
          } catch {
            console.log(`[SKIP] ${agent.name}: cannot create ${dir}`);
            skipped++;
            continue;
          }
        } else {
          console.log(`[SKIP] ${agent.name}: ${dir} does not exist`);
          skipped++;
          continue;
        }
      }

      if (force && fs.existsSync(path.join(dir, skillName))) {
        try {
          fs.rmSync(path.join(dir, skillName), { recursive: true });
        } catch {
          console.log(`[FAIL] ${agent.name}: could not remove existing ${dir}/${skillName}`);
          failed++;
          continue;
        }
      }

      if (linkSkill(dir, agent.name)) {
        installed++;
      } else {
        skipped++;
      }
    }
  }

  console.log('');
  console.log(`Done. Installed: ${installed}, Skipped: ${skipped}, Failed: ${failed}`);

  if (installed > 0) {
    console.log('');
    console.log('Verify the installation by running:');
    console.log('  pwsh init.ps1');
  }
}

main();
