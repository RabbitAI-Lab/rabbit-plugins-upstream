## Description:

This skill should be used when the user asks about Canvas LMS data — their own student account or any observed student. Triggers on phrases like "check Canvas", "what's my grade", "Canvas inbox", "what's due", "missing assignments", "Canvas LMS", "Instructure", "course announcements", "syllabus", or any request about courses, assignments, grades, conversations, announcements, planner items, or files in Canvas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, guardians, and other authorized Canvas observers use this skill to review linked students' courses, grades, assignments, submissions, calendar items, announcements, conversations, discussions, and course files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment is benign with medium confidence, but scan coverage is incomplete because a local path-like reference could not be resolved.

Mitigation: Review the unresolved reference and setup guidance before enabling the skill.

Risk: Canvas responses and downloaded course files can contain student grades, submissions, conversations, and other personal information.

Mitigation: Use an account authorized for the requested observer scope and share retrieved records or expiring file links only with intended recipients.

Risk: The documented authentication options can expose browser session access or stored credentials if configured or shared carelessly.

Mitigation: Use the institution-approved authentication method and keep session access, tokens, and passwords private.

## Reference(s):

- [canvas-parent-mcp package](https://www.npmjs.com/package/canvas-parent-mcp)
- [Project repository](https://github.com/chrischall/canvas-parent-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Files, Guidance]

**Output Format:** [Canvas records and natural-language summaries, with file links or downloaded files when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Canvas data returned for the user's account or an authorized observee.]

## Skill Version(s):

2.2.3 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
