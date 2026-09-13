## Description:

claudebox helps agents install, configure, launch, and script Claude Code inside a Docker-backed container through CLI, HTTP API, OpenAI-compatible, MCP, Telegram, and cron interfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use claudebox to run Claude Code from scripts, CI, HTTP clients, OpenAI-compatible clients, MCP clients, Telegram, or scheduled jobs while managing container setup, credentials, workspaces, and hardening choices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unauthenticated API or MCP server modes can expose prompt execution and file operations when mode-specific tokens are unset.

Mitigation: Set API, MCP, and Telegram bearer tokens before enabling server modes, and bind services to localhost or place them behind an authenticated proxy.

Risk: Mounting /var/run/docker.sock can grant host-level container control.

Mitigation: Avoid mounting the Docker socket unless required, and use trusted, disposable hosts with container hardening controls when it is mounted.

Risk: Default broad permissions, mounted credentials, custom scripts, always-active skills, extra mounts, and cron configuration can expand the impact of an unsafe prompt or exposed service.

Mitigation: Use trusted inputs, isolate workspaces, review SSH keys and mounted paths, inspect always-active skills and custom scripts, and review scheduled jobs before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/claudebox)
- [Publisher profile](https://clawhub.ai/user/psyb0t)
- [Setup guide](references/setup.md)
- [Project homepage](https://github.com/psyb0t/docker-claudebox)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API request examples, MCP client configuration, Docker or docker-compose snippets, and risk guidance.]

## Skill Version(s):

2.4.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
