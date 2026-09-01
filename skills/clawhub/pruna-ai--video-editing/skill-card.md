## Description:

Use when assembling or polishing already-rendered clips with ffmpeg: concat, crossfades, burned captions and subtitles, text or logo overlays, before/after sliders, background music beds, platform export, or multi-layer HTML combination videos with HyperFrames.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and external users use this skill to guide local post-production on finished video/audio assets: joining clips, adding captions or overlays, mixing beds, composing narrated showcases, and exporting social formats.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional related skills for caption alignment, audio, or uploads may use paid APIs or send media outside the local environment.

Mitigation: Enable those add-ons only when the user explicitly needs missing audio, caption timing, or uploads, and review the related skill before use.

Risk: Video assembly commands can overwrite files or produce poor output when source resolution, frame rate, pixel format, or audio layout do not match.

Mitigation: Probe media with ffprobe, review inputs before concat, normalize mismatched streams, and write to explicit output paths.

Risk: Caption styling, bed volume, and export settings can reduce readability or speech clarity if applied without review.

Mitigation: Preview captions and audio levels, keep instrumental beds under speech, and run the documented export checks before final delivery.

## Reference(s):

- [Assembly and concat](references/assembly-concat.md)
- [Transitions](references/transitions.md)
- [Captions and subtitles](references/captions.md)
- [Overlays](references/overlays.md)
- [Comparison sliders](references/comparison-sliders.md)
- [Background music](references/background-music.md)
- [Narrated showcase](references/narrated-showcase.md)
- [Combination videos with HyperFrames](references/combination-hyperframes.md)
- [Social use-case reels](references/social-usecase-reel.md)
- [Motion composition craft](references/motion-composition-craft.md)
- [Export presets](references/export-presets.md)
- [HyperFrames](https://github.com/heygen-com/hyperframes)
- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/video-editing)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with ffmpeg and ffprobe commands, caption/export recipes, and optional HyperFrames project guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose local command sequences and file changes; optional alignment or media-generation add-ons are used only when explicitly needed.]

## Skill Version(s):

1.0.10 (source: evidence release, skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
