## Description: <br>
codexbox runs the OpenAI Codex CLI inside an aicodebox container and exposes it through shell, exec, HTTP API, OpenAI-compatible chat, MCP, Telegram, and cron interfaces. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use codexbox to run Codex programmatically over HTTP, MCP, Telegram, cron, or an OpenAI-compatible endpoint, and to manage workspace files without an interactive terminal. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Network-exposed API or MCP surfaces can provide run execution and workspace file access if tokens are unset or weak. <br>
Mitigation: Set strong, separate API and MCP bearer tokens before binding ports, and keep services on localhost or behind an authenticated proxy. <br>
Risk: Workspace file deletion and writes may affect shared or sensitive directories. <br>
Mitigation: Mount only the directories needed for the task, avoid sensitive host paths, and confirm destructive file operations before use. <br>
Risk: The quick installer can execute a remote shell script. <br>
Mitigation: Download and inspect the installer before running it, or install from a trusted local checkout. <br>


## Reference(s): <br>
- [ClawHub codexbox listing](https://clawhub.ai/psyb0t/skills/codexbox) <br>
- [codexbox homepage](https://github.com/psyb0t/docker-codexbox) <br>
- [codexbox setup](references/setup.md) <br>
- [OpenAI Codex CLI](https://github.com/openai/codex) <br>
- [aicodebox container base](https://github.com/psyb0t/docker-aicodebox) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Markdown] <br>
**Output Format:** [Markdown with inline bash, JSON, YAML, and Python examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct an agent to call networked Codex, file-management, MCP, Telegram, or cron surfaces when configured.] <br>

## Skill Version(s): <br>
0.5.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
