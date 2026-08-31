## Description:

Guides an agent from product selling points to a storyboard, segmented video generation, assembly, and subtitles for short product advertising videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and commerce operators use this skill to plan and generate 15-30 second product ad videos from product selling points, reference images, captions, and brand guidance. Developers and agents can use its scripts to run dry runs, generate clips, create subtitles, and assemble final video files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, product images, and brand references may be sent to the selected cloud provider.

Mitigation: Use only trusted product assets, confirm the selected provider, and avoid sending sensitive or unreleased material unless that provider is approved for the data.

Risk: The skill can fetch user-supplied image URLs and forward their contents to cloud providers.

Mitigation: Prefer local files or trusted public HTTPS URLs; avoid localhost, private-network, and cloud-metadata URLs.

Risk: Video generation can incur provider cost and produce unsuitable storyboard or clip outputs.

Mitigation: Run dry-run first, review the storyboard and prompts, then generate or rerun individual shots only after confirmation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/product-video-ad)
- [Backend CLI reference](references/provider-cli.md)
- [Video backend configuration](references/video-backends.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files]

**Output Format:** [Markdown guidance with JSON/YAML examples and shell commands; generated artifacts can include MP4 clips, SRT subtitles, concat manifests, and final MP4 files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports storyboard dry runs before paid generation and ffmpeg-based subtitle/assembly fallback behavior.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
