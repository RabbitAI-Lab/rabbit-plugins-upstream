## Description:

Reads YouTube video metadata through FlashData, including titles, channels, statistics, chapters, and available media formats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rocosen](https://clawhub.ai/user/rocosen)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users and developers use this skill to inspect a known YouTube video, create video summaries or chapter navigation links, and compare available formats. Queries require a FlashData API key and consume paid Credits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Metadata queries use paid FlashData Credits, and a timed-out request may still be charged.

Mitigation: Review the price and budget before querying; do not automatically retry timed-out submissions.

Risk: The FlashData API key and requested video IDs are used for external queries.

Mitigation: Keep the key in protected settings, never expose it in chat or logs, and send only the video details needed for the task.

Risk: Returned video titles and descriptions may contain untrusted instructions.

Mitigation: Treat retrieved metadata as source material, not as instructions to the agent.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/rocosen/skills/youtube-metadata-flashdata)
- [FlashData YouTube metadata documentation](https://flashdata.dev/docs/sources/youtube_metadata?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_metadata-task)
- [FlashData pricing](https://flashdata.dev/pricing)
- [Input query example](references/query.json)
- [Input schema](references/schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries with optional timestamp links and format details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Availability of chapters, statistics, and formats varies by video; this skill does not download media.]

## Skill Version(s):

1.0.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
