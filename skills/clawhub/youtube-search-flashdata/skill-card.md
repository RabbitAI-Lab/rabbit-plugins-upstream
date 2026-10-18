## Description:

Searches YouTube with FlashData using keywords and filters to find videos, tutorials, and talks with video and channel details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rocosen](https://clawhub.ai/user/rocosen)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, developers, and other users can find and shortlist YouTube videos by topic, date, duration, subtitles, or popularity, then use video IDs and channel details to check the results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and video identifiers are sent to FlashData and its upstream providers.

Mitigation: Avoid sensitive queries and use the service only when its data handling is acceptable.

Risk: The integration requires a FlashData API key.

Mitigation: Keep the key in protected environment settings, out of prompts and logs.

Risk: Data queries spend paid FlashData Credits, and timed-out submissions may still be charged.

Mitigation: Check pricing and budget before searching, monitor usage, and check existing jobs rather than automatically retrying timed-out submissions.

Risk: Running the skill fetches a third-party npm package.

Mitigation: Review the pinned package before use in environments with strict dependency requirements.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/rocosen/skills/youtube-search-flashdata)
- [FlashData YouTube Search documentation](https://flashdata.dev/docs/sources/youtube_search?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_search-task)
- [Search request schema](references/schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [JSON search results or a Markdown video shortlist]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Standard searches return up to 20 results; available metadata varies, and subtitles filtering does not provide transcripts.]

## Skill Version(s):

1.0.0 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
