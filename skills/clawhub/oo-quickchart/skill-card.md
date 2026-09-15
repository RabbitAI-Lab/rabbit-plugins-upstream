## Description:

QuickChart helps agents use the OOMOL oo CLI to build QuickChart chart image URLs, generate QR code URLs, and create chart short URLs from validated action schemas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to work with QuickChart through OOMOL-connected actions, including creating chart URLs, QR code URLs, and QuickChart short URLs after inspecting the live action schema.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands executed directly in a shell.

Mitigation: Review the installer step before use and prefer a verified package manager or installer with a published checksum or signature.

Risk: The create_chart_short_url action writes QuickChart short URL state from the submitted payload.

Mitigation: Inspect the live action schema and confirm the exact payload and effect before running write actions.

## Reference(s):

- [QuickChart homepage](https://quickchart.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce QuickChart image URLs, QR code URLs, short URLs, and creation metadata returned by the connector.]

## Skill Version(s):

1.0.4 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
