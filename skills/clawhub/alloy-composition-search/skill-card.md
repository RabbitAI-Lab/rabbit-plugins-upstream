## Description:

Generate professional alloy composition search responses by interpreting user queries, retrieving and analyzing relevant alloy data optionally via MCP tools, and presenting structured composition tables with clear filtering, classification, and insights.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, materials engineers, and patent analysts use this skill to search, filter, classify, and summarize metal alloy compositions from user queries and optional alloy, patent, or paper data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may use a configured mace-mcp server for alloy, patent, or paper retrieval.

Mitigation: Confirm the MCP server configuration is trusted before installation or use.

Risk: Alloy composition answers can be incomplete or misleading if retrieved source data is incomplete.

Mitigation: Follow the skill guidance to avoid fabricated composition data, distinguish exact from partial matches, and state limitations when data is incomplete.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/alloy-composition-search)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown with structured composition tables, summaries, match notes, and concise technical insights]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include human-readable patent or paper references when source data supports them.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
