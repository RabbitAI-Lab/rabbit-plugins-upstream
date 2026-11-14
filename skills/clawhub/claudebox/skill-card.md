## Description:

Install, configure, or run Claude Code through the claudebox wrapper, or connect to its HTTP, MCP, Telegram, or cron surfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to install and operate Claude Code in a Docker-backed workspace, run one-shot coding tasks, or configure API, OpenAI-compatible, MCP, Telegram, and scheduled job access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The default wrapper bypasses permission checks and exposes the host Docker socket to Claude Code.

Mitigation: Use only with trusted prompts and isolate the container or host when working with untrusted input.

Risk: The documented quick install pipes a remote installer directly into Bash.

Mitigation: Download and inspect the installer and related components before running them.

Risk: API and MCP endpoints have no authentication when their respective tokens are unset.

Mitigation: Set separate bearer tokens and bind to loopback or use an authenticated proxy before exposing endpoints beyond localhost.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/psyb0t/skills/claudebox)
- [Project repository](https://github.com/psyb0t/docker-claudebox)
- [Setup guide](references/setup.md)
- [API mode documentation](https://github.com/psyb0t/docker-claudebox/blob/master/docs/modes/api.md)
- [MCP mode documentation](https://github.com/psyb0t/docker-claudebox/blob/master/docs/modes/mcp.md)
- [Environment variables reference](https://github.com/psyb0t/docker-claudebox/blob/master/docs/environment-variables.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Text, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON or YAML examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples cover interactive and one-shot CLI use, server configuration, and structured agent responses.]

## Skill Version(s):

2.8.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
