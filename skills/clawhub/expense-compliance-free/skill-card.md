## Description:

把一沓发票和一张报销单放在一起核一遍，每条结论都带原文行号，不需要付款，也不需要注册。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and finance reviewers use this skill to pre-check reimbursement packets before submission. It performs mechanical checks for duplicate invoice numbers, missing invoice elements, and leftover template placeholders, with findings tied back to source lines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The pre-check is narrow and does not provide full finance approval or invoice authenticity review.

Mitigation: Use the output as an early screening aid and route reimbursement materials through the normal finance approval and invoice verification process.

Risk: The local helper runs through Bash and Node on reimbursement materials.

Mitigation: Review the skill before installation and run it only in an environment approved for the documents being checked.

Risk: The separate web checker may require submitting document data outside the local environment.

Mitigation: Use the web link only when intentional and permitted by the organization's data handling rules; otherwise use the local workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/expense-compliance-free)
- [Free web checker](https://www.tokendidi.cn/check)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Human-readable text or structured JSON containing findings, severity levels, evidence lines, advice, executed checks, and withheld checks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May exit with code 3 for insufficient input and intentionally withhold conclusions when materials are not adequate.]

## Skill Version(s):

1.0.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
