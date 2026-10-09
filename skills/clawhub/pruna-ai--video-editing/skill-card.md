## Description:

Guides local post-production of finished media with ffmpeg or optional Hyperframes compositions, including assembly, captions, overlays, audio mixing, and export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, editors, and developers use this skill to assemble and polish existing clips, stills, narration, and music for social or presentation videos. It provides local editing workflows rather than AI video generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing suggested skills may add more third-party content than intended.

Mitigation: Review the npx install commands and avoid full-suite installs unless the source is trusted.

Risk: Some ffmpeg examples can overwrite an existing output file.

Mitigation: Choose a fresh output filename or remove -y before running the command.

## Reference(s):

- [Video Editing on ClawHub](https://clawhub.ai/pruna-ai/skills/video-editing)
- [Assembly and concat](artifact/references/assembly-concat.md)
- [Captions and subtitles](artifact/references/captions.md)
- [Export presets](artifact/references/export-presets.md)
- [Hyperframes project](https://github.com/heygen-com/hyperframes)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code]

**Output Format:** [Markdown with ffmpeg commands and optional HTML composition examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Rendered media requires source assets and execution of the suggested workflow.]

## Skill Version(s):

1.0.14 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
