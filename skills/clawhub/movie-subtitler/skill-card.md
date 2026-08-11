## Description: <br>
Download a foreign-language movie or video, or use a local file, transcribe and translate it to English with WhisperX, and recreate the video with English subtitles through a local yt-dlp, WhisperX, and ffmpeg workflow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nelsonscott](https://clawhub.ai/user/nelsonscott) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and end users use this skill to generate English subtitle sidecars and subtitled MP4 files from local or downloadable foreign-language videos while keeping processing local. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow runs ffmpeg, yt-dlp, and WhisperX locally on user-provided media. <br>
Mitigation: Install dependencies from trusted sources and run the skill only in an environment where local media processing is acceptable. <br>
Risk: Video and audio processing can create large temporary files that may contain private media content. <br>
Mitigation: Use a suitable work directory for sensitive media and remove the work directory after processing. <br>
Risk: Users may process media they are not authorized to download, transcribe, or translate. <br>
Mitigation: Use the skill only with media the user is allowed to process. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nelsonscott/skills/movie-subtitler) <br>
- [Project homepage](https://github.com/NelsonScott/movie-subtitler) <br>
- [WhisperX](https://github.com/m-bain/whisperX) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance, Files] <br>
**Output Format:** [Markdown guidance with bash commands; generated MP4 and SRT files when executed] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires local ffmpeg, WhisperX, and yt-dlp for URL inputs; media processing can be long-running and may create large temporary files.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
