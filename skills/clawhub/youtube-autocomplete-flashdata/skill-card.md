## Description:

Get YouTube autocomplete suggestions with FlashData. Use for YouTube keyword research, discovering search phrases, expanding a topic or comparing suggestions across languages and regions. Requires a FlashData API key and paid Credits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rocosen](https://clawhub.ai/user/rocosen)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, creators, and marketers use the skill to discover YouTube search phrase ideas from a partial query and compare suggestions across languages and regions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends the API key and query arguments to FlashData's hosted endpoint.

Mitigation: Keep the key in protected secret settings and send only query details needed for the user's request.

Risk: Data queries spend FlashData Credits; regional comparisons require a separately billed request for each region.

Mitigation: Check pricing or request a quote, limit calls to the approved budget, and do not automatically resubmit a timed-out request.

Risk: The security review was partial because two referenced local paths were missing, so its evidence is incomplete.

Mitigation: Resolve the missing paths and complete the review before deployment.

## Reference(s):

- [FlashData YouTube Suggestions documentation](https://flashdata.dev/docs/sources/youtube_suggestions?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_suggestions-task)
- [FlashData API pricing](https://flashdata.dev/pricing?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_suggestions-task)
- [FlashData hosted MCP endpoint](https://data.flashdata.dev/mcp)
- [references/schema.json](references/schema.json)
- [references/query.json](references/query.json)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [A list of suggestion phrases or a Markdown keyword sheet, with the query and locale preserved]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Suggestions are not search-volume estimates or video results; each regional query is billed separately.]

## Skill Version(s):

1.0.2 (source: SKILL.md frontmatter; server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
