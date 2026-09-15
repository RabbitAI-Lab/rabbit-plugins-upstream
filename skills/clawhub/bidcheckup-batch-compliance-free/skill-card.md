## Description:

一次把多家投标文件的报价算术全部核一遍，不需要付款，也不需要注册。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External users and procurement reviewers use this skill to run a local pre-check of bidder quote arithmetic across multiple bidding documents. It reports per-bidder verdicts and findings for quantity, unit price, and amount consistency without treating the output as an award or evaluation decision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documentation includes an optional upgrade path that asks an agent to install unpinned remote payment tooling and start a paid workflow.

Mitigation: Do not paste or run the upgrade prompt unless you intend to use the paid workflow; manually verify the source, version, permissions, and payment steps, and require the user to confirm any wallet authorization or payment.

Risk: The checker only performs per-bidder quote arithmetic and does not provide a bid award decision, qualification review, technical evaluation, or legal conclusion.

Mitigation: Use the output as a pre-check only and route findings to qualified reviewers or the responsible evaluation process before taking procurement action.

Risk: Incomplete input can produce NOT_CHECKED or insufficient-input results that may be mistaken for a clean check.

Mitigation: Provide complete bidder items or parseable quote text, and treat NOT_CHECKED or insufficient-input output as no conclusion.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chenqg618/skills/bidcheckup-batch-compliance-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)
- [AI 核对工具铺](https://skillpay.alipay.com/public/tokendidi)
- [SkillPay build guide](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Console text or JSON result object]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local Node.js execution; insufficient input exits without a conclusion rather than fabricating a verdict.]

## Skill Version(s):

1.0.8 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
