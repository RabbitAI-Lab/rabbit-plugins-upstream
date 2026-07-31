## Description: <br>
Video Analyzer is a local video-analysis CLI skill that creates transcripts, scene analysis, OCR, multimodal alignment, timestamped summaries, chapter slices, short-video platform analysis, editing suggestions, subtitles, EDL timelines, and HTML, JSON, and Markdown reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fyniujin](https://clawhub.ai/user/fyniujin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, editors, and content teams use this skill to analyze local or downloadable video into searchable transcripts, structured reports, chapter cuts, subtitles, and editing timelines. It is most useful for offline media review, short-video analysis, and preparation of material for manual editing workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is described as local and offline, but security evidence notes that it may contact GitHub, download from video sites, and fetch models or media. <br>
Mitigation: Prefer local video files, review allowed network access before use, and run with --no-update-check in offline or private environments. <br>
Risk: Processing untrusted media through ffmpeg, yt-dlp, or curl can expose the runtime to downloader and media-parser risk while also storing analyzed media, metadata, reports, and caches locally. <br>
Mitigation: Run the skill in a sandbox or disposable workspace, pin or update dependencies before handling untrusted media, avoid cookies or account-scoped URLs unless required, and treat generated outputs and caches as potentially sensitive. <br>
Risk: The artifact includes cleanup guidance involving rm -rf .cache/, which can delete data if copied or adapted without checking the current path. <br>
Mitigation: Verify the exact cache directory before deleting files, prefer an explicit --temp-dir for temporary data, and avoid broad recursive deletion commands in shared workspaces. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/video-analyzer) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/fyniujin) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration] <br>
**Output Format:** [HTML, JSON, Markdown, SRT, VTT, ASS, CMX3600 EDL, CSV, shell scripts, and media-derived asset files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include local media slices, cached intermediate files, platform metadata, subtitles, waveform or timeline assets, and editing suggestions.] <br>

## Skill Version(s): <br>
4.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
