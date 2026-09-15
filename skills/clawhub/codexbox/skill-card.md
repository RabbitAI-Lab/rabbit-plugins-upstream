## Description:

Install, configure, or run Codex through the codexbox wrapper, or connect to its HTTP, MCP, Telegram, or cron surfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to install and run Codex in a containerized codexbox environment, including local wrapper execution and optional HTTP, MCP, Telegram, and cron interfaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: HTTP API or MCP modes can expose agent execution and workspace file access when bearer tokens are unset.

Mitigation: Set distinct API and MCP bearer tokens before enabling those modes, and bind services to localhost or place them behind a protected proxy.

Risk: The installer can execute a remotely fetched script.

Mitigation: Download, inspect, and pin or otherwise verify the installer and Docker image before running them.

Risk: Mounted credentials, SSH keys, Docker access, or extra host directories can broaden the impact of a compromised or misused containerized agent.

Mitigation: Mount only the credentials and host paths needed for the task, and avoid SSH, Codex auth, Docker, or extra host mounts unless required.

Risk: File-management surfaces include destructive delete behavior with no undo.

Mitigation: Delete only files the current task created or files the user explicitly asked to remove, and confirm target paths before deletion.

## Reference(s):

- [codexbox setup](references/setup.md)
- [codexbox ClawHub page](https://clawhub.ai/psyb0t/skills/codexbox)
- [codexbox project homepage](https://github.com/psyb0t/docker-codexbox)
- [OpenAI Codex CLI](https://github.com/openai/codex)
- [aicodebox container](https://github.com/psyb0t/docker-aicodebox)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell, JSON, YAML, and code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include wrapper commands, Docker commands, HTTP API payloads, MCP setup, and workspace file-management guidance.]

## Skill Version(s):

0.6.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
