---
name: env-manager
description: Scaffolds dev project files (package.json, Dockerfile, Cargo.toml, etc.) for Python, Node, Docker, Go, and Rust. Returns a list of toolchain commands for the calling agent to run. Writes files only inside the agent workspace.
---

# Env Manager

Creates the initial project files for a new dev environment and returns a list of toolchain commands the calling agent should run to set up the rest.

## What it does

For each language (`python`, `node`, `docker`, `go`, `rust`), it:

1. **Writes starter files** to a project directory inside the agent workspace using `fs.writeFileSync`:
   - `node` → `package.json`, `index.js`, `.gitignore`
   - `docker` → `Dockerfile`, `docker-compose.yml`
   - `go` → `main.go`
   - `rust` → `Cargo.toml`, `src/main.rs`
   - `python` → `.env.example`
2. **Returns a list of toolchain commands** the agent should run, like `python3 --version`, `go mod init`, etc. The agent (not this skill) executes those commands.
3. **Tracks state** in `memory/environments/` so the agent can list environments, ports, and services later.

## What it does not do

- It does not run shell commands, scripts, or binaries.
- It does not start any system process.
- It does not modify files outside the agent workspace.
- It does not touch `ENV_DIR` from the environment or accept a `--dir` flag for runtime path redirection.
- It does not provide its own network or file-system scanning.

## Important: file writes happen on every call

Every call to `setupEnvironment(type, name)` will:

- Create a directory at `environments/<name>/` inside the agent workspace.
- Write starter files into that directory.
- Update `memory/environments/environments.json`.

These writes happen unconditionally before the toolchain commands are returned. If you do not want files written, do not call `setupEnvironment`. There is no preview / no confirm step.

## Output shape

```js
{
  environment: { name, type, path, created, status, /* type-specific fields */ },
  commands: [
    {
      binary: "/usr/bin/python3",
      args: ["-m", "venv", "/path/to/env"],
      cwd: "/workspace",
      description: "Create Python venv",
      status: "ready" // "ready" | "blocked" | "not_found" | "error"
    }
  ],
  commandsText: "  [1] python3 --version\n  [2] python3 -m venv ...",
  warnings: [],
  filesGenerated: true,
  message: "Created Python environment: my-app\n  Path: /workspace/environments/my-app\n  Activate: source /workspace/environments/my-app/bin/activate"
}
```

`commands[]` is for the calling agent to run. The skill does not run them.

## Programmatic API

```js
const em = require('./env-manager.js');

// Create a project and get back toolchain commands.
const r = em.setupEnvironment('node', 'my-api');
// r.environment, r.commands, r.warnings

// List what already exists.
em.listEnvironments();   // → { environments: {...}, count }
em.listPorts();          // → { ports: {...}, count }
em.listServices();       // → { services: {...}, count }
em.showStatus();         // → { environments, services, ports }

// Mark a service as running or stopped (data only, no process control).
em.startService('my-api');   // sets running: true in services.json
em.stopService('my-api');    // sets running: false

// Find a free port.
em.findFreePorts(5);    // → { freePorts: [3000, 3010, 3020, ...] }

// Build a port-check command (the agent runs it).
em.buildServiceHealthCommands('my-api');
// → { name, service, commands: [{ binary, args, ... }] }

// Remove tracking for inactive environments (data only).
em.cleanupEnvs();
```

## CLI

```bash
node env-manager.js --setup <type> <name>   # scaffold a project + return commands
node env-manager.js --status                # show counts of envs / services / ports
node env-manager.js --cleanup               # list inactive environments
node env-manager.js --services              # list services
node env-manager.js --services --start <name>  # mark service as started
node env-manager.js --services --stop <name>   # mark service as stopped
node env-manager.js --services --status <name> # return port-check commands
node env-manager.js --ports                 # list ports
node env-manager.js --ports --free          # find free ports
node env-manager.js --commands              # return all setup commands for stored envs
```

## Data storage

All state is written to `memory/environments/` inside the agent workspace:

- `environments.json` — created environments
- `ports.json` — port tracking
- `services.json` — service metadata (name, port, type, running flag)

The data directory is the only thing the skill writes to. No other paths are touched.

## Trust model

- The skill writes files only inside the agent workspace, in a known data directory (`memory/environments/` plus per-project scaffolding inside the workspace).
- File writes are limited to well-known starter files (`package.json`, `index.js`, `.gitignore`, `Dockerfile`, `docker-compose.yml`, `main.go`, `Cargo.toml`, `src/main.rs`, `.env.example`) plus three small JSON state files. No other paths are touched.
- The skill does not run any external process.
- The skill does not call network functions.
- The agent that calls the skill is responsible for executing the returned `commands[]`.
- The agent is responsible for checking `warnings[]` before executing anything.

## Risk surface

- **File writes are the only side effect.** Every successful `setupEnvironment` call creates or overwrites the files listed above. There is no preview, no confirm step, and no `--dry-run` mode in v2.0.1. If a file with the same name already exists in the project directory, it is overwritten.
- **State lives in the workspace.** `memory/environments/*.json` files are written and updated on each call. `cleanupEnvs()` removes inactive entries from those files; it does not delete project directories.
- **Returned commands are not run by the skill.** The `commands[]` array is a JSON description of work the agent should do. The skill never invokes those binaries.
- **Service/port tracking is metadata only.** `startService` / `stopService` toggle a `running` flag in `services.json`. They do not start, stop, or signal any real OS process.

## Exports

```js
em.setupEnvironment(type, name)             // → { environment, commands, commandsText, warnings, filesGenerated, message }
em.buildSetupCommands(type, name)           // → { commands, environment }
em.generateScaffoldFiles(type, name, dir)   // → void; writes files with fs.writeFileSync
em.listEnvironments / em.listPorts / em.listServices
em.startService / em.stopService
em.buildServiceHealthCommands
em.findFreePorts
em.cleanupEnvs
em.showStatus
em.run(argv)                                // → { mode, output, commands, commandsText, warnings }
```
