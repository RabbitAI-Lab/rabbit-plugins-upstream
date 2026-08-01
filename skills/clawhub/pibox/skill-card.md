## Description: <br>
pibox guides an agent through using pi-coding-agent inside an aicodebox Docker container across interactive shell, one-shot exec, REST, OpenAI-compatible, MCP, Telegram, and cron modes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use pibox to run or integrate pi-coding-agent over Docker, HTTP, OpenAI-compatible clients, MCP, Telegram, or cron. The skill helps select the right mode, configure credentials and workspace mounts, and understand endpoint behavior and safety constraints. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A reachable pibox API or MCP surface can run an agent and read, write, or delete files in the mounted workspace. <br>
Mitigation: Set separate API and MCP bearer tokens, bind services to localhost or put them behind authenticated access, and mount only the workspace needed for the task. <br>
Risk: Delete and cancel endpoints can remove files or terminate runs without undo. <br>
Mitigation: Treat delete and cancel actions as admin-only, confirm the exact target before use, and avoid broad or shared-workspace deletion workflows. <br>
Risk: Shared workspaces can let one caller disrupt another caller's files or in-flight runs. <br>
Mitigation: Use separate workspaces for separate users or tasks and avoid exposing a multi-user instance without explicit isolation and authentication. <br>


## Reference(s): <br>
- [pibox setup](references/setup.md) <br>
- [ClawHub pibox release](https://clawhub.ai/psyb0t/skills/pibox) <br>
- [pibox homepage](https://github.com/psyb0t/docker-pibox) <br>
- [pi-coding-agent](https://github.com/earendil-works/pi-mono/tree/main/packages/coding-agent) <br>
- [aicodebox](https://github.com/psyb0t/docker-aicodebox) <br>
- [Model Context Protocol](https://modelcontextprotocol.io) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown with Docker, curl, JSON, and YAML examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Covers REST, OpenAI-compatible, MCP, Telegram, cron, interactive shell, and one-shot execution modes.] <br>

## Skill Version(s): <br>
0.15.7 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
