## Description:

Helps agents plan and generate multi-platform social-media visuals with platform-specific specs, safe-area checks, layered in-image text, captions, and dLazy CLI image-generation commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and content teams use this skill to plan, adapt, and generate social-media images, carousels, thumbnails, and captions for platforms such as Instagram, TikTok, YouTube, LinkedIn, and Xiaohongshu.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media can be sent to dLazy cloud services during image generation.

Mitigation: Use the skill only with content approved for that service, and avoid sending confidential or regulated media unless your organization permits it.

Risk: The dLazy CLI may save an API key in the local user configuration.

Mitigation: Prefer per-session environment variables when persistent storage is not desired, and rotate or revoke the key from the dLazy dashboard when needed.

Risk: The skill relies on a third-party CLI and cloud service.

Mitigation: Review the pinned npm package or source before installation, and use npx when you do not want a global CLI install.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-image-social-media)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with design plans, platform checks, caption copy, inline shell commands, and generated image URLs when commands are executed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require npm or npx, a dLazy API key, and access to dLazy cloud services for image generation.]

## Skill Version(s):

1.3.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
