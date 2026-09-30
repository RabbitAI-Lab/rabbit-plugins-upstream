## Description:

Guides users in querying Canvas LMS courses, grades, assignments, and other educational data for themselves or linked students using authenticated shell commands without an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, students, and linked observers use this skill to retrieve permitted Canvas course information and student progress through the institution's API without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running an unpinned QR-login helper through eval can execute unreviewed shell output.

Mitigation: Use a pinned or locally reviewed helper and avoid eval on untrusted output.

Risk: Shell commands and long-lived refresh tokens can expose Canvas credentials or educational data.

Mitigation: Review commands before execution, limit access to trusted environments, and keep refresh tokens out of long-lived shell sessions.

Risk: Downloaded Canvas files could overwrite existing local data.

Mitigation: Download only to trusted paths and check for existing files first.

## Reference(s):

- [Canvas API endpoint reference](references/canvas-endpoints.md)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/canvas-parent-api)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Authenticated Canvas API responses may include student records and grades.]

## Skill Version(s):

2.1.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
