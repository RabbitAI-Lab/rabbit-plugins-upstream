## Description:

Helps an agent select and run dLazy video-generation models for text-to-video, image-to-video, reference-driven video, digital avatars, and lip sync.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to choose a video model and generate or edit short videos from prompts, images, audio, or existing video through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any media supplied for generation may be sent to the third-party dLazy service.

Mitigation: Review prompts and media for sensitive content before submitting them.

Risk: Authentication can save a dLazy API key on the user's device.

Mitigation: Protect local account access and review or revoke the key in the dLazy dashboard when needed.

Risk: A global CLI installation remains on the user's device.

Mitigation: Use the documented pinned npx invocation if a persistent global installation is not wanted.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-video-generate)
- [dLazy CLI repository (declared in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text with shell commands and links to generated video]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns JSON results containing hosted output URLs.]

## Skill Version(s):

1.4.23 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
