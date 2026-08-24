## Description:

Configure, verify, and recover authenticated Mermail MCP connections across Codex, Claude, Cursor, OpenClaw, and other external MCP clients.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to set up, verify, and recover Mermail MCP connections, choose OAuth or API-key authentication, select the correct profile, and diagnose status, scope, rate-limit, and tool-discovery failures without exposing credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential exposure during MCP setup or diagnostics.

Mitigation: Prefer OAuth where available, keep MERMAIL_API_KEY in a secret store or launch environment, and redact keys, tokens, cookies, and sensitive headers from chat, logs, and configuration examples.

Risk: Connection verification could be mistaken for permission to perform writes or wallet/PayBox actions.

Mitigation: Verify with initialize, tools/list, and a read-only workspace or mailbox smoke test; route send, delete, external-provider, and wallet work to the appropriate domain workflow.

Risk: Wrong authentication mode or profile can hide expected tools or cross intended workspace boundaries.

Mitigation: Confirm endpoint, workspace, OAuth or API-key mode, and profile before recovery; do not switch identities, rotate keys, broaden profiles, or retry writes without explicit user direction.

## Reference(s):

- [Mermail MCP platform configuration](references/platforms.md)
- [Mermail MCP connection safety](references/security.md)
- [Mermail MCP verification and recovery](references/troubleshooting.md)
- [Mermail AI skills documentation](https://docs.mermail.app/ai/skills)
- [Mermail agents setup](https://mermail.app/agents)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON, YAML, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Redacts credential values and uses environment-variable references such as MERMAIL_API_KEY in configuration examples.]

## Skill Version(s):

1.2.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
