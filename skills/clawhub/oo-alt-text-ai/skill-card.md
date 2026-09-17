## Description:

AltText.ai lets an agent manage AltText.ai image records and generate alt text through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to generate alt text for public image URLs, inspect AltText.ai account details, search or list image records, and manage image library entries through OOMOL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends piping remote installer scripts directly into bash or PowerShell.

Mitigation: Review the OOMOL CLI installation path before installing and prefer official, version-pinned, signed, or checksum-verified installation instructions.

Risk: The skill can add images to AltText.ai and delete image records.

Mitigation: Confirm the exact payload and expected effect before write actions, and get explicit approval before destructive delete actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-alt-text-ai)
- [AltText.ai homepage](https://alttext.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses an OOMOL-connected AltText.ai account; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.4 (source: artifact metadata and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
