## Description:

Mailgun lets agents inspect and manage Mailgun domains, templates, events, suppressions, tracking settings, and email sending through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and support teams use this skill to perform Mailgun account operations without handling raw API tokens, including domain checks, event review, suppression management, template maintenance, and controlled email sending.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include commands that execute internet-downloaded installer scripts.

Mitigation: Review the OOMOL CLI installation path before running it; prefer an official package manager, pinned release, or installer with verified checksum or signature.

Risk: Mailgun write and destructive actions can send email, change tracking settings, or alter suppression and allowlist records.

Mitigation: Confirm the exact action, target, and payload before sends, writes, tracking changes, or deletion of suppressions.

## Reference(s):

- [Mailgun homepage](https://www.mailgun.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include JSON returned by the oo CLI, including connector response data and execution metadata.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
