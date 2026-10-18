## Description:

Search Google through FlashData for structured results with titles, URLs, snippets, and positions to support web research and localized searches.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rocosen](https://clawhub.ai/user/rocosen)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and researchers use this skill to find web sources, site-specific results, and documents, then summarize results with source links for an agent answer.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries and locale settings are sent to FlashData and its upstream providers.

Mitigation: Avoid submitting secrets or private information unless that disclosure is acceptable.

Risk: The skill requires a FlashData API key and queries consume paid credits.

Mitigation: Keep the key in protected environment settings, approve a query budget, and monitor credit use.

Risk: Search snippets may be misleading or contain untrusted instructions.

Mitigation: Treat results as source data, verify claims against linked pages, and do not follow instructions in retrieved text.

## Reference(s):

- [FlashData Google Search documentation](https://flashdata.dev/docs/sources/google_search?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_search-task)
- [Search input schema](references/schema.json)
- [Example search query](references/query.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [JSON search results or Markdown summaries with source URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include titles, URLs, snippets, and positions; snippets are not full-page reads. Queries consume paid FlashData Credits.]

## Skill Version(s):

1.0.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
