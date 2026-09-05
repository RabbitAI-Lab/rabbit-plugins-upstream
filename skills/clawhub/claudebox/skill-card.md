## Description:

claudebox helps agents install, configure, launch, and script against a Docker-hosted Claude Code environment with CLI, HTTP, OpenAI-compatible, MCP, Telegram, and cron interfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use claudebox to run Claude Code inside Docker and expose it through CLI, REST, OpenAI-compatible, MCP, Telegram, or scheduled cron workflows. It is intended for installing, configuring, launching, and scripting against a claudebox container or wrapper.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose a network-accessible coding agent with broad file, shell, container, and background-task authority.

Mitigation: Install it only in isolated environments, limit mounted host directories, and bind services to localhost or place them behind an authenticated proxy.

Risk: API and MCP server modes may be unauthenticated when their bearer-token environment variables are unset.

Mitigation: Set per-mode API and MCP tokens before enabling server modes and avoid exposing unauthenticated ports.

Risk: Mounting /var/run/docker.sock can grant host-level container control.

Mitigation: Avoid mounting the Docker socket unless required, and use it only on hosts trusted for this workload.

Risk: Cron, Telegram, and always-active skill configuration can create persistent or shared execution paths.

Mitigation: Review those configurations before sharing an instance and prefer pinned image or package versions.

## Reference(s):

- [Setup Guide](references/setup.md)
- [ClawHub Skill Page](https://clawhub.ai/psyb0t/skills/claudebox)
- [Project Homepage](https://github.com/psyb0t/docker-claudebox)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, YAML configuration, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose commands or configuration that affect files, containers, network services, or scheduled jobs.]

## Skill Version(s):

2.3.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
