## Description:

Access Artsonia student-art portfolios, comments, fans, teacher feedback, and downloads from a shell with curl by logging in with a username/password form POST and using a session cookie against server-rendered member pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation-oriented Artsonia account holders use this skill to retrieve and manage Artsonia student portfolio data from shell workflows without running the Artsonia MCP server. It is intended for accounts, students, artwork, comments, fan invitations, and profile settings the user is authorized to access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles authenticated Artsonia access to student and family data.

Mitigation: Use it only with accounts and artwork the operator is authorized to access, and store the Artsonia cookie jar with the same care as a password.

Risk: The documented workflows can download private artwork from public image URLs once artwork identifiers are known.

Mitigation: Avoid bulk exports unless necessary and confirm that each download is permitted for the relevant student, family, and school context.

Risk: Some workflows can submit comments, change profile settings, mark feedback read, or send fan invitation emails.

Mitigation: Require explicit human confirmation before any write action, then re-read the affected Artsonia page to verify the intended state changed.

Risk: Comment parsing is documented as unverified against live artwork with comments.

Mitigation: Validate comment extraction against a known commented artwork before relying on list_comments output.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/chrischall/skills/artsonia-api)
- [Artsonia endpoints](references/endpoints.md)
- [Artsonia website](https://www.artsonia.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell command examples and endpoint notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-supplied Artsonia credentials and a local cookie jar for authenticated member requests.]

## Skill Version(s):

0.10.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
