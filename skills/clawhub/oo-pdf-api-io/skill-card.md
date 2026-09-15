## Description:

PDF-API.io helps agents list PDF-API.io templates, retrieve template details, and render PDFs through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to operate PDF-API.io from an OOMOL-connected account: list accessible templates, inspect template details, and render PDFs from JSON data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup guidance may lead users to run unverified remote installer scripts directly in a shell.

Mitigation: Review the oo CLI installation path first and prefer official, version-pinned installation instructions with checksum or signature verification.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/oomol/skills/oo-pdf-api-io)
- [PDF-API.io homepage](https://pdf-api.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads; connector responses may include temporary hosted PDF URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before execution so payloads match the authoritative action contract.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
