## Description:

Helps students and parent observers access Canvas LMS courses, grades, assignments, messages, and files through an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Students and parent observers use this skill to check Canvas courses, upcoming or missing work, grades, announcements, inbox messages, and course files for accounts they can access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to sensitive school records, including observed students' grades, submissions, messages, and files.

Mitigation: Grant access only to accounts you are authorized to view; review the data returned before sharing it.

Risk: Browser-session authentication grants access to a signed-in Canvas account.

Mitigation: Prefer OAuth or a scoped token if supported; review the extension and npm package source before using browser cookies.

## Reference(s):

- [Canvas Parent on ClawHub](https://clawhub.ai/chrischall/skills/canvas-parent)
- [canvas-parent-mcp npm package](https://www.npmjs.com/package/canvas-parent-mcp)
- [Canvas Parent MCP project linked in skill documentation](https://github.com/chrischall/canvas-parent-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Canvas records summarized in text or Markdown; optional course file downloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Selected records support compact or full views.]

## Skill Version(s):

2.1.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
