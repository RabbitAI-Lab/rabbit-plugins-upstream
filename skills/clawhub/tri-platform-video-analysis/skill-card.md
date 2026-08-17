## Description:

Tri Platform Video Analysis helps agents process a user-provided Douyin, Bilibili, or Xiaohongshu video link into local transcripts, structured analysis, and an interactive HTML report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhouq2039-lang](https://clawhub.ai/user/zhouq2039-lang)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to turn one explicitly provided tri-platform video link into local transcript files, AI-authored analysis JSON, and a browser-viewable HTML report. It is suited for content review, summarization, and structure analysis of videos the user has rights to process.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow downloads third-party videos and may download a Whisper model, and it can use platform cookies supplied by the user.

Mitigation: Process only user-provided links after confirmation, prefer public or non-sensitive videos, and keep any cookies scoped to the target platform.

Risk: Transcript, analysis JSON, and HTML report files may contain personal or sensitive information from the source video.

Mitigation: Keep the output directory under the user's control, avoid sensitive or copyrighted videos unless authorized, and delete local outputs when they are no longer needed.

Risk: Generated HTML can reflect untrusted analysis content.

Mitigation: Review generated HTML before opening or sharing reports from untrusted video content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhouq2039-lang/skills/tri-platform-video-analysis)
- [Douyin report preview](https://8eb04cd68f594e89a6515cb53567c5a1.sh5.agentos-app.net/douyin.png)
- [Bilibili report preview](https://8eb04cd68f594e89a6515cb53567c5a1.sh5.agentos-app.net/bilibili.png)
- [Xiaohongshu report preview](https://8eb04cd68f594e89a6515cb53567c5a1.sh5.agentos-app.net/xiaohongshu.png)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with shell commands and JSON schemas; runtime output includes transcript text files, analysis JSON, and an HTML report.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The generated report is written locally, and stdout returns JSON status objects with output paths.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
