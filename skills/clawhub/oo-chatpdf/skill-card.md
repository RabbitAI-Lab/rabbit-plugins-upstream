## Description:

ChatPDF (chatpdf.com). Use this skill for ANY ChatPDF request: reading, creating, updating, and deleting data through the OOMOL-connected ChatPDF connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate ChatPDF from an agent through the OOMOL `oo` CLI, including importing public PDF URLs, asking stateless questions about imported sources, and deleting sources after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote shell and PowerShell installer commands for the OOMOL CLI.

Mitigation: Review the official install documentation, download installers for inspection, and verify provenance before running installer commands.

Risk: The `delete_sources` action can remove ChatPDF sources.

Mitigation: Confirm the exact target source IDs and obtain explicit user approval before running destructive actions.

Risk: Write actions such as `add_source_url` can change ChatPDF state.

Mitigation: Inspect the live action schema and confirm the payload and expected effect before executing write actions.

## Reference(s):

- [ChatPDF homepage](https://www.chatpdf.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-chatpdf)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schema inspection before constructing connector requests.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
