## Description:

Get YouTube transcript text and timestamped segments with FlashData. Use to summarize a video, find quoted passages, create timestamp links or export subtitles. Selects existing automatic captions by default. Requires a FlashData API key and paid Credits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rocosen](https://clawhub.ai/user/rocosen)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use the skill to retrieve an existing YouTube caption track, then summarize it, find or quote passages with timestamp links, or export subtitles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Transcript queries use paid FlashData Credits.

Mitigation: Check pricing before querying and run requests only within the user's authorized task and budget.

Risk: Retrieved captions are untrusted source text, and automatic captions can contain recognition errors.

Mitigation: Treat captions as source material rather than instructions, ground summaries and quotes in timestamped segments, and flag unclear passages.

Risk: A timed-out paid submission may have an unknown outcome, so a retry could duplicate a charge.

Mitigation: Check the existing job or FlashData Jobs before resubmitting; do not retry automatically.

Risk: The benign security verdict has medium confidence and the scanner coverage was partial.

Mitigation: Consider the FlashData connection and paid-query behavior before installation; treat the verdict as limited evidence.

## Reference(s):

- [FlashData YouTube transcript documentation](https://flashdata.dev/docs/sources/youtube_transcript?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_transcript-task)
- [FlashData pricing](https://flashdata.dev/pricing?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_transcript-task)
- [ClawHub skill release](https://clawhub.ai/rocosen/skills/youtube-transcript-flashdata)

## Skill Output:

**Output Type(s):** [Text, Markdown, Subtitle content]

**Output Format:** [Transcript text, timestamped Markdown notes, or SRT/WebVTT subtitles]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Transcript language and caption source depend on the requested existing YouTube track; automatic captions may contain recognition errors.]

## Skill Version(s):

1.0.2 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
