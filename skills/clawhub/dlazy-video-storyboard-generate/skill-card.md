## Description:

Turns storyboard scenes into a canvas video-generation pipeline with shared scene assets and per-scene audio and video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to translate storyboard scenes, dialogue, and visual prompts into a canvas pipeline for video generation; optional dLazy CLI commands can generate media after user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and referenced media may be sent to dLazy cloud services.

Mitigation: Avoid sensitive media and review what will be sent before generation.

Risk: CLI use requires an API key stored in local configuration, and a global installation persists on the device.

Mitigation: Protect local credentials and prefer on-demand npx use if a global install is unnecessary.

Risk: The skill combines canvas planning with executable generation commands.

Mitigation: Clarify whether the user wants only the canvas pipeline or actual media generation before allowing commands to run.

## Reference(s):

- [dLazy CLI source (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package (skill metadata)](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Markdown, Shell commands]

**Output Format:** [JSON canvas pipeline with Markdown guidance and optional CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Shared source audio and scene image; per-scene cloned audio and video.]

## Skill Version(s):

1.2.29 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
