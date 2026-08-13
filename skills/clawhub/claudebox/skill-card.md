## Description:

Claude Code running on the network inside a Docker container, managed through the claudebox wrapper and exposed through CLI, HTTP API, OpenAI-compatible, MCP, Telegram, and cron interfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to install, configure, launch, and script against a Docker-hosted Claude Code environment. It is intended for operating claudebox through its wrapper, API, OpenAI-compatible adapter, MCP server, Telegram bot, or cron scheduler.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unauthenticated API, MCP, or Telegram surfaces can expose agent execution and workspace file access when bearer tokens are unset.

Mitigation: Set the per-mode bearer tokens before exposing any port, bind services to localhost or an authenticating proxy, and install only on hosts you trust.

Risk: Mounting /var/run/docker.sock gives processes in the container host-level container control.

Mitigation: Avoid mounting the Docker socket unless the workload requires it, and only mount it on trusted hosts.

Risk: Downloaded install scripts and scheduled or Telegram-triggered tasks can run with sensitive local context.

Mitigation: Download and inspect install scripts before running them, and treat cron and Telegram history as sensitive because recent job context can be reused in later prompts.

## Reference(s):

- [Claudebox setup](references/setup.md)
- [Claudebox ClawHub page](https://clawhub.ai/psyb0t/skills/claudebox)
- [Project homepage](https://github.com/psyb0t/docker-claudebox)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce commands and configuration that affect Docker containers, mounted workspaces, API/MCP endpoints, Telegram mode, and cron jobs.]

## Skill Version(s):

2.3.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
