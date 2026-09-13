## Description:

Use when assembling or polishing already-rendered clips with ffmpeg -- concat, crossfades, burned captions and subtitles, text/logo overlays, before/after sliders, background music beds, platform export -- or when composing a multi-layer HTML combination video with Hyperframes; not for AI video generation, prompt craft, or model-based video edits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT

## Use Case:

Developers, creators, and media operators use this skill to assemble and polish finished local media into reels, showcases, comparisons, captioned videos, and platform-ready exports. It guides post-production workflows using local ffmpeg/ffprobe, optional caption alignment, and optional HyperFrames composition for designed multi-layer videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unattended or unpinned external installs can change the agent environment.

Mitigation: Review install commands before running them and prefer pinned versions or reviewed commits.

Risk: Broad full-suite installs can add more tooling than the task requires.

Mitigation: Avoid broad --full-depth or full-suite installs unless those companion skills are actually needed.

Risk: External render tools may run with access to the project environment.

Mitigation: Run render tooling in a project-limited environment without unnecessary secrets.

Risk: ffmpeg commands that include -y can overwrite existing media outputs.

Mitigation: Use new output filenames or remove -y when preserving prior media matters.

## Reference(s):

- [Assembly and concat](references/assembly-concat.md)
- [Transitions](references/transitions.md)
- [Captions and subtitles](references/captions.md)
- [Overlays](references/overlays.md)
- [Comparison sliders](references/comparison-sliders.md)
- [Background music](references/background-music.md)
- [Narrated showcase](references/narrated-showcase.md)
- [Combination videos](references/combination-hyperframes.md)
- [Social use-case reels](references/social-usecase-reel.md)
- [Motion composition craft](references/motion-composition-craft.md)
- [Export presets](references/export-presets.md)
- [HyperFrames](https://github.com/heygen-com/hyperframes)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with ffmpeg, ffprobe, ASS subtitle, HTML, JSON, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose local media workflows, install commands, project layouts, render checks, and post-production validation steps.]

## Skill Version(s):

1.0.12 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
