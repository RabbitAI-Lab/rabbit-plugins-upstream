## Description:

pibox helps agents and developers run pi-coding-agent in a Docker container through shell, REST/OpenAI-compatible HTTP, MCP, Telegram, or cron interfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation teams use pibox to expose pi-coding-agent through containerized HTTP, OpenAI-compatible, MCP, Telegram, cron, or one-shot command workflows. It is useful when an agent or integration needs remote execution, workspace file access, scheduled runs, or SDK-compatible chat access instead of a local terminal session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unauthenticated API or MCP surfaces can allow remote agent execution and workspace file access when tokens are left empty.

Mitigation: Set non-empty API and MCP bearer tokens and keep the service on localhost or behind an authenticating proxy or firewall.

Risk: Delete and cancel routes can permanently remove files, cancel runs, or affect another caller on shared instances.

Mitigation: Treat delete and cancel routes as admin-only actions and require explicit confirmation of the specific target before use.

Risk: Shared multi-tenant workspaces can expose one caller's runs or files to another caller.

Mitigation: Avoid shared multi-tenant workspaces or isolate workspaces per user, project, or automation context.

## Reference(s):

- [pibox ClawHub page](https://clawhub.ai/psyb0t/skills/pibox)
- [pibox setup](references/setup.md)
- [pibox homepage](https://github.com/psyb0t/docker-pibox)
- [pi-coding-agent](https://github.com/earendil-works/pi-mono/tree/main/packages/coding-agent)
- [aicodebox](https://github.com/psyb0t/docker-aicodebox)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with command, JSON, YAML, and HTTP examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can include mode selection advice, Docker commands, API calls, MCP configuration, Telegram or cron configuration, and security guidance.]

## Skill Version(s):

0.15.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
