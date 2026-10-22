## Description:

Retrieves existing YouTube captions through FlashData as transcript text and timestamped segments for summaries, quotes, time links, and subtitle exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rocosen](https://clawhub.ai/user/rocosen)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents analyzing YouTube videos use this skill to retrieve existing caption tracks, summarize them with timestamp links, find quotations, or export subtitles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries send the selected video ID, caption options, and FlashData API key to FlashData.

Mitigation: Use a protected secret for the API key and submit only authorized video IDs and options.

Risk: Transcript queries spend paid FlashData Credits, and a timed-out request may already have been charged.

Mitigation: Set a budget, check pricing before querying, and check the existing job or console instead of automatically retrying.

Risk: Automatic captions may contain recognition errors that distort quotations or summaries.

Mitigation: Ground claims in returned segments and timestamps, and flag unclear text rather than inventing corrections.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/rocosen/skills/youtube-transcript-flashdata)
- [FlashData YouTube transcript documentation](https://flashdata.dev/docs/sources/youtube_transcript?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_transcript-task)
- [FlashData pricing](https://flashdata.dev/pricing)
- [Transcript query example](artifact/references/query.json)
- [Transcript query schema](artifact/references/schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code]

**Output Format:** [Plain text or Markdown with timestamps; JSON segments or SRT/WebVTT subtitles when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses existing captions only; language and automatic versus uploader-provided tracks must be available.]

## Skill Version(s):

1.0.1 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
