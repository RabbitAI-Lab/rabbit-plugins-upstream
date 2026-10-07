## Description:

Install, configure, or run Claude Code through the claudebox wrapper, or connect to its HTTP, MCP, Telegram, or cron surfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use claudebox to run Claude Code for coding tasks in a container, or connect other tools to its HTTP and MCP services and schedule recurring jobs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The standard wrapper can give the coding agent host-level Docker control.

Mitigation: Use only with trusted prompts; do not rely on the container as a sandbox for untrusted input.

Risk: Exposed API, MCP, or Telegram modes can permit unauthorized agent or file operations when configured without access controls.

Mitigation: Use separate service tokens and Telegram allowlists; bind services to loopback or place them behind an authenticated proxy.

Risk: Remote installation scripts and unpinned dependencies can change unexpectedly.

Mitigation: Inspect the installer before running it and pin image and package versions for production.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/psyb0t/skills/claudebox)
- [Installation and setup guide](artifact/references/setup.md)
- [Project homepage](https://github.com/psyb0t/docker-claudebox)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with command and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Output depends on the requested Claude Code task and enabled service mode.]

## Skill Version(s):

2.4.7 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
