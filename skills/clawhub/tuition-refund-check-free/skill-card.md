## Description:

退费核对表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文行号。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Education and training operators use this skill to check tuition refund tables for arithmetic consistency, total-row reconciliation, duplicate students, and missing fields. It helps produce line-cited findings for refund review, while leaving legal, contract, and policy judgments out of scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release includes an optional paid-upgrade flow that asks an assistant to run an unpinned remote npm installer and initiate a purchase.

Mitigation: Do not let an assistant run the installer or start a purchase unless the package, source, permissions, and payment flow have been independently verified; require the user to confirm wallet authorization or payment.

Risk: The checker only covers the free deterministic checks and does not decide contract legality, policy compliance, or whether the source records are true.

Mitigation: Use the output as arithmetic/table-review support and route legal, contractual, regulatory, and source-record questions to qualified reviewers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/tuition-refund-check-free)
- [SkillPay paid-upgrade shelf referenced by artifact](https://skillpay.alipay.com/public/tokendidi)
- [SkillPay install and purchase guide referenced by artifact](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Human-readable console text or JSON from a local Node.js runner]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source line numbers; insufficient input returns missing-field guidance without a substantive conclusion.]

## Skill Version(s):

1.0.5 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
