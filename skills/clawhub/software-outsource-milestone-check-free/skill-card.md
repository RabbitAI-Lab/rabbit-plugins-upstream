## Description:

软件外包里程碑验收与付款核对表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashier, and operations staff use this skill during month-end settlement, reconciliation, or inventory-style payment checks to verify software outsourcing milestone acceptance and payment tables. It recalculates row-level payment amounts, cumulative paid amounts, totals, duplicates, blanks, and negative amounts, while declining to conclude when required source material is missing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The free release explicitly excludes several higher-impact checks, including over-contract payment, unpaid acceptance conflicts, retention mismatch, incomplete payment ratio, and repeated payment detection.

Mitigation: Review the reported checks_not_run before relying on results, and use contract records, acceptance records, finance approval, or a fuller review for excluded checks before authorizing payment.

Risk: The checker is an arithmetic and consistency aid, not approval to pay or a substitute for contract and acceptance judgment.

Mitigation: Treat findings as reconciliation evidence only, and have the responsible finance or project owner validate payment decisions against the contract, acceptance documents, and internal controls.

Risk: Running the skill executes local Node.js code over business payment-table data.

Mitigation: Install only from the validated release, run it in an appropriate local environment, and avoid providing unrelated confidential material beyond the table needed for the check.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/software-outsource-milestone-check-free)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Console text or JSON findings from a local Node.js checker, with source-row references for findings.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The free version lists executed checks and withheld checks; insufficient input returns missing-material guidance instead of a payment conclusion.]

## Skill Version(s):

1.0.47 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
