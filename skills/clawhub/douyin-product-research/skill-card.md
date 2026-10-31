## Description:

当用户需要做抖音电商选品、抖音小店类目研究或整理候选商品时使用。输入类目、预算与筛选条件，输出候选清单、入选理由和需要进一步核实的问题。来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Douyin sellers and product researchers can use this skill to shortlist products from a category or keyword using supplied budget and filters, then review visible product details and identify questions that still need verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and supplied product IDs or URLs are sent to SocialDataX, and requests may consume paid credits.

Mitigation: Avoid confidential search inputs, provide only the intended SocialDataX API key, and review usage before expanding searches.

Risk: The external CLI was not inspected as part of the supplied security assessment.

Mitigation: Review and pin a CLI version before use where possible.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/douyin-product-research)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown]

**Output Format:** [Markdown table with concise prose]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A traceable shortlist based on returned product information, with matching reasons and follow-up checks; normally up to five candidates and two to three detail reviews. It does not estimate market-wide sales, popularity, or profit.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
