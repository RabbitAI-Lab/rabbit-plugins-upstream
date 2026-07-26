## Description: <br>
codexbox runs OpenAI Codex CLI inside an aicodebox container and exposes shell, REST, OpenAI-compatible, MCP, Telegram, and cron interfaces for programmatic Codex use. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation engineers use codexbox to run Codex through scripts, CI jobs, OpenAI-compatible clients, MCP-aware agents, Telegram, or scheduled cron jobs instead of only through a local terminal. It is useful when a workflow needs prompt execution, workspace file operations, or schema-constrained Codex responses over networked interfaces. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Networked REST and MCP surfaces can provide run execution and full workspace file access when their bearer tokens are unset. <br>
Mitigation: Set CODEXBOX_API_MODE_TOKEN and CODEXBOX_MCP_MODE_TOKEN before exposing ports, bind to loopback where possible, or place the service behind an authenticating proxy. <br>
Risk: Workspace file deletion and prompt-running tools can remove or alter user data. <br>
Mitigation: Review requested file operations, delete only task-owned files, avoid unauthenticated shared workspaces, and keep mounted workspaces scoped to the intended task. <br>
Risk: The installer can execute remote shell code when piped directly into bash. <br>
Mitigation: Download the installer, inspect it, and then run it only after trusting the source and channel. <br>
Risk: Mounted Codex auth, session, and configuration directories can contain sensitive credentials or account state. <br>
Mitigation: Treat mounted Codex directories as sensitive, restrict host and container access, and avoid sharing them across untrusted users or workloads. <br>


## Reference(s): <br>
- [ClawHub codexbox page](https://clawhub.ai/psyb0t/skills/codexbox) <br>
- [codexbox setup](references/setup.md) <br>
- [OpenAI Codex CLI](https://github.com/openai/codex) <br>
- [aicodebox](https://github.com/psyb0t/docker-aicodebox) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Docker, curl, Python, YAML, and shell examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Describes bearer-token setup, workspace file operations, OpenAI-compatible requests, MCP tool access, Telegram operation, cron jobs, and destructive-operation cautions.] <br>

## Skill Version(s): <br>
0.4.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
