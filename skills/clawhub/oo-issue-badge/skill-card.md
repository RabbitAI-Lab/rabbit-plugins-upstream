## Description:

Helps users manage IssueBadge templates and issued badges through their connected OOMOL account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

IssueBadge users can list badge templates, retrieve issued badge records, and issue existing templates to recipients through a connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback installation instructions run a remote installer directly in a shell.

Mitigation: Review the official CLI installation instructions and the installer before running it; do not approve remote execution without trusting the source and understanding the changes.

Risk: Connected access can expose recipients' personal data or create publicly verifiable badge records and notification emails.

Mitigation: Handle read results as sensitive and confirm the exact recipient, badge, email, and intended effect with the user before issuing a badge.

## Reference(s):

- [IssueBadge](https://issuebadge.com)
- [OOMOL CLI installation guide](https://cli.oomol.com/install-guide.md)
- [IssueBadge skill release](https://clawhub.ai/oomol/skills/oo-issue-badge)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with command examples and summarized JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read results may contain recipient details, verification URLs, and PDF URLs; issuance can create a public verification URL and send an email notification.]

## Skill Version(s):

1.0.0 (source: skill frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
