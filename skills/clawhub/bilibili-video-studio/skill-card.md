## Description:

解析 Bilibili 视频并将其整理为文字稿、分析报告、脚本、提示词、课件内容或备考笔记。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, learners, and video analysts use this skill to turn a Bilibili video URL and a request into transcripts, summaries, script analyses, new scripts, prompts, slide notes, or study notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions ask users to paste a complete API key into chat.

Mitigation: Use a local secret-entry or credential method where available; rotate any key that was exposed in chat.

Risk: Video URLs are sent to a remote service for processing.

Mitigation: Avoid submitting sensitive or private video links unless remote processing is acceptable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/panting09266-ai/skills/bilibili-video-studio)
- [Cue Omni Reader online service](https://cuecue.cn/hub/omni-reader)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown reports and notes, with structured JSON when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include tables, timestamps, transcripts, and extracted slide images when source material supports them.]

## Skill Version(s):

1.1.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
