## Description:

Get YouTube channel information and recent videos with FlashData. Use for channel research, listing uploads, exporting video data or comparing channels, starting from a channel handle. Requires a FlashData API key and paid Credits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rocosen](https://clawhub.ai/user/rocosen)

### License/Terms of Use:

MIT-0

## Use Case:

Channel researchers and analysts can retrieve a YouTube channel profile and a bounded list of recent videos for research, exports, or comparisons.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries connect to hosted FlashData and use paid Credits.

Mitigation: Keep the API key in protected secret configuration and check the pricing or Credits balance before running queries.

## Reference(s):

- [FlashData YouTube Channel documentation](https://flashdata.dev/docs/sources/youtube_channel?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_channel-task)
- [FlashData pricing](https://flashdata.dev/pricing?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_channel-task)
- [FlashData API key signup](https://flashdata.dev/signup?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_channel-task)
- [ClawHub release page](https://clawhub.ai/rocosen/skills/youtube-channel-flashdata)

## Skill Output:

**Output Type(s):** [JSON, Text, CSV]

**Output Format:** [Structured channel and video data, with optional text summaries or CSV exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recent videos are bounded by the requested limit; unavailable counts remain blank, and results are not a full channel archive.]

## Skill Version(s):

1.0.2 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
