## Description:

Guides agents in choosing PixelLab workflows to create, edit, inspect, and repair game art and animation, with practical setup and cost guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shilo](https://clawhub.ai/user/shilo)

### License/Terms of Use:

MIT

## Use Case:

Developers and game artists use this skill to route PixelLab requests for sprites, characters, tiles, backgrounds, effects, and animation, and to manage setup, costs, and local asset workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: PixelLab generation can spend credits.

Mitigation: Keep Auto off or set a run budget, and review the planned paid calls before generation.

Risk: A bearer token could be exposed in conversation.

Mitigation: Keep the token out of chat and configure it in the MCP client or local PIXELLAB_SECRET environment.

Risk: Recipes or copied artwork may be unsuitable to share.

Mitigation: Review recipes and copied images before sharing them.

Risk: Local repair steps can alter image files.

Mitigation: Inspect repaired copies before replacing original assets.

## Reference(s):

- [PixelLab documentation](https://www.pixellab.ai/docs)
- [PixelLab REST API v2 documentation](https://api.pixellab.ai/v2/docs)
- [PixelLab MCP documentation](https://api.pixellab.ai/mcp/docs)
- [PixelLab MCP setup](https://www.pixellab.ai/mcp)

## Skill Output:

**Output Type(s):** [Images and animation assets, Text and Markdown guidance, Code, Shell commands, Configuration]

**Output Format:** [Pixel art image files and animations, plus text, Markdown, code, shell commands, and JSON configuration or recipes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated assets and local helper outputs vary by task; blueprints and setup details are provided when relevant.]

## Skill Version(s):

3.0.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
