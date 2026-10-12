## Description:

Creates short product ads from selling points by planning shots, generating video clips, and assembling them with subtitles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketers use this skill to turn product selling points and reference images into a multi-shot video ad with timed captions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product prompts and reference images are sent to the selected generation provider.

Mitigation: Use only media you have rights to upload, and avoid private content unless provider sharing is acceptable.

Risk: Generated filenames may overwrite existing outputs.

Mitigation: Review the plan with --dry-run and generate into a dedicated output directory.

## Reference(s):

- [Product Video Ad skill listing](https://clawhub.ai/dlazyai/skills/product-video-ad)
- [Provider CLI reference](artifact/references/provider-cli.md)
- [Video backend reference](artifact/references/video-backends.md)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Shell commands, Video files, Subtitle files]

**Output Format:** [Storyboard guidance and JSON shot plans; generated MP4 clips, assembled video, and SRT subtitles]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video assembly and embedded subtitles depend on available ffmpeg capabilities.]

## Skill Version(s):

1.0.17 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
