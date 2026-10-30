## Description:

Turn storyboard details into a JSON audio and video generation pipeline that can be added to a canvas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use the skill to turn storyboard details, dialogue, aspect ratio, and resolution into a JSON pipeline for adding audio and video nodes to a canvas. Its instructions also require a stepwise cloud media-generation workflow through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The mandatory cloud image-generation workflow exceeds the advertised storyboard-to-canvas task and may trigger generation or charges.

Mitigation: Clarify whether cloud generation is intended and get separate approval for generation, submitted media, and potential charges.

Risk: Prompts and local media may be sent to dLazy hosted services, and the CLI stores an API key in its local configuration.

Mitigation: Review the media and prompts before submission, and confirm the credential storage method before using the CLI.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-video-storyboard-generate)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)
- [CLI project link listed in skill metadata (server-resolved provenance unavailable)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [JSON, Guidance]

**Output Format:** [JSON pipeline for storyboard-derived audio and video canvas nodes, with accompanying execution guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Node dimensions and positions are derived from the storyboard aspect ratio, resolution, and order. The documented workflow can send prompts and local media to dLazy cloud services.]

## Skill Version(s):

1.2.34 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
