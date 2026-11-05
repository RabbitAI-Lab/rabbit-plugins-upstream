## Description:

This skill should be used when the user asks about Canvas LMS data — their own student account or any observed student. Triggers on phrases like "check Canvas", "what's my grade", "Canvas inbox", "what's due", "missing assignments", "Canvas LMS", "Instructure", "course announcements", "syllabus", or any request about courses, assignments, grades, conversations, announcements, planner items, or files in Canvas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and other Canvas observers use this skill to retrieve a linked student's courses, grades, assignments, planner items, announcements, conversations, and course files. It can also retrieve data from the user's own Canvas account and download course files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Canvas access can expose private student records and the active sign-in session.

Mitigation: Confirm the intended Canvas account and student before retrieval, and protect downloaded records.

Risk: The external server and browser extension executable behavior was not verified from this documentation-only package.

Mitigation: Review and pin the server and extension versions before use.

Risk: Password or OAuth authentication may involve session caching.

Mitigation: Review session caching before using password or OAuth authentication.

## Reference(s):

- [canvas-parent-mcp package on npm](https://www.npmjs.com/package/canvas-parent-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [Canvas LMS records and downloaded course files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Compact view removes avatar URLs; full view preserves the upstream payload. Planner items also support a brief view.]

## Skill Version(s):

2.2.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
