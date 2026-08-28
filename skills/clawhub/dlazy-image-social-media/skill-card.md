## Description:

A structured skill for creating platform-aware social media images and copy plans across Instagram, TikTok, YouTube, LinkedIn, Xiaohongshu, and similar channels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, marketers, and agent developers use this skill to plan and generate social-media image concepts, in-image text, captions, and platform-specific adaptations through the dLazy CLI workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party CLI and sends prompts to dLazy services.

Mitigation: Review the generated prompt content before execution and avoid sending confidential or regulated information unless dLazy processing is approved.

Risk: Local media paths referenced by the user may be uploaded to dLazy media storage for model access.

Mitigation: Only reference files that are intended for upload, and remove or redact sensitive media before using the workflow.

Risk: The dLazy CLI can persist an API key in local configuration.

Mitigation: Use the DLAZY_API_KEY environment-variable option when a persistent local key is not desired, and rotate or revoke keys through the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-social-media)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with structured planning text, captions, prompt drafts, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated image URLs hosted by dLazy media storage when the dLazy CLI is executed.]

## Skill Version(s):

1.3.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
