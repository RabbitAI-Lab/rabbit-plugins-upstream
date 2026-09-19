## Description:

PDF.co (pdf.co) skill for PDF.co requests including reading, creating, and updating data through the OOMOL oo CLI instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate PDF.co through an OOMOL-connected account for PDF compression, metadata inspection, text extraction, splitting, merging, and PDF creation from HTML or public URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes one-line remote installer commands for the oo CLI.

Mitigation: Prefer an official signed or package-managed oo CLI install, or download and verify the installer before executing it.

Risk: Write-capable PDF.co actions can create or modify generated outputs based on the supplied payload.

Mitigation: Confirm write action payloads and expected effects with the user before running the connector action.

## Reference(s):

- [ClawHub PDF.co Skill Page](https://clawhub.ai/oomol/skills/oo-pdf-co)
- [PDF.co Homepage](https://pdf.co)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Text, Files, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [PDF.co actions may return generated file URLs, inline text, account metadata, or execution metadata.]

## Skill Version(s):

1.0.3 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
