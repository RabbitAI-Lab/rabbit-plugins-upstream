## Description: <br>
Downloads videos from supported links and transcribes spoken content into timestamped text using local yt-dlp and OpenAI Whisper tooling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xunx33](https://clawhub.ai/user/xunx33) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content creators, editors, and agents can use this skill to turn online video speech into timestamped transcript segments and full copyable text for editing, review, or reuse. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A crafted prompt or environment path could be incorporated into generated local Python code during transcription. <br>
Mitigation: Use only trusted prompt text and trusted environment paths; prefer a fixed version that calls Whisper directly or passes inputs through safe structured arguments. <br>
Risk: Video and model downloads may write large files to local paths or apply a global yt-dlp configuration beyond this skill. <br>
Mitigation: Confirm where videos and model files will be stored, and avoid optional global yt-dlp configuration unless that broader behavior is intended. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, files] <br>
**Output Format:** [Plain text transcript with timestamped segments and a full-text section, plus a downloaded video file saved locally.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires local yt-dlp, ffmpeg, openai-whisper, and storage for downloaded videos and Whisper model files.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
