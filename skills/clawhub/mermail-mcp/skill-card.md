## Description:

Configure, verify, and recover the hosted Mermail MCP connection in Codex, Claude, Cursor, OpenClaw, or another external MCP client.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to configure Mermail MCP in agent clients, choose OAuth or API-key authentication, verify tool discovery, and diagnose connection or scope failures without exposing credentials or testing with writes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys, OAuth tokens, authorization headers, wallet credentials, OTPs, or magic links could be exposed while configuring or troubleshooting the connection.

Mitigation: Prefer OAuth where supported, store API keys in a secret store or launch environment, reference MERMAIL_API_KEY instead of secret values, and redact credentials from diagnostics.

Risk: Connectivity testing could accidentally perform email delivery, data deletion, external-provider writes, or wallet actions.

Mitigation: Verify only with initialize, tools/list, and a bounded read-only workspace or mailbox list; route write and wallet operations to the relevant domain workflow.

Risk: A wrong workspace, profile, or authentication mode could broaden access or hide expected tool boundaries.

Mitigation: Keep each credential bound to the selected workspace, use the agent-inbox profile only for its limited workflow, and do not switch accounts, workspaces, keys, or profiles without the user's explicit choice.

## Reference(s):

- [Mermail AI Skills Documentation](https://docs.mermail.app/ai/skills)
- [Mermail Agents](https://mermail.app/agents)
- [Mermail MCP Platform Configuration](references/platforms.md)
- [Mermail MCP Connection Safety](references/security.md)
- [Mermail MCP Verification and Recovery](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Configuration, Shell commands, Code]

**Output Format:** [Markdown with JSON and shell snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Redacts secrets and separates connection status, verification evidence, failure class, and recovery action.]

## Skill Version(s):

1.2.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
