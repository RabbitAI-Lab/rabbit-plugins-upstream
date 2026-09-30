## Description:

Turns product selling points into a storyboard, generates individual shots, and assembles a subtitled short video ad.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketers and creators use this skill to plan and produce short, multi-shot product ads with captions for social and ecommerce campaigns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, prompts, and campaign details may be sent to a cloud generation provider.

Mitigation: Select an approved provider and avoid confidential unreleased assets unless its data handling is acceptable.

Risk: Generation requests may incur provider charges.

Mitigation: Confirm the storyboard and run the dry-run preview before generating clips.

## Reference(s):

- [ClawHub product-video-ad release](https://clawhub.ai/dlazyai/skills/product-video-ad)
- [Video backend configuration](artifact/references/video-backends.md)
- [Provider setup and data flow](artifact/references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Markdown, Configuration, Shell commands, Video files, Subtitle files]

**Output Format:** [Storyboard text and JSON shot plan; MP4 clips and assembled video with SRT captions when run.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Offers a dry-run preview; video assembly and subtitle embedding require ffmpeg.]

## Skill Version(s):

1.0.12 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
