## Description:

Operate Postqued through its remote MCP server or v2 REST API for social content uploads, multi-platform publishing and scheduling, calendar status, analytics, engagement, approval workflows, revisions, caption suggestions, client reviews, collaborators, connected accounts, workspaces, and billing capability checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[syeddhasnainn](https://clawhub.ai/user/syeddhasnainn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent operate Postqued workspaces through MCP or the v2 REST API for publishing, scheduling, approvals, analytics, engagement, collaboration, and client review workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform externally visible publishing, scheduling, moderation, collaborator, approval, disconnect, and delete actions in Postqued.

Mitigation: Use dry-run validation where available and require confirmation of the workspace, connected accounts, captions, destinations, times, and exact action before live changes.

Risk: A Postqued organization API key, presigned upload URL, access token, or private response field could be exposed in user-facing output or logs.

Mitigation: Store the API key in POSTQUED_API_KEY, never place it in query parameters or storage uploads, and redact credentials, presigned URLs, and private fields from summaries.

Risk: Actions could be applied to the wrong organization or client workspace if scope is ambiguous.

Mitigation: Resolve scope with list_workspaces or GET /v2/mcp/context first, pass explicit workspaceId values, include the exact organizationId when creating workspaces, and ask the user when a workspace is ambiguous.

Risk: Retries or stale approval mutations could duplicate live requests or overwrite newer review work.

Mitigation: Use a fresh UUID idempotency key per distinct live publish, poll durable status before retrying after timeouts, and reread approval posts before mutations that require current revision and version values.

## Reference(s):

- [Postqued OpenClaw setup](https://postqued.com/openclaw)
- [Postqued MCP server](https://mcp.postqued.com/mcp)
- [Postqued v2 OpenAPI](https://api.postqued.com/v2/docs/openapi.json)
- [Postqued MCP tool catalog](references/mcp-tools.md)
- [Postqued publishing targets](references/platforms.md)
- [Postqued v2 REST API reference](references/api.md)
- [ClawHub skill page](https://clawhub.ai/syeddhasnainn/skills/postqued-api)
- [Publisher profile](https://clawhub.ai/user/syeddhasnainn)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON, and inline code or shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include proposed MCP tool calls, REST request examples, workspace-scoped summaries, and confirmation prompts for high-impact actions.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
