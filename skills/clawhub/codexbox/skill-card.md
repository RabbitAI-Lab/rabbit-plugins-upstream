## Description:

codexbox exposes OpenAI Codex CLI through containerized shell, HTTP API, OpenAI-compatible chat, MCP, Telegram, and cron workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation engineers use codexbox to run Codex programmatically over HTTP, MCP, Telegram, cron, or an OpenAI-compatible endpoint while managing files in a mounted workspace.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: HTTP API or MCP mode can expose Codex execution and workspace file access if reachable without a token.

Mitigation: Set CODEXBOX_API_MODE_TOKEN and CODEXBOX_MCP_MODE_TOKEN before exposing ports, and bind services to localhost or a trusted authenticated proxy.

Risk: Mounted workspace file tools can delete files without an undo path.

Mitigation: Mount only the workspace Codex should modify and confirm deletion targets before using file removal tools.

Risk: The quick installer pattern can execute a remote shell script directly.

Mitigation: Download and inspect the install script before running it unless the source and channel are already trusted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/codexbox)
- [codexbox setup](references/setup.md)
- [codexbox homepage](https://github.com/psyb0t/docker-codexbox)
- [OpenAI Codex CLI](https://github.com/openai/codex)
- [aicodebox](https://github.com/psyb0t/docker-aicodebox)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON, OpenAI-compatible chat responses, shell output, and workspace files depending on the enabled surface]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can stream chat output, return schema-constrained JSON, poll asynchronous run results, and read or write mounted workspace files.]

## Skill Version(s):

0.5.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
