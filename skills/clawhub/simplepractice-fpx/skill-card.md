## Description:

Guides authorized clients in reading their SimplePractice Client Portal records using shell commands, with email sign-in or an existing browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Authorized SimplePractice clients and their assistants use this skill to retrieve appointments, billing records, shared documents, and practice announcements without an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Session cookies, sign-in tokens, and PINs can expose private medical records.

Mitigation: Use only your authorized portal, protect credentials and responses, keep the cookie jar out of git, and remove it and any fpx profile after use.

Risk: Downloaded documents and billing details contain sensitive personal information.

Mitigation: Verify the practice host and avoid logging or sharing portal responses.

## Reference(s):

- [SimplePractice portal request reference](artifact/references/requests.md)
- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/simplepractice-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only guidance; requires authorized portal access.]

## Skill Version(s):

1.2.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
