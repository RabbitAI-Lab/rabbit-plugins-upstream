## Description:

This skill helps agents work with OurFamilyWizard co-parenting data, including messages, calendar events, shared expenses, and journal entries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to access and manage OurFamilyWizard co-parenting records through the documented MCP tools. It supports message review and drafting, calendar management, shared expense tracking, journal entries, and attachment handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose sensitive OurFamilyWizard co-parenting records from broad activation phrases.

Mitigation: Avoid broad automatic activation and require clear user intent before accessing OFW account data.

Risk: Some actions can visibly change record state or create, send, upload, or delete OFW content.

Mitigation: Require explicit user confirmation before reading unread messages, calling visibility-affecting tools, uploading files, or creating, sending, or deleting OFW records.

Risk: OFW account credentials are required for use.

Mitigation: Store credentials only in protected credential storage and limit installation to users who intentionally want agent access to their OFW account.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chrischall/skills/ofw)
- [npm Package](https://www.npmjs.com/package/ofw-mcp)
- [Source Repository](https://github.com/chrischall/ofw-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or request MCP tool calls that read or change OurFamilyWizard records.]

## Skill Version(s):

2.12.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
