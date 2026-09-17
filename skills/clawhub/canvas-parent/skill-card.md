## Description:

Helps agents access Canvas LMS data for a user's own student account or observed students, including courses, grades, assignments, announcements, conversations, planner items, and files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users, parents or observers, students, and developers use this skill to connect an agent to Canvas LMS and retrieve course status, grades, assignments, messages, announcements, planner items, and course files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release evidence flags use of unpinned external code.

Mitigation: Use a pinned, reviewed package version or commit before installation.

Risk: The release evidence flags reuse of sensitive Canvas session or account credentials.

Mitigation: Prefer the narrowest institution-approved OAuth or token flow, avoid storing secrets in project-level config files, and avoid browser-cookie or password reuse when possible.

Risk: Canvas file download workflows can place files on local disk.

Mitigation: Allow downloads only to trusted paths.

## Reference(s):

- [canvas-parent-mcp npm package](https://www.npmjs.com/package/canvas-parent-mcp)
- [canvas-parent-mcp source repository](https://github.com/chrischall/canvas-parent-mcp)
- [fetchproxy extension](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide Canvas MCP tool calls that return Canvas LMS payloads; compact view strips avatar URL fields by default.]

## Skill Version(s):

1.5.6 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
