## Description:

Query a configurable Infinite Campus parent portal with curl to retrieve grades, attendance, assignments, schedules, messages, documents, and fees without an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and developers use this skill to access a district's Campus Parent portal from scripts and retrieve student records such as grades, attendance, assignments, schedules, messages, documents, and fees.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Document downloads can send portal credentials or session tokens to an unchecked destination.

Mitigation: Verify that download URLs use HTTPS and belong to the district before requesting them; omit portal tokens for external destinations.

Risk: Saved reports can overwrite existing files or expose student records.

Mitigation: Save reports to unique, private files and retrieve only the student records needed.

Risk: The cookie jar contains active session credentials after use.

Mitigation: Remove the cookie jar when portal access is complete.

## Reference(s):

- [Infinite Campus endpoints](references/endpoints.md)
- [ClawHub release page](https://clawhub.ai/chrischall/skills/infinitecampus-api)

## Skill Output:

**Output Type(s):** [Shell commands, API responses, JSON, Guidance]

**Output Format:** [Markdown instructions with inline shell commands and JSON or text responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [District-dependent portal results; may include sensitive student records.]

## Skill Version(s):

3.3.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
