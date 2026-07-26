## Description: <br>
Video Clip Assistant helps agents transcribe media, generate edit decision lists, render clips with FFmpeg, create subtitles, self-check outputs, and export videos for social platforms. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dwan25744](https://clawhub.ai/user/dwan25744) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, video editors, and content teams use this skill to turn long video or audio into transcripts, EDL JSON, rendered clips, subtitles, quality reports, and social-platform exports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local transcripts, EDL files, subtitles, and quality reports may contain sensitive media content. <br>
Mitigation: Avoid sensitive meetings or private videos unless local transcript and edit files are acceptable; use a dedicated output directory and remove generated files when no longer needed. <br>
Risk: User-selected output paths may overwrite existing files. <br>
Mitigation: Review all output paths before execution, keep backups of important media, and prefer a separate empty output directory for each run. <br>
Risk: Untrusted subtitle filenames or custom style files can affect subtitle rendering. <br>
Mitigation: Use trusted subtitle and style files only, inspect filenames and style JSON before rendering, and avoid processing files from untrusted sources. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/dwan25744/skills/video-clip-assistant) <br>
- [FFmpeg Command Reference](references/ffmpeg_cheatsheet.md) <br>
- [EDL JSON Schema](templates/edl_schema.json) <br>
- [Clip Strategy Presets](templates/clip_strategies.yaml) <br>
- [Subtitle Style Presets](templates/subtitle_styles.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands plus JSON EDL/transcript/quality files, SRT subtitles, and rendered video files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local media and metadata files; review output paths because existing files may be overwritten.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
