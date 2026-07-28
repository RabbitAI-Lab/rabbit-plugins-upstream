## Description: <br>
codexbox runs the OpenAI Codex CLI inside an aicodebox Docker container and exposes it through shell, exec, HTTP API, OpenAI-compatible chat, MCP, Telegram, and cron interfaces. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation engineers use codexbox to run Codex programmatically over HTTP, MCP, Telegram, cron, or an OpenAI-compatible chat endpoint instead of only through a local terminal. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Exposed API or MCP surfaces can allow remote Codex runs and workspace file access if bearer tokens are unset. <br>
Mitigation: Set CODEXBOX_API_MODE_TOKEN and CODEXBOX_MCP_MODE_TOKEN for enabled modes, bind to localhost when possible, or place the service behind an authenticating proxy. <br>
Risk: Mounted workspaces or host directories may expose sensitive files to the running service. <br>
Mitigation: Mount only directories the service needs and avoid sensitive paths unless callers should be able to read or modify them. <br>
Risk: The installer can execute remote shell code if run directly from a pipe. <br>
Mitigation: Download the installer, inspect it, and then run it only after trusting the source and channel. <br>
Risk: Workspace file deletion through file tools has no undo. <br>
Mitigation: Confirm target paths before deletion and delete only files created for the current task or explicitly requested by the user. <br>


## Reference(s): <br>
- [codexbox setup](references/setup.md) <br>
- [codexbox GitHub repository](https://github.com/psyb0t/docker-codexbox) <br>
- [OpenAI Codex CLI](https://github.com/openai/codex) <br>
- [aicodebox GitHub repository](https://github.com/psyb0t/docker-aicodebox) <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/codexbox) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON/API examples, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Docker and curl; may include executable commands and service configuration examples.] <br>

## Skill Version(s): <br>
0.4.9 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
