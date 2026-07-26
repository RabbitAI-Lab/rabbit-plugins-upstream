## Description: <br>
Video Analyzer locally decomposes videos into transcripts, scene and OCR analysis, multimodal timelines, timestamped highlights, and HTML/JSON/Markdown reports with multi-engine ASR and Chinese-language enhancements. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fyniujin](https://clawhub.ai/user/fyniujin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content analysts use this skill to process local or downloadable video into structured reports, transcripts, scene summaries, timestamped highlights, and chapter assets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill presents itself as local/offline but can perform update checks, first-run model downloads, and remote video downloads. <br>
Mitigation: For sensitive or air-gapped use, preinstall required models, use local video files, and run with --no-update-check. <br>
Risk: Remote media download behavior and media parsing can expose users to untrusted URLs or attacker-supplied video files. <br>
Mitigation: Avoid untrusted URLs, process only trusted media when possible, and run the tool in an isolated environment for untrusted inputs. <br>
Risk: External media tooling and Python dependencies affect the security of video processing. <br>
Mitigation: Pin and update dependencies, and configure trusted ffmpeg and ffprobe paths before processing sensitive files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/video-analyzer) <br>
- [Skill instructions](artifact/SKILL.md) <br>
- [README](artifact/README.md) <br>
- [Configuration reference](artifact/config.yaml) <br>


## Skill Output: <br>
**Output Type(s):** [files, markdown, JSON, HTML, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with shell commands; generated analysis artifacts may include HTML, JSON, Markdown, SRT/VTT, images, and video clips.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are written to a local output directory; optional features can generate chapter clips, subtitles, timeline assets, and cached model/media files.] <br>

## Skill Version(s): <br>
3.5.0 (source: frontmatter, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
