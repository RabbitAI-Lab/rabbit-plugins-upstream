## Description:

This skill helps agents access Canvas LMS data for a user or observed student, including courses, grades, assignments, announcements, planner items, conversations, and course files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and caregivers use this skill to check Canvas LMS course, grade, assignment, communication, planner, and file information for their own account or an observed student account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Canvas credentials, live browser session cookies, and sensitive student or observer account data.

Mitigation: Install only when that access is acceptable, use the least-privilege authentication method available, and keep tokens, passwords, and cookies out of shared configs and logs.

Risk: The skill can download Canvas course files to user-chosen disk paths.

Mitigation: Review destination paths before allowing file writes and restrict downloads to expected workspace locations.

Risk: Fetchproxy-based authentication may not fit every user's session handling or caching risk model.

Mitigation: Disable fetchproxy or session caching when that behavior is not appropriate for the deployment.

## Reference(s):

- [canvas-parent ClawHub skill page](https://clawhub.ai/chrischall/skills/canvas-parent)
- [canvas-parent-mcp npm package](https://www.npmjs.com/package/canvas-parent-mcp)
- [fetchproxy extension](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with JSON configuration snippets and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May summarize sensitive Canvas account or observed-student data and may include local file paths for downloaded course files.]

## Skill Version(s):

1.5.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
