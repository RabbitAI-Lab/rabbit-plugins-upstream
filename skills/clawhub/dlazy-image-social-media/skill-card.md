## Description:

This skill helps agents plan and produce platform-adapted social media image concepts, in-image text, captions, and generation steps for formats such as Instagram, TikTok, YouTube, LinkedIn, and Xiaohongshu.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agent users use this skill to plan social media visuals, captions, safe-area checks, and platform-specific image generation workflows. It is aimed at multi-platform campaign assets rather than general image editing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on a third-party CLI with inconsistent install provenance.

Mitigation: Review the dLazy CLI source and npm package version before use, and prefer npx or an isolated install instead of a global install.

Risk: The CLI stores credentials for dLazy services.

Mitigation: Use the device-code login flow where possible and avoid passing API keys directly on the command line.

Risk: Local media supplied to the CLI may be uploaded to dLazy-hosted services.

Mitigation: Only provide prompts and media files that are appropriate to share with the third-party service.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-social-media)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, image-generation prompts, caption copy, and generated result URLs when commands are executed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use a third-party CLI to send prompts and uploaded media to dLazy-hosted services.]

## Skill Version(s):

1.3.17 (source: server release evidence; artifact frontmatter says 1.3.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
