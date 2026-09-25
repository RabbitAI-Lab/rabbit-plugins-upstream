## Description:

Install, configure, or run Codex through the codexbox wrapper, or connect to its HTTP, MCP, Telegram, or cron surfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use codexbox to install and run Codex in Docker, expose it through HTTP, OpenAI-compatible, MCP, Telegram, or cron surfaces, and manage workspace files or automated runs when those modes are requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API or MCP modes can expose agent execution and workspace file access if reachable without authentication.

Mitigation: Set distinct API and MCP bearer tokens before publishing any port, and prefer loopback binding or an authenticated proxy.

Risk: The Dockerized service has access to the mounted workspace and Codex authentication state.

Mitigation: Use trusted workspaces, avoid unauthenticated shared deployments, and pin or review Docker images before use.

Risk: The one-line installer executes a remote shell script.

Mitigation: Download and inspect the installer before running it unless the source and channel are already trusted.

Risk: Workspace file deletion through exposed file tools has no undo.

Mitigation: Confirm target paths and delete only files that the current task created or the user explicitly asked to remove.

## Reference(s):

- [codexbox setup](references/setup.md)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/codexbox)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON, YAML, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Docker, HTTP API, OpenAI-compatible endpoint, MCP, Telegram, and cron configuration examples.]

## Skill Version(s):

0.6.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
