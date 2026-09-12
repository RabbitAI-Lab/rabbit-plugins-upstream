## Description:

Access Artsonia student-art portfolios, comments, fans, teacher feedback, and downloads from a shell with curl by logging in with a username/password form POST and using the resulting session cookie.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and authorized Artsonia account users use this skill to retrieve Artsonia account data and run documented curl recipes without operating the related MCP server. It is intended for accounts and student content the user is permitted to access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose broad Artsonia account data and student content.

Mitigation: Use it only with accounts and student content the user is authorized to access, and avoid redistributing downloaded artwork without consent.

Risk: The documented private-image download path can retrieve artwork without an authenticated session.

Mitigation: Avoid the unauthenticated private-image path unless access and downstream handling are explicitly authorized.

Risk: Write recipes can change account state or send invite emails.

Mitigation: Run write commands only when real changes are intended, then re-read the affected page to confirm the result.

Risk: Session cookies and fetched HTML can contain sensitive account or student information.

Mitigation: Store cookies and temporary HTML in private 700/600 locations and remove them after use.

Risk: Parser execution depends on local JavaScript code from the related repository.

Mitigation: Run parsers only from a verified pinned source in a sandboxed environment.

## Reference(s):

- [Artsonia endpoint recipes](references/endpoints.md)
- [Artsonia member login](https://www.artsonia.com/members/login.asp)
- [Artsonia member area](https://www.artsonia.com/members/)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/artsonia-api)
- [ClawHub publisher profile](https://clawhub.ai/user/chrischall)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Configuration, Guidance]

**Output Format:** [Markdown with inline shell and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces curl recipes, parser invocation examples, jq projections, and operational caveats for Artsonia reads, downloads, and account writes.]

## Skill Version(s):

0.12.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
