## Description:

Guides cinematic and narrative storyboard creation through approved specifications, character design, scripts, and image generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and production teams use this skill to plan film, advertising, short-video, educational, and comic-style storyboards, approving each stage before generating images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied local media may be sent to dLazy's cloud service, with generated images hosted remotely.

Mitigation: Avoid sensitive material and approve prompts and local media before submission; review hosted output links before sharing.

Risk: The dLazy API key may be saved in the user's local CLI profile.

Mitigation: Use the DLAZY_API_KEY environment variable when persistent storage is unwanted, and rotate or revoke exposed keys.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-image-storyboard)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Image URLs, Storyboard guidance]

**Output Format:** [Markdown bullet lists with per-panel prompts, generation commands, and image links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes shot and scene specifications, approval checkpoints, and A4 landscape print/PDF layout guidance.]

## Skill Version(s):

1.3.25 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
