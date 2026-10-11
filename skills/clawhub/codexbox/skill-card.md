## Description:

Install, configure, or run Codex through the codexbox wrapper, or connect to its HTTP, MCP, Telegram, or cron surfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to install and operate containerized Codex for interactive work, automated jobs, and authenticated HTTP or MCP integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An unreviewed installer or container image can execute code with access to the user's workspace.

Mitigation: Inspect the installer, trust its source, and review or pin the container image version before running it.

Risk: Exposed HTTP or MCP services without tokens allow remote prompt execution and workspace file access.

Mitigation: Set distinct strong API and MCP bearer tokens and bind services to localhost or an authenticated proxy.

Risk: Telegram or scheduled runs can access sensitive workspaces without direct human supervision.

Mitigation: Avoid these modes for sensitive workspaces unless access controls are configured.

## Reference(s):

- [codexbox setup guide](references/setup.md)
- [codexbox project documentation](https://github.com/psyb0t/docker-codexbox)
- [OpenAI Codex CLI](https://github.com/openai/codex)
- [aicodebox container](https://github.com/psyb0t/docker-aicodebox)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Instructions and examples for installation, operation, and integration.]

## Skill Version(s):

0.7.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
