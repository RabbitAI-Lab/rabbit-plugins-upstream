## Description:

YouTube 视频总结和字幕提取，带时间戳，可直接译成中文。用户发来 YouTube 链接（youtube.com、youtu.be、Shorts），要中文总结、要点、逐字稿、字幕、画面上的文字，或者想不看视频先知道讲了什么时使用。没有字幕的视频也能读：由模型直接看视频，口播和画面文字一起出。不需要梯子抓字幕、不需要 yt-dlp、不需要 Cookie。通过 LinkDigest API 读取，需要 LINKDIGEST_API_KEY，按分钟计费，注册送 10 积分。

This skill is ready for commercial/non-commercial use.

## Publisher:

[jackchew7143](https://clawhub.ai/user/jackchew7143)

### License/Terms of Use:

MIT-0

## Use Case:

People who share YouTube links can use this skill to get timestamped summaries, transcripts, on-screen text, and optional translations without retrieving captions themselves.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is benign with medium confidence but partial because one reference was unresolved.

Mitigation: Review the unresolved reference and confirm the reported environment and network access fit your needs before installing.

Risk: The skill sends the supplied video link to LinkDigest and requests can incur usage charges.

Mitigation: Only submit links you are comfortable sharing with LinkDigest, and use --max-credits to cap per-video spend.

## Reference(s):

- [LinkDigest documentation](https://linkdigest.dev/zh/docs?ref=skill-linkdigest-youtube-summary)
- [LinkDigest Digest API](https://linkdigest.dev/api/v1/digest)
- [ClawHub release](https://clawhub.ai/jackchew7143/skills/linkdigest-youtube-summary)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Markdown or JSON, including timestamped transcript, key points, and on-screen text when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include translated output; usage is billed in LinkDigest credits based on video duration.]

## Skill Version(s):

1.2.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
