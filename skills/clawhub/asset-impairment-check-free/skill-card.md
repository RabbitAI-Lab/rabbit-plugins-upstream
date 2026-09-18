## Description:

资产减值测试表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文；本免费版执行引擎声明的免费检查项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, accounting, and review staff use this skill to check asset impairment test tables during closing, reconciliation, or inventory-review workflows. It recalculates listed arithmetic relationships, checks totals, detects duplicates and blanks, and reports source-cited findings without making valuation judgments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security summary flags a paid-upgrade path that points users or agents to an unpinned external `npx ...@latest` installer and payment workflow.

Mitigation: Use the free local checker without invoking the paid-upgrade prompt unless the package, publisher, version, and payment flow are independently verified; require the user to confirm any wallet authorization or payment.

Risk: The free version runs only the listed subset of checks and omits additional paid-version checks.

Mitigation: Treat results as limited to the executed checks and review the reported checks-not-run before relying on the assessment.

Risk: The artifact states that valuation judgments, recoverable amount calculations, discount-rate selection, and asset-grouping decisions are out of scope.

Mitigation: Use management conclusions, source accounting records, and any valuation report for those judgments; use this skill only for arithmetic and internal-consistency checks.

Risk: Users may paste financial table data into the local checker.

Mitigation: Run the checker on a trusted local machine and avoid sending the pasted table or paid-upgrade instructions to external agents or services.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/asset-impairment-check-free)

## Skill Output:

**Output Type(s):** [text, JSON, guidance]

**Output Format:** [Human-readable console text or structured JSON findings from a local Node.js command]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite input line references; insufficient input returns missing fields instead of a positive conclusion.]

## Skill Version(s):

1.0.5 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
