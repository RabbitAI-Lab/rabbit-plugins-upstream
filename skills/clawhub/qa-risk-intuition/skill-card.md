## Description:

识别那些"看起来很简单但实际风险很高"的测试区域，帮测试人员在资源有限时判断测试重点、标注风险概率和影响等级，并给出缓解建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers, test leads, and developers use this skill to identify hidden high-risk areas, prioritize testing effort, and produce risk matrices, high-risk area lists, and mitigation suggestions from requirements, scenario trees, and optional defect history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional full QA skill set referenced by the artifact may have different contents and permissions than this single read-only skill.

Mitigation: Review the separate package before installing or deploying it.

Risk: Risk-prioritization output can miss important test areas or overstate coverage when source requirements are incomplete.

Mitigation: Review the generated risk assessment against current requirements, scenario coverage, and defect history before using it for release decisions.

## Reference(s):

- [风险信号雷达与检查清单](artifact/references/risk-signals.md)
- [ClawHub Skill Page](https://clawhub.ai/kokxi/skills/qa-risk-intuition)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Analysis]

**Output Format:** [Markdown risk assessment report with tables and structured risk matrices]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes risk IDs, linked requirement IDs, probability and impact levels, prioritized high-risk areas, and mitigation suggestions.]

## Skill Version(s):

1.7.6 (source: release evidence; artifact frontmatter lists 1.7.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
