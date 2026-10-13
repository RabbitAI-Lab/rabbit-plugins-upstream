## Description:

Plans and generates platform-specific social-media visuals, in-image copy, and captions for Instagram, TikTok, YouTube, LinkedIn, and Xiaohongshu.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and marketing teams use this skill to plan and generate social-media images, thumbnails, and carousels with platform-specific layouts, safe areas, headlines, and captions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files may be sent to dLazy, which hosts generated results.

Mitigation: Use only content approved for upload to the dLazy cloud service.

Risk: The API key may be stored in a local CLI configuration file.

Mitigation: Use the DLAZY_API_KEY environment variable to avoid persistent storage, or protect and rotate the local key.

Risk: Global installation of an external CLI introduces package supply-chain exposure.

Mitigation: Review the CLI source and package before installation, or use the versioned npx option.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-image-social-media)
- [dLazy CLI source (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands, Image links]

**Output Format:** [Markdown with design plans, copy, CLI commands, and generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes platform specifications, safe-area checks, and iteration suggestions; generated images are hosted by dLazy.]

## Skill Version(s):

1.3.29 (source: ClawHub release metadata; bundled skill frontmatter says 1.3.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
