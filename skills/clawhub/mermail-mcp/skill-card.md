## Description:

Helps connect, verify, and troubleshoot Mermail MCP in supported agent clients using OAuth or workspace-scoped API keys.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and workspace administrators use this skill to configure Mermail MCP in an agent client, verify a workspace connection with read-only checks, and diagnose authentication or tool-discovery problems.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workspace API keys or OAuth credentials could be exposed in chat, configuration, or logs.

Mitigation: Prefer OAuth; otherwise keep API keys in the launch environment or a secret store, reference the variable rather than its value, and redact diagnostics.

Risk: A custom connection-check URL could direct a credential to an unintended server.

Mitigation: Before running the bundled check, ensure MERMAIL_MCP_URL is unset or points to https://console.mermail.app/mcp.

Risk: A connection test or retry could affect mailbox data or cross the intended workspace boundary.

Mitigation: Confirm the workspace and profile; use read-only discovery and mailbox checks, and do not replay uncertain writes.

## Reference(s):

- [Mermail skills documentation](https://docs.mermail.app/ai/skills)
- [Connect Mermail MCP on ClawHub](https://clawhub.ai/mermail/skills/mermail-mcp)
- [Platform configuration](references/platforms.md)
- [Connection security](references/security.md)
- [Verification and troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Configuration instructions, Shell commands, Guidance]

**Output Format:** [Markdown with configuration and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Redacts credentials and distinguishes read-only verification from write operations.]

## Skill Version(s):

1.2.14 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
