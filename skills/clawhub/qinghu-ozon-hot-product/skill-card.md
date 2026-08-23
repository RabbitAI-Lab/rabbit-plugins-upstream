## Description:

青虎AI Ozon 爆款跟卖与选品技能用于拉取 Ozon 热卖榜和中国专区产品列表，查看商品详情、趋势快照与信息追踪，帮助判断候选商品适合跟卖、改良、观望还是放弃。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce operators, and sourcing analysts use this skill to screen Ozon hot products, compare general and China-zone rankings, inspect product trends, and decide whether to follow-sell or differentiate a product.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Qinghu API calls can use a user-provided token or an approved environment token and may consume Qinghu points.

Mitigation: Confirm the planned Qinghu tools, token source, and cost uncertainty before the first API call in a session.

Risk: Large Ozon market datasets may be written to local export files or reused from cached file paths.

Mitigation: Export only intended result sets, share explicit file links, and avoid copying cached raw datasets into chat.

Risk: Follow-selling recommendations can involve brand authorization, patent, marketplace, or product-compliance risk.

Mitigation: Treat strategy labels as screening guidance and require independent compliance checks before listing or follow-selling products.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-ozon-hot-product)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu workflow credential check endpoint](https://www.iqinghu.com/api/desktop/qh/workflow/page?pageNum=1&pageSize=5)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown summaries with optional exported tabular files and inline JSON or shell snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Large result arrays may be exported to local files; replies should include a concise link and key preview rather than full raw datasets.]

## Skill Version(s):

0.1.1 (source: server release evidence, released 2026-08-21)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
