## Description:

A structured skill for planning and generating platform-optimized social media visuals, including layout direction, platform-safe composition checks, in-image text, captions, and iterative variants.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketers, creators, and developers use this skill to plan social media image concepts and generate platform-specific visuals through the dLazy CLI. It helps adapt content for Instagram, TikTok, YouTube, LinkedIn, Xiaohongshu, and carousel formats while keeping captions separate from rendered image text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs or runs a third-party CLI to access dLazy services.

Mitigation: Review the @dlazy/cli package or source before use and prefer npx when a persistent global install is not needed.

Risk: The dLazy CLI can store an API key in a local user configuration file.

Mitigation: Use DLAZY_API_KEY for per-run credentials when possible, and rotate or revoke keys from the dLazy dashboard if exposure is suspected.

Risk: Prompts and selected local media paths may be sent to dLazy APIs and uploaded to dLazy-hosted file storage.

Mitigation: Avoid submitting sensitive prompts or media unless the user intends those files to be processed by the dLazy cloud service.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-social-media)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown with structured sections and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include image-generation result URLs, platform-safe layout checks, in-image text, caption copy, and next-step suggestions.]

## Skill Version(s):

1.3.19 (source: server release metadata; artifact frontmatter says 1.3.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
