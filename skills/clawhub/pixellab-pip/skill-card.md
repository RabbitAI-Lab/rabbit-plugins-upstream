## Description:

PixelLab Pip helps agents route PixelLab requests and create, edit, inspect, and assemble pixel art, game assets, animations, and visual effects through documented PixelLab interfaces and local tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shilo](https://clawhub.ai/user/shilo)

### License/Terms of Use:

MIT

## Use Case:

Developers and game artists use the skill to plan and generate pixel-art assets, edit and inspect images or animation, and assemble game-ready outputs using PixelLab MCP or REST and local tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected artwork are sent to PixelLab for generation.

Mitigation: Review prompts and artwork before sending; keep sensitive inputs local.

Risk: Generation may spend PixelLab credits.

Mitigation: Keep Auto off when approval is needed and consult the cost guidance before generation.

Risk: PIXELLAB_SECRET grants access to PixelLab services.

Mitigation: Store the token locally in a secret setting or environment variable; do not paste it into chat.

Risk: Output folders may contain recipes and copied input images.

Mitigation: Review output folders before sharing them.

Risk: User-level MCP setup can make PixelLab available across projects.

Mitigation: Choose project-only MCP setup when access should stay scoped to one project.

## Reference(s):

- [PixelLab API documentation](https://www.pixellab.ai/docs)
- [PixelLab REST v2 API reference](https://api.pixellab.ai/v2/docs)
- [PixelLab MCP tool guide](https://api.pixellab.ai/mcp/docs)
- [PixelLab MCP setup](https://www.pixellab.ai/mcp)
- [Official PixelLab documentation links and interface guidance](references/official-pixellab-documentation.md)
- [Setup and credentials guidance](references/setup.md)
- [Generation cost and routing guidance](references/cost-routing.md)

## Skill Output:

**Output Type(s):** [Pixel art images and sprite assets, Animation and visual effects assets, Markdown guidance, Code and shell commands, Configuration and blueprint files]

**Output Format:** [Image files, Markdown, code, shell commands, and JSON configuration or blueprints]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May involve PixelLab generation credits; outputs can include sprite sheets, animations, VFX, maps, and assembled assets.]

## Skill Version(s):

3.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
