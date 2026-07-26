## Description: <br>
Downloads a Douyin video without a watermark, extracts MP3 audio, and guides the agent to use an ASR skill plus the OpenClaw LLM to produce a transcript-based summary and chapter structure. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhaobod1](https://clawhub.ai/user/zhaobod1) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to process a Douyin link into local video and audio files, then generate a transcript-grounded video summary with chapters. It is intended for clear Douyin video-summary requests where local cookie access and media processing are expected. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The downloader can read local browser cookies through yt-dlp and use them for Douyin network requests. <br>
Mitigation: Install and run the skill only when browser-cookie access is expected, and use it only with explicit Douyin links from trusted requests. <br>
Risk: The skill downloads third-party video content and creates local media artifacts. <br>
Mitigation: Use downloaded files for personal analysis workflows and avoid redistributing original videos unless the user has the required rights. <br>
Risk: The final summary depends on ASR output and may be inaccurate if transcription quality is poor. <br>
Mitigation: Ground the summary in the transcript and review the transcript before relying on the generated conclusions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/zhaobod1/skills/huo15-douyin-video-summary) <br>
- [Skill Homepage](https://cnb.cool/huo15/ai/huo15-skills) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, Markdown, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands, local file paths, transcript-derived summaries, and chapter notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local video.mp4 and audio.mp3 paths before downstream ASR transcription and LLM summarization.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
