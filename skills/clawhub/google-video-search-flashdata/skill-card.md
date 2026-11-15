## Description:

Search Google Videos with FlashData for video pages across websites. Use for cross-platform video discovery, finding tutorials or talks, and collecting video titles, links, sources and duration labels. Requires a FlashData API key and paid Credits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rocosen](https://clawhub.ai/user/rocosen)

### License/Terms of Use:

MIT-0

## Use Case:

People using an AI agent can search for video pages across websites to discover tutorials, talks, demonstrations, and coverage, then review titles, source sites, links, and available duration labels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Data queries use paid FlashData Credits.

Mitigation: Confirm the available credit budget before submitting a query.

Risk: Search queries are sent to FlashData's hosted service.

Mitigation: Avoid including sensitive information unless sending it to FlashData is approved.

## Reference(s):

- [FlashData Google Videos documentation](https://flashdata.dev/docs/sources/google_videos?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_videos-task)
- [Query example](references/query.json)
- [Request schema](references/schema.json)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Video search results with titles, page links, source websites, and available duration labels; results can be summarized in text or returned as structured data.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Result count and available fields vary by query; results describe video pages and do not include the media or a transcript.]

## Skill Version(s):

1.0.2 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
