## Description:

通过极鲸云查询和组合分析 Ozon 当前支持站点的商品、店铺、类目、关键词和评论数据，帮助用户完成跨境选品、市场调研、竞品分析和用户反馈研究。

This skill is ready for commercial/non-commercial use.

## Publisher:

[geekbi](https://clawhub.ai/user/geekbi)

### License/Terms of Use:

MIT-0

## Use Case:

跨境电商经营、选品和市场研究人员使用该 skill 查询 Ozon 商品、店铺、类目、关键词和评论数据，并将多类数据组合成经营判断、机会风险和后续验证动作。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill persists GeekBI login tokens in local state files, including the current workspace.

Mitigation: Review before installing in shared, synced, archived, or customer workspaces; treat .geekbi/agent-auth.json and the GeekBI user-config auth file as credentials, and clear or revoke access when no longer needed.

Risk: Returned Ozon data may be sampled, time-windowed, estimated, partial, or missing.

Mitigation: Disclose site, currency, filters, sample size, data source, metric window, observed time, and confidence; avoid treating high sales, high search volume, or high ratings as proof of profitability.

Risk: Commercial conclusions can be misleading if Ozon policies, logistics, commissions, promotions, taxes, or exchange rates have changed.

Mitigation: Recheck official Ozon pages and current cost inputs before acting on fees, fulfillment, restrictions, promotions, or profit assumptions.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/geekbi/geekbi-ozon-research-skill)
- [ClawHub skill page](https://clawhub.ai/geekbi/skills/geekbi-ozon-research-skill)
- [接口总览](references/接口总览.md)
- [Ozon 商品接口](references/Ozon商品接口.md)
- [Ozon 商品研究](references/Ozon商品研究.md)
- [Ozon 店铺接口](references/Ozon店铺接口.md)
- [Ozon 店铺研究](references/Ozon店铺研究.md)
- [Ozon 类目接口](references/Ozon类目接口.md)
- [Ozon 类目研究](references/Ozon类目研究.md)
- [Ozon 关键词接口](references/Ozon关键词接口.md)
- [Ozon 关键词研究](references/Ozon关键词研究.md)
- [Ozon 评论接口](references/Ozon评论接口.md)
- [Ozon 评论研究](references/Ozon评论研究.md)
- [Ozon 运营与政策口径](references/Ozon运营与政策口径.md)
- [查询暂停与恢复流程](references/查询暂停与恢复流程.md)
- [Ozon Partner Delivery](https://docs.ozon.com/global/en/fulfillment/rfbs/logistic-settings/partner-delivery-ozon/?country=TR)
- [Ozon Analytics Tools](https://docs.ozon.com/global/tr/analytics/analytics-and-metrics/analytics-tools/?country=TR)
- [Ozon 商品与价格管理](https://docs.ozon.com/global/ozon-seller-app/product-management/)
- [Ozon 促销说明](https://docs.ozon.com/global/promotion/promotions/promo/?country=OTHER)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with data summaries and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports site, currency, filters, sample size, timestamps, sources, confidence, risks, and validation actions when data is available.]

## Skill Version(s):

0.1.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
