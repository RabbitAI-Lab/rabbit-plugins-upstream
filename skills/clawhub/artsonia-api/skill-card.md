## Description:

Guides agents in using shell commands to access Artsonia student-art portfolios, comments, fans, teacher feedback, and downloads through an authorized parent account without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and authorized agents use this skill to retrieve student artwork and account information from Artsonia using shell commands, and to manage permitted account interactions without an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Direct access to a parent account exposes login credentials, session cookies, and student information.

Mitigation: Use only an account and student data you are authorized to access; protect credentials and local session cookies, and review access before installing.

Risk: Unauthenticated artwork links and bulk downloads can expose artwork described as private.

Mitigation: Avoid private-artwork and bulk-download recipes without clear permission.

Risk: Comments, fan invitations, feedback reads, and profile or notification changes may affect other people or account settings.

Mitigation: Require explicit confirmation before these actions and verify any submitted change by reading it back.

## Reference(s):

- [Artsonia API endpoint recipes](references/endpoints.md)
- [Artsonia API ClawHub release](https://clawhub.ai/chrischall/skills/artsonia-api)
- [Artsonia](https://www.artsonia.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration instructions]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can retrieve page data or submit account changes; responses may include student information.]

## Skill Version(s):

1.2.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
