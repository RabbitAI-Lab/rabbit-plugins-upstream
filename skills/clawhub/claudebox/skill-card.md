## Description:

Install, configure, or run Claude Code through the claudebox wrapper, or connect to its HTTP, MCP, Telegram, or cron surfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to run Claude Code in a containerized wrapper, automate one-shot CLI tasks, or expose Claude Code through HTTP, OpenAI-compatible, MCP, Telegram, and cron surfaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Server modes can expose agent execution and workspace file access if API or MCP tokens are unset or services are reachable beyond localhost.

Mitigation: Set distinct bearer tokens for API and MCP modes, bind services to localhost or place them behind an authenticating proxy, and expose only the modes needed for the deployment.

Risk: Mounting /var/run/docker.sock grants host-level container control to processes that can use the mounted socket.

Mitigation: Avoid mounting the Docker socket unless the workload requires host Docker control; when it is required, run only on trusted hosts and combine it with container hardening and network isolation.

Risk: The wrapper runs Claude Code with broad shell, file, and container capabilities inside the container, including bypassed permission prompts by default.

Mitigation: Use claudebox only in trusted isolated workspaces, avoid untrusted prompts or files unless the container itself is isolated, and limit forwarded credentials to what the task needs.

Risk: Installer and update flows may download and execute remote scripts or images with the user's privileges.

Mitigation: Prefer the documented download-inspect-run install path, pin images or packages where possible, and review downloaded scripts before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/claudebox)
- [Artifact homepage](https://github.com/psyb0t/docker-claudebox)
- [setup.md](references/setup.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code, markdown]

**Output Format:** [Markdown guidance with inline shell commands, JSON, YAML, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce commands and configuration for local wrappers, container launches, HTTP API calls, MCP setup, Telegram mode, or cron scheduling.]

## Skill Version(s):

2.4.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
