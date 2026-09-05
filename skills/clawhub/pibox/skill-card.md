## Description:

pibox helps agents and developers run pi-coding-agent in a Docker container through shell, REST, OpenAI-compatible, MCP, Telegram, and cron interfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use pibox to expose a self-hosted pi-coding-agent workspace through Docker, HTTP, OpenAI-compatible chat, MCP, Telegram, or scheduled cron workflows. It is useful when an agent or service needs programmatic access to pi-coding-agent rather than a local terminal session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unauthenticated API or MCP surfaces can expose agent execution and workspace file read/write/delete access.

Mitigation: Set both API and MCP bearer tokens, bind endpoints to localhost or an authenticated proxy, and do not expose unauthenticated surfaces to a network.

Risk: Workspace mounts and delete or cancel operations can cause irreversible data loss or disrupt another caller on shared instances.

Mitigation: Mount only the workspace the agent may modify, confirm destructive targets before use, and treat delete and cancel routes as privileged operations.

Risk: Host networking and unpinned container images can increase deployment risk on shared or exposed machines.

Mitigation: Avoid --network host outside local use, publish only required ports, and pin the Docker image version for deployment.

## Reference(s):

- [pibox setup](references/setup.md)
- [ClawHub pibox skill page](https://clawhub.ai/psyb0t/skills/pibox)
- [pibox source homepage](https://github.com/psyb0t/docker-pibox)
- [pi-coding-agent](https://github.com/earendil-works/pi-mono/tree/main/packages/coding-agent)
- [aicodebox container](https://github.com/psyb0t/docker-aicodebox)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Docker, curl, MCP, Telegram, cron, and OpenClaw configuration guidance.]

## Skill Version(s):

0.15.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
