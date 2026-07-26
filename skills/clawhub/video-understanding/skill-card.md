## Description: <br>
Analyzes video URLs and local video files with Google Gemini to produce transcripts, visual descriptions, summaries, and answers to user questions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bill492](https://clawhub.ai/user/bill492) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, support teams, and agent users use this skill to inspect user-provided video URLs or files, extract structured transcripts and visual summaries, and answer follow-up questions about video content. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Video content or video URLs may be sent to Google Gemini for analysis. <br>
Mitigation: Avoid confidential, regulated, private, or unlisted videos unless that processing is acceptable for the user's account and organization. <br>
Risk: Follow-up sessions can reuse Gemini File API handles or explicit CachedContent, which may retain processing state beyond a single question. <br>
Mitigation: Use the documented purge option after sensitive sessions, and avoid reuse or context-cache options when durable follow-up state is not appropriate. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bill492/skills/video-understanding) <br>
- [yt-dlp supported sites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands; script output is JSON by default or raw text when requested.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires GEMINI_API_KEY, yt-dlp, ffmpeg, and Python 3.10+ with uv; optional cache and download flags can retain reusable video handles or local files.] <br>

## Skill Version(s): <br>
1.3.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
