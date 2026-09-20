## Description:

QuickChart lets agents use the OOMOL oo CLI connector to build QuickChart chart image URLs, QR code URLs, and short URLs from supplied payloads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and external users can use this skill through an agent to generate QuickChart chart image URLs, QR code URLs, and chart short URLs while checking live action schemas before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands for the oo CLI.

Mitigation: Use a verified oo CLI installation path, or inspect and verify the installer before running it.

Risk: Write-tagged actions can create QuickChart URLs or short URLs from user-supplied payloads.

Mitigation: Fetch the live action schema and confirm the exact payload and effect before running write actions.

## Reference(s):

- [QuickChart homepage](https://quickchart.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub QuickChart skill page](https://clawhub.ai/oomol/skills/oo-quickchart)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, text]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent output may include oo CLI schema inspection commands, action execution commands, QuickChart URLs, QR code URLs, short URLs, and execution metadata.]

## Skill Version(s):

1.0.5 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
