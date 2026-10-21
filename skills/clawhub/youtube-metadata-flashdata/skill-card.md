## Description:

Helps agents retrieve YouTube video details through FlashData to build video cards, chapter links, and format summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rocosen](https://clawhub.ai/user/rocosen)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can inspect a known YouTube video to summarize its title, channel, duration, available statistics and formats, or create chapter navigation links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video IDs and query options are sent to FlashData.

Mitigation: Use the service only for videos the user has authorized and is comfortable sharing with FlashData.

Risk: Metadata queries consume paid FlashData Credits, including submissions that time out.

Mitigation: Check pricing and the approved budget before querying; after a timeout, check the existing job or Jobs rather than automatically resubmitting.

Risk: Exposing the FlashData API key can allow unauthorized use.

Mitigation: Keep the key in protected environment or secret settings, never in chat or committed files.

## Reference(s):

- [FlashData YouTube metadata documentation](https://flashdata.dev/docs/sources/youtube_metadata?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_metadata-task)
- [FlashData pricing](https://flashdata.dev/pricing)
- [ClawHub skill listing](https://clawhub.ai/rocosen/skills/youtube-metadata-flashdata)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with structured video details and optional timestamp links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chapters, statistics, and formats depend on availability; the skill does not download media or return caption text.]

## Skill Version(s):

1.0.1 (source: frontmatter, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
