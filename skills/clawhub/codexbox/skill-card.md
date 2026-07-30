## Description: <br>
OpenAI Codex CLI running inside an aicodebox container, put on the network for shell, HTTP REST, OpenAI-compatible chat, MCP, Telegram, and cron access. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use codexbox to run Codex programmatically over HTTP, MCP, Telegram, cron, or an OpenAI-compatible endpoint instead of only through a local terminal. It also supports workspace file operations and scripted or scheduled agent runs when the service is configured with appropriate authentication. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Exposed API or MCP surfaces can allow remote prompt execution and workspace file access if mode tokens are unset or ports are reachable by untrusted callers. <br>
Mitigation: Set separate strong bearer tokens for each enabled API and MCP surface, bind services to localhost, or place them behind an authenticating proxy before exposing ports. <br>
Risk: Workspace file deletion and automation through cron or Telegram can remove data or perform high-impact operations without interactive review. <br>
Mitigation: Avoid shared workspaces for multiple callers, limit deletion to files created for the current task, and review scheduled or remote-control workflows before enabling them. <br>
Risk: The quick installer can execute a remote shell script directly. <br>
Mitigation: Download and inspect the installer before running it unless the source and delivery channel are already trusted. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/codexbox) <br>
- [codexbox homepage](https://github.com/psyb0t/docker-codexbox) <br>
- [OpenAI Codex CLI](https://github.com/openai/codex) <br>
- [aicodebox](https://github.com/psyb0t/docker-aicodebox) <br>
- [setup.md](references/setup.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline code blocks, shell commands, configuration examples, and API request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include HTTP, OpenAI-compatible chat, MCP, Telegram, cron, Docker, and workspace file-operation instructions.] <br>

## Skill Version(s): <br>
0.5.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
