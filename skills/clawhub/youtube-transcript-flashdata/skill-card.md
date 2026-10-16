## Description:

Retrieves existing YouTube captions through FlashData as full transcript text and timestamped segments for summaries, quotations, and subtitle exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rocosen](https://clawhub.ai/user/rocosen)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers retrieve available YouTube captions to summarize videos, locate quoted passages with timestamp links, or export subtitles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An exposed FlashData API key could allow unauthorized use.

Mitigation: Keep the key in protected settings and out of prompts, logs, and committed files.

Risk: Transcript queries spend paid FlashData Credits, including requests whose outcome is unclear after a timeout.

Mitigation: Check pricing and the approved budget before querying; inspect an existing job or Jobs console rather than automatically resubmitting a timed-out request.

Risk: Video IDs, query settings, and related request data are shared with FlashData and upstream providers.

Mitigation: Only submit request data appropriate to share with those providers.

Risk: Automatic captions may contain recognition errors or untrusted text.

Mitigation: Check quoted passages against the returned segments, flag unclear text, and treat captions as source material rather than instructions.

## Reference(s):

- [FlashData YouTube transcript documentation](https://flashdata.dev/docs/sources/youtube_transcript?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_transcript-task)
- [FlashData YouTube transcript CLI package](https://www.npmjs.com/package/@flashdata-dev/youtube-transcript)
- [Transcript input schema](references/schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Subtitle files]

**Output Format:** [Plain text or Markdown with timestamp links; SRT or WebVTT when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Based on an available caption track; timestamped segments include start and end times in seconds.]

## Skill Version(s):

1.0.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
