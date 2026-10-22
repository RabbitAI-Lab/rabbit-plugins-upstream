## Description:

Turns a user's idea into a user-approved video-production plan and canvas-ready workflow, with optional image and video generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use the skill to turn a creative idea into a reviewable story, scene, shot, and media-generation workflow. They can adjust the plan before creating canvas shapes or generating images and video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are sent to dLazy for cloud generation, which may incur charges.

Mitigation: Confirm each prompt and expected charges before generation, and provide only media intended for upload.

Risk: The API key may be stored in local CLI configuration.

Mitigation: Protect the local configuration file or use the DLAZY_API_KEY environment-variable alternative; rotate or revoke exposed keys.

Risk: The canvas-planning and direct CLI workflows are not clearly reconciled in the skill instructions.

Mitigation: Choose the intended workflow explicitly before starting, and review the pinned dLazy CLI 1.2.3 dependency.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-idea2video)
- [dLazy website](https://dlazy.com)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Guidance, Configuration, Images, Video]

**Output Format:** [Markdown guidance and JSON workflow-plan configuration; generated image and video media]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Interactive workflow; prompts and generation steps require user confirmation.]

## Skill Version(s):

1.3.36 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
