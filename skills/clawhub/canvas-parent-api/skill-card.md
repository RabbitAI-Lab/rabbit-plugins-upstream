## Description:

Guides agents in querying Canvas LMS for a user or linked observee through authenticated shell requests without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Students, parents, and developers use this skill to retrieve their own or a linked student's Canvas courses, grades, assignments, messages, and files through the institution's API without an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Canvas access and refresh credentials could be exposed through shell history, logs, or insecure storage.

Mitigation: Keep credentials in a secure secret store, limit access to command output, and unset shell variables when finished.

Risk: The suggested QR-login command executes an unpinned helper through eval.

Mitigation: Review and pin the helper before running it, and avoid eval where possible.

Risk: Downloaded Canvas files and API responses may contain sensitive student or message data.

Mitigation: Keep downloaded files and command output private and share them only with authorized recipients.

## Reference(s):

- [Canvas API endpoint examples](references/canvas-endpoints.md)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/canvas-parent-api)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can retrieve Canvas JSON, including sensitive student records and messages.]

## Skill Version(s):

2.1.6 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
