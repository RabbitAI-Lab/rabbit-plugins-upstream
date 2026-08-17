## Description:

pibox guides agents and developers in running pi-coding-agent in a Docker container through shell, REST, OpenAI-compatible, MCP, Telegram, and cron interfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use pibox to choose and configure a containerized pi-coding-agent access mode for scripted, HTTP, MCP, Telegram, or scheduled automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An unauthenticated API or MCP surface can allow remote agent execution and workspace file access.

Mitigation: Set both PIBOX_API_MODE_TOKEN and PIBOX_MCP_MODE_TOKEN, bind services to localhost or place them behind an authenticating proxy, and avoid exposing host networking unless required.

Risk: A broad bind mount can give the containerized agent access to files outside the intended task scope.

Mitigation: Bind-mount only the workspace directory the agent is allowed to read or modify.

Risk: Cancel and delete operations can irreversibly remove run state or workspace files.

Mitigation: Treat delete and cancel endpoints as admin-only operations and require explicit user confirmation for the exact target.

## Reference(s):

- [pibox setup](references/setup.md)
- [pibox source repository](https://github.com/psyb0t/docker-pibox)
- [pi-coding-agent](https://github.com/earendil-works/pi-mono/tree/main/packages/coding-agent)
- [aicodebox container base](https://github.com/psyb0t/docker-aicodebox)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, configuration examples, endpoint descriptions, and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Docker commands, curl examples, environment variables, YAML snippets, and mode-selection guidance.]

## Skill Version(s):

0.15.11 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
