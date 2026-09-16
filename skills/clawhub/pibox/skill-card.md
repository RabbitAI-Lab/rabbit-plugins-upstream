## Description:

Install, configure, or run pi-coding-agent through the pibox wrapper, or connect to its HTTP, MCP, Telegram, or cron surfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use pibox to run pi-coding-agent locally, in one-shot automation, or through REST, OpenAI-compatible, MCP, Telegram, and cron interfaces. It is suited for agent-driven workspace tasks where containerized execution, wrapper-managed state, and configurable upstream LLM access are useful.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The wrapper and service modes can expose selected workspace files and agent execution capabilities.

Mitigation: Install and run only against workspaces where that access is acceptable, and keep service endpoints bound to localhost or behind an authenticated proxy.

Risk: REST and MCP modes can be unauthenticated when their bearer-token environment variables are unset.

Mitigation: Set strong, separate `PIBOX_API_MODE_TOKEN` and `PIBOX_MCP_MODE_TOKEN` values before exposing those surfaces.

Risk: File deletion and run cancellation actions are destructive and may affect shared or in-flight work.

Mitigation: Confirm the exact target before using delete or cancel operations, scope them to the current task, and treat them as administrative actions.

Risk: The curl-to-shell installer and floating Docker image tags can make installation harder to verify.

Mitigation: Download and inspect installers before execution and pin Docker images by digest for controlled deployments.

Risk: Broad network settings and chat or cron integrations may expose the agent to untrusted callers or sensitive workspaces.

Mitigation: Avoid `--network host` for normal deployments, restrict Telegram and cron use to trusted chats and non-sensitive workspaces, and use explicit port publishing where needed.

## Reference(s):

- [pibox setup](references/setup.md)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/pibox)
- [pi-coding-agent](https://github.com/earendil-works/pi-mono/tree/main/packages/coding-agent)
- [aicodebox container](https://github.com/psyb0t/docker-aicodebox)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline bash, JSON, and YAML examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include wrapper commands, Docker deployment examples, API calls, MCP setup guidance, and configuration snippets.]

## Skill Version(s):

0.18.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
