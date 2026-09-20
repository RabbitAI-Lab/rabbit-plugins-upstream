## Description:

工会经费与残保金计提表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。本免费版执行引擎声明的免费检查项。触发词包括 工会经费与残保金计提核对、工会经费与残保金计提表对不上。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounting users use this skill during monthly closing, reconciliation, or review to check union fund and disability fund accrual tables for arithmetic, totals, duplicate periods, blanks, and missing required fields.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat accounting-check output as a final compliance opinion.

Mitigation: Review results as an accounting aid and confirm conclusions against source records and applicable local policy or regulatory guidance.

Risk: The free version intentionally does not perform every check listed for the complete product.

Mitigation: Review the reported withheld checks and perform those checks separately when they are relevant to the decision.

Risk: Findings may not quote the full original row even when they cite line-level evidence.

Mitigation: Compare each finding with the original table row before using it in reconciliation or reporting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/union-reserve-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Sample input template](artifact/templates/sample.json)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Plain text or JSON from a local Node.js command]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs findings, missing-input messages, executed free checks, and withheld checks; accounting conclusions require review against the source table and applicable local rules.]

## Skill Version(s):

1.0.42 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
