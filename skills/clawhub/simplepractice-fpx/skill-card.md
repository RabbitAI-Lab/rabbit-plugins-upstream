## Description:

Guides agents in reading authorized SimplePractice Client Portal information through shell commands, using email sign-in or an existing browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Portal users and developers use this skill to retrieve appointments, billing records, documents, and practice information they are authorized to access without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Portal responses may expose sensitive medical and billing information.

Mitigation: Access only your own data or data you are authorized to view, and avoid logging full responses.

Risk: A session cookie or captured browser profile can grant access to the portal.

Mitigation: Protect the cookie jar and profile like passwords, avoid shared machines, and prefer email magic-link or PIN sign-in when possible.

## Reference(s):

- [SimplePractice FPX request reference](references/requests.md)
- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/simplepractice-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires access to an authorized portal account.]

## Skill Version(s):

1.2.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
