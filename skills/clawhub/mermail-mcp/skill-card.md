## Description:

Configure, verify, and recover the hosted Mermail MCP connection in Codex, Claude, Cursor, OpenClaw, or another external MCP client.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and workspace administrators use this skill to connect MCP clients to Mermail, select OAuth or API-key authentication, verify the selected tool profile, and diagnose connection, scope, credits, rate-limit, stale-registry, or argument errors before routing healthy business work to domain skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled API-key checker can send MERMAIL_API_KEY to the endpoint named by MERMAIL_MCP_URL.

Mitigation: Before running the checker, leave MERMAIL_MCP_URL unset or confirm it points only to the intended trusted Mermail endpoint.

Risk: API keys, OAuth tokens, cookies, PayBox credentials, OTPs, and signing keys may be exposed through chat, logs, shell history, command arguments, or tracked configuration.

Mitigation: Use OAuth where supported or store MERMAIL_API_KEY in a secret store, redact all credential values, and reference only environment variable names in examples and diagnostics.

Risk: Connectivity tests could accidentally perform writes such as sending mail, changing configuration, invoking provider actions, or using wallet functionality.

Mitigation: Verify with initialize, tools/list, and a bounded read-only workspace or mailbox list; route destructive or business operations to the appropriate domain skill after the connection is healthy.

Risk: A workspace mismatch, stale catalog, or missing tool profile could lead to silent identity or permission changes.

Mitigation: Keep credentials bound to the intended workspace, report exact failure classes, inspect the live tool schema, and ask the user before changing accounts, workspaces, keys, or profiles.

## Reference(s):

- [Mermail AI skills documentation](https://docs.mermail.app/ai/skills)
- [Mermail agents](https://mermail.app/agents)
- [Mermail MCP platform configuration](references/platforms.md)
- [Mermail MCP connection safety](references/security.md)
- [Mermail MCP verification and recovery](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with JSON, YAML, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Credential values should be fully redacted and represented only by environment-variable references such as MERMAIL_API_KEY.]

## Skill Version(s):

1.2.13 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
