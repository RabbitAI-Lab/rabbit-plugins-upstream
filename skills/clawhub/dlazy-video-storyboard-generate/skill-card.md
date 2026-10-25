## Description:

Converts storyboard details into a canvas-ready audio, image, and video generation pipeline.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use the skill to turn storyboard details into a media-generation pipeline and add it to a canvas. Generation can send prompts and supplied media to cloud services, so users should review what will be sent and any charges before proceeding.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud media generation may send storyboard prompts and supplied media to external services and incur charges without a clearly separate opt-in.

Mitigation: Before generating, explain what prompts and media will be sent and what charges may apply, then obtain user approval; use a pipeline-only workflow when preparing the canvas without cloud rendering.

Risk: The release version is 1.2.31, while the skill's documented CLI install commands specify version 1.2.3.

Mitigation: Verify the intended CLI package version before installing or running generation commands.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-video-storyboard-generate)
- [dLazy CLI project (metadata link)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [JSON, Guidance, Canvas actions]

**Output Format:** [JSON media-generation pipeline and canvas update]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation may transmit prompts and supplied media to cloud services.]

## Skill Version(s):

1.2.31 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
