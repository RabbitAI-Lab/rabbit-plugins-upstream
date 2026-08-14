## Description:

通过极鲸云实时搜索和分析 Temu 类目，返回可信类目 ID 和完整路径，并支持按站点、名称、层级、父类目、蓝海指数、销量、销售额、商品数、店铺数、半托管供给和增长指标筛选及排序。

This skill is ready for commercial/non-commercial use.

## Publisher:

[geekbi](https://clawhub.ai/user/geekbi)

### License/Terms of Use:

MIT-0

## Use Case:

Cross-border sellers and market researchers use this skill to find Temu category IDs, validate category paths, and compare category-level demand, supply, pricing, growth, and blue-ocean indicators before further product research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs local Python scripts, contacts GeekBI's API, and reuses or stores GeekBI login state for authenticated queries.

Mitigation: Install and run the skill only in environments where GeekBI is trusted with Temu category research requests and shared login-state reuse is acceptable.

Risk: Category-level market data can support research but cannot prove a specific product or store opportunity.

Mitigation: Use returned category IDs, paths, sample size, update time, and demand/supply indicators as inputs for further product-level validation.

Risk: Partial pagination, missing values, or ambiguous category names can lead to overconfident conclusions.

Mitigation: Check pagination, sample size, update time, full category path, level, and parent category before presenting conclusions or selecting a category ID.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/geekbi/geekbi-temu-category-search-skill)
- [ClawHub skill page](https://clawhub.ai/geekbi/skills/geekbi-temu-category-search-skill)
- [GeekBI OpenAPI service](https://openapi.geekbi.com)
- [Temu 类目搜索](references/Temu类目搜索.md)
- [Temu 类目搜索接口](references/Temu类目搜索接口.md)
- [Temu 类目榜单查询预设](references/Temu类目榜单预设.md)
- [查询暂停与恢复流程](references/查询暂停与恢复流程.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with category tables, clickable category links, concise analysis, and occasional shell commands for agent execution]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should distinguish returned data, calculated comparisons, and business judgment; category-level data should not be presented as proof of a specific product opportunity.]

## Skill Version(s):

0.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
