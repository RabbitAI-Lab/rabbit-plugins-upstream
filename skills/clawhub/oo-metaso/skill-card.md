## Description:

Metaso lets agents search Metaso content, read webpages, and create grounded chat completions through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Metaso through an OOMOL-connected account for search, webpage reading, and grounded chat completions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions document remote installer commands that execute downloaded shell or PowerShell scripts.

Mitigation: Review the installer source before use and prefer a verified package, pinned release, checksum, or signature-checked install path where available.

Risk: Write-tagged Metaso actions can create chat completions or otherwise change remote Metaso state.

Mitigation: Confirm the exact action payload and expected effect with the user before running write-tagged actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-metaso)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Metaso Homepage](https://metaso.cn)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include extracted webpage content, search results, or streamed and aggregated assistant content from Metaso.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
