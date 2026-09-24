## Description:

Query Canvas LMS from a shell with curl and a bearer access token for courses, grades, assignments, submissions, calendar items, planner items, announcements, conversations, discussions, and files for yourself or a linked observee.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and Canvas users use this skill to query Canvas LMS data directly from shell sessions without running the canvas-parent-mcp server. It is useful for scripted or ad hoc access to courses, grades, assignments, submissions, calendar, planner, announcements, conversations, discussions, and files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Canvas tokens, refresh tokens, client secrets, and downloaded files can expose sensitive education records if handled carelessly in shell history, logs, or shared paths.

Mitigation: Treat Canvas credentials as long-lived secrets, unset them after use, avoid logging Authorization headers, and validate file URLs and output destinations before downloading files.

Risk: The OAuth QR-login helper is invoked through an eval/npx pattern that can execute unpinned package output in the user's shell.

Mitigation: Verify and pin the helper package before use, or manually inspect the generated environment assignments instead of evaluating them directly.

## Reference(s):

- [Canvas API endpoints for curl](references/canvas-endpoints.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline bash code blocks and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes endpoint patterns, environment variable setup, pagination guidance, jq projections, and credential-handling cautions.]

## Skill Version(s):

2.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
