## Description: <br>
Use when assembling or polishing already-rendered clips with ffmpeg, including concat, crossfades, burned captions, overlays, comparison layouts, background music beds, platform exports, or multi-layer HyperFrames compositions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, creators, and agents use this skill to assemble finished local video assets into polished reels, showcases, captions, overlays, comparison clips, and social exports. It is for post-production on existing media, not AI video generation or prompt-driven video edits. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Caption alignment or generated audio workflows may involve paid external services and uploading media-derived audio. <br>
Mitigation: Use external captioning, TTS, or audio generation only when explicitly needed, and review what media or derived audio would be sent before running those steps. <br>
Risk: Optional HyperFrames or sibling skill installs expand the toolchain beyond local ffmpeg. <br>
Mitigation: Confirm the additional tools are required for the requested edit and review their installation and execution steps before use. <br>
Risk: Local video-editing commands may create, overwrite, or transform media files on disk. <br>
Mitigation: Confirm input and output paths before execution and keep original media separate from rendered outputs. <br>


## Reference(s): <br>
- [Assembly and concat](references/assembly-concat.md) <br>
- [Transitions (xfade)](references/transitions.md) <br>
- [Captions and subtitles](references/captions.md) <br>
- [Overlays (text and logo)](references/overlays.md) <br>
- [Comparison sliders](references/comparison-sliders.md) <br>
- [Background music (bed mix)](references/background-music.md) <br>
- [Narrated showcase (multi-act)](references/narrated-showcase.md) <br>
- [Combination videos (Hyperframes)](references/combination-hyperframes.md) <br>
- [Social use-case reels - HyperFrames portrait](references/social-usecase-reel.md) <br>
- [Motion composition craft (HTML / HyperFrames)](references/motion-composition-craft.md) <br>
- [Export presets](references/export-presets.md) <br>
- [Hyperframes](https://github.com/heygen-com/hyperframes) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Code, Guidance] <br>
**Output Format:** [Markdown with inline shell commands, ffmpeg filter examples, configuration notes, and optional HTML/HyperFrames guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local post-production instructions for existing media; generated commands may create or transform video, audio, caption, and subtitle files on disk.] <br>

## Skill Version(s): <br>
1.0.8 (source: evidence.release.version and SKILL.md metadata.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
