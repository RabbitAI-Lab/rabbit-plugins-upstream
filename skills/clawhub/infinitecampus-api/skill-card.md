## Description:

Guides authenticated, district-specific Infinite Campus Parent portal queries using curl and jq without an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and authorized developers use this skill to retrieve student grades, attendance, assignments, messages, documents, and other school records from their own district portal without running the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Portal credentials, session cookies, or student records may be exposed through shell history, logs, or retained files.

Mitigation: Use only your authorized account on a trusted machine, keep secrets out of history and logs, protect the cookie jar, and delete cookies and downloaded records when finished.

Risk: An absolute document URL may send an authenticated download request to an unexpected host.

Mitigation: Verify absolute download URLs belong to the expected district or Infinite Campus host before requesting them.

## Reference(s):

- [Infinite Campus endpoint recipes](artifact/references/endpoints.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with curl and jq command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [District-specific endpoints and feature availability.]

## Skill Version(s):

3.1.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
