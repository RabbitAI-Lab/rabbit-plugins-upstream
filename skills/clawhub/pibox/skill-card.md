## Description: <br>
pibox lets agents and developers run pi-coding-agent in a Docker container through shell, REST, OpenAI-compatible chat, MCP, Telegram, or cron interfaces. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation teams use pibox to expose pi-coding-agent as a containerized coding agent that can be driven from scripts, HTTP clients, OpenAI-compatible clients, MCP-aware agents, Telegram, or scheduled cron jobs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Unauthenticated API or MCP surfaces can allow remote agent execution and workspace file access when bearer tokens are empty. <br>
Mitigation: Set non-empty API and MCP bearer tokens, bind services to localhost, or place them behind an authenticating proxy. <br>
Risk: Workspace mounts expose files to the coding agent and to network surfaces enabled by the deployment. <br>
Mitigation: Mount only the workspace intended for agent access and avoid shared unauthenticated deployments. <br>
Risk: Delete and cancel routes can remove files or interrupt runs without undo. <br>
Mitigation: Treat delete and cancel actions as admin-only operations and confirm the specific target before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/pibox) <br>
- [Publisher profile](https://clawhub.ai/user/psyb0t) <br>
- [Setup reference](references/setup.md) <br>
- [docker-pibox repository](https://github.com/psyb0t/docker-pibox) <br>
- [pi-coding-agent](https://github.com/earendil-works/pi-mono/tree/main/packages/coding-agent) <br>
- [docker-aicodebox](https://github.com/psyb0t/docker-aicodebox) <br>
- [Model Context Protocol](https://modelcontextprotocol.io) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline code blocks, shell commands, JSON examples, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill guides setup and use of a high-power networked coding-agent surface; generated commands and configuration should be reviewed before execution.] <br>

## Skill Version(s): <br>
0.15.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
