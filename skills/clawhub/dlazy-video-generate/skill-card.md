## Description:

Helps an agent choose a dLazy video model and generate videos from text, images, reference media, or audio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to select a video-generation model and make short videos or animations from prompts and supplied media, including lip-synced clips.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and media supplied to the CLI may be sent to dLazy cloud services.

Mitigation: Only submit media and prompts you are comfortable sharing with dLazy; review the pinned CLI package before using sensitive material.

Risk: The dLazy API key can be stored in local CLI configuration.

Mitigation: Protect the local key, or supply it per invocation; rotate or revoke it if exposed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-video-generate)
- [dLazy CLI repository (package reference)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown with commands and links to generated videos]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns JSON containing links to hosted results.]

## Skill Version(s):

1.4.29 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
