## Description:

当用户需要回答商品咨询、整理售前 FAQ 或起草售后解释时，本技能根据商品资料、买家问题与已确认的店铺规则生成可复制回复和商家待核实事项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

商家客服人员可用此技能回答商品咨询、整理售前 FAQ，并起草售后解释；回复依据已提供或按需读取的商品资料和已确认的店铺规则，同时单列需要商家核实的信息。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Online lookups send product links or IDs to SocialDataX using the configured API key and may consume paid credits.

Mitigation: Use online lookup only when needed, with a reviewed fixed CLI version and limited local access; use supplied product materials when they are sufficient.

Risk: A drafted customer reply could contain incorrect or misleading claims.

Mitigation: Check each draft against the product evidence and confirmed store policies, and review it before sending.

## Reference(s):

- [SocialDataX API Key and service information](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/ecommerce-customer-service)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown customer reply drafts and FAQ entries, with separate internal verification notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Drafts only; does not send messages or process orders or after-sales requests.]

## Skill Version(s):

0.1.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
