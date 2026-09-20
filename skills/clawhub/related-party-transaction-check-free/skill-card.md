## Description:

关联交易台账逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。本免费版执行引擎声明的免费检查项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External users at companies with related-party transactions use this skill before annual tax settlement, related-party reporting, or contemporaneous documentation preparation to check ledger totals, repeated rows, blank fields, negative balances, and consistency among reported, ledger, and transaction amounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat deterministic consistency findings as tax, legal, transfer-pricing, or assurance advice.

Mitigation: State that the skill checks supplied ledger consistency only and that tax, legal, transfer-pricing, and assurance conclusions require professional review.

Risk: The free version intentionally omits advanced checks, so a clean result can miss issues outside the free scope.

Mitigation: Surface the executed checks and checks not run with every result, and avoid describing a clean result as comprehensive compliance.

Risk: Insufficient or malformed ledger input can produce misleading confidence if treated as a completed check.

Mitigation: Return an insufficient-input status and do not issue a consistency conclusion until recognizable headers and data rows are provided.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/related-party-transaction-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [analysis, json, shell commands, guidance]

**Output Format:** [Human-readable text or JSON containing consistency findings, missing-input messages, executed checks, checks not run, and cited row evidence.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard library; accepts a JSON file or pasted ledger text with table headers.]

## Skill Version(s):

1.0.18 (source: server release evidence; artifact frontmatter reports 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
