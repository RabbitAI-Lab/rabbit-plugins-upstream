## Description:

Searches Google Videos through FlashData to find video pages across websites and return titles, links, sources, and available durations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rocosen](https://clawhub.ai/user/rocosen)

### License/Terms of Use:

MIT-0

## Use Case:

People using an agent can discover tutorials, talks, and demonstrations across video websites and compare source pages before choosing what to watch.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries and locale settings are sent to FlashData and its providers.

Mitigation: Avoid sensitive queries and review data-sharing requirements before use.

Risk: Data queries consume paid FlashData Credits.

Mitigation: Check pricing and approve a query budget before submitting requests; do not automatically repeat timed-out submissions.

Risk: The runtime package is fetched from npm, and a FlashData API key is required.

Mitigation: Review the pinned package and keep the API key in protected settings, never in prompts or files.

## Reference(s):

- [FlashData Google Videos documentation](https://flashdata.dev/docs/sources/google_videos?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_videos-task)
- [FlashData Google Video Search package](https://www.npmjs.com/package/@flashdata-dev/google-video-search)
- [Query parameter schema](references/schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown listing video titles, source websites, links, and available durations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Links point to video pages; media files and transcripts are not provided.]

## Skill Version(s):

1.0.0 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
