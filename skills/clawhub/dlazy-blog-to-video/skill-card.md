## Description:

Helps turn blog posts or documents into narrated videos with storyboards and voiceovers through the dLazy hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and teams use this skill to request narrated video adaptations of blog posts or documents for social media, explainers, or training.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files may be sent to the third-party dLazy service.

Mitigation: Review content and obtain approval before sending sensitive material or attaching files.

Risk: Login stores an API key locally.

Mitigation: Protect the local credential and rotate or revoke it if exposed.

Risk: The blog-to-video label invokes a broader file-to-video workflow.

Mitigation: Review the requested task and resulting video for scope and accuracy.

## Reference(s):

- [dLazy CLI source listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Terminal text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Hosted video creation is requested through the dLazy file-to-video workflow; the CLI streams responses and tracks projects for follow-up.]

## Skill Version(s):

1.0.22 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
