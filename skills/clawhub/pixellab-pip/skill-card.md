## Description:

Guides agents through PixelLab setup, API routing, and the creation, editing, and animation of game art and other visual assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shilo](https://clawhub.ai/user/shilo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and artists use this skill to choose supported PixelLab tools, configure access, and produce or revise sprites, tilesets, animations, and related game assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid PixelLab generation can incur credit charges.

Mitigation: Review the planned paid calls and costs before approval; leave auto mode off unless skipping future cost prompts is intentional.

Risk: Credential setup or local output may expose secrets or write files unexpectedly.

Mitigation: Keep PixelLab secrets out of chat, use a local secret setting, and review configuration and output destinations before changes.

Risk: Remote actions and generated assets may alter projects or produce unsuitable results.

Mitigation: Confirm destructive actions and inspect generated files and reports before relying on them.

## Reference(s):

- [PixelLab Pip on ClawHub](https://clawhub.ai/shilo/skills/pixellab-pip)
- [PixelLab REST v2 documentation](https://api.pixellab.ai/v2/docs)
- [PixelLab MCP tool documentation](https://api.pixellab.ai/mcp/docs)
- [PixelLab API and MCP documentation guide](artifact/references/official-pixellab-documentation.md)
- [Cost approval and auto mode](artifact/references/auto.md)
- [Generation blueprints](artifact/references/blueprint.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance and code; generated asset files and JSON blueprints when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live generation requires PixelLab access and may consume credits; generated assets and usage reports may be saved locally.]

## Skill Version(s):

1.9.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
