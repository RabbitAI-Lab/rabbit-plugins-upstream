## Description:

Guides agents through accessing Artsonia student portfolios, comments, fans, feedback, and artwork downloads with authenticated shell commands instead of an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and authorized developers use the skill to retrieve Artsonia student portfolios and account information or manage permitted member actions from a shell without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Member credentials and session cookies could expose a live parent account.

Mitigation: Keep the cookie jar private, avoid shared machines, and use the skill only for an intentionally authorized Artsonia session.

Risk: Account changes, invite emails, and bulk artwork downloads can have unintended effects.

Mitigation: Require explicit approval before any POST, invitation, profile change, feedback marking, or bulk download.

Risk: Student artwork and profile or contact details are sensitive.

Mitigation: Retrieve and store only content you are authorized to handle.

## Reference(s):

- [Artsonia API skill release](https://clawhub.ai/chrischall/skills/artsonia-api)
- [Artsonia endpoint recipes](references/endpoints.md)
- [Artsonia member site](https://www.artsonia.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may require an authorized Artsonia member session and local HTML parsing.]

## Skill Version(s):

1.3.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
