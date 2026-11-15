## Description:

Video generation skill that automatically selects the best dlazy CLI video model based on the prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to select a dLazy model and generate or transform videos from prompts and reference media, including lip-sync and digital-human workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are sent to dLazy hosted services for generation.

Mitigation: Avoid submitting sensitive or confidential prompts, images, video, or audio unless your organization permits that processing.

Risk: The skill has reported speech and image-upscaling capabilities alongside video generation, and the security review was partial because some references could not be resolved.

Mitigation: Review the selected model and submitted content before execution, and review generated media before sharing it.

## Reference(s):

- [dLazy CLI project](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-video-generate)

## Skill Output:

**Output Type(s):** [Videos, JSON]

**Output Format:** [Generated video media and output URLs in a JSON response envelope]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Available video modes and media options depend on the selected model.]

## Skill Version(s):

1.4.41 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
