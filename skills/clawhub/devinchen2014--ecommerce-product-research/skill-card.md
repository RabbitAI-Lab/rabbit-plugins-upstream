## Description:

根据商品类目或已有资料整理电商选品候选清单，并标注可见价格、匹配理由与待核实事项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

外部用户可用此技能根据商品类目、预算和受众条件初筛电商商品，也可直接整理已有商品资料。它输出带来源和待核实事项的候选清单，帮助用户决定哪些商品值得进一步复核。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Online queries send search inputs to SocialDataX and may consume paid credits.

Mitigation: Avoid confidential inputs and keep online queries within the user's intended scope.

Risk: The security review does not certify future CLI releases.

Mitigation: Prefer a reviewed, fixed CLI version over @latest and limit its access to unrelated secrets.

## Reference(s):

- [SocialDataX API key and product research](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/ecommerce-product-research)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown table with product candidates, visible prices, match reasons, sources, and verification notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source links or product IDs and observation scope when available; does not imply market-wide sales, profitability, or demand.]

## Skill Version(s):

0.1.7 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
