## Description:

codexbox helps agents and developers run OpenAI Codex in a Docker container through shell, HTTP, OpenAI-compatible, MCP, Telegram, and cron interfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation teams use codexbox to run Codex programmatically over HTTP, MCP, OpenAI-compatible APIs, Telegram, scheduled cron jobs, or containerized shell workflows. It is useful when Codex needs to be exposed as a service instead of used only from a local terminal.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Network-exposed API or MCP surfaces can run prompts and access workspace files if reachable without adequate authentication.

Mitigation: Set separate strong API and MCP bearer tokens, bind services to localhost or an authenticated proxy, and expose ports only when the deployment requires it.

Risk: Workspace file operations include write and delete capabilities, and deletion has no undo.

Mitigation: Use isolated workspaces and credentials, avoid shared workspaces for delete-capable surfaces, and confirm destructive actions before use.

Risk: The documented one-line installer can execute a remote shell script before local review.

Mitigation: Download and inspect the installer or source before running it, and prefer pinned Docker image digests after review.

## Reference(s):

- [codexbox setup](references/setup.md)
- [codexbox ClawHub release](https://clawhub.ai/psyb0t/skills/codexbox)
- [codexbox project homepage](https://github.com/psyb0t/docker-codexbox)
- [OpenAI Codex CLI](https://github.com/openai/codex)
- [aicodebox container base](https://github.com/psyb0t/docker-aicodebox)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with command examples, JSON API payloads, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include REST, OpenAI-compatible, MCP, Docker, Telegram, and cron setup examples.]

## Skill Version(s):

0.5.9 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
