## Description:

视频翻译 · 逐字稿翻译 / Video transcript translate: read a video link and return its spoken transcript with timestamps plus a full translation — 抖音、小红书、B站 videos into English (出海 research, subtitles, sharing with a foreign team), or YouTube、TikTok、X videos into Chinese. On-screen text is read too. Use when someone wants to know exactly what a foreign-language video says, needs a translated transcript to subtitle or quote, or is studying overseas competitors' videos. No login or cookies; needs an API key for the translation (+1 credit).

This skill is ready for commercial/non-commercial use.

## Publisher:

[jackchew7143](https://clawhub.ai/user/jackchew7143)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, researchers, and multilingual teams can use this skill to turn supported video links into timestamped transcripts and translations, including text read from video frames. It is useful for understanding foreign-language videos, preparing quotes or subtitle drafts, and reviewing overseas content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Full transcript and translation requests use LinkDigest credits, and optional analysis features can add cost.

Mitigation: Review the requested options and expected credits before running; use --max-credits to cap a request.

Risk: Video content is sent to LinkDigest for remote processing, whose handling cannot be verified from this client.

Mitigation: Review the provider's current privacy terms and submit only videos you are authorized to share.

## Reference(s):

- [LinkDigest documentation](https://linkdigest.dev/zh/docs?ref=skill-video-transcript-translate)
- [LinkDigest API key setup](https://linkdigest.dev/signin?ref=skill-video-transcript-translate&next=/app/keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Timestamped transcript with its translation, in Markdown or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Keeps the original transcript alongside the translation; timestamps are per segment. Translations of transcripts longer than 24,000 characters may cover only the beginning.]

## Skill Version(s):

1.0.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
