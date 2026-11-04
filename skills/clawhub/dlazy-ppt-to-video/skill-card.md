## Description:

Turns PowerPoint and other documents into narrated explainer, presentation, course, or training videos through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users such as presenters, educators, and teams use the skill to turn a PowerPoint or other document into a narrated explainer, pitch, course, or training video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Documents attached to a task are uploaded to dLazy storage, and project context is saved.

Mitigation: Attach only documents you are authorized to share, and consider service terms and data-retention needs before uploading.

Risk: The service requires an API key; the CLI may store it locally, and service usage may incur charges.

Mitigation: Use environment-variable authentication to avoid local key storage, and check available credits or charges before generating.

## Reference(s):

- [dLazy CLI project information](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-ppt-to-video)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration instructions, Video files]

**Output Format:** [Text and shell commands, with generated video files delivered through the dLazy service]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Attached documents are uploaded to dLazy; generated results and project context depend on the hosted service.]

## Skill Version(s):

1.0.34 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
