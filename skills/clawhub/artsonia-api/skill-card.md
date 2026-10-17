## Description:

Guides agents in using curl and optional HTML parsing to access authorized Artsonia student-art portfolios and account pages without an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and authorized Artsonia account holders use this skill to retrieve student portfolios, activity, comments, fans, and feedback with shell commands, or to make explicitly approved account changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unauthenticated image links can expose private student artwork or enable bulk collection.

Mitigation: Avoid the no-auth private-image download workflow; access only artwork you are authorized to view and do not bulk-download or retain it without consent.

Risk: Live write commands can alter student content or account settings, and redirects may not prove a change persisted.

Mitigation: Run writes only when the account owner explicitly intends the change, then re-read the affected page to verify it.

Risk: Session cookies and student profile information may be exposed through persistent files or logs.

Mitigation: Keep the cookie jar in a temporary 0600 file, delete it after use, and avoid logging cookies or profile information.

## Reference(s):

- [Artsonia API skill release](https://clawhub.ai/chrischall/skills/artsonia-api)
- [Artsonia endpoint recipes](references/endpoints.md)
- [Artsonia](https://www.artsonia.com)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Guidance]

**Output Format:** [Markdown with shell commands and parsing examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may retrieve account data or change account settings when explicitly authorized.]

## Skill Version(s):

1.3.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
