#!/usr/bin/env node
/**
 * env-manager — Dev project file scaffolder
 *
 * Writes starter files for new dev projects and returns a list of toolchain
 * commands as data. The skill itself does not start any process: it does
 * not import any process-spawning module, and there
 * is no code path that runs a binary.
 *
 * The calling agent inspects the returned commands array and runs each
 * one using its own shell tool.
 *
 * Modes:
 *   --setup <type> [name]   Write starter files; return toolchain commands.
 *                            Types: python, node, docker, go, rust.
 *   --ports                 List stored port records (JSON only).
 *   --ports --free          Find unused port numbers in stored data.
 *   --services              List stored service records (JSON only).
 *   --services --start <n>  Mark a service as started in services.json.
 *   --services --stop <n>   Mark a service as stopped in services.json.
 *   --services --status <n> Return port-check commands for a service.
 *   --cleanup               List stored environments marked inactive.
 *   --status                Show counts of stored envs/services/ports.
 *   --commands              Return setup commands for all stored envs.
 *
 * See SKILL.md and README.md for the trust model and what the skill does
 * not do.
 */

const fs = require('fs');
const path = require('path');

// ─── Constants ──────────────────────────────────────────────────────────────
//
// These are the binary names this skill is willing to *describe* in the
// returned commands. The skill never runs any of them. The agent inspects
// the command and runs it (or not) using its own shell tool.

const DEFAULT_ACCEPTED_BINARIES = [
  'python3', 'node', 'npm', 'docker', 'go',
  'rustc', 'pip3', 'lsof', 'which', 'mkdir',
  'mvn', 'gradle', 'cargo', 'ruby', 'pip',
  'make', 'gcc', 'g++', 'clang', 'cmake',
  'java', 'javac', 'dotnet', 'go1',
  'perl', 'php', 'lua', 'tclsh',
];

// ─── Workspace helpers ─────────────────────────────────────────────────────
//
// The workspace root is fixed: the parent directory of this skill. There is
// no runtime path redirection via environment variable or CLI flag. This
// keeps the file-write surface predictable and auditable.

function getWorkspace() {
  let dir = __dirname;
  for (let i = 0; i < 10; i++) {
    if (fs.existsSync(path.join(dir, 'MEMORY.md'))) return dir;
    dir = path.resolve(dir, '..');
  }
  return path.resolve(__dirname, '..', '..');
}

function getDataDir() {
  return path.join(getWorkspace(), 'memory', 'environments');
}

function getEnvsFile()     { return path.join(getDataDir(), 'environments.json'); }
function getPortsFile()    { return path.join(getDataDir(), 'ports.json'); }
function getServicesFile() { return path.join(getDataDir(), 'services.json'); }

function ensureDir(dir) {
  if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
}

function loadJSON(file, fallback) {
  try {
    const data = fs.readFileSync(file, 'utf8');
    return JSON.parse(data);
  } catch {
    return fallback || {};
  }
}

function saveJSON(file, data) {
  ensureDir(path.dirname(file));
  fs.writeFileSync(file, JSON.stringify(data, null, 2), 'utf8');
}

function getToday() {
  return new Date().toISOString().split('T')[0];
}

// ─── Pure-Node binary resolution (fs-based PATH scanning) ──────────────────

/**
 * Resolve a binary name to its absolute path by scanning PATH.
 * Uses fs.accessSync with X_OK — no shell, no spawn, no exec.
 *
 * @param {string} binary - Binary name (e.g. "python3")
 * @returns {string|null} Absolute path or null if not found
 */
function findBinary(binary) {
  const pathDirs = (process.env.PATH || '').split(path.delimiter);
  for (const dir of pathDirs) {
    const fullPath = path.join(dir, binary);
    try {
      fs.accessSync(fullPath, fs.constants.X_OK);
      return fullPath;
    } catch {
      // Not found in this directory, continue
    }
  }
  return null;
}

function isOnAcceptlist(binaryName, accepted) {
  const list = accepted || DEFAULT_ACCEPTED_BINARIES;
  return list.includes(binaryName);
}

// ─── Command builder — generates structured command objects ────────────────

/**
 * Build a validated command object.
 * This is the ONLY place commands are assembled. They are NEVER executed here.
 *
 * @param {string} binary      - Binary name (must be on the accepted list)
 * @param {string[]} args      - Argument array (each element is one argv token)
 * @param {object}  opts       - Options
 * @param {string}  opts.cwd   - Working directory
 * @param {object}  opts.env   - Environment overrides
 * @param {string}  opts.desc  - Human-readable description
 * @param {string[]} opts.accepted - Custom accepted-binary list (defaults to DEFAULT_ACCEPTED_BINARIES)
 * @returns {{binary:string, args:string[], cwd?:string, env?:object, description:string, resolvedBinary?:string|null, error?:string}}
 */
function buildCommand(binary, args, opts = {}) {
  const accepted = opts.accepted || DEFAULT_ACCEPTED_BINARIES;
  const desc = opts.description || `${binary} ${args.join(' ')}`;

  // Gate 1 — accepted-binary check. The skill does not run anything; this
  // gate just marks the returned command so the calling agent can decide.
  if (!isOnAcceptlist(binary, accepted)) {
    return {
      binary, args, cwd: opts.cwd, env: opts.env, description: desc,
      error: `NOT_ACCEPTED: ${binary} is not on the skill's accepted-binary list`,
      status: 'blocked'
    };
  }

  // Gate 2 — Resolve binary path (pure Node.js, no shell)
  const resolved = findBinary(binary);
  if (!resolved) {
    return {
      binary, args, cwd: opts.cwd, env: opts.env, description: desc,
      error: `NOT_FOUND: ${binary} not on PATH`,
      status: 'not_found'
    };
  }

  return {
    binary: resolved,
    args: args || [],
    cwd: opts.cwd,
    env: opts.env,
    description: desc,
    status: 'ready'
  };
}

// ─── Command set builder for an environment type ──────────────────────────

/**
 * Validate an environment name. Rejects anything that could escape the
 * `environments/` directory (path separators, parent-dir references,
 * absolute paths, or characters outside a conservative allowlist).
 *
 * Returns the sanitized name on success, or throws an Error on rejection.
 */
function sanitizeEnvName(name) {
  if (typeof name !== 'string' || name.length === 0) {
    throw new Error('INVALID_NAME: environment name must be a non-empty string');
  }
  if (name.length > 64) {
    throw new Error('INVALID_NAME: environment name must be 64 characters or fewer');
  }
  // Allow only: lowercase letters, digits, hyphen, underscore, dot
  // Reject path separators, parent-dir refs, absolute paths, and shell metacharacters
  if (!/^[a-z0-9_.-]+$/.test(name)) {
    throw new Error(
      'INVALID_NAME: environment name must contain only lowercase letters, ' +
      'digits, hyphen, underscore, or dot (no path separators, spaces, or special characters)'
    );
  }
  if (name === '.' || name === '..' || name.startsWith('..') || name.includes('..')) {
    throw new Error('INVALID_NAME: environment name cannot contain parent-directory references');
  }
  return name;
}

/**
 * Build all commands needed to set up a development environment.
 * Returns { commands: [...], environment: { name, type, path, ... } }
 */
function buildSetupCommands(type, name) {
  const timestamp = Date.now();
  // If a name was provided, sanitize it. If not, generate a safe default.
  let envName;
  if (name) {
    envName = sanitizeEnvName(name);
  } else {
    envName = `${type}-env-${timestamp}`;
  }
  const envDir = path.join(getWorkspace(), 'environments', envName);

  const commands = [];
  const environment = {
    name: envName,
    type: type,
    path: envDir,
    created: getToday(),
    status: 'active'
  };

  // Always: create directory
  commands.push(buildCommand('mkdir', ['-p', envDir], {
    description: `Create environment directory: ${envDir}`
  }));

  switch (type) {

    case 'python': {
      // Verify python3
      commands.push(buildCommand('python3', ['--version'], {
        description: 'Check Python3 version'
      }));
      // Create venv
      commands.push(buildCommand('python3', ['-m', 'venv', envDir], {
        cwd: getWorkspace(),
        description: `Create Python venv at ${envDir}`
      }));
      // Check pip
      commands.push(buildCommand('pip3', ['--version'], {
        cwd: path.join(envDir, 'bin'),
        description: 'Check pip3 version'
      }));
      environment.python = '${python3 --version}';
      environment.pip = '${pip3 --version}';
      environment.activation = `source ${envDir}/bin/activate`;
      break;
    }

    case 'node': {
      // Check versions
      commands.push(buildCommand('node', ['--version'], {
        description: 'Check Node version'
      }));
      commands.push(buildCommand('npm', ['--version'], {
        description: 'Check npm version'
      }));
      environment.node = '${node --version}';
      environment.npm = '${npm --version}';
      // Note: package.json etc. are written by this skill (fs.writeFileSync)
      break;
    }

    case 'docker': {
      commands.push(buildCommand('docker', ['--version'], {
        description: 'Check Docker version'
      }));
      environment.docker = '${docker --version}';
      environment.buildCmd = `docker compose -f ${envDir}/docker-compose.yml build`;
      environment.runCmd = `docker compose -f ${envDir}/docker-compose.yml up`;
      break;
    }

    case 'go': {
      commands.push(buildCommand('go', ['version'], {
        description: 'Check Go version'
      }));
      commands.push(buildCommand('go', ['mod', 'init', envName], {
        cwd: envDir,
        description: `Initialize Go module in ${envDir}`
      }));
      environment.go = '${go version}';
      break;
    }

    case 'rust': {
      commands.push(buildCommand('rustc', ['--version'], {
        description: 'Check Rust version'
      }));
      commands.push(buildCommand('cargo', ['--version'], {
        description: 'Check Cargo version'
      }));
      environment.rust = '${rustc --version}';
      environment.cargo = '${cargo --version}';
      break;
    }

    default:
      commands.unshift({
        binary: type,
        args: [],
        error: `Unknown environment type: ${type}`,
        status: 'error',
        description: `Setup for unknown type: ${type}`
      });
  }

  // Always: verify binary availability
  const binariesToCheck = new Set();
  for (const cmd of commands) {
    if (cmd.status === 'ready' || cmd.status === 'blocked') {
      binariesToCheck.add(cmd.binary || cmd);
    }
  }
  for (const b of binariesToCheck) {
    const resolved = findBinary(b);
    if (resolved) {
      environment[b] = resolved;
    }
  }

  return { commands, environment };
}

// ─── File generation (fs-only, no exec) ────────────────────────────────────

/**
 * Write all scaffold files for an environment type.
 * This uses ONLY fs.writeFileSync — no shell access.
 */
function generateScaffoldFiles(type, envName, envDir) {
  ensureDir(envDir);

  switch (type) {

    case 'node': {
      const pkg = {
        name: envName,
        version: '1.0.0',
        description: '',
        main: 'index.js',
        scripts: {
          start: 'node index.js',
          dev: 'node --watch index.js',
          test: 'echo "No tests configured"'
        },
        keywords: [],
        author: '',
        license: 'ISC'
      };
      fs.writeFileSync(path.join(envDir, 'package.json'), JSON.stringify(pkg, null, 2));
      fs.writeFileSync(path.join(envDir, 'index.js'),
        `// ${envName}\nconsole.log('${envName} running');\n`);
      fs.writeFileSync(path.join(envDir, '.gitignore'), 'node_modules\n.env\n*.log\n');
      break;
    }

    case 'docker': {
      const dockerfile = `FROM node:20-alpine\nWORKDIR /app\nCOPY package*.json ./\nRUN npm install\nCOPY . .\nEXPOSE 3000\nCMD ["node", "index.js"]\n`;
      fs.writeFileSync(path.join(envDir, 'Dockerfile'), dockerfile);

      const compose = `version: '3.8'\nservices:\n  app:\n    build: .\n    ports:\n      - "3000:3000"\n    volumes:\n      - .:/app\n    environment:\n      - NODE_ENV=development\n`;
      fs.writeFileSync(path.join(envDir, 'docker-compose.yml'), compose);
      break;
    }

    case 'go': {
      fs.writeFileSync(path.join(envDir, 'main.go'),
        `package main\n\nimport "fmt"\n\nfunc main() {\n\tfmt.Println("${envName} running")\n}\n`);
      break;
    }

    case 'rust': {
      const cargo = `[package]\nname = "${envName}"\nversion = "0.1.0"\nedition = "2021"\n\n[dependencies]\n`;
      fs.writeFileSync(path.join(envDir, 'Cargo.toml'), cargo);
      ensureDir(path.join(envDir, 'src'));
      fs.writeFileSync(path.join(envDir, 'src', 'main.rs'),
        `fn main() {\n    println!("${envName} running");\n}\n`);
      break;
    }

    case 'python': {
      fs.writeFileSync(path.join(envDir, '.env.example'),
        '# Environment variables example\nAPP_NAME=' + envName + '\n');
      break;
    }
  }
}

// ─── Full env setup (files + commands) ────────────────────────────────────

/**
 * Full environment setup: generate files + return commands for shell actions.
 *
 * @param {string} type - Environment type
 * @param {string} [name] - Optional environment name
 * @returns {{environment: object, commands: object[], commandsText: string, warnings: string[]}}
 */
function setupEnvironment(type, name) {
  const timestamp = Date.now();
  // Sanitize name to prevent path traversal; fall back to safe default if invalid
  let envName;
  if (name) {
    try {
      envName = sanitizeEnvName(name);
    } catch (err) {
      // Return error result rather than throwing — callers may not handle throws
      return {
        environment: null,
        commands: [],
        commandsText: '',
        warnings: [err.message],
        filesGenerated: false,
        message: `Error: ${err.message}`
      };
    }
  } else {
    envName = `${type}-env-${timestamp}`;
  }
  const envDir = path.join(getWorkspace(), 'environments', envName);

  // Step 1: Create directory and scaffold files (fs-only, always executed)
  ensureDir(envDir);
  generateScaffoldFiles(type, envName, envDir);

  // Step 2: Build shell commands (agent must execute these)
  const { commands, environment } = buildSetupCommands(type, envName);
  const environmentData = {
    ...environment,
    created: getToday(),
    status: 'active'
  };

  // Persist environment metadata
  const envs = loadJSON(getEnvsFile(), {});
  envs[envName] = environmentData;
  saveJSON(getEnvsFile(), envs);

  // Format commands for agent consumption
  const commandsText = formatCommands(commands);
  const warnings = [];

  // Check for blocked or not-found binaries
  for (const cmd of commands) {
    if (cmd.status === 'blocked') {
      warnings.push(`Command blocked: ${cmd.description} (${cmd.error})`);
    } else if (cmd.status === 'not_found') {
      warnings.push(`Binary missing: ${cmd.description} (${cmd.error})`);
    }
  }

  return {
    environment: environmentData,
    commands,
    commandsText,
    warnings,
    filesGenerated: true,
    message: type === 'python'
      ? `Created Python environment: ${envName}\n  Path: ${envDir}\n  Activate: source ${envDir}/bin/activate`
      : `Created ${type} environment: ${envName}\n  Path: ${envDir}`
  };
}

// ─── Command formatting ───────────────────────────────────────────────────

/**
 * Format a commands array into human-readable text.
 */
function formatCommands(commands) {
  return commands.map((cmd, i) => {
    if (cmd.error) {
      return `  [!] ${cmd.description}: ${cmd.error}`;
    }
    const prefix = cmd.cwd ? `[${cmd.cwd}] ` : '';
    const bin = path.basename(cmd.binary);
    return `  [${i + 1}] ${prefix}${bin} ${cmd.args.join(' ')}`;
  }).join('\n');
}

/**
 * Format a single command for display.
 */
function formatSingleCommand(cmd) {
  if (cmd.error) return `[ERROR] ${cmd.error}`;
  return `${cmd.description}\n  → ${cmd.binary} ${cmd.args.join(' ')}`;
}

// ─── Port tracking (data-only, no shell) ──────────────────────────────────

function listPorts() {
  const ports = loadJSON(getPortsFile(), {});
  const entries = Object.entries(ports);

  if (entries.length === 0) {
    return { ports: {}, message: 'No managed ports.' };
  }

  return {
    ports,
    count: entries.length,
    table: formatPortsTable(entries)
  };
}

function formatPortsTable(entries) {
  const lines = [
    `${'Port'.padEnd(8)} ${'Service'.padEnd(25)} ${'Status'.padEnd(10)} ${'Bound To'.padEnd(15)}`,
    '-'.repeat(60)
  ];
  for (const [port, info] of entries) {
    lines.push(
      `${port.padEnd(8)} ${(info.service || 'unknown').padEnd(25)} ${(info.running ? 'running' : 'stopped').padEnd(10)} ${(info.bind || '0.0.0.0').padEnd(15)}`
    );
  }
  return lines.join('\n');
}

function findFreePorts(count = 5) {
  const ports = loadJSON(getPortsFile(), {});
  const used = Object.keys(ports).map(Number);
  const free = [];

  for (let port = 3000; port < 9000 && free.length < count; port++) {
    if (!used.includes(port) && port % 10 === 0) {
      free.push(port);
    }
  }

  return { freePorts: free };
}

// ─── Service management (data-only, no shell) ─────────────────────────────

function listServices() {
  const services = loadJSON(getServicesFile(), {});
  const entries = Object.entries(services);

  if (entries.length === 0) {
    return { services: {}, message: 'No managed services.' };
  }

  return {
    services,
    count: entries.length,
    table: formatServicesTable(entries)
  };
}

function formatServicesTable(entries) {
  const lines = [
    `${'Name'.padEnd(20)} ${'Port'.padEnd(8)} ${'Status'.padEnd(10)} ${'Type'.padEnd(10)}`,
    '-'.repeat(50)
  ];
  for (const [name, svc] of entries) {
    lines.push(
      `${name.padEnd(20)} ${String(svc.port || '—').padEnd(8)} ${(svc.running ? 'running' : 'stopped').padEnd(10)} ${(svc.type || 'unknown').padEnd(10)}`
    );
  }
  return lines.join('\n');
}

function buildServiceHealthCommands(name) {
  const services = loadJSON(getServicesFile(), {});
  const svc = services[name];
  if (!svc) {
    return {
      name, error: `Service not found: ${name}`,
      commands: []
    };
  }

  const commands = [];
  if (svc.port) {
    commands.push(buildCommand('lsof', ['-i', `:${svc.port}`, '-sTCP:LISTEN'], {
      description: `Check if port ${svc.port} is listening (service: ${name})`
    }));
  }

  return { name, service: svc, commands };
}

function startService(name) {
  const services = loadJSON(getServicesFile(), {});
  const svc = services[name];
  if (!svc) {
    return { name, error: `Service not found: ${name}` };
  }

  svc.running = true;
  saveJSON(getServicesFile(), services);

  return { name, service: svc, message: `Service ${name} registered as started on port ${svc.port}` };
}

function stopService(name) {
  const services = loadJSON(getServicesFile(), {});
  const svc = services[name];
  if (!svc) {
    return { name, error: `Service not found: ${name}` };
  }

  svc.running = false;
  saveJSON(getServicesFile(), services);

  return { name, service: svc, message: `Service ${name} registered as stopped` };
}

// ─── Cleanup ──────────────────────────────────────────────────────────────

function cleanupEnvs() {
  const envs = loadJSON(getEnvsFile(), {});
  const inactive = [];

  for (const [name, env] of Object.entries(envs)) {
    if (env.status === 'inactive') {
      inactive.push({ name, type: env.type, path: env.path });
    }
  }

  return {
    total: Object.keys(envs).length,
    inactive: inactive,
    message: `Found ${inactive.length} inactive environments out of ${Object.keys(envs).length} total`
  };
}

// ─── Status overview ──────────────────────────────────────────────────────

function showStatus() {
  const envs = loadJSON(getEnvsFile(), {});
  const services = loadJSON(getServicesFile(), {});
  const ports = loadJSON(getPortsFile(), {});

  const running = Object.values(services).filter(s => s.running).length;

  const types = {};
  for (const env of Object.values(envs)) {
    types[env.type] = (types[env.type] || 0) + 1;
  }

  return {
    environments: {
      count: Object.keys(envs).length,
      types
    },
    services: {
      count: Object.keys(services).length,
      running
    },
    ports: {
      managed: Object.keys(ports).length
    }
  };
}

// ─── CLI / entry point ────────────────────────────────────────────────────

/**
 * Main entry point.
 * Parses CLI arguments and generates command outputs.
 * The calling agent should execute any returned commands.
 */
function run(argv) {
  const args = argv || process.argv.slice(2);
  let mode = 'status';
  let submode = null;
  let extraArgs = [];
  let dryRun = false;

  for (let i = 0; i < args.length; i++) {
    if (args[i] === '--setup')     mode = 'setup';
    if (args[i] === '--ports')     mode = 'ports';
    if (args[i] === '--services')  mode = 'services';
    if (args[i] === '--cleanup')   mode = 'cleanup';
    if (args[i] === '--status')    mode = 'status';
    if (args[i] === '--commands')  mode = 'commands';
    if (args[i] === '--free')      submode = 'free';
    if (args[i] === '--start')     submode = 'start';
    if (args[i] === '--stop')      submode = 'stop';
    if (args[i] === '--status')    submode = 'health';
    if (args[i] === '--dry-run')   dryRun = true;
  }

  // Collect positional args for setup/services
  for (const a of args) {
    if (!a.startsWith('--') && a !== '--setup') extraArgs.push(a);
  }

  const result = { mode, output: null, commands: [], warnings: [], dryRun };

  switch (mode) {

    case 'setup': {
      const type = extraArgs[0];
      const name = extraArgs[1];
      if (!type) {
        result.output = {
          error: 'Missing environment type',
          usage: 'env-manager.js --setup <type> [name]\nTypes: python, node, docker, go, rust'
        };
      } else {
        const setup = setupEnvironment(type, name);
        result.output = {
          message: setup.message,
          environment: setup.environment,
          filesGenerated: setup.filesGenerated
        };
        result.commands = setup.commands;
        result.commandsText = setup.commandsText;
        result.warnings = setup.warnings;
      }
      break;
    }

    case 'ports': {
      if (submode === 'free') {
        result.output = findFreePorts();
      } else {
        const ports = listPorts();
        result.output = { ports: ports.ports, table: ports.table, count: ports.count };
      }
      break;
    }

    case 'services': {
      const name = extraArgs[0];
      if (submode === 'health') {
        result.output = buildServiceHealthCommands(name);
        result.commands = result.output.commands || [];
      } else if (submode === 'start') {
        result.output = startService(name);
      } else if (submode === 'stop') {
        result.output = stopService(name);
      } else {
        const services = listServices();
        result.output = { services: services.services, table: services.table, count: services.count };
      }
      break;
    }

    case 'cleanup':
      result.output = cleanupEnvs();
      break;

    case 'status':
      result.output = showStatus();
      break;

    case 'commands':
      // --commands mode: generate setup + health-check commands for all envs
      {
        const envs = loadJSON(getEnvsFile(), {});
        const allCommands = [];
        for (const [name, env] of Object.entries(envs)) {
          const { commands } = buildSetupCommands(env.type, name);
          allCommands.push(...commands);
        }
        result.output = { totalCommands: allCommands.length, commands };
        result.commands = allCommands;
      }
      break;

    default:
      result.output = showStatus();
      break;
  }

  return result;
}

// CLI execution when run directly
if (require.main === module) {
  const result = run();

  // Always print output
  if (result.output) {
    if (typeof result.output === 'object' && result.output.table) {
      console.log(result.output.table);
    } else if (typeof result.output === 'object' && result.output.error) {
      console.error(`[env-manager] ${result.output.error}`);
      if (result.output.usage) console.log(result.output.usage);
    } else if (typeof result.output === 'object' && result.output.freePorts) {
      console.log(`[env-manager] Free ports: ${result.output.freePorts.join(', ')}`);
    } else if (typeof result.output === 'object' && result.output.inactive) {
      console.log(`[env-manager] ${result.output.message}`);
      for (const inv of result.output.inactive || []) {
        console.log(`  Would remove: ${inv.name} (${inv.type}) at ${inv.path}`);
      }
    } else if (typeof result.output === 'object' && result.output.environment) {
      console.log(`[env-manager] ${result.output.message}`);
      if (result.output.environment.activation) {
        console.log(`[env-manager]   Activate: ${result.output.environment.activation}`);
      }
    } else if (typeof result.output === 'object' && result.output.name && result.output.message) {
      console.log(`[env-manager] ${result.output.message}`);
    } else if (typeof result.output === 'object' && result.output.environments) {
      // Status overview
      const s = result.output;
      console.log('[env-manager] Status:\n');
      console.log(`  Environments: ${s.environments.count} (${JSON.stringify(s.environments.types)})`);
      console.log(`  Services: ${s.services.count} (${s.services.running} running)`);
      console.log(`  Ports managed: ${s.portss?.managed || s.ports?.managed || 0}`);
    } else {
      console.log(JSON.stringify(result.output, null, 2));
    }
  }

  // Print commands the agent needs to execute
  if (result.commands && result.commands.length > 0) {
    console.log('\n[env-manager] --- Commands for agent execution ---\n');
    console.log(result.commandsText);
    console.log('\n[env-manager] --- End commands ---\n');
  }

  // Print warnings
  if (result.warnings && result.warnings.length > 0) {
    console.log('\n[env-manager] Warnings:\n');
    for (const w of result.warnings) {
      console.log(`  ⚠ ${w}`);
    }
    console.log('\n[env-manager] Fix these issues before executing the commands above.\n');
  }

  // Always output structured commands JSON for machine consumption
  if (result.commands && result.commands.length > 0) {
    console.log('\n[env-manager] STRUCTURED_COMMANDS:');
    console.log(JSON.stringify({
      mode: result.mode,
      commands: result.commands.map(c => ({
        binary: c.binary,
        args: c.args,
        cwd: c.cwd,
        env: c.env,
        description: c.description,
        status: c.status,
        error: c.error
      }))
    }, null, 2));
  }
}

// ─── Exports ───────────────────────────────────────────────────────────────

module.exports = {
  // Core builders
  buildCommand,
  buildSetupCommands,
  setupEnvironment,

  // Binary resolution (pure Node.js)
  findBinary,
  isOnAcceptlist,

  // Data operations (no shell)
  listPorts,
  findFreePorts,
  listServices,
  buildServiceHealthCommands,
  startService,
  stopService,
  cleanupEnvs,
  showStatus,

  // File scaffolding (fs only)
  generateScaffoldFiles,

  // Formatting
  formatCommands,
  formatSingleCommand,

  // CLI
  run,

  // Constants
  DEFAULT_ACCEPTED_BINARIES
};