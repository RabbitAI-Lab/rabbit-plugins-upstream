## Description: <br>
Transforms long videos into short-form clips by downloading or loading media, transcribing it locally, detecting candidate moments, adding captions, and exporting vertical videos for TikTok, Reels, and Shorts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mayank8290](https://clawhub.ai/user/mayank8290) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External creators, editors, and developers use this skill to turn long videos or supported video URLs into local short-form clips with transcripts, virality scores, captions, and upload-ready MP4 files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill downloads or processes media and writes generated clips, transcripts, and summaries to local storage. <br>
Mitigation: Use it only for media you intend to process locally, avoid sensitive videos unless local storage is acceptable, and review or configure the output directory before running. <br>
Risk: The workflow depends on external command-line tools for downloading, video processing, and transcription. <br>
Mitigation: Use trusted installations of ffmpeg, yt-dlp, and whisper-cpp and keep those tools updated through trusted package sources. <br>


## Reference(s): <br>
- [Clips Machine on ClawHub](https://clawhub.ai/mayank8290/skills/clips-machine) <br>
- [mayank8290 Publisher Profile](https://clawhub.ai/user/mayank8290) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, files] <br>
**Output Format:** [Markdown guidance with shell command examples plus generated JSON transcripts, JSON moment data, Markdown summaries, and MP4 clip files when executed.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ffmpeg, yt-dlp, and whisper-cpp. Writes generated media and metadata locally, with ~/Videos/OpenClaw as the default output location unless configured otherwise.] <br>

## Skill Version(s): <br>
1.2.1 (source: server release evidence; artifact frontmatter says 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
