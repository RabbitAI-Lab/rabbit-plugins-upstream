## Description:

Install, configure, or run pi-coding-agent through the pibox wrapper, or connect to its HTTP, MCP, Telegram, or cron surfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use pibox to run pi-coding-agent in a container, expose it through REST, OpenAI-compatible, MCP, Telegram, or cron interfaces, and connect it to configured upstream LLM endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installation is shown through a curl-to-shell command, which can execute unverified code.

Mitigation: Prefer downloading the installer first, inspecting it, and verifying its source before execution.

Risk: API and MCP modes can expose agent execution and workspace file access without authentication when their tokens are unset.

Mitigation: Set strong, separate API and MCP bearer tokens, bind services to localhost or place them behind an authenticating proxy, and avoid exposing unauthenticated surfaces to a network.

Risk: Host networking and broad workspace mounts can expand the impact of a compromised or misconfigured service.

Mitigation: Avoid host networking for non-local deployments, publish only required ports, and mount only a dedicated non-sensitive workspace.

Risk: Cron and Telegram modes can provide persistent scheduled or chat-driven agent access.

Mitigation: Enable those modes only when persistence is intended, use allowlists for Telegram access, and review scheduled jobs before deployment.

Risk: Delete and cancel operations can remove files or interrupt runs without undo.

Mitigation: Require explicit user confirmation for destructive operations and scope each action to the current task and target.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/pibox)
- [pibox setup](references/setup.md)
- [pibox homepage](https://github.com/psyb0t/docker-pibox)
- [pi-coding-agent](https://github.com/earendil-works/pi-mono/tree/main/packages/coding-agent)
- [aicodebox](https://github.com/psyb0t/docker-aicodebox)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, shell commands, JSON API responses, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can emit agent run results, file-operation guidance, API examples, MCP tool usage, Telegram configuration, and cron configuration.]

## Skill Version(s):

0.18.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
