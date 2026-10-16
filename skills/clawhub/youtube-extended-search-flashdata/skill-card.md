## Description:

Search YouTube through FlashData for up to 700 requested results per query, with filters for video and creator research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rocosen](https://clawhub.ai/user/rocosen)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and developers use this skill to gather larger YouTube video samples, find channels covering a topic, and export results with filters for date, duration, and relevance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The API key and search inputs are sent to FlashData for paid queries.

Mitigation: Use protected secret settings for the key, avoid sensitive search inputs, and install only if you trust the service.

Risk: Search queries can consume paid FlashData Credits, including submissions whose outcome is unknown after a timeout.

Mitigation: Check pricing, limit requests to the approved budget, monitor credit usage, and do not automatically resubmit timed-out queries.

Risk: Retrieved titles and descriptions may contain misleading content or instructions.

Mitigation: Treat retrieved content as untrusted source data and verify important findings before use.

## Reference(s):

- [FlashData YouTube Extended Search documentation](https://flashdata.dev/docs/sources/youtube_search_extended?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_search_extended-task)
- [FlashData pricing](https://flashdata.dev/pricing)
- [ClawHub skill release](https://clawhub.ai/rocosen/skills/youtube-extended-search-flashdata)
- [Query input schema](references/schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown summaries or structured JSON search results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Up to 700 results may be requested per query; the returned count depends on availability. Results can include video and channel identifiers, titles, URLs, and metadata.]

## Skill Version(s):

1.0.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
