## Description:

Access Artsonia student-art portfolios, comments, fans, teacher feedback, and downloads from a shell with curl instead of running the artsonia-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical users use this skill to access Artsonia member pages, extract student portfolio data, download artwork images, and perform documented account actions with curl and parser recipes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill teaches access to sensitive student-art account data.

Mitigation: Use it only with an Artsonia account and artwork the user is authorized to access, and review outputs before storing or sharing them.

Risk: The cookie jar represents an authenticated Artsonia session.

Mitigation: Store the cookie jar in a protected location, avoid committing it, and refresh or revoke the session when access is no longer needed.

Risk: Anonymous CDN and bulk-download recipes can retrieve artwork the skill describes as private.

Mitigation: Avoid CDN or bulk-download use for private student artwork unless explicit permission exists.

Risk: Write recipes can send emails or change account state.

Mitigation: Treat write commands as real account actions and verify changed pages after each POST before relying on the result.

## Reference(s):

- [Artsonia endpoint recipes](artifact/references/endpoints.md)
- [Artsonia website](https://www.artsonia.com)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/artsonia-api)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, curl examples, parser snippets, and verification steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces credential-handling, session-cookie, read/write, verification, and download guidance for authorized Artsonia account access.]

## Skill Version(s):

0.10.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
