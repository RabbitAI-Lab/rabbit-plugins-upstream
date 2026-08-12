## Description:

This skill helps agents use GeekBI's Temu data to research products, image matches, shops, categories, keywords, and reviews for ecommerce selection, market research, competitor analysis, demand trends, pricing, competition, customer pain points, and opportunity assessment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[geekbi](https://clawhub.ai/user/geekbi)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, market researchers, and sourcing teams use this skill to ask an agent for Temu product discovery, same-item image search, shop research, category sizing, keyword demand analysis, and review-based customer insight. The skill is intended to turn GeekBI-returned Temu data into concise Chinese business findings with stated data scope, sample limits, opportunities, risks, and next steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Temu queries and image-search inputs are sent to GeekBI.

Mitigation: Avoid submitting private, sensitive, or confidential product images or query details unless sharing them with GeekBI is intended.

Risk: The skill keeps GeekBI login state in the user's configuration directory.

Mitigation: Install and run the skill only in trusted user environments, and remove or revoke GeekBI login state when access is no longer needed.

Risk: Using an alternate service URL can send requests and image inputs to a non-default endpoint.

Mitigation: Use the default GeekBI service endpoint unless the operator has intentionally approved the alternate endpoint.

## Reference(s):

- [Server-resolved source repository](https://github.com/geekbi/geekbi-temu-research-skill)
- [ClawHub skill page](https://clawhub.ai/geekbi/skills/geekbi-temu-research-skill)
- [README](README.md)
- [接口总览](references/接口总览.md)
- [查询暂停与恢复流程](references/查询暂停与恢复流程.md)
- [Temu商品搜索](references/Temu商品搜索.md)
- [Temu图搜同款](references/Temu图搜同款.md)
- [Temu店铺搜索](references/Temu店铺搜索.md)
- [Temu类目搜索](references/Temu类目搜索.md)
- [Temu关键词搜索](references/Temu关键词搜索.md)
- [Temu评论搜索](references/Temu评论搜索.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Guidance, Shell commands, Configuration]

**Output Format:** [Chinese Markdown business analysis, with internal JSON API responses used only when needed for tool execution or troubleshooting]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should state site, time window, filters, pagination or sample limits, data update time, and any missing or anomalous values when available.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
