## Description:

青虎AI Ozon 爆款跟卖与选品：拉取 Ozon 热卖产品榜与中国专区产品列表，批量看商品详情、产品趋势快照与信息追踪，锁定当前爆款与飙升款，分析价格带和销量结构，判断是做同款跟卖还是差异化改良。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace sellers and ecommerce operators use this skill to research Ozon hot products, compare general and China-zone rankings, inspect product details and trends, and decide whether to follow existing listings or differentiate a product.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated Qinghu API calls may use a user-provided token and consume Qinghu points.

Mitigation: Ask for user authorization before Qinghu API calls, use only user-provided credentials or documented environment variables, and report actual point consumption from the response envelope.

Risk: Request failures can appear successful unless the full response envelope and nested business payload are checked.

Mitigation: Check protocol errors, result.isError, and the parsed inner code and success fields before presenting product recommendations.

Risk: Follow-selling recommendations can involve brand authorization, patent, or marketplace compliance concerns.

Mitigation: Tell users to verify rights, patents, and Ozon compliance requirements before acting on a follow-selling strategy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-ozon-hot-product)
- [Qinghu data API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Concise Markdown summaries with optional exported table files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a file link when returned records are 10 or more; reports Qinghu point consumption after paid calls.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
