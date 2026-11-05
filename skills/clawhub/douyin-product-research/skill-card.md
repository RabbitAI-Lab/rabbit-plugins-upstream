## Description:

当用户需要做抖音电商选品、抖音小店类目研究或整理候选商品时使用。输入类目、预算与筛选条件，输出候选清单、入选理由和需要进一步核实的问题。来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

面向抖音电商经营者及选品研究人员，用于按商品类目、预算和筛选条件初筛候选商品，整理匹配依据、来源信息及后续核实事项。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, product IDs, and supplied URLs are sent to SocialDataX and may use paid credits.

Mitigation: Avoid confidential inputs and review the query before sending; check current credit costs and limits.

Risk: The skill uses an API key and an external CLI whose implementation and future releases are outside this artifact review.

Mitigation: Keep the key in supported secret storage and use a reviewed, pinned CLI version where possible.

## Reference(s):

- [SocialDataX skill and API key information](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/douyin-product-research)

## Skill Output:

**Output Type(s):** [Markdown, Analysis, Guidance]

**Output Format:** [Markdown table of candidate products, matching rationale, sources, and follow-up checks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A concise, traceable first-pass shortlist with up to five candidates from one page and follow-up checks for the most relevant items.]

## Skill Version(s):

0.1.4 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
