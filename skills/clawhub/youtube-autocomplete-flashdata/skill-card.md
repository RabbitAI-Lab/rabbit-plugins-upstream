## Description:

Retrieves YouTube autocomplete suggestions through FlashData to help users explore search phrases and compare languages or regions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rocosen](https://clawhub.ai/user/rocosen)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and researchers use this skill to gather YouTube search phrase ideas and compare autocomplete suggestions across languages and regions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries send the API key and search text to FlashData.

Mitigation: Store the API key in protected environment configuration and avoid sending sensitive query text.

Risk: Data requests spend paid FlashData Credits, and timed-out submissions may still be charged.

Mitigation: Approve a query budget, avoid automatic retries, and check existing jobs before resubmitting.

Risk: Default language and region may not match the intended audience.

Mitigation: Set language and region explicitly when locale matters.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/rocosen/skills/youtube-autocomplete-flashdata)
- [FlashData YouTube suggestions documentation](https://flashdata.dev/docs/sources/youtube_suggestions?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=youtube_suggestions-task)
- [Query example](references/query.json)
- [Query schema](references/schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [List of suggested search phrases, optionally grouped for comparison]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Include the query and locale; suggestions are not search-volume estimates.]

## Skill Version(s):

1.0.1 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
