## Description:

A structured agent skill for planning and generating platform-specific social media visuals, including layouts, in-image text, captions, safe-area checks, and dLazy CLI image generation commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agent users use this skill to create social media images, thumbnails, carousel concepts, captions, and platform-specific design plans for Instagram, TikTok, YouTube, LinkedIn, Xiaohongshu, and related formats.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files may be sent to dLazy's cloud API for image generation.

Mitigation: Use the skill only when cloud processing by dLazy is acceptable, and avoid sending confidential prompts or media unless the user's data-handling requirements allow it.

Risk: Default login stores a dLazy API key in the local CLI configuration.

Mitigation: Use the DLAZY_API_KEY environment variable for per-command credentials when persistent local credential storage is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The workflow executes remote generation commands through the dLazy CLI.

Mitigation: Require user confirmation before each generation command and execute one synchronous command at a time, matching the artifact workflow and security summary.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-social-media)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with structured design plans, platform checks, copy blocks, prompts, and inline CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated image URLs returned by the dLazy service after user-confirmed CLI execution.]

## Skill Version(s):

1.3.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
