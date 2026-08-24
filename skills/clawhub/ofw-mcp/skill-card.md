## Description:

Connects an agent to the OurFamilyWizard MCP server to read and manage co-parenting messages, calendar events, shared expenses, journal entries, and attachments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to OurFamilyWizard records for co-parenting workflows such as checking messages, reviewing calendars, managing shared expenses, drafting or sending messages, and creating journal entries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill grants broad ongoing authenticated access to sensitive co-parenting records.

Mitigation: Install only when that access is intended, use a tightly scoped MCP configuration, and protect OFW credentials.

Risk: State-changing actions such as sending messages, deleting drafts, creating events, or logging expenses can affect legal co-parenting records.

Mitigation: Require explicit user confirmation before every write, send, delete, upload, or other state-changing operation.

Risk: Some reads can update visible status, such as marking messages read or updating last-seen information.

Mitigation: Warn the user before reads that can change visibility, avoid silent background calls, and use refusal options such as allowMarkRead:false when the user wants to preserve unread status.

Risk: Cached message or draft data can be stale or incomplete.

Mitigation: Check freshness, completeness, paging fields, and live status before reporting current OFW state or final counts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/ofw-mcp)
- [ofw-mcp npm package](https://www.npmjs.com/package/ofw-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls]

**Output Format:** [Markdown with JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call MCP tools that read or modify OFW records; results can include cached or live OFW data and downloaded files.]

## Skill Version(s):

2.11.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
