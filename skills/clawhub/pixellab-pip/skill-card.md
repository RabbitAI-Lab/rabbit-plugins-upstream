## Description:

Guides agents through PixelLab setup, supported image and animation workflows, asset generation, and cost-aware API use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shilo](https://clawhub.ai/user/shilo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to choose and run supported PixelLab workflows for generating, editing, and animating game assets, and to troubleshoot setup and credit use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A PixelLab bearer token could be exposed in chat or logs.

Mitigation: Configure the token in the MCP client or environment; do not paste secrets into chat.

Risk: Paid generation can consume credits without an expected budget.

Mitigation: Confirm the cost or budget before generation and keep auto mode off unless skipping per-run approval is intended.

Risk: Generated assets and related files may be written locally.

Mitigation: Review the output location and generated files before using or sharing them.

Risk: Destructive asset operations may remove or replace existing work.

Mitigation: List the affected assets and confirm the scope before destructive operations.

## Reference(s):

- [PixelLab Pip on ClawHub](https://clawhub.ai/shilo/skills/pixellab-pip)
- [PixelLab API documentation](https://api.pixellab.ai/v2/docs)
- [PixelLab MCP documentation](https://api.pixellab.ai/mcp/docs)
- [PixelLab credential guidance](artifact/references/credentials.md)
- [PixelLab cost routing](artifact/references/cost-routing.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration, Files]

**Output Format:** [Markdown guidance and commands; generated asset files and JSON blueprints when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live generation requires PixelLab authentication and may consume credits; generated files can be saved locally.]

## Skill Version(s):

2.2.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
