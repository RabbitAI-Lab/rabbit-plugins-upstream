## Description:

Guides agents in querying Canvas LMS for their own or a linked student's courses, grades, assignments, messages, calendar, and files using authenticated shell requests without an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, students, and developers use this skill to retrieve authorized Canvas course and student information from a shell or script when the MCP server is unavailable or unnecessary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional login helper and shell setup can expose reusable Canvas credentials.

Mitigation: Use only a trusted Canvas tenant; avoid the eval/npx login command unless its package source and version are trusted, and protect tokens and client secrets from shared terminals and logs.

Risk: Downloading Canvas files to an unverified location can expose data or overwrite files.

Mitigation: Validate file URLs and output paths before downloading.

## Reference(s):

- [Canvas API endpoints for curl](references/canvas-endpoints.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Queries return Canvas API data subject to the user's access permissions.]

## Skill Version(s):

2.1.10 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
