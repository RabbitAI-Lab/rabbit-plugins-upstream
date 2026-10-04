## Description:

Helps agents retrieve Canvas LMS courses, grades, assignments, messages, and files for a student or linked observer account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Students and parents or guardians with observer access use this skill to ask an agent about Canvas coursework, grades, deadlines, announcements, inbox messages, and course files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to private student records, grades, inbox messages, and course files may expose sensitive school information.

Mitigation: Use only with authorized accounts and limit who can access the agent's responses and downloads.

Risk: The optional browser bridge can reuse Canvas session cookies for authentication.

Mitigation: Verify the browser extension source, prefer token or OAuth setup when feasible, and disable the cookie bridge if session reuse is not desired.

Risk: Installing the package and downloading course files introduces local software and file-handling exposure.

Mitigation: Verify the npm package and save downloads to a dedicated output directory.

## Reference(s):

- [Canvas Parent skill release](https://clawhub.ai/chrischall/skills/canvas-parent)
- [Canvas Parent MCP package](https://www.npmjs.com/package/canvas-parent-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, JSON, Files]

**Output Format:** [Text summaries and structured Canvas responses; downloaded course files when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [File downloads are confined to the configured output directory.]

## Skill Version(s):

2.1.6 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
