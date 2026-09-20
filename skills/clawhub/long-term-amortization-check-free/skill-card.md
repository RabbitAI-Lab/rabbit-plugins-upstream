## Description:

长期待摊费用摊销台账逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。本免费版执行引擎声明的免费检查项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounting users use this skill during monthly close, reconciliation, or inventory checks to verify long-term prepaid expense amortization ledgers for arithmetic consistency, totals, duplicate items, and missing fields. It is an arithmetic consistency checker, not accounting, tax, capitalization, or policy advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The output can be mistaken for accounting, tax, capitalization, or amortization-period advice.

Mitigation: Use it only as an arithmetic consistency check and have accounting policy decisions reviewed by qualified finance personnel.

Risk: The free version omits several checks that are listed in the skill description, including over-amortization and negative-balance checks.

Mitigation: Review the omitted checks list in the output and cover those checks manually or with a separate approved workflow.

Risk: The skill processes Chinese-language financial ledger text with a local Node.js script.

Mitigation: Install and run it only in environments approved for the ledger data being checked; inspect the release and security summary before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/long-term-amortization-check-free)

## Skill Output:

**Output Type(s):** [text, JSON, guidance]

**Output Format:** [Human-readable text or JSON containing executed checks, findings, summary, omitted checks, missing-input guidance, and scope notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs on local ledger text input; insufficient input returns missing fields instead of a conclusion]

## Skill Version(s):

1.0.53 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
