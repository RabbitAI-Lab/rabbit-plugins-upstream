## Description:

Guides direct curl access to district Infinite Campus Parent portals for student grades, attendance, assignments, schedules, messages, documents, and fees without an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and authorized developers use the skill to retrieve student portal information from their district with curl when they do not use the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live portal credentials and session tokens may be exposed through shared machines, logs, or shell history.

Mitigation: Use a private machine and secret storage; protect temporary cookie files and avoid logging credentials or tokens.

Risk: Downloaded PDFs and JSON responses may expose sensitive student education records.

Mitigation: Choose private output paths, secure temporary files, and delete session files and downloaded records when no longer needed.

Risk: Opening a message body may mark it read in some districts.

Mitigation: Confirm this possible side effect before retrieving message bodies.

## Reference(s):

- [Infinite Campus endpoint recipes](references/endpoints.md)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/infinitecampus-api)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with curl and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [District-specific portal settings and student or enrollment IDs are required for requests.]

## Skill Version(s):

3.1.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
