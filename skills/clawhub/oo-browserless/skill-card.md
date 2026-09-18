## Description:

Browserless lets an agent use the OOMOL oo CLI to inspect Browserless action schemas and fetch rendered content, PDFs, or screenshots through a connected Browserless account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Browserless through an OOMOL-connected account for rendered page content, PDF generation, and screenshot capture without handling raw Browserless credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes commands that run remote installer scripts directly.

Mitigation: Review the installer source and delivery path before running setup commands; prefer signed or version-pinned packages, checksum verification, or manual inspection of the downloaded installer.

## Reference(s):

- [ClawHub Browserless Skill](https://clawhub.ai/oomol/skills/oo-browserless)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Browserless](https://www.browserless.io)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Browserless action responses containing rendered HTML, base64 PDF content, base64 screenshot content, and execution metadata.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
