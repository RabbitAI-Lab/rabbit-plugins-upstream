## Description:

Install, configure, or run pi-coding-agent through the pibox wrapper, or connect to its HTTP, MCP, Telegram, or cron surfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use Pibox to run pi-coding-agent in a chosen workspace, interactively or through one-shot commands, and optionally expose it through HTTP, OpenAI-compatible, MCP, Telegram, or scheduled-run interfaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The HTTP/API and MCP interfaces can provide powerful agent execution and workspace file access, and are unauthenticated when their respective tokens are unset.

Mitigation: Set distinct, nonempty API and MCP tokens before startup; keep local services on loopback with bridge networking or place them behind an authenticating proxy.

Risk: Server examples that weaken network isolation can expose powerful command and file operations.

Mitigation: Avoid host networking for ordinary deployments, publish ports only as needed, and limit mounted workspaces and credentials.

Risk: Installer and image choices, recurring jobs, and upstream model providers affect supply-chain and data-exposure risks.

Mitigation: Inspect a pinned installer, use a verified image digest, enable recurring jobs only when intended, and account for task content being sent to the configured LLM provider.

## Reference(s):

- [Setup guide](references/setup.md)
- [Pibox project homepage](https://github.com/psyb0t/docker-pibox)
- [pi-coding-agent project](https://github.com/earendil-works/pi-mono/tree/main/packages/coding-agent)
- [aicodebox project](https://github.com/psyb0t/docker-aicodebox)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.20.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
