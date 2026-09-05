## Description:

Happy Horse 1.0 is a dLazy cloud video-generation skill for text-to-video, first-frame-to-video, reference-to-video, and video editing workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke Happy Horse 1.0 through the dLazy CLI for video generation and editing from prompts, reference images, first frames, or input video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and user-provided media paths may be sent to dLazy cloud services for inference and storage.

Mitigation: Use the skill only with inputs appropriate for dLazy's hosted service, and avoid submitting sensitive media or prompts unless that handling is acceptable.

Risk: Login can store a dLazy API key in the local CLI configuration.

Mitigation: Use DLAZY_API_KEY per invocation or the pinned npx command when persistent local credentials or a global install are not desired.

Risk: Generated outputs are hosted remotely on dLazy media storage.

Mitigation: Review generated URLs and retention expectations before sharing outputs or using them in downstream workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-happyhorse-1-0)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON response with generated media URLs; optional saved media file when --save is used]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous task IDs with --no-wait and polling through the dLazy CLI.]

## Skill Version(s):

1.3.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
