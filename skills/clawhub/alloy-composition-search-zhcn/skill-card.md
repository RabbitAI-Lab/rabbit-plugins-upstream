## Description:

Generates structured alloy composition search responses by interpreting alloy queries, optionally retrieving and analyzing alloy, patent, or paper data through MCP tools, and presenting filtered composition tables with concise insights.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, engineers, and IP analysts use this skill to search, filter, classify, and summarize metal alloy compositions from user queries and available alloy or literature data. It is especially suited to Chinese-language alloy composition lookup workflows that need clear tables and source-aware technical observations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries may contain confidential alloy formulas, unpublished R&D details, or patent strategy that could be shared with the disclosed MCP service.

Mitigation: Confirm that mace-mcp use is approved for the deployment environment before submitting sensitive alloy queries or derived composition parameters.

Risk: Returned alloy composition data may be incomplete, approximate, or lack usable source support.

Mitigation: Prefer literature-supported composition data, distinguish exact values from ranges or missing data, and avoid inventing sources or assuming missing elements are zero.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/alloy-composition-search-zhcn)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown with structured tables and concise narrative analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include alloy composition percentages, match summaries, source labels, classifications, data-quality notes, and next-step suggestions when supported by the query and available data.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
