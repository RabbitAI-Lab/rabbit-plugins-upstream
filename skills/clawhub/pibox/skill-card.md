## Description:

pibox helps agents and developers run pi-coding-agent inside an aicodebox container through shell, REST and OpenAI-compatible HTTP, MCP, Telegram, and cron interfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to choose, configure, and operate pibox as a containerized pi-coding-agent surface for scripted runs, HTTP integrations, MCP clients, Telegram workflows, and scheduled cron jobs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A long-lived pibox service can run coding-agent prompts and read, modify, or delete files in the mounted workspace.

Mitigation: Mount only the smallest workspace needed, keep the service bound to localhost or a trusted proxy, and review generated changes before relying on them.

Risk: REST and MCP surfaces are unauthenticated when their bearer-token environment variables are empty.

Mitigation: Set nonempty PIBOX_API_MODE_TOKEN and PIBOX_MCP_MODE_TOKEN values, prefer Authorization headers, and do not expose unauthenticated instances to untrusted networks or agents.

Risk: Broad networking and unpinned container images can increase deployment and supply-chain risk.

Mitigation: Pin and verify the Docker image and avoid host networking unless the deployment explicitly requires it.

Risk: Delete, cancel, and cron capabilities can remove state or perform administrative actions without an undo path.

Mitigation: Treat delete and cron operations as administrative actions and require explicit user confirmation for the specific target before use.

## Reference(s):

- [pibox ClawHub release](https://clawhub.ai/psyb0t/skills/pibox)
- [pibox setup](references/setup.md)
- [pibox project homepage](https://github.com/psyb0t/docker-pibox)
- [pi-coding-agent](https://github.com/earendil-works/pi-mono/tree/main/packages/coding-agent)
- [docker-aicodebox](https://github.com/psyb0t/docker-aicodebox)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON and YAML snippets, and HTTP examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Docker, curl, OpenAI-compatible API, MCP, Telegram, and cron configuration guidance.]

## Skill Version(s):

0.16.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
