## Description:

使用极鲸云查询 Shopee 店铺详情和商品样本，帮助分析销量、销售额、评分、粉丝、商品规模、跨境属性、类目结构和经营趋势。

This skill is ready for commercial/non-commercial use.

## Publisher:

[geekbi](https://clawhub.ai/user/geekbi)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers, analysts, and operators use this skill to research Shopee shops by site and shop ID or by representative product ID. It supports shop overview, product-structure analysis, operating evidence, risk notes, sample boundaries, and next-step validation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Login state and access tokens can be written into local user config, skill, and workspace folders.

Mitigation: Install only in trusted, non-shared workspaces and clear GeekBI auth state when finished.

Risk: Authentication and API destinations can be changed from the default GeekBI endpoint.

Mitigation: Use the default GeekBI endpoint unless the publisher and destination are explicitly trusted.

Risk: Shop metrics, Shopee policies, and market rules can be snapshot-based or market-specific.

Mitigation: Verify business actions, compliance decisions, and Seller Centre status in the target Shopee market before acting.

## Reference(s):

- [Server-resolved source repository](https://github.com/geekbi/geekbi-shopee-shop-search-skill)
- [ClawHub skill page](https://clawhub.ai/geekbi/skills/geekbi-shopee-shop-search-skill)
- [Shopee店铺接口](artifact/references/Shopee店铺接口.md)
- [Shopee店铺研究](artifact/references/Shopee店铺研究.md)
- [Shopee运营与政策口径](artifact/references/Shopee运营与政策口径.md)
- [查询暂停与恢复流程](artifact/references/查询暂停与恢复流程.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with JSON results from helper scripts when live queries are run]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include shop summaries, operating evidence, product sample analysis, risk notes, sample boundaries, and next-step recommendations.]

## Skill Version(s):

0.1.0 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
