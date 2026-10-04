## Description:

Connects agents to personal Outlook mail, calendars, contacts, and tasks through Microsoft Graph tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mpalermiti](https://clawhub.ai/user/mpalermiti)

### License/Terms of Use:

MIT

## Use Case:

Agent builders and users of personal Outlook accounts use this connector to read, organize, and update mail, calendars, contacts, and tasks. Work or school accounts are not supported.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent can access private Outlook content or modify and send mailbox data.

Mitigation: Start with read_only enabled; when writes are needed, restrict them with allow_categories.

Risk: The local read_only setting does not limit the permissions on a Microsoft access token.

Mitigation: For credential-level read-only access, register a separate Azure app with read-only scopes.

Risk: Attachment tools can transfer files reachable in the configured attachment directory.

Mitigation: Keep attachments_dir narrowly scoped to files the agent may access.

Risk: Allowing an unencrypted token cache can leave reusable credentials in plaintext on the host.

Mitigation: Keep allow_unencrypted_token_cache disabled unless plaintext token storage is an accepted host risk.

## Reference(s):

- [ClawHub release](https://clawhub.ai/mpalermiti/skills/outlook-mcp)
- [PyPI package](https://pypi.org/project/outlook-graph-mcp/)
- [OpenClaw MCP documentation](https://docs.openclaw.ai/cli/mcp)

## Skill Output:

**Output Type(s):** [Text, JSON, Files]

**Output Format:** [Structured tool responses and text; downloaded attachments as files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Mail, calendar, contacts, and task results depend on the connected account and enabled tools.]

## Skill Version(s):

1.23.0 (source: ClawHub release metadata, pyproject.toml, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
