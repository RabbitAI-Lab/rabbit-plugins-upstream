## Description: <br>
claudebox helps agents install, configure, launch, and script Claude Code inside a Docker-backed claudebox environment through CLI, HTTP API, OpenAI-compatible, MCP, Telegram, and cron interfaces. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to install and operate claudebox as a containerized Claude Code environment for scripting, CI automation, HTTP-backed agent workflows, MCP access, Telegram access, and scheduled jobs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API or MCP surfaces can be unauthenticated when bearer tokens are unset. <br>
Mitigation: Set per-mode bearer tokens before enabling API or MCP mode, and bind services to localhost or place them behind an authenticating proxy. <br>
Risk: The containerized agent can access mounted workspaces, credentials, and any mounted Docker socket. <br>
Mitigation: Mount only trusted workspaces and credentials, avoid mounting /var/run/docker.sock unless required, and isolate the container when handling untrusted input. <br>
Risk: Workspace file operations include deletion. <br>
Mitigation: Confirm target paths before destructive operations and limit deletion to files created for the current task. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/claudebox) <br>
- [Publisher profile](https://clawhub.ai/user/psyb0t) <br>
- [Project homepage](https://github.com/psyb0t/docker-claudebox) <br>
- [claudebox setup](references/setup.md) <br>
- [Model Context Protocol](https://modelcontextprotocol.io/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, configuration snippets, API examples, and optional JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include commands or configuration that launch network services, manipulate workspace files, or configure agent access.] <br>

## Skill Version(s): <br>
2.3.7 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
