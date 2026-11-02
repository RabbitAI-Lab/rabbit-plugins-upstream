## Description:

Install, configure, or run Codex through the codexbox wrapper, or connect to its HTTP, MCP, Telegram, or cron surfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use codexbox to install, configure, and run Codex in a container for workspace tasks, or to connect it to explicitly enabled HTTP, MCP, Telegram, and scheduled-job workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic sandbox bypass combined with host Docker access can extend an agent's reach beyond its workspace.

Mitigation: Use an isolated machine and dedicated Codex/SSH state; review the installer and wrapper, select a reviewed image digest, use separate API and MCP tokens, bind services to loopback, and enable scheduled jobs only with explicit scope and a stopping plan.

## Reference(s):

- [codexbox setup](references/setup.md)
- [codexbox project](https://github.com/psyb0t/docker-codexbox)
- [aicodebox project](https://github.com/psyb0t/docker-aicodebox)
- [OpenAI Codex CLI](https://github.com/openai/codex)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Code]

**Output Format:** [Markdown guidance with shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.7.6 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
