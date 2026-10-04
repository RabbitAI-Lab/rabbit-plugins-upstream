## Description:

Helps agents work with OurFamilyWizard co-parenting messages, calendar events, expenses, and journal entries through the OFW MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People managing co-parenting records use this skill to help an agent review OFW messages, events, expenses, and journal entries, and prepare or perform updates with their approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OFW credentials and private co-parenting records could be exposed.

Mitigation: Store credentials in a protected, non-version-controlled location and verify the package source and version before installation.

Risk: Sending, deleting, uploading, or changing shared records can affect a sensitive legal and family record.

Mitigation: Show the proposed action and obtain explicit approval before co-parent-visible writes or deletion.

Risk: Reading an unread message or checking notifications can change visible read or last-seen status.

Mitigation: Warn the user before these reads and avoid them when the user wants unread or last-seen status preserved.

## Reference(s):

- [ofw-mcp npm package](https://www.npmjs.com/package/ofw-mcp)
- [Project repository linked in skill](https://github.com/chrischall/ofw-mcp)

## Skill Output:

**Output Type(s):** [Text, API calls, Shell commands, Configuration instructions]

**Output Format:** [Markdown with tool results, JSON examples, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include sensitive co-parenting records; verify live status before reporting current state.]

## Skill Version(s):

2.20.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
