## Description:

当用户需要回答商品咨询、整理售前FAQ或起草售后解释时使用。输入商品链接或资料、买家问题与已确认的店铺规则，输出可复制回复和商家待核实事项。在线商品详情支持抖音与小红书，已有资料可直接起草；不自动发送消息或办理售后。来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

外部商家和客服人员可用此技能依据商品资料与已确认的店铺规则，起草买家咨询回复、售前 FAQ 和售后解释，并把需商家核实的事项单独列出。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Online product lookups use an automatically updated CLI package and may consume paid credits.

Mitigation: Use a reviewed, pinned CLI version and confirm expected credit use before lookup.

Risk: Credentials could be exposed to unrelated processes during online lookups.

Mitigation: Keep unrelated secrets outside the execution environment and provide only the required SocialDataX credential.

Risk: Drafts may contain inaccurate or misleading customer-service guidance if source facts are incomplete.

Mitigation: Check claims against current product and store-policy evidence, then review the draft before sending.

## Reference(s):

- [SocialDataX 商品详情与 API Key 信息](https://socialdatax.com/ai?from=clawhub)
- [ClawHub 技能发布页](https://clawhub.ai/devinchen2014/skills/ecommerce-customer-service)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown customer-reply drafts, FAQs, and internal verification checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Separates buyer-facing drafts from merchant verification items; does not send messages or process after-sales actions.]

## Skill Version(s):

0.1.1 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
