## Description:

Fund Analysis guides agents through private and public fund analysis, including NAV trends, performance metrics, holdings review, fund screening, and FOF portfolio reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[simpleeelv](https://clawhub.ai/user/simpleeelv)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to resolve funds, retrieve fof99 fund data, compare NAV and performance metrics, inspect holdings, screen funds, and draft fund or FOF analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can query private fund or portfolio information through the fof99 data source.

Mitigation: Confirm the user has permission to access the requested fund or portfolio data before running those queries.

Risk: Fund metrics and generated reports may be mistaken for investment advice.

Mitigation: Present results as analytical reference only, include data-source caveats, and avoid recommending investment actions.

Risk: Analysis quality depends on the trustworthiness and availability of the fof99 MCP data source.

Mitigation: Confirm the data source is trusted before installation or use, and state when requested data is unavailable or incomplete.

## Reference(s):

- [Server-resolved GitHub source](https://github.com/simpleeelv/FOF99-SKILLS/tree/main/skills/Fund-Analysis)
- [ClawHub skill page](https://clawhub.ai/simpleeelv/skills/fund-analysis-fof99)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown reports with tables, ECharts JSON or configuration snippets, and concise analytical guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use fof99 MCP fund-data tools and ECharts rendering; outputs should cite data sources, note limitations, and avoid investment advice.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
