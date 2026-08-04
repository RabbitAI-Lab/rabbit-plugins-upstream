## Description: <br>
pibox helps agents and developers run pi-coding-agent inside an aicodebox container through interactive shell, one-shot execution, REST, OpenAI-compatible chat, MCP, Telegram, and cron interfaces. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to choose, configure, and operate pibox modes for remote coding-agent access over HTTP, OpenAI-compatible clients, MCP, Telegram, cron, or Docker one-shot runs. It is most useful when an agent needs guidance for programmatic execution, workspace file access, model configuration, or safe deployment boundaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: REST, OpenAI-compatible, or MCP surfaces can be unauthenticated when their bearer-token environment variables are unset. <br>
Mitigation: Set strong PIBOX_API_MODE_TOKEN and PIBOX_MCP_MODE_TOKEN values before exposing services, and bind to localhost or place the service behind an authenticating proxy. <br>
Risk: Workspace file deletion and run cancellation are destructive and may affect shared or in-flight work. <br>
Mitigation: Treat delete and cancel actions as admin-level operations, confirm the exact target before use, and avoid shared unauthenticated workspaces. <br>
Risk: Telegram and cron operation can run agent tasks or access workspaces without an interactive approval moment. <br>
Mitigation: Restrict Telegram chats and users, review cron job definitions before deployment, and scope workspaces to the intended automation. <br>


## Reference(s): <br>
- [pibox ClawHub listing](https://clawhub.ai/psyb0t/skills/pibox) <br>
- [pibox setup reference](references/setup.md) <br>
- [pibox project homepage](https://github.com/psyb0t/docker-pibox) <br>
- [pi-coding-agent](https://github.com/earendil-works/pi-mono/tree/main/packages/coding-agent) <br>
- [docker-aicodebox](https://github.com/psyb0t/docker-aicodebox) <br>
- [Model Context Protocol](https://modelcontextprotocol.io) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, JSON examples, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include HTTP API calls, MCP setup commands, Docker commands, environment variables, and safety guidance.] <br>

## Skill Version(s): <br>
0.15.8 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
