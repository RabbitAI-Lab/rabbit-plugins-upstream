## Description:

Guides agents in using curl to access a district's Infinite Campus parent portal for student grades, attendance, assignments, messages, documents, and fees without an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and authorized developers use this skill to retrieve student information from their own district's Infinite Campus parent portal using shell commands instead of an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Portal credentials, session cookies, and downloaded student documents may be exposed through shell history, logs, or retained files.

Mitigation: Use a secret store, avoid pasting credentials or session data into chats or logs, and delete cookie jars and downloaded documents when finished.

Risk: An absolute document URL could send session cookies and tokens outside the district portal.

Mitigation: Restrict document downloads to the same Infinite Campus host before sending authenticated requests.

## Reference(s):

- [Infinite Campus API skill release](https://clawhub.ai/chrischall/skills/infinitecampus-api)
- [Infinite Campus endpoint recipes](artifact/references/endpoints.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with curl and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an authorized district portal account; retrieved student records and downloaded documents are sensitive.]

## Skill Version(s):

3.2.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
