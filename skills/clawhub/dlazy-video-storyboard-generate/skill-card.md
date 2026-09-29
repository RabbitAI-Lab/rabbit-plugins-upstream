## Description:

Turns storyboard scenes into a canvas-ready video-generation pipeline and guides optional media generation with dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to turn storyboard dialogue and scene prompts into a canvas pipeline for cloned audio and generated video. Its additional instructions guide stepwise image generation through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill expands from arranging a storyboard on a canvas to running a media-generation CLI.

Mitigation: Review the requested workflow and confirm before installing or running generation commands.

Risk: The CLI may store an API key locally and send prompts, parameters, and referenced media to dLazy cloud services.

Mitigation: Use only intended media and credentials, review cloud-upload terms, and rotate or revoke the key if necessary.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-video-storyboard-generate)
- [dLazy CLI package (listed in skill metadata)](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Media URLs]

**Output Format:** [JSON canvas pipeline and Markdown guidance; generated media URLs when media generation is requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Shared source audio and scene image, with per-storyboard cloned audio and video nodes.]

## Skill Version(s):

1.2.20 (source: ClawHub release; embedded skill frontmatter says 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
