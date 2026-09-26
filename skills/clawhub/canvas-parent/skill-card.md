## Description:

Helps agents answer questions about Canvas courses, assignments, grades, messages, and files for a student or linked observee.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Students and parents or guardians use this skill to ask an agent about Canvas coursework, grades, due dates, announcements, inbox messages, and course files within their account's access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser-session reuse and broad Canvas account access can expose grades, messages, files, and observed-student records to the agent.

Mitigation: Install only if you trust the npm package and fetchproxy extension; use the least-privileged authentication method your institution supports and review what student data the agent can access.

Risk: Downloading course files may place sensitive records on disk.

Mitigation: Set CANVAS_OUTPUT_DIR deliberately and review downloaded files and their destination.

## Reference(s):

- [Canvas Parent on ClawHub](https://clawhub.ai/chrischall/skills/canvas-parent)
- [canvas-parent-mcp npm package](https://www.npmjs.com/package/canvas-parent-mcp)
- [fetchproxy extension](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Natural-language answers based on Canvas records, with downloadable course files on request]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may contain sensitive student records.]

## Skill Version(s):

2.1.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
