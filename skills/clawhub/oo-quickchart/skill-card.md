## Description:

QuickChart helps agents build chart image URLs, QR code URLs, and chart short URLs through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate QuickChart chart and QR-code URLs and create chart short URLs from structured payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer scripts executed directly in a shell.

Mitigation: Review the installer path before installing, and prefer a verified package, pinned release, checksum, or signature-backed method when available.

Risk: The create_chart_short_url action creates a QuickChart short URL from the submitted chart configuration.

Mitigation: Confirm the exact payload and expected effect with the user before running this write action.

## Reference(s):

- [ClawHub QuickChart skill](https://clawhub.ai/oomol/skills/oo-quickchart)
- [QuickChart homepage](https://quickchart.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce QuickChart image URLs, QR code URLs, or chart short URL creation metadata.]

## Skill Version(s):

1.0.4 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
