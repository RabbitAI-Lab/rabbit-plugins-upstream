## Description:

社保缴费基数核对表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。本免费版执行引擎声明的免费检查项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, payroll, and HR operations users use this skill to check Chinese social-insurance contribution-base tables during monthly reconciliation or closing. It recalculates contribution amounts, checks totals, detects duplicates and blanks, and withholds conclusions when required table evidence is missing.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The free version does not run several checks listed as withheld, including base-limit compliance, unit/person base mismatch, and back-payment mismatch.

Mitigation: Treat results as limited to the executed checks reported at runtime and review withheld checks before relying on the outcome.

Risk: Payroll and social-insurance tables can contain sensitive employee compensation data.

Mitigation: Run the checker locally on trusted machines and avoid sharing input files or outputs beyond the review team.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/social-insurance-base-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Shell commands, Guidance]

**Output Format:** [Human-readable console output or JSON containing executed checks, withheld checks, findings, summary, and missing-input guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs from local Node.js scripts; sample and custom table inputs are supported.]

## Skill Version(s):

1.0.44 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
