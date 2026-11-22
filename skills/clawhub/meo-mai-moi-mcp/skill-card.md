## Description:

Use when the user asks to connect to, authorize, or do anything with Meo Mai Moi through its remote OAuth MCP gateway: a pet, care, placement, finance, or account task run over MCP, or choosing and upgrading the scopes one needs. Not for direct REST calls with a personal Meo API token, which the separate meo-mai-moi skill covers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[troioi-vn](https://clawhub.ai/user/troioi-vn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to connect to Meo Mai Moi through OAuth-enabled MCP clients, choose scopes suited to a task, and carry out pet or account operations safely. It guides connection checks, privacy handling, and verification of consequential changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad OAuth scopes can permit sensitive reads and writes across pet records, placement, messages, finances, and account data.

Mitigation: Request only scopes needed for the task; offer Full management only after an explicit choice and a clear sensitivity warning.

Risk: Authorization details or personal records could be exposed in chat or logs.

Mitigation: Never request or share access tokens, refresh tokens, client secrets, or personal API tokens; keep personal records out of chat unless needed for a decision.

Risk: Consequential writes may affect another person, health history, finances, access, or a real-world handover.

Mitigation: Read and verify the exact resource and its current version before acting, then confirm the resulting state with a follow-up read.

## Reference(s):

- [Connection and scope selection](artifact/references/connection.md)
- [OpenClaw native MCP onboarding](artifact/references/openclaw.md)
- [Safety and error handling](artifact/references/safety.md)
- [Client setup documentation](https://github.com/troioi-vn/meo-mcp/blob/main/docs/clients.md)
- [MCP tools documentation](https://github.com/troioi-vn/meo-mcp/blob/main/docs/tools.md)
- [OAuth documentation](https://github.com/troioi-vn/meo-mcp/blob/main/docs/oauth.md)
- [Error reference](https://github.com/troioi-vn/meo-mcp/blob/main/docs/errors.md)

## Skill Output:

**Output Type(s):** [Guidance, Configuration instructions, API calls, Text]

**Output Format:** [Markdown guidance, native MCP configuration instructions, and concise summaries of tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live operations require an authorized MCP connection and scopes covering the requested task.]

## Skill Version(s):

0.4.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
