## Description:

Install, configure, or run Codex through the codexbox wrapper, or connect to its HTTP, MCP, Telegram, or cron surfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to install and operate containerized Codex, run agent tasks, and connect applications through its HTTP, MCP, Telegram, or scheduled interfaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A remote installer or unverified container image could execute untrusted code.

Mitigation: Inspect the installer before running it; trust the repository and verify or pin the container image where possible.

Risk: Unauthenticated HTTP or MCP endpoints can allow remote agent execution and workspace file access.

Mitigation: Set distinct API and MCP bearer tokens and bind services to localhost or place them behind an authenticated proxy.

Risk: Broad host mounts or file deletion could expose or irreversibly remove data.

Mitigation: Limit host mounts, confirm paths before deletion, and delete only files the current task created with user approval.

Risk: Unattended cron or Telegram automation can perform high-impact actions without immediate review.

Mitigation: Restrict authorized chats and scheduled jobs, scope their workspace access, and review tasks before enabling automation.

## Reference(s):

- [codexbox on ClawHub](https://clawhub.ai/psyb0t/skills/codexbox)
- [Setup guide](references/setup.md)
- [codexbox project homepage](https://github.com/psyb0t/docker-codexbox)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Instructions may include HTTP requests and scheduled-job configuration.]

## Skill Version(s):

0.7.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
