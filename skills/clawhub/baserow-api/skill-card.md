## Description:

Helps agents read and manage Baserow database rows, fields, and tables through an authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to query and manage Baserow data, with optional approved functions and triggers for automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Database writes or new connections can change data or grant access unexpectedly.

Mitigation: Default to read-only requests and confirm the specific connection, target, and effect before any write or authorization.

Risk: Triggers and destinations can keep forwarding future event data after setup.

Mitigation: Review each trigger and destination and obtain separate approval for its event scope and recipient; remove it when no longer needed.

Risk: Exposed API keys or responses can disclose account access or business data.

Mitigation: Prefer device login and credential storage; never embed credentials in destinations or log unneeded response data.

## Reference(s):

- [Baserow API documentation](https://baserow.io/api-docs)
- [Baserow database API](https://baserow.io/user-docs/database-api)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Maton homepage](https://maton.ai)
- [Baserow skill release](https://clawhub.ai/byungkyu/skills/baserow-api)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with command, code, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Operations are limited to the connected account's authorization; writes and automation require user approval.]

## Skill Version(s):

1.2.9 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
