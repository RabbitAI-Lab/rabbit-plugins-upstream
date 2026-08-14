# OpenClaw SKILL.md schema (cheat sheet)

OpenClaw skills are folders containing a `SKILL.md` file. OpenClaw follows the
[AgentSkills](https://agentskills.io) spec. Use this when authoring a skill from
a Teach demonstration so the result loads and validates.

## Minimal file

```markdown
---
name: my-skill
description: One-line summary shown to the agent and in discovery (<160 chars).
---

# Title
Markdown instructions telling the agent *what* to do.
```

## Required frontmatter

| Field         | Rule                                              |
| ------------- | ------------------------------------------------- |
| `name`        | 1–64 chars, lowercase letters/digits/hyphens     |
| `description` | One line, under 160 characters                   |

## Optional frontmatter

| Field                    | Default | Notes                                         |
| ------------------------ | ------- | --------------------------------------------- |
| `version`                | —       | Semver string                                 |
| `homepage`               | —       | URL shown in Skills UI                        |
| `user-invocable`         | `true`  | Expose as a slash command (`/<name>`)        |
| `disable-model-invocation` | `false` | Keep instructions out of the system prompt   |
| `command-dispatch`       | —       | Set `"tool"` to route slash cmd straight to a tool |
| `command-tool`          | —       | Tool name when `command-dispatch: tool`       |
| `command-arg-mode`       | `"raw"` | Arg forwarding for tool dispatch              |
| `metadata.openclaw`      | —       | Gating/runtime metadata (see below)           |

## Gating under `metadata.openclaw`

| Key                | Type       | Meaning                                         |
| ------------------ | ---------- | ----------------------------------------------- |
| `requires.bins`    | `string[]` | All binaries must exist on `PATH`              |
| `requires.anyBins` | `string[]` | At least one must exist on `PATH`              |
| `requires.env`     | `string[]` | Each env var must be present                    |
| `requires.config`  | `string[]` | Each `openclaw.json` path must be truthy        |
| `primaryEnv`       | `string`   | Main credential env var                         |
| `envVars`          | `array`    | `{name, required, description}` per var         |
| `always`           | `boolean`  | Skip all gates, always include                  |
| `skillKey`         | `string`   | Override the invocation key                     |
| `emoji`            | `string`   | Display emoji                                    |
| `homepage`         | `string`   | URL                                             |
| `os`               | `string[]` | `["darwin"]` / `["linux"]` / `["win32"]`         |
| `install`          | `array`    | brew/node/go/uv/download dependency specs        |

## Body rules

- Instruct the model on **what** to do, not how to be an AI.
- Reference in-skill files with `{baseDir}` (e.g. `{baseDir}/scripts/run.sh`).
- Keep `description` short — it is injected into the system prompt per skill.
- Prefer connectors/MCP tools over UI replay; mark consequential steps
  confirm-first; never embed credentials.

## Placement (load order, highest first)

1. `<workspace>/skills` — workspace skills (Teach writes here)
2. `<workspace>/.agents/skills` — project-agent skills
3. `~/.agents/skills` — personal-agent skills
4. `<state-dir>/skills` — managed/local
5. bundled — shipped with install
6. extra dirs / plugin skills

Invoke with `/<name>` or reference with `$<name>` in a prompt.

## Validate

```bash
skills-ref validate ./my-skill      # agentskills.io reference tool
openclaw skills list                 # confirm it loaded
```
