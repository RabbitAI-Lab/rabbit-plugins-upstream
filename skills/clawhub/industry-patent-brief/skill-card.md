## Description:

Creates a shareable industry patent brief covering filing trends, leading applicants, geographic and technical distribution, and representative patents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Business analysts and research teams use this skill to prepare a concise industry patent overview with sourced statistics and representative patents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent searches and identifiers are sent to an external paid API, which may expose confidential R&D or incur charges.

Mitigation: Do not submit unpublished or sensitive invention details without approval; confirm expected charges before running paid searches.

Risk: A trial API key is provisioned and stored locally if no key is supplied.

Mitigation: Set PATENTMAX_API_KEY and choose an approved cache location when credential persistence matters.

Risk: A configurable API destination may redirect queries or credentials to an unintended server.

Mitigation: Leave PATENTMAX_BASE_URL unset unless the destination is controlled and approved.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ip930/skills/industry-patent-brief)
- [PatentMax API reference](artifact/references/api-reference.md)
- [Patent search workflow](artifact/references/search-workflow.md)
- [Patent query syntax](artifact/references/query-syntax.md)

## Skill Output:

**Output Type(s):** [Markdown, CSV data, Text]

**Output Format:** [Markdown brief and UTF-8 CSV data table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes search terms, retrieval date, data source, and patent-publication lag caveat.]

## Skill Version(s):

1.0.0 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
