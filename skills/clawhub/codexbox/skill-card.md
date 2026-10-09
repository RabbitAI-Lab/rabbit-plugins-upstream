## Description:

Install, configure, or run Codex through the codexbox wrapper, or connect to its HTTP, MCP, Telegram, or cron surfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use codexbox to run Codex in a container for interactive or automated workspace tasks, or to connect it to HTTP, MCP, Telegram, and scheduled workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exposed API or MCP endpoints may allow unauthenticated execution and workspace file access.

Mitigation: Set separate API and MCP bearer tokens and bind services to loopback or use an authenticating proxy.

Risk: File deletion can permanently remove workspace data.

Mitigation: Review the target before deletion and only remove files the user has authorized.

Risk: Remote installers and container images run code in the user's environment.

Mitigation: Inspect or pin the installer and Docker image before use.

## Reference(s):

- [codexbox on ClawHub](https://clawhub.ai/psyb0t/skills/codexbox)
- [codexbox setup guide](references/setup.md)
- [codexbox project documentation](https://github.com/psyb0t/docker-codexbox)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration instructions]

**Output Format:** [Plain text, Markdown, code, shell commands, or structured API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Output depends on the requested Codex task and interface.]

## Skill Version(s):

0.7.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
