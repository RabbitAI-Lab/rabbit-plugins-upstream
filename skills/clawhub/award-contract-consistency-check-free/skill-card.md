## Description:

中标通知书与合同草案逐项核对，执行逐行复算、合计勾稽、重复与空缺检测，并为每条结论引用原文依据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashier, procurement, and contract-review users use this skill to compare an award notice against a draft contract before settlement, reconciliation, or contract execution. It reports mismatched, missing, duplicated, blank, or placeholder elements while listing checks that the free version did not run.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The free version has limited coverage and is not a full legal or procurement compliance review.

Mitigation: Review the checks_not_run output and route contract or procurement compliance decisions through qualified reviewers.

Risk: Insufficient or malformed source material can prevent a reliable comparison.

Mitigation: Provide a table with the required award-notice and draft-contract columns, and treat insufficient-input output as no conclusion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/award-contract-consistency-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Console text or JSON containing executed checks, findings, missing-input messages, and checks not run.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local execution; when materials are insufficient, it reports missing inputs and does not issue an consistency conclusion.]

## Skill Version(s):

1.0.57 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
