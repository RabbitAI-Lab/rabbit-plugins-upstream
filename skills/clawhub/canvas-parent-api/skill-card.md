## Description:

Guides agents in querying Canvas LMS with curl and bearer-token authentication for courses, grades, assignments, submissions, calendars, announcements, conversations, discussions, and files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and education support users can use this skill to have an agent produce Canvas REST API curl commands and endpoint guidance without running the Canvas parent MCP server. It is intended for scripted or shell-based Canvas data access using a user-supplied institution host and token.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Canvas bearer tokens and student data could be exposed through shared terminals, logs, copied commands, or unreviewed helper output.

Mitigation: Review commands before use, keep tokens out of shared shells and logs, and pin and review any helper used to mint OAuth credentials.

Risk: Authorization headers could be sent to an unintended host if a base URL, pagination URL, file URL, or redirect target is not validated.

Mitigation: Use only the official Canvas hostname for the institution and validate pagination and file download URLs before sending bearer tokens or downloading files.

Risk: The documented eval-based token setup can execute unexpected shell text from the helper output.

Mitigation: Inspect helper output before exporting it, avoid eval where possible, and run the helper only from a reviewed and pinned package version.

## Reference(s):

- [Canvas API endpoint reference](references/canvas-endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/canvas-parent-api)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and Canvas REST API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-supplied Canvas base URL and bearer or OAuth token; Canvas responses are retrieved outside the skill.]

## Skill Version(s):

1.5.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
