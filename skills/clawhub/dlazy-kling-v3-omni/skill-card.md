## Description:

Versatile video generation with Kling v3 Omni, supporting multimodal inputs such as images and prompts to create videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and developers use the skill to generate videos with Kling v3 Omni from text prompts and supported image or video references, with options for duration, aspect ratio, sound, and generation mode.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Input media is uploaded to dLazy for cloud processing, and the supplied evidence does not establish the service's data-retention practices.

Mitigation: Only submit media you are comfortable sharing with the service; review its terms before sending sensitive content.

Risk: The workflow uses a stored dLazy API key and may incur generation costs.

Mitigation: Protect the saved key, rotate or revoke it when needed, and monitor available credits and usage.

Risk: The supplied artifacts do not establish the external CLI package's runtime security.

Mitigation: Review the CLI package before installing it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3-omni)
- [dLazy](https://dlazy.com)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [video, JSON]

**Output Format:** [Generated video asset returned as a hosted URL or saved file, with JSON task and result metadata.]

**Output Parameters:** [Prompt; optional image or video references; generation mode; aspect ratio; duration; standard or pro mode; optional sound and source-audio settings.]

**Other Properties Related to Output:** [Generation may be asynchronous; results can include a task identifier for later status checks.]

## Skill Version(s):

1.3.32

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
