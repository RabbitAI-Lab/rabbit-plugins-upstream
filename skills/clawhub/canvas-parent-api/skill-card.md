## Description:

Guides agents in querying a user's or linked student's Canvas LMS courses, grades, assignments, messages, and files through authenticated API calls without an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, parents, and other authorized Canvas users can use this skill to retrieve course and student information from their institution's Canvas account in scripts or shell-based agent workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated queries can expose sensitive Canvas account and student information.

Mitigation: Use a scoped token and grant access only to agents authorized to handle the account data.

Risk: Evaluating QR-login helper output or running an unverified npx package can execute untrusted commands.

Mitigation: Review helper output instead of evaluating it and pin or verify the package before running it.

Risk: Refresh tokens can leak through shared shells or logs, and file downloads can overwrite unintended destinations.

Mitigation: Keep tokens out of shared shells and logs; restrict downloads to a known safe folder and refuse overwrites.

## Reference(s):

- [Canvas API endpoint examples](references/canvas-endpoints.md)
- [Canvas Parent API release on ClawHub](https://clawhub.ai/chrischall/skills/canvas-parent-api)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands return Canvas API JSON and may download course files when run.]

## Skill Version(s):

2.1.9 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
