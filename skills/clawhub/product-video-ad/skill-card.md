## Description:

Plans product ad storyboards, generates individual video shots, and assembles short ads with captions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants and marketers use this skill to turn product selling points into a multi-shot short video ad, with a reviewable storyboard, generated clips, and optional subtitles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, prompts, captions, and brand references may be sent to the selected generation provider.

Mitigation: Choose the provider intentionally, review its data terms, use a dry run first, and avoid confidential or unreleased assets unless permitted.

Risk: Generated shots can depict the product inconsistently or contain inaccurate promotional claims.

Mitigation: Reuse a consistent product reference image and brand profile, then review storyboard, claims, and final video before publication.

## Reference(s):

- [ClawHub product-video-ad release](https://clawhub.ai/dlazyai/skills/product-video-ad)
- [Video backend configuration](artifact/references/video-backends.md)
- [Provider CLI guidance](artifact/references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration guidance]

**Output Format:** [Storyboard JSON and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Execution can produce per-shot MP4 clips, a combined MP4 ad, and SRT subtitles; ffmpeg is needed for assembly.]

## Skill Version(s):

1.0.19 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
