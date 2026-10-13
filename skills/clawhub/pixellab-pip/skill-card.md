## Description:

Guides agents through PixelLab setup, cost-aware asset generation, editing, animation, and integration across supported MCP, API, and editor surfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shilo](https://clawhub.ai/user/shilo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to plan and carry out PixelLab sprite, image, animation, and game-asset workflows, including setup, integration, and credit-aware generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live PixelLab generations can spend credits.

Mitigation: Review the planned paid calls and costs before approving; enable automatic cost approval only if you accept future jobs without per-job prompts.

Risk: A disclosed integration uses a bearer token and can write or replace local outputs.

Mitigation: Keep PIXELLAB_SECRET in a local secret store, never in chat, and confirm setup, updates, removal, deletion, and overwrites before allowing them.

## Reference(s):

- [PixelLab Pip release](https://clawhub.ai/shilo/skills/pixellab-pip)
- [PixelLab REST v2 documentation](https://api.pixellab.ai/v2/docs)
- [PixelLab MCP documentation](https://api.pixellab.ai/mcp/docs)
- [Setup guidance](references/setup.md)
- [Cost routing guidance](references/cost-routing.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions, Image files, Animation files]

**Output Format:** [Markdown guidance and code blocks; PixelLab-generated assets and JSON blueprints for live jobs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live generations may consume credits and write local output files.]

## Skill Version(s):

2.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
