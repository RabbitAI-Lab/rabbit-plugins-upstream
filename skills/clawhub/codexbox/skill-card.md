## Description:

codexbox exposes OpenAI Codex CLI through containerized shell, exec, HTTP REST, OpenAI-compatible chat, MCP, Telegram, and cron interfaces for programmatic agent runs and workspace file operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to run Codex from scripts, services, MCP-aware clients, Telegram, or scheduled jobs instead of only through a local terminal. It is useful when a team needs containerized Codex access over network interfaces with workspace file management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Network API or MCP surfaces can expose prompt execution and workspace file access if reached by untrusted callers.

Mitigation: Set the API and MCP bearer tokens, bind services to localhost or an authenticating proxy, and expose only intended ports.

Risk: Workspace file operations can remove or alter files in the mounted workspace.

Mitigation: Mount only the workspace intended for the task and avoid shared workspaces unless all callers are trusted.

Risk: The installer path can execute a remote script.

Mitigation: Download and inspect the installer before running it unless the source and delivery channel are already trusted.

Risk: Cron and Telegram modes can run unattended with access to the mounted workspace.

Mitigation: Configure access controls, review scheduled instructions, and treat unattended modes as privileged automation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/codexbox)
- [codexbox setup](references/setup.md)
- [codexbox project homepage](https://github.com/psyb0t/docker-codexbox)
- [OpenAI Codex CLI](https://github.com/openai/codex)
- [aicodebox](https://github.com/psyb0t/docker-aicodebox)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or structured text with command, configuration, and API examples when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can also return JSON or files when callers use the documented API, OpenAI-compatible, or MCP surfaces.]

## Skill Version(s):

0.5.5 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
