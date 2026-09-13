## Description:

pibox helps agents and developers run pi-coding-agent in an aicodebox container through shell, REST/OpenAI-compatible HTTP, MCP, Telegram, and cron interfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use pibox to expose pi-coding-agent as local or network-accessible automation over HTTP, MCP, Telegram, cron, or one-shot Docker execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A network-reachable REST, OpenAI-compatible, or MCP surface can allow agent execution and workspace file access when API or MCP tokens are unset.

Mitigation: Set both PIBOX_API_MODE_TOKEN and PIBOX_MCP_MODE_TOKEN, bind services to localhost or an authenticated proxy, and avoid exposing unauthenticated instances to networks or untrusted agents.

Risk: Mutable external install scripts and container images may receive credentials and writable workspace access.

Mitigation: Use pinned image digests or verified releases, avoid curl | bash installation, and mount only the workspace the agent is intended to access.

Risk: Run cancellation and file deletion operations are destructive and may affect shared runs or workspace data.

Mitigation: Treat delete and cancel operations as explicit admin actions, confirm the exact target first, and avoid enumerate-then-bulk-delete workflows.

Risk: MCP tokens sent in query strings may be exposed through logs or URL history.

Mitigation: Prefer Authorization bearer headers for MCP authentication and avoid query-string tokens where the client supports headers.

## Reference(s):

- [pibox setup](references/setup.md)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/pibox)
- [docker-pibox repository](https://github.com/psyb0t/docker-pibox)
- [pi-coding-agent](https://github.com/earendil-works/pi-mono/tree/main/packages/coding-agent)
- [docker-aicodebox](https://github.com/psyb0t/docker-aicodebox)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON/YAML configuration snippets, API examples, and operational cautions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference required environment variables such as PIBOX_URL and credentials for API, MCP, Telegram, Docker, and upstream LLM providers.]

## Skill Version(s):

0.18.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
