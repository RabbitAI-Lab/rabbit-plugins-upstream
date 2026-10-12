## Description:

Install, configure, or run Claude Code through the claudebox wrapper, or connect to its HTTP, MCP, Telegram, or cron surfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to run Claude Code in a container and configure local, HTTP, MCP, Telegram, or scheduled workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The container can access mounted files, credentials, and the host Docker daemon with broad execution authority.

Mitigation: Use only for trusted tasks; isolate the container and review mounted host state, keys, hooks, and always-active skills before use.

Risk: HTTP and MCP services may expose powerful actions without authentication if tokens are unset.

Mitigation: Set separate API and MCP tokens before starting server modes, and bind services to loopback or a trusted proxy.

Risk: Installing unreviewed scripts or mutable images can introduce unexpected behavior.

Mitigation: Inspect the installer before running it and prefer pinned image versions.

Risk: Scheduled tasks and custom initialization scripts can execute later without direct supervision.

Mitigation: Review cron jobs, initialization hooks, and custom scripts before enabling them.

## Reference(s):

- [Claudebox setup guide](references/setup.md)
- [Claudebox release on ClawHub](https://clawhub.ai/psyb0t/skills/claudebox)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with command and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

2.5.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
