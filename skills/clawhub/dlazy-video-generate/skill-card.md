## Description:

Video Generate helps agents select and invoke an appropriate dLazy CLI video model for text-to-video, image-to-video, animation, first/last-frame video, digital human, and lip-sync requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate or transform video from prompts and media inputs through the dLazy hosted API and CLI. It supports workflows such as text-to-video, image-to-video, first/last-frame generation, digital human video, segmentation, and lip-sync.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media files may be sent to dLazy cloud services, and generated outputs are hosted by dLazy.

Mitigation: Use the skill only with content appropriate for dLazy's hosted service and avoid submitting sensitive media unless the user accepts that transfer.

Risk: The dLazy API key may be stored in the local CLI configuration.

Mitigation: Use the per-invocation DLAZY_API_KEY environment variable when persistent local credential storage is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Agent-selected multi-step workflows can trigger additional paid dLazy operations such as image generation, TTS, super-resolution, segmentation, or lip-sync.

Mitigation: Ask users to confirm requested workflow scope before adding extra generation or processing steps.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-generate)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, Text]

**Output Format:** [Markdown with inline bash commands and generated media URL references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The dLazy CLI prints JSON envelopes that can be piped between commands.]

## Skill Version(s):

1.4.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
