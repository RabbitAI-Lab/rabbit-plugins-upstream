## Description:

Get the transcript of a YouTube video with timestamps through the okdata API, in the original or a chosen language, then summarise it, pull quotes with time links, or compare what several videos say. Use when the user shares a YouTube link and wants a summary, notes, key points, quotes, chapters or the full text, or wants to research what videos on a topic actually say. 视频转文字：取 YouTube 视频字幕（带时间戳），总结、摘录金句、按时间跳转，或对比多个视频的观点。

This skill is ready for commercial/non-commercial use.

## Publisher:

[conn-ho](https://clawhub.ai/user/conn-ho)

### License/Terms of Use:

MIT-0

## Use Case:

External users can share a video link to get its transcript and use timestamped summaries, notes, key points, quotes, or comparisons for research and review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented HTTP example targets Weibo trends even though the skill is presented as a video transcript tool.

Mitigation: Check that the endpoint matches the requested transcript operation before making a call.

Risk: Video identifiers or links are sent to an external API, and the skill requires an API key.

Mitigation: Confirm the API destination is trusted and needed, and keep OKDATA_API_KEY out of chat and logs.

## Reference(s):

- [okdata video transcript API](https://okdata.online/apis/youtube/videos/transcript/get/)
- [ClawHub skill release](https://clawhub.ai/conn-ho/skills/okdata-transcripts)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with timestamped source links, summaries, notes, and transcript quotes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Timestamps link back to video moments; long transcripts are handled in sections.]

## Skill Version(s):

0.1.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
