## Description:

资产减值测试表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文，本免费版执行引擎声明的免费检查项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and operations staff use this skill to check asset impairment test tables during close, reconciliation, or review workflows. It recalculates stated impairment losses, checks provision rollforwards and totals, and reports duplicate, blank, or negative amount issues with source-line evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The checker is limited to deterministic table checks and is not a full accounting judgment.

Mitigation: Have a qualified reviewer assess recoverable amount assumptions, impairment indicators, asset grouping, discount rates, and any management judgments outside the tool scope.

Risk: This free release omits the additional checks listed by the artifact, so a clean result may not cover every impairment-table issue.

Mitigation: Review the executed and withheld check lists before relying on output, and perform separate review for omitted checks that matter to the workflow.

Risk: Incomplete or malformed input can prevent the skill from reaching a conclusion.

Mitigation: Provide the asset impairment table with required headers and treat insufficient-input output as no conclusion, not as a pass.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/asset-impairment-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Plain text or JSON check results with cited findings and omitted-check notices]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on supplied asset impairment table text; material that lacks required columns returns an insufficient-input result rather than an accounting conclusion.]

## Skill Version(s):

1.0.53 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
