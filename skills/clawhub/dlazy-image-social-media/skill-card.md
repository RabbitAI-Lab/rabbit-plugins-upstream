## Description:

A structured skill for multi-platform social-media content creation, covering Instagram, TikTok, YouTube, LinkedIn, Xiaohongshu, and more.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and content creators use this skill to plan and generate platform-specific social-media visuals, including layouts, in-image text, captions, and iteration guidance for formats such as Instagram posts, TikTok or YouTube Shorts assets, LinkedIn carousels, YouTube thumbnails, and Xiaohongshu posts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media paths may be sent to dLazy services, and generated results may be hosted remotely.

Mitigation: Avoid sensitive private media and secrets in prompts or media inputs; review generated output before publication.

Risk: Login can store a dLazy API key in local CLI configuration.

Mitigation: Use the DLAZY_API_KEY environment variable for per-run credentials when persistent local storage is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The skill depends on a third-party npm CLI package to perform image generation.

Mitigation: Review the pinned @dlazy/cli package and installation command before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-social-media)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples, image-generation prompts, caption copy, and generated image URLs when the CLI is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may reference dLazy-hosted generated media URLs and should keep in-image text separate from caption copy.]

## Skill Version(s):

1.3.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
