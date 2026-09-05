## Description:

提取抖音播放页音频并通过自建服务转写字幕，随后总结内容、重点、观点或行动项。用户发送 douyin.com 链接、抖音分享文案，或要求总结、转写抖音视频时使用；不处理用户上传的本地视频文件。

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruidongyuan-dot](https://clawhub.ai/user/ruidongyuan-dot)

### License/Terms of Use:

MIT-0

## Use Case:

Users send a Douyin video link or shared Douyin text so an agent can extract the playable audio URL, call the disclosed transcription service, and return a concise summary, key points, notes, action items, or readable subtitles. The skill is intended for Douyin web videos and does not process locally uploaded video files or non-Douyin links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Douyin audio URLs, video metadata, and a service API key to calapi.ailuk.cn for transcription.

Mitigation: Use it only for videos and account credentials the user is comfortable sharing with that service; store the API key in a secure credential store when available.

Risk: The support service temporarily uploads audio as a public OSS object and passes it to Tencent Cloud before deletion.

Mitigation: Avoid private or sensitive videos unless the user trusts the service, its temporary storage behavior, and its billing page.

Risk: Transcripts may contain homophone or proper-noun errors that could affect conclusions.

Mitigation: Mark uncertain transcript-derived claims and do not introduce facts outside the subtitles.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ruidongyuan-dot/skills/douyin-video-summary)
- [Transcription service endpoint](https://calapi.ailuk.cn)
- [API key and billing page](https://payhtml.ailuk.cn)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with transcript-derived summaries, timestamped points, notes, action items, or subtitle text; helper script output is JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include video title, author, duration, charged amount, transcript, and SRT subtitles; signed audio URLs and full API keys should not be displayed.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
