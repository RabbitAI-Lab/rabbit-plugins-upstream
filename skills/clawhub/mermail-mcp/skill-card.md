## Description:

Configure, verify, and recover the hosted Mermail MCP connection for Codex, Claude, Cursor, OpenClaw, and other external MCP clients.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators use this skill to connect Mermail's hosted MCP server to supported agent clients, choose OAuth or API-key setup, verify tool discovery, and diagnose authentication, scope, credit, rate-limit, and transport failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A workspace API key or OAuth credential could be exposed through chat, logs, tracked configuration, shell history, or command arguments.

Mitigation: Reference MERMAIL_API_KEY through a secret store or launch environment, redact credential values in diagnostics, and revoke any exposed secret before replacing it.

Risk: The client may connect to the wrong workspace, authentication mode, or tool profile, causing missing tools or broader access than intended.

Mitigation: Verify the selected workspace and profile, prefer OAuth where supported, and use the agent-inbox profile only when its limited mailbox-provisioning and safe-read capability set is sufficient.

Risk: Connection checks could accidentally invoke email delivery, deletion, PayBox, wallet, Composio, or other provider-write behavior.

Mitigation: Limit verification to initialize, tools/list, and one bounded read-only list_workspaces or list_mailboxes smoke test.

Risk: After reconnecting or changing clients, replaying an uncertain prior write could duplicate or alter real Mermail state.

Mitigation: Restore the connection, inspect authoritative state once, and return control to the relevant domain workflow instead of retrying the write from this connection skill.

## Reference(s):

- [Mermail AI skills documentation](https://docs.mermail.app/ai/skills)
- [Mermail agents setup](https://mermail.app/agents)
- [Mermail MCP platform configuration](references/platforms.md)
- [Mermail MCP connection safety](references/security.md)
- [Mermail MCP verification and recovery](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration snippets and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Redacts credential values and keeps connection verification read-only unless the task is handed to a domain skill.]

## Skill Version(s):

1.2.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
