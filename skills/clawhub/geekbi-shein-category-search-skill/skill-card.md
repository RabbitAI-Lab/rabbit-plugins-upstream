## Description:

搜索和分析 SHEIN 类目，返回可信类目 ID、层级、父链、完整路径、市场规模、供需趋势和品类机会信号。

This skill is ready for commercial/non-commercial use.

## Publisher:

[geekbi](https://clawhub.ai/user/geekbi)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, analysts, and commerce operators use this skill to query SHEIN category IDs and compare category demand, sales, pricing, supply, competition, blue-ocean indicators, and semi-managed penetration using live GeekBI data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill contacts GeekBI's API and may reuse or store GeekBI login state.

Mitigation: Install only when this data flow is acceptable, use an isolated environment where possible, and follow only login links returned by the GeekBI authentication flow.

Risk: The skill may install a Python dependency if it is missing.

Mitigation: Review dependency installation in the target environment before running the scripts.

Risk: Large result sets can exceed the accessible pagination window, which can make broad analyses sample-based.

Mitigation: Narrow filters or paginate explicitly, and state when conclusions are based on a partial result set.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/geekbi/geekbi-shein-category-search-skill)
- [ClawHub skill page](https://clawhub.ai/geekbi/skills/geekbi-shein-category-search-skill)
- [GeekBI API endpoint](https://openapi.geekbi.com)
- [SHEIN 类目搜索方法](references/SHEIN类目搜索.md)
- [SHEIN 类目搜索接口](references/SHEIN类目搜索接口.md)
- [SHEIN 类目榜单查询预设](references/SHEIN类目榜单预设.md)
- [查询暂停与恢复流程](references/查询暂停与恢复流程.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Chinese Markdown with category tables, linked category paths when available, and concise business analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live GeekBI API results; queries may pause for a user authentication action.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
