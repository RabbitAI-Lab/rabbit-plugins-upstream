## Description:

This skill helps agents search GeekBI Temu category data, verify category IDs and full category paths, and summarize category-level market signals such as sales, demand growth, supply, competition, blue-ocean index, and semi-managed penetration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[geekbi](https://clawhub.ai/user/geekbi)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, category researchers, and commerce operators use this skill to find trustworthy Temu category IDs, compare category demand and supply signals, and identify categories worth further business validation. It supports category-level research and does not prove individual product or store opportunity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Temu category query parameters to GeekBI APIs.

Mitigation: Use it only when sharing category research queries with GeekBI is acceptable, and avoid including unrelated confidential business information in prompts.

Risk: The skill can reuse and persist GeekBI login state locally.

Mitigation: Run it in an approved user environment, protect local configuration files, and clear stored login state according to organizational access-control policy.

Risk: Returned market analysis is category-level research rather than proof of product success.

Mitigation: Treat outputs as screening signals and validate promising categories with product-level demand, margin, sourcing, compliance, and operational data before acting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/geekbi/skills/geekbi-temu-category-search-skill)
- [Server-resolved GitHub provenance](https://github.com/geekbi/geekbi-temu-category-search-skill)
- [GeekBI OpenAPI endpoint](https://openapi.geekbi.com)
- [Temu 类目搜索](references/Temu类目搜索.md)
- [Temu 类目搜索接口](references/Temu类目搜索接口.md)
- [Temu 类目榜单查询预设](references/Temu类目榜单预设.md)
- [查询暂停与恢复流程](references/查询暂停与恢复流程.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Chinese Markdown with concise conclusions, data scope, category tables or lists, clickable category links, and explicit limitations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include category IDs, full category paths, market metrics, sample size, pagination scope, update time, and next-step validation guidance.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
