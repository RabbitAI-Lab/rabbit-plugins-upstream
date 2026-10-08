## Description:

Selects a dLazy video model to generate or edit videos from text, images, video, or audio inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to select and run video-generation models for text-to-video, image animation, reference-driven clips, and lip synchronization through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local image, video, or audio files may be uploaded to dLazy services.

Mitigation: Use only media and prompts approved for sharing with the dLazy cloud service.

Risk: Authentication may store an API key in the local dLazy configuration.

Mitigation: Protect the local configuration and rotate or revoke the key if exposed.

Risk: Running the dLazy CLI installs and executes a third-party package.

Mitigation: Review the pinned @dlazy/cli package before use; prefer on-demand npx execution to avoid a persistent global install.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-video-generate)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Video URLs]

**Output Format:** [Text instructions and CLI JSON responses containing generated video URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key and access to the dLazy cloud service.]

## Skill Version(s):

1.4.27 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
