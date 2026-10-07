## Description:

Helps users check their own or linked students' Canvas courses, grades, assignments, announcements, messages, and files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Students and parents or observers use this skill to review Canvas coursework, grades, due dates, school communications, and course files for accounts they are authorized to access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Canvas access can expose sensitive student grades, messages, and other educational records.

Mitigation: Access only authorized accounts, share only necessary details, and confirm ambiguous school-related requests before retrieving records.

Risk: Authentication may expose session cookies or credentials to untrusted software.

Mitigation: Install only if you trust the npm package and browser extension maintainers; prefer the least-sensitive authentication method and avoid username/password mode when possible.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/canvas-parent)
- [canvas-parent-mcp npm package](https://www.npmjs.com/package/canvas-parent-mcp)
- [ContextMint Bridge extension releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Markdown responses about Canvas records; downloaded course files when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Compact records by default; full records available on request.]

## Skill Version(s):

2.1.8 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
