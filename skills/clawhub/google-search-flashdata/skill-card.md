## Description:

Search Google with FlashData and return structured web results with titles, URLs, snippets and positions. Use for web research, SERP data, site-specific searches, document discovery and localized search results. Requires a FlashData API key and paid Credits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rocosen](https://clawhub.ai/user/rocosen)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agents use this skill to search Google for current web sources, site-specific pages, documents, and localized results. It returns structured result details that can support research and linked answers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries connect to FlashData and consume paid Credits.

Mitigation: Review FlashData pricing and decide whether an external search service and its query costs fit the task.

Risk: The security scan was partial, with two unresolved local path-like references.

Mitigation: Review the unresolved references and complete a full scan before relying on the assessment.

Risk: Retrieved titles, snippets, and other search content can contain untrusted instructions.

Mitigation: Treat retrieved content as source material rather than instructions, and keep API keys and credentials out of prompts and logs.

## Reference(s):

- [FlashData Google Search documentation](https://flashdata.dev/docs/sources/google_search?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_search-task)
- [FlashData pricing](https://flashdata.dev/pricing?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_search-task)
- [FlashData MCP service](https://flashdata.dev/mcp?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_search-task)
- [FlashData query schema](references/schema.json)
- [FlashData query example](references/query.json)

## Skill Output:

**Output Type(s):** [JSON, Text, Markdown]

**Output Format:** [Structured search results with titles, URLs, snippets, and positions; results may be summarized as linked text or Markdown.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Result counts vary by query. Search snippets are excerpts and do not represent full-page contents.]

## Skill Version(s):

1.0.2 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
