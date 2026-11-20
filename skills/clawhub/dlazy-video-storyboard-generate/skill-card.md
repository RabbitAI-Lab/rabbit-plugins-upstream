## Description:

Converts storyboard details into a video-generation pipeline that can be added to a canvas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video creators can use the skill to turn storyboard details, dialogue, and generation prompts into a video pipeline for a canvas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires login and API key setup, which the security summary flags as undeclared credential actions.

Mitigation: Avoid installation until the publisher clarifies why authentication is required; protect the API key and rotate or revoke it if needed.

Risk: Cloud generation sends prompts and potentially local media to dLazy services and may involve charges.

Mitigation: Review prompts and media before sending, obtain consent for sharing, and confirm expected costs and whether cloud generation can be optional.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-video-storyboard-generate)
- [CLI project page listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, API Calls]

**Output Format:** [JSON video-generation pipeline and canvas tool call]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Pipeline elements are repeated for each storyboard, with shared source audio and scene image.]

## Skill Version(s):

1.2.40 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
