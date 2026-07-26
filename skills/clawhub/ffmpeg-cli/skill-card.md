## Description: <br>
Comprehensive video/audio processing with FFmpeg for transcoding, cutting and merging clips, audio extraction, thumbnails, GIFs, speed changes, filters, subtitles, and watermarks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ascendswang](https://clawhub.ai/user/ascendswang) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, editors, and automation agents use this skill to run local FFmpeg workflows for common video and audio processing tasks such as converting formats, trimming media, merging clips, extracting audio, generating thumbnails or GIFs, changing playback speed, and adding watermarks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: FFmpeg scripts write local output files and use overwrite behavior for destinations. <br>
Mitigation: Use fresh output filenames, review paths before execution, and keep backups of source media. <br>
Risk: Merging media with file names or file lists from untrusted sources can create unsafe local file handling scenarios. <br>
Mitigation: Only pass trusted local media paths to merge.sh and review the generated merge inputs before execution when paths come from another source. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ascendswang/skills/ffmpeg-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and local file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a local ffmpeg binary and writes media outputs to user-selected paths.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
