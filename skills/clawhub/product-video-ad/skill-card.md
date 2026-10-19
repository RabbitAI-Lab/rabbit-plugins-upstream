## Description:

Turns product selling points into a shot-by-shot storyboard, generates video clips, and assembles a subtitled product ad.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants and marketing teams use this skill to turn product selling points into short, multi-shot video ads with captions for promotional campaigns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Storyboard prompts and reference product images may be sent to a selected generation provider.

Mitigation: Use only images approved for external processing; avoid sensitive or private images.

Risk: Video generation may incur charges or produce unsuitable shots.

Mitigation: Review the storyboard and run a dry-run before approving paid generation.

Risk: The example brand persona may not match a specific advertiser.

Mitigation: Adapt brand settings to the actual product and campaign before generating clips.

## Reference(s):

- [Product Video Ad on ClawHub](https://clawhub.ai/dlazyai/skills/product-video-ad)
- [Video backend configuration](references/video-backends.md)
- [Provider CLI reference](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Guidance, JSON, Shell commands, Files]

**Output Format:** [Storyboard text and JSON; MP4 clips and assembled video, with SRT captions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Subtitled video when supported; no voice-over or music generation.]

## Skill Version(s):

1.0.20 (source: frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
