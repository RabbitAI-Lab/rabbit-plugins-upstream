## Description:

Creates short product ads from selling points by planning shots, generating clips, assembling video, and adding subtitles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketers and creators use this skill to turn product selling points and reference images into a multi-shot, subtitled short-form video ad.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product prompts and reference images may be sent to the selected third-party generation provider.

Mitigation: Choose the provider deliberately and review what will be shared using a dry run before generation.

Risk: Generation uses provider API credentials.

Mitigation: Use scoped, rotatable API keys and avoid sharing credentials in prompts or storyboards.

Risk: Example brand or model settings may not match the campaign.

Mitigation: Replace example defaults and confirm the storyboard and reference images before generating the ad.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/product-video-ad)
- [Video backends](references/video-backends.md)
- [Provider CLI](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Video files, Subtitle files]

**Output Format:** [Storyboard JSON and text prompts; MP4 clips and assembled ad; SRT subtitles]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video assembly requires ffmpeg; subtitles can be burned in, embedded as a selectable track, or delivered as an SRT file.]

## Skill Version(s):

1.0.11 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
