## Description:

当用户需要做抖音电商选品、抖音小店类目研究或整理候选商品时使用。输入类目、预算与筛选条件，输出候选清单、入选理由和需要进一步核实的问题。来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

抖音电商运营者可按商品类目、关键词、预算和筛选条件整理候选商品，查看入选依据，并标出需要进一步核实的信息。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and supplied product IDs or URLs are sent to SocialDataX and may consume paid credits.

Mitigation: Avoid confidential inputs and confirm applicable data-sharing and credit costs before querying.

Risk: The workflow uses an npm package and requires a SocialDataX API key; the skill description does not provide a technical sandbox for package execution.

Mitigation: Protect SOCIALDATAX_API_KEY, review and pin a package version rather than using @latest, and limit execution permissions to the task.

## Reference(s):

- [SocialDataX API key and service information](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/douyin-product-research)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown candidate list with selection rationale and follow-up verification questions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typically presents up to 5 candidates from one page and reviews 2–3 relevant product details; preserves available product identifiers or links and distinguishes returned data from claims.]

## Skill Version(s):

0.1.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
