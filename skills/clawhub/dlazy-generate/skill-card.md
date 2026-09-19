## Description:

A comprehensive generation skill that can generate images, videos, and audio by automatically selecting the appropriate dlazy CLI model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and agent users use this skill to route multimodal generation requests to the dLazy CLI for image, video, audio, speech, music, segmentation, upscaling, and vectorization workflows. The skill supports command chaining through JSON stdout envelopes and pipe references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and media file paths may be sent to the dLazy cloud service, and generated outputs may be hosted by dLazy.

Mitigation: Avoid sending sensitive or restricted content unless the user is comfortable with the dLazy cloud workflow and applicable organizational policy permits it.

Risk: Authentication can store a dLazy API key in the local CLI configuration.

Mitigation: Use per-invocation DLAZY_API_KEY where practical, keep local config permissions restricted, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The skill depends on the external dLazy CLI and cloud service for execution.

Mitigation: Use the pinned npx or install command from the release metadata and review the linked CLI source before enabling the skill in sensitive environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-generate)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output conventions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media outputs are returned by the dLazy CLI as URLs hosted by dLazy.]

## Skill Version(s):

1.3.16 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
