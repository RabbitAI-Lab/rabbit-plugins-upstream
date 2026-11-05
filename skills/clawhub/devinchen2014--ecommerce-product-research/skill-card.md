## Description:

提供商品类目或已有商品资料，整理电商选品候选清单，列出可见价格、匹配条件、入选理由和待核实事项。预算与受众有则提供；已有资料可直接分析，无需 API Key。在线商品查询支持抖音与小红书。来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

面向需要进行电商商品初筛的用户，根据其提供的类目、商品资料和可选预算或受众条件，整理候选商品、可见信息、匹配理由及待核实事项。在线查询仅支持抖音与小红书；用户提供的资料也可直接分析。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Online lookups require a SocialDataX credential and may consume paid credits.

Mitigation: Use online lookup only when needed, keep the API key out of chat and version control, and review usage and costs.

Risk: The external CLI release and hosted service are outside the supplied security audit.

Mitigation: Use a reviewed, fixed CLI version and limit its access to the files and secrets needed for the task.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/ecommerce-product-research)
- [SocialDataX API Key information](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown table with concise explanatory text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Candidate shortlist with visible prices, matching conditions, reasons for inclusion, sources, items to verify, and suggested products for follow-up review.]

## Skill Version(s):

0.1.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
