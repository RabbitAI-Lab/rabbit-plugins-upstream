## Description:

租金账单/租赁结算表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文行号。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business operators use this skill to check Chinese-language lease rent worksheets for arithmetic mismatches, total-line errors, duplicate tenants, blank placeholders, and missing evidence before relying on monthly rent or deposit-settlement calculations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat arithmetic findings as legal, tax, contract, or full financial assurance.

Mitigation: Use the output only as a rent worksheet arithmetic check and have qualified reviewers assess legal, tax, contract, and final financial conclusions.

Risk: The free version deliberately omits several validations, including non-positive rent, negative ending arrears, and month-range checks.

Mitigation: Review the listed withheld checks before relying on the result, and run additional validation when those cases matter.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/lease-rent-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Console text or JSON findings with cited source line numbers]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports executed checks, withheld free-version checks, insufficient-input status, and line-referenced findings.]

## Skill Version(s):

1.0.30 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
