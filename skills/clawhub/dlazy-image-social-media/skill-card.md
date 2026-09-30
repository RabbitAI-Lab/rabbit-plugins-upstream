## Description:

Plans and generates platform-specific social media visuals and captions for Instagram, TikTok, YouTube, LinkedIn, and Xiaohongshu.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketing teams use this skill to plan, generate, and revise social media graphics, carousel content, thumbnails, and accompanying captions for specific platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media may be sent to dLazy's cloud service, and generated images are hosted there.

Mitigation: Avoid submitting sensitive prompts or local files unless cloud processing and hosting are intended.

Risk: The third-party CLI may store an API key locally and introduces package supply-chain exposure.

Mitigation: Review the CLI package before installation and protect or rotate locally stored API keys.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-image-social-media)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Image URLs]

**Output Format:** [Markdown with design plans, image links, and separate caption copy]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes platform specifications, safe-area checks, generation status, and iteration suggestions; generated image URLs are hosted by dLazy.]

## Skill Version(s):

1.3.24 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
