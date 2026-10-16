## Description:

Retrieves YouTube autocomplete suggestions through FlashData for keyword research and comparisons across languages and regions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rocosen](https://clawhub.ai/user/rocosen)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and researchers use this skill to discover YouTube search phrase ideas and compare autocomplete suggestions by language or region. It requires a FlashData API key and paid Credits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Query text and locale settings are sent to FlashData and its upstream data providers.

Mitigation: Submit only queries and settings you are comfortable sharing with those services.

Risk: Data queries use paid FlashData Credits; retrying a timed-out submission may incur another charge.

Mitigation: Check pricing and the approved budget before querying; inspect existing jobs rather than automatically resubmitting after a timeout.

Risk: An exposed FlashData API key could allow unauthorized use.

Mitigation: Keep FLASHDATA_API_KEY in protected secret configuration and scope it to the needed source.

Risk: The skill fetches a pinned npm package for its command-line integration.

Mitigation: Review the package and pinned version before use in stricter environments.

## Reference(s):

- [FlashData YouTube suggestions documentation](https://flashdata.dev/docs/sources/youtube_suggestions?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_suggestions-task)
- [FlashData pricing](https://flashdata.dev/pricing)
- [Example query](references/query.json)
- [Query input schema](references/schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown list of suggestion phrases with query and locale]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Suggestions are not search-volume estimates or video results.]

## Skill Version(s):

1.0.0 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
