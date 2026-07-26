# env-manager

Scaffolds starter files for new dev projects (Python, Node, Docker, Go, Rust) and returns a list of toolchain commands the calling agent should run.

## What it does

For each language, it writes a few starter files into a project directory and returns commands the agent should run. The skill does not run any commands itself.

| Type   | Files written                                                            |
|--------|--------------------------------------------------------------------------|
| node   | `package.json`, `index.js`, `.gitignore`                                 |
| docker | `Dockerfile`, `docker-compose.yml`                                       |
| go     | `main.go`                                                                |
| rust   | `Cargo.toml`, `src/main.rs`                                              |
| python | `.env.example`                                                           |

It also tracks environments, ports, and services in `memory/environments/`.

## What it does not do

- It does not run shell commands, scripts, or binaries.
- It does not import or use any process-spawning module.
- It does not modify files outside the agent workspace.
- It does not read or accept `ENV_DIR` for runtime path redirection.
- It does not perform network calls.

## Programmatic use

```js
const em = require('./env-manager.js');

const result = em.setupEnvironment('node', 'my-api');
// result.environment — metadata
// result.commands — array of { binary, args, cwd, description, status }
// result.commandsText — formatted text version
// result.warnings — anything the agent should know
// result.filesGenerated — always true after a setup call
```

The agent that called the skill should look at `result.commands` and run each one where `status === "ready"`.

## CLI

```bash
node env-manager.js --setup <type> <name>
node env-manager.js --status
node env-manager.js --cleanup
node env-manager.js --services
node env-manager.js --services --start <name>
node env-manager.js --services --stop <name>
node env-manager.js --services --status <name>
node env-manager.js --ports
node env-manager.js --ports --free
node env-manager.js --commands
```

## Data storage

State is written to `memory/environments/` inside the agent workspace:

- `environments.json`
- `ports.json`
- `services.json`

No other paths are touched.

## License

MIT — Part of the OpenClaw skill ecosystem.
