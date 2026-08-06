## Description: <br>
Video Editing helps agents assemble and polish already-rendered clips with ffmpeg, captions, overlays, comparison layouts, background music, export presets, and optional Hyperframes compositions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, creators, and production agents use this skill to assemble finished MP4, MOV, or WebM media into polished reels with captions, overlays, music beds, transitions, and platform exports. It is for post-production on existing assets, not for generating or prompt-editing video. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated ffmpeg examples commonly include `-y`, which can overwrite existing output files. <br>
Mitigation: Review commands before execution, change output paths when preserving source or previous renders matters, or remove `-y` during manual runs. <br>
Risk: Caption alignment can drift or miss words when whisperx is run on a bed-heavy master or when narration starts later than the final timeline. <br>
Mitigation: Use isolated narration for alignment when available, keep narration aligned to t=0, and offset caption timestamps only when the composition intentionally delays voiceover. <br>
Risk: Optional external tools and companion skills may introduce paid API calls or additional install steps. <br>
Mitigation: Confirm ffmpeg and ffprobe locally first, and call whisperx, Hyperframes, Pruna API helpers, TTS, or music tools only when the requested deliverable needs them. <br>


## Reference(s): <br>
- [Assembly and concat](references/assembly-concat.md) <br>
- [Background music](references/background-music.md) <br>
- [Captions and subtitles](references/captions.md) <br>
- [Combination videos](references/combination-hyperframes.md) <br>
- [Comparison sliders](references/comparison-sliders.md) <br>
- [Export presets](references/export-presets.md) <br>
- [Motion composition craft](references/motion-composition-craft.md) <br>
- [Narrated showcase](references/narrated-showcase.md) <br>
- [Overlays](references/overlays.md) <br>
- [Social use-case reels](references/social-usecase-reel.md) <br>
- [Transitions](references/transitions.md) <br>
- [Hyperframes](https://github.com/heygen-com/hyperframes) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline code, shell commands, file recipes, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide local ffmpeg, ffprobe, ffmpeg-full, Hyperframes, and optional whisperx or companion-skill workflows; outputs should be reviewed before execution.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
