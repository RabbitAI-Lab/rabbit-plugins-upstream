## Description:

This skill helps users inspect a SchoolPass parent account for student arrival and dismissal details, authorized drivers, pickup changes, dismissal locations, and school information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and their agents use this skill to review SchoolPass arrival and dismissal records, linked students, authorized drivers, pickup changes, and school dismissal locations. It can also prepare and, after explicit confirmation, submit or cancel dismissal changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change a child's real dismissal arrangements even though the release security summary notes that its description is mostly read-oriented.

Mitigation: Show the dismissal-change preview to the user and require explicit confirmation before submitting or canceling any dismissal change.

Risk: The skill requires SchoolPass parent credentials and access to parent-scoped student, driver, calendar, and dismissal data.

Mitigation: Install only where the user accepts sharing SchoolPass credentials with the MCP server, and never echo passwords or session tokens in conversation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/schoolpass)
- [schoolpass-mcp npm package](https://www.npmjs.com/package/schoolpass-mcp)
- [schoolpass-mcp source link from skill documentation](https://github.com/chrischall/schoolpass-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON configuration snippets and tool-use guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read tools default to compact responses that omit student and driver photo URLs when supported; write tools return previews or receipts after confirmation.]

## Skill Version(s):

0.4.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
