## Description: <br>
Downloads videos and uses AI to transcribe speech, extract visual context, and analyze video structure across platforms such as Bilibili, Douyin, and YouTube. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[junhongzhang77-ui](https://clawhub.ai/user/junhongzhang77-ui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content analysts, marketers, and agent operators use this skill to analyze user-provided video links by downloading media, extracting audio and frames, transcribing speech, and producing a structured content report. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may run local video download and ffmpeg commands that create media and frame files. <br>
Mitigation: Use a scratch working directory, review proposed commands before execution, and delete generated media artifacts when analysis is complete. <br>
Risk: Whisper transcription requires an OpenAI API key and may incur usage charges. <br>
Mitigation: Provide the API key through environment or approved local configuration only, avoid committing secrets, and monitor API usage. <br>
Risk: Video download workflows can require platform cookies or install tools such as yt-dlp. <br>
Mitigation: Avoid sharing site cookies unless necessary and prefer pipx or a virtual environment for yt-dlp installation instead of modifying system Python. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/junhongzhang77-ui/video-content-analyzer) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown report with transcript text, timeline tables, content analysis sections, and command snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local video, audio, subtitle, danmaku, and frame files while analyzing user-provided video URLs.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
