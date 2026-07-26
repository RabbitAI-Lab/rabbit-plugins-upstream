## Description: <br>
竖版视频生成免费版 helps personal content creators turn Markdown scripts into 9:16 vertical short videos with TTS narration, burned-in subtitles, and synchronized visuals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators and developers use this skill to generate a single vertical MP4 video from Markdown scene descriptions, narration text, subtitles, and optional prebuilt images. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated or suggested shell commands may install dependencies, run FFmpeg or Chrome, or invoke a custom TTS command. <br>
Mitigation: Review commands before execution and run them in a trusted workspace with expected media dependencies installed. <br>
Risk: Narration text may be sent to the configured TTS service, and the artifact states the default TTS may require network access. <br>
Mitigation: Use approved TTS providers, avoid sensitive text in scripts, or configure a local TTS command when privacy requirements apply. <br>
Risk: The skill is intended for media and video workflows and is not appropriate for copyrighted media processing. <br>
Mitigation: Use it only with content you have rights to process and keep generated media workflows scoped to the stated video-generation use case. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/lh-video-gen-tool-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown guidance with inline shell commands and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May result in local MP4, PNG, audio, subtitle, and temporary media files when the proposed commands are run.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
