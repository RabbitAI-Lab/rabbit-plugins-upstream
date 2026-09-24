## Description:

Access Artsonia (artsonia.com) student-art portfolios, comments, fans, teacher feedback, and downloads from a shell with curl instead of running the artsonia-mcp server by logging in with a username/password form POST to get a session cookie, then curling the server-rendered member pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and authorized Artsonia account holders use this skill to script access to student portfolios, artwork metadata, comments, fans, teacher feedback, awards, profile settings, and image downloads through documented curl workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide access to student artwork, private images, and account data.

Mitigation: Use only with an Artsonia account and student portfolios the operator is authorized to access, and treat downloaded artwork as sensitive child or student data.

Risk: The skill includes workflows for bulk artwork downloads.

Mitigation: Avoid bulk downloads unless there is a clear need, a retention plan, and appropriate handling controls for the downloaded files.

Risk: The skill documents POST actions that can invite fans, post comments, mark feedback read, or change notification and profile settings.

Mitigation: Require explicit operator confirmation before any POST action and re-read the affected page afterward to verify the result.

## Reference(s):

- [Artsonia endpoints - curl + parser recipes](artifact/references/endpoints.md)
- [Artsonia member login](https://www.artsonia.com/members/login.asp)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/artsonia-api)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and endpoint recipes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes curl command patterns, parser invocations, endpoint notes, and verification guidance for read and write operations.]

## Skill Version(s):

1.1.4 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
