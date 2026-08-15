## Description:

Searches and analyzes GeekBI Temu product data to help sellers evaluate sales, pricing, trends, supply price, ratings, listing age, and same-product competition.

This skill is ready for commercial/non-commercial use.

## Publisher:

[geekbi](https://clawhub.ai/user/geekbi)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and analysts use this skill to search Temu product data, compare candidate products, and judge product-selection opportunities from GeekBI service results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores reusable GeekBI login state locally and may reuse that state across GeekBI Temu skills.

Mitigation: Install only when shared GeekBI login reuse is acceptable, review the external service trust boundary, and clear the auth state when reuse is no longer desired.

Risk: Product analysis depends on GeekBI service responses and may be incomplete when data, pagination, or service access is limited.

Mitigation: Keep data-scope notes in the response, avoid unsupported market-wide claims from partial samples, and rerun the original query after required service actions are completed.

## Reference(s):

- [Source repository](https://github.com/geekbi/geekbi-temu-product-search-skill)
- [ClawHub skill page](https://clawhub.ai/geekbi/skills/geekbi-temu-product-search-skill)
- [Temu 商品搜索](references/Temu商品搜索.md)
- [Temu 商品搜索接口](references/Temu商品搜索接口.md)
- [Temu 商品榜单查询预设](references/Temu商品榜单预设.md)
- [查询暂停与恢复流程](references/查询暂停与恢复流程.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown summaries with product links, data-scope notes, findings, risks, and recommended next actions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses GeekBI returned data only; displayed product titles are expected to link to the returned product URLs.]

## Skill Version(s):

0.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
