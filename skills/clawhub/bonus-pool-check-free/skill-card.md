## Description:

年终奖池分配与个税核对（免费）在本地复算年终奖分配表中的奖金分摊、实发奖金、全年一次性奖金个税、合计行、重复人员和空白占位字段，并在结果中引用原文行号。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Payroll, finance, and HR reviewers can use this skill to check year-end bonus pool allocation worksheets before payout. It reports missing material instead of making default assumptions, and its findings are scoped to the free checks implemented in the local engine.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill text promotes a separate paid installation flow using an unpinned external installer.

Mitigation: Use the free local worksheet checker only; do not run the payment or install command unless the package, publisher, version, permissions, and payment flow have been independently verified.

Risk: The free engine intentionally omits some payroll and tax validation checks.

Mitigation: Review the omitted and out-of-scope checks before relying on results, and use qualified payroll or tax review for decisions outside the implemented checks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/bonus-pool-check-free)
- [SkillPay shelf referenced by the skill](https://skillpay.alipay.com/public/tokendidi)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Plain text or JSON from a local Node.js CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source line numbers; insufficient input exits without a correctness conclusion.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
