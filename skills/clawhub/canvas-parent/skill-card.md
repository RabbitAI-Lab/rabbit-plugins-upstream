## Description:

This skill helps an agent work with Canvas LMS data for a user's student account or observed students, including courses, assignments, grades, inbox messages, announcements, planner items, and files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to let an authorized agent inspect Canvas LMS coursework, grades, messages, announcements, planner items, and course files for themselves or linked observees. It is most relevant for students, parents, and observers who want a conversational view of school records and upcoming work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose sensitive school records such as grades, messages, observee data, and course files.

Mitigation: Install only for authorized Canvas accounts and prefer scoped tokens or managed secret storage.

Risk: Authentication can involve browser session cookies or credentials.

Mitigation: Avoid pasting passwords into prompts, and disable browser-cookie fallback when session-cookie reuse is not desired.

Risk: Course files can be downloaded to local storage.

Mitigation: Choose download destinations deliberately and review downloaded files before opening or sharing them.

## Reference(s):

- [canvas-parent-mcp npm package](https://www.npmjs.com/package/canvas-parent-mcp)
- [canvas-parent-mcp source](https://github.com/chrischall/canvas-parent-mcp)
- [fetchproxy extension](https://github.com/chrischall/fetchproxy)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/canvas-parent)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance]

**Output Format:** [Markdown responses with setup snippets, Canvas LMS summaries, and downloaded files when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include sensitive Canvas records; file downloads are written to user-selected local paths.]

## Skill Version(s):

1.4.0 (source: evidence.release.version and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
