## Description:

Converts storyboard details into a video-generation pipeline that can be added to a canvas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers can use the skill to turn storyboard context, dialogue, and video prompts into a JSON generation pipeline and add it to a canvas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generation can submit story content or media to the external provider and may incur charges.

Mitigation: Before generation, approve the provider, submitted content, and possible charges; request a preparation-only version if only storyboard preparation is needed.

Risk: The executable package and credential-file protections were not verified in this review.

Mitigation: Verify the intended CLI version and confirm package integrity and credential-file access restrictions before installation.

## Reference(s):

- [CLI project homepage (skill metadata)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [JSON, Configuration, Guidance]

**Output Format:** [JSON generation pipeline and canvas tool action]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses storyboard names, dialogue, prompts, aspect ratio, and resolution as inputs.]

## Skill Version(s):

1.2.35 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
