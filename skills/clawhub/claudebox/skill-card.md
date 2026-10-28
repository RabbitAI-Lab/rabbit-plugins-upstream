## Description:

Install, configure, or run Claude Code through the claudebox wrapper, or connect to its HTTP, MCP, Telegram, or cron surfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use claudebox to install, configure, and run Claude Code for workspace tasks, or to connect it to HTTP, MCP, Telegram, and scheduled-job workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The default setup bypasses permission prompts and gives the coding agent Docker access that extends beyond the selected workspace.

Mitigation: Use a dedicated environment without the host Docker socket for untrusted content, and review what credentials and files the agent can access.

Risk: Exposed API or MCP endpoints may be unauthenticated when tokens are unset; Telegram access may be too broad without an allowlist.

Mitigation: Configure distinct API and MCP tokens and a Telegram chat allowlist before exposing these services.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/psyb0t/skills/claudebox)
- [Setup guide](references/setup.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Operational guidance]

**Output Format:** [Bash commands and concise setup, usage, and security guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Mode-specific instructions for local CLI use and optional HTTP, MCP, Telegram, or scheduled-job workflows.]

## Skill Version(s):

2.8.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
