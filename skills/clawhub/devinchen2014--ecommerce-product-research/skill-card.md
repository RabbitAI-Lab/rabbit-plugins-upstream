## Description:

根据用户提供的商品类目或商品资料整理电商选品候选清单，列出可见价格、匹配情况、入选理由和待核实事项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

外部用户可根据已有商品资料或抖音、小红书的在线商品信息进行选品初筛，比较可见价格与筛选条件，并整理需要复核的候选商品。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags supply-chain exposure from invoking the mutable third-party CLI at @latest, including during API key entry; the review does not establish malicious intent.

Mitigation: Pin a reviewed CLI version and verify its package integrity before use.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/devinchen2014/skills/ecommerce-product-research)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Analysis, Markdown]

**Output Format:** [Markdown table of candidate products, visible prices, fit, source links, and verification notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Up to five initial candidates with 2–3 prioritized detail checks; findings reflect only provided or returned information.]

## Skill Version(s):

0.1.11 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
