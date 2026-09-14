## Description:

固定资产折旧核对（免费）对固定资产台账执行逐行折旧算术、合计勾稽、重复资产编号和空白占位符检查，并为结论引用原文行号。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounting staff use this skill to locally check fixed-asset depreciation ledgers for arithmetic mismatches, total-line inconsistencies, duplicate asset IDs, and blank or placeholder fields before month-end review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may mistake arithmetic and consistency checks for accounting, audit, or tax advice.

Mitigation: Treat results as fixed-asset ledger checks only, and route policy, audit, tax, depreciation-life, residual-rate, impairment, transfer-to-fixed-asset, and physical-existence questions to qualified reviewers.

Risk: Input JSON may include unrelated secrets or control-like fields such as token, credit, or full.

Mitigation: Provide only the ledger text or required ledger fields, and remove credentials, tokens, and unrelated sensitive fields before running the skill.

Risk: The free mode withholds several checks, including over-depreciation, depreciation-cap, stopped-depreciation, and residual-rate range checks.

Mitigation: Review the reported checks_executed and checks_not_run fields, and do not interpret a clean result as coverage of checks that were listed as withheld or out of scope.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/depreciation-check-free)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Plain text or JSON result summaries from local Node commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source lines when available; insufficient input returns missing fields and advice instead of a conclusion.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
