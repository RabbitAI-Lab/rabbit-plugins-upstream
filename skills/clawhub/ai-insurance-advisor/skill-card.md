## Description:

面向中国大陆个人和家庭，提供保险需求分析、产品比较、保费估算、方案建议、保险知识问答及合规提示。

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

供中国大陆有保险需求的个人和家庭了解保障需求、比较本地产品资料、估算保费并查看方案建议。输出可辅助理解与规划，具体保障应以保险公司现行条款和最终承保信息为准。

### Deployment Geography for Use:

中国大陆

## Known Risks and Mitigations:

Risk: A generated insurance plan may continue to show a 6 million medical coverage figure after the actual coverage is reduced.

Mitigation: Review the coverage figures and listed features in each generated plan against the actual product terms and final coverage amounts before relying on it.

## Reference(s):

- [保险产品资料](references/products.json)
- [保险知识参考](references/insurance-knowledge.md)
- [合规参考](references/compliance.md)
- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor)
- [Security audit](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor/security-audit)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Markdown, JSON]

**Output Format:** [Chinese-language text and Markdown reports or comparison tables; calculation scripts return JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations and estimates should be checked against current product terms and final coverage amounts.]

## Skill Version(s):

2.3.8 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
