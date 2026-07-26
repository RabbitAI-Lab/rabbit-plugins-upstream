## Description: <br>
从视频链接、字幕文件或浏览器可访问课程页面中提取已暴露字幕或 transcript，并生成带时间戳的 Markdown 学习笔记。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hejunhui-73](https://clawhub.ai/user/hejunhui-73) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to summarize videos, course pages, or local subtitle files into timestamped study notes when subtitles or transcripts are already available. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a logged-in browser session for course pages and may save extracted course or page data locally. <br>
Mitigation: Use it only where browser-based access and local saving are acceptable, treat generated JSON files as potentially private, and review them before sharing. <br>
Risk: The security review notes token inspection and broad authenticated page/API capture beyond a simple transcript workflow. <br>
Mitigation: Avoid accounts or courses where token inspection or broad page/API capture is not acceptable, and do not use the skill to collect or expose credentials. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/hejunhui-73/skills/video-subtitle-summary) <br>
- [Online Subtitle Strategy](references/online-subtitle-strategy.md) <br>
- [Playwright Browser Automation](references/playwright-browser-automation.md) <br>
- [Processing Policy](references/processing-policy.md) <br>
- [Report Format](references/report-format.md) <br>
- [Time Estimation](references/time-estimation.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown reports with timestamps; optional docx, PDF, HTML, and JSON extraction artifacts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Subtitle-only workflow; no audio transcription, audio extraction, playback capture, DRM bypass, or login bypass.] <br>

## Skill Version(s): <br>
1.3.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
