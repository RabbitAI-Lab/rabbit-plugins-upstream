## Description:

Guides users in reading their SimplePractice Client Portal appointments, billing records, documents, announcements, and practice details from a shell using curl, with optional browser-session access through fpx.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People accessing their own SimplePractice Client Portal, and developers assisting them, use this skill to retrieve appointments, billing information, documents, and practice details without running an MCP server. It provides read-focused shell instructions for signing in and querying the portal.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Portal responses may disclose sensitive medical and billing records.

Mitigation: Use only for your own authorized portal access on a trusted personal machine; keep responses out of shared files and chat logs.

Risk: Magic links, PINs, and session cookies can grant access to the portal if exposed.

Mitigation: Protect the cookie jar with restricted permissions, avoid sharing credentials or command output, and remove the cookie jar or fpx profile when finished.

Risk: Using the wrong practice host could send authentication data to an unintended destination.

Mitigation: Verify the practice's SP_HOST against the provider's portal link before running commands.

## Reference(s):

- [SimplePractice FPX release](https://clawhub.ai/chrischall/skills/simplepractice-fpx)
- [Client Portal request reference](references/requests.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-focused; retrieved records can contain protected health information.]

## Skill Version(s):

1.2.3 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
