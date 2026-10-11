## Description:

Creates short product ads from selling points by planning shots, generating video clips, and assembling subtitles and a final video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams and creators use this skill to turn product selling points into a reviewed multi-shot storyboard and a short video ad with captions for campaigns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference images may be sent to an external AI provider.

Mitigation: Use the dry-run first and share sensitive or proprietary media only when the selected provider is acceptable for that data.

Risk: Example brand demographics may not match the intended campaign audience.

Mitigation: Edit the example brand settings to reflect the actual campaign requirements before generating clips.

Risk: Generated clips can differ in product appearance or require editing before publication.

Mitigation: Review the storyboard and finished ad, reuse a consistent product reference image, and rerun individual shots as needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/product-video-ad)
- [Video backend configuration](references/video-backends.md)
- [Provider and data-flow reference](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown storyboard and JSON shot plan with generation commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Execution can save individual MP4 clips, a final MP4 ad, and SRT subtitles; ffmpeg is needed for assembly.]

## Skill Version(s):

1.0.16 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
