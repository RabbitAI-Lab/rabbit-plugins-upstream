## Description:

Search Google Places with FlashData for local businesses, addresses, ratings and review counts. Use for local business search, comparing places, or building a list of businesses in a chosen city. Requires a FlashData API key and paid Credits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rocosen](https://clawhub.ai/user/rocosen)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search for local businesses by category and location, then review returned names, addresses, ratings, and review counts to build a shortlist or comparison.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search requests and the API key are sent to FlashData’s hosted service; the supplied scan reports medium confidence and incomplete coverage.

Mitigation: Review the query data before use, decide whether the hosted service is appropriate for it, and store FLASHDATA_API_KEY in protected secret configuration.

Risk: Each data query spends paid FlashData Credits, and a timed-out submission may have an unknown outcome.

Mitigation: Check the existing job or FlashData Jobs before retrying a timed-out submission; do not resubmit automatically.

## Reference(s):

- [FlashData Google Places documentation](https://flashdata.dev/docs/sources/google_places?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_places-task)
- [FlashData pricing](https://flashdata.dev/pricing?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_places-task)
- [FlashData MCP endpoint](https://flashdata.dev/mcp?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_places-task)
- [Query example](artifact/references/query.json)
- [Query schema](artifact/references/schema.json)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Text, Markdown]

**Output Format:** [Structured place-search results, with optional text or Markdown shortlists and comparisons]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returned place count and available fields vary by query; missing ratings or review counts remain unknown.]

## Skill Version(s):

1.0.2 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
