## Description:

CraftMyPDF helps agents read, create, and update CraftMyPDF data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to work with CraftMyPDF through an OOMOL-connected account, including listing templates, inspecting template details, checking account information, and generating PDFs from templates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes downloaded installer scripts that can execute code during installation.

Mitigation: Review the installer source before use and prefer signed packages, pinned releases, or checksum/signature verification.

Risk: The create_pdf action generates hosted PDF outputs from user-supplied template payloads.

Mitigation: Confirm the exact payload and intended effect with the user before running create_pdf, then review the generated output URL and transaction metadata.

## Reference(s):

- [ClawHub CraftMyPDF skill page](https://clawhub.ai/oomol/skills/oo-craftmypdf)
- [CraftMyPDF homepage](https://craftmypdf.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI installation guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the oo CLI to inspect live connector schemas and run CraftMyPDF actions; create_pdf returns hosted file URLs and transaction metadata.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
