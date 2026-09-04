## Description:

Use when assembling or polishing already-rendered clips with ffmpeg - concat, crossfades, burned captions and subtitles, text/logo overlays, before/after sliders, background music beds, platform export - or when composing a multi-layer HTML combination video with Hyperframes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and production teams use this skill to assemble and polish finished video assets with local ffmpeg workflows, including joins, transitions, captions, overlays, comparison layouts, music beds, and social export presets. It also guides optional Hyperframes composition when the deliverable needs designed multi-layer frames before post-render polish.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: npx-based installation can execute package code from a moving dependency or remote source.

Mitigation: Pin or verify the installer and package version before installing the skill in a production agent environment.

Risk: Several ffmpeg examples use forced overwrite behavior and may replace existing media files if paths are reused.

Mitigation: Write renders to unique output filenames or temporary directories, then promote reviewed outputs to final paths.

Risk: Caption alignment may require sending audio to whisperx or related API helpers.

Mitigation: Only upload media when the user is comfortable sharing that audio with the selected alignment service.

## Reference(s):

- [Assembly and concat](references/assembly-concat.md)
- [Transitions](references/transitions.md)
- [Captions and subtitles](references/captions.md)
- [Overlays](references/overlays.md)
- [Comparison sliders](references/comparison-sliders.md)
- [Background music](references/background-music.md)
- [Narrated showcase](references/narrated-showcase.md)
- [Combination videos with Hyperframes](references/combination-hyperframes.md)
- [Social use-case reels](references/social-usecase-reel.md)
- [Motion composition craft](references/motion-composition-craft.md)
- [Export presets](references/export-presets.md)
- [Hyperframes](https://github.com/heygen-com/hyperframes)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with ffmpeg, ffprobe, shell command, HTML, CSS, ASS, SRT, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are procedural guidance and command/code snippets for local media processing; the skill does not itself generate video content.]

## Skill Version(s):

1.0.11 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
