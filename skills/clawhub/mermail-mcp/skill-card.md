## Description:

Configure, verify, and recover the hosted Mermail MCP connection in Codex, Claude, Cursor, OpenClaw, or another external MCP client.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to configure, verify, and troubleshoot authenticated Mermail MCP connections across supported agent clients. It helps choose OAuth or API-key authentication, select the correct profile, validate discovery, and recover safely from common connection failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential or token exposure while configuring Mermail MCP access.

Mitigation: Keep API keys and OAuth credentials in a secret store or process environment, reference MERMAIL_API_KEY in examples, and redact credential values from diagnostics.

Risk: Using a connection-check workflow to perform email sends, deletes, provider writes, or wallet transactions.

Mitigation: Verify with initialize, tools/list, and a bounded read-only workspace or mailbox smoke test, then route operational work to the relevant domain skill.

Risk: Wrong workspace, authentication mode, or profile can expose missing tools or insufficient-scope failures.

Mitigation: Verify the selected workspace and profile, prefer OAuth where supported, and use the agent-inbox profile only when its limited capability set is sufficient.

Risk: Reconnects or stale client discovery can lead to unsafe retries or guessed tool identifiers.

Mitigation: Use the smallest safe reconnect or reload action, inspect the live catalog and schema, preserve host-exposed tool identifiers, and do not replay uncertain writes.

## Reference(s):

- [Mermail AI Skills documentation](https://docs.mermail.app/ai/skills)
- [Mermail agents setup](https://mermail.app/agents)
- [Mermail MCP endpoint](https://console.mermail.app/mcp)
- [Mermail MCP platform configuration](references/platforms.md)
- [Mermail MCP connection safety](references/security.md)
- [Mermail MCP verification and recovery](references/troubleshooting.md)
- [API-key connection checker](scripts/check-connection.mjs)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with configuration snippets and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Credential values are redacted; API keys are referenced by environment variable only.]

## Skill Version(s):

1.2.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
