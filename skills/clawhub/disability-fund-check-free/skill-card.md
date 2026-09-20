## Description:

对残保金申报表进行本地逐项复算，检查应安排人数、应缴金额、已缴与应缴差异、合计勾稽、重复行和关键字段空缺，并在每条结论中引用原文行号。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and tax staff use this skill before disability employment fund filing to recalculate worksheet arithmetic, compare paid and payable amounts, and identify duplicate rows or missing key fields. It is intended for consistency checking of user-provided worksheet text, not tax advice or regional policy validation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat arithmetic consistency checks as tax advice or as confirmation that regional policy parameters are correct.

Mitigation: Review the output as worksheet arithmetic only and separately confirm applicable regional policy parameters, exemptions, reductions, and filing requirements.

Risk: Incomplete or incorrectly formatted worksheet text can prevent reliable checking or omit relevant rows.

Mitigation: Provide the required table headers and worksheet rows as text, review any missing-input messages, and do not rely on a pass result when the skill reports insufficient material.

Risk: The free release explicitly omits exemption checks, tiered reduction checks, certificate and labor-contract validation, wage-basis review, and refund or supplement payment lists.

Mitigation: Use the reported scope and withheld-checks list to decide which items need manual review or another workflow before filing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/disability-fund-check-free)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Shell commands, Guidance]

**Output Format:** [Human-readable console text or JSON with findings, source line references, executed checks, missing-input guidance, and scope notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node standard library; input worksheet text is user-provided and the free tier reports withheld checks explicitly.]

## Skill Version(s):

1.0.45 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
