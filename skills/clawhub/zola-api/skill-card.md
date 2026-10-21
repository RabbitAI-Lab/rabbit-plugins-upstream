## Description:

Provides shell commands to read and update Zola wedding-planning data directly through its mobile API without an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Zola account holders use this skill to query or update wedding vendors, budgets, guests, events, registry items, and website content from a shell without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A long-lived Zola refresh token grants direct authenticated access to account data.

Mitigation: Treat the token like a password; do not paste it into logged terminals or shared sessions.

Risk: Write and delete commands can change or erase wedding records, and partial updates can overwrite unrelated fields.

Mitigation: Require explicit review before mutations; fetch the current record and preserve unchanged fields when updating.

Risk: Raw API error responses may expose session credentials or account details.

Mitigation: Review and redact sensitive values before sharing errors or command output.

## Reference(s):

- [Zola mobile API endpoint recipes](references/mobile-api-endpoints.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with curl and jq commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Authenticated API responses may contain private wedding and account data.]

## Skill Version(s):

2.1.11 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
