## Description:

Access Artsonia student-art portfolios, comments, fans, teacher feedback, and downloads from shell commands that log in with a session cookie and fetch server-rendered pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and authorized Artsonia account holders use this skill to script reads and carefully confirmed writes for student artwork, portfolio, feedback, fan, profile, and download workflows without running the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose sensitive student and family Artsonia data, including private artwork and account pages.

Mitigation: Use only authorized Artsonia accounts, avoid retaining private artwork unless permission is clear, restrict cookie-jar permissions, delete the cookie jar when finished, and handle downloaded HTML and images as sensitive data.

Risk: The documented write flows can change account settings, mark feedback, submit comments, or send fan invitations.

Mitigation: Require explicit confirmation before any write or fan invitation, re-read the affected page after POST requests, and treat redirects as insufficient proof that a change persisted.

## Reference(s):

- [Artsonia endpoints - curl + parser recipes](references/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/artsonia-api)
- [Artsonia](https://www.artsonia.com)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes credential, cookie-jar, read/write endpoint, parser, and verification guidance.]

## Skill Version(s):

1.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
