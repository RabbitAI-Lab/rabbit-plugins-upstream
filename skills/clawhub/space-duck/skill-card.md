## Description:

Connect and manage an agent's identity on the Space Duck network, including pairing, status checks, trusted connections, pecks, listener setup, MCP access, workspace sync, and Telegram BYOB routing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[askegor](https://clawhub.ai/user/askegor)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use Space Duck to pair an agent with the Space Duck identity network, manage trusted duck-to-duck communication, inspect connection permissions, run local listeners, and configure optional Telegram, MCP, and workspace bridges.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can request high-impact local authority through listener and owner-approval workflows.

Mitigation: Enable strict consent for Telegram owner approvals, avoid read-only auto-execution, and run listeners under a dedicated low-privilege account.

Risk: Installer or update flows can execute local shell commands.

Mitigation: Review scripts before installing or updating and avoid the curl-to-bash installer path.

Risk: Workspace snapshot and bridge features may expose local project content.

Mitigation: Disable workspace snapshots when they are not needed, or scope the workspace directory to only files intended for sharing.

Risk: MCP server integrations may receive credentials or access to local capabilities.

Mitigation: Pin and sandbox MCP servers before giving them credentials, and grant only the minimum access needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/askegor/skills/space-duck)
- [Space Duck API Reference](references/api.md)
- [Capability Grants Guide](references/grants.md)
- [Connection Ceremony](references/CONNECTION-CEREMONY.md)
- [Space Duck MCP Client Spec](references/MCP-CLIENT-SPEC.md)
- [Security Manifest](SECURITY-MANIFEST.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON snippets, and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include commands that configure local credentials, listeners, MCP clients, Telegram routing, or Space Duck network actions.]

## Skill Version(s):

0.9.7 (source: server release metadata and artifact changelog, released 2026-09-15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
