## Description:

Helps agents answer questions about a user's Canvas courses, grades, assignments, announcements, conversations, and linked students, and retrieve course files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Students, parents or observers use this skill to review their own or linked students' Canvas coursework, grades, schedules, and messages, and download course files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to sensitive academic records, inbox messages, and observed student information.

Mitigation: Grant access deliberately and use the narrowest authentication method you trust.

Risk: Session authentication and third-party extension or package access.

Mitigation: Verify the npm package and browser extension source before installation.

Risk: Course files may be saved to local disk.

Mitigation: Confirm the destination before downloading course files.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/canvas-parent)
- [canvas-parent-mcp npm package](https://www.npmjs.com/package/canvas-parent-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [Canvas records and downloaded course files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Compact responses omit avatar URLs by default; full responses retain them.]

## Skill Version(s):

2.1.10 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
