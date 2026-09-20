## Description:

Use when assembling or polishing already-rendered clips with ffmpeg: concat, crossfades, burned captions and subtitles, text/logo overlays, before/after sliders, background music beds, platform export, or multi-layer HTML combination videos with Hyperframes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and media-production agents use this skill to assemble and polish existing video and audio assets into social reels, narrated showcases, comparison clips, captioned exports, and HyperFrames-based compositions. It is not for generating video or performing model-based video edits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local ffmpeg examples may overwrite existing output files when run with -y.

Mitigation: Check output filenames and paths before execution, and remove -y when an overwrite should require confirmation.

Risk: Install examples and optional HyperFrames usage depend on third-party sources.

Mitigation: Verify the PrunaAI and HyperFrames sources before installation, and prefer pinned package versions when available.

## Reference(s):

- [ClawHub video-editing skill page](https://clawhub.ai/pruna-ai/skills/video-editing)
- [Hyperframes](https://github.com/heygen-com/hyperframes)
- [Assembly and concat](references/assembly-concat.md)
- [Transitions (xfade)](references/transitions.md)
- [Captions and subtitles](references/captions.md)
- [Overlays (text and logo)](references/overlays.md)
- [Comparison sliders](references/comparison-sliders.md)
- [Background music (bed mix)](references/background-music.md)
- [Narrated showcase (multi-act)](references/narrated-showcase.md)
- [Combination videos (Hyperframes)](references/combination-hyperframes.md)
- [Social use-case reels - HyperFrames portrait](references/social-usecase-reel.md)
- [Motion composition craft (HTML / HyperFrames)](references/motion-composition-craft.md)
- [Export presets](references/export-presets.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands, ffmpeg recipes, HTML/CSS/JavaScript guidance, and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local media-processing commands that overwrite outputs when run with ffmpeg -y.]

## Skill Version(s):

1.0.13 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
