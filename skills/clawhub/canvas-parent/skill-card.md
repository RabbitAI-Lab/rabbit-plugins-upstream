## Description:

Helps users review Canvas LMS courses, assignments, grades, announcements, messages, and files for their own account or linked students.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Students and parents or guardians with observer access use this skill to check coursework, grades, upcoming deadlines, announcements, and Canvas messages, and to download course files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser session reuse can expose sensitive Canvas grades, messages, and linked student records.

Mitigation: Prefer scoped OAuth or a limited token where available; verify the package and browser extension before use and request confirmation before accessing sensitive records.

Risk: Course file downloads can place student or class materials on the local device.

Mitigation: Confirm downloads explicitly and store files only in an appropriate, access-controlled directory.

## Reference(s):

- [Canvas Parent on ClawHub](https://clawhub.ai/chrischall/skills/canvas-parent)
- [Canvas Parent MCP package](https://www.npmjs.com/package/canvas-parent-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Text or Markdown responses; downloaded course files when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses can contain sensitive student information; file downloads are written to a configured local directory.]

## Skill Version(s):

2.1.5 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
