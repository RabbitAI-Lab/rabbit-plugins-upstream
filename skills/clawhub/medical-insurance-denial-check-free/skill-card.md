## Description:

医保拒付与申诉核对表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文，本免费版执行引擎声明的免费检查项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashier, and reconciliation staff use this skill during monthly medical insurance denial settlement review to check table arithmetic, totals, duplicate rows, blanks, and negative amounts before appeal follow-up. It supports local review of provided tables and does not decide whether a denial should be appealed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security evidence marks the skill suspicious because it steers users or agents toward an external package install and paid purchase flow.

Mitigation: Use the bundled local checker only when intended; do not run the payment installer or follow newly installed skill instructions unless the package is independently trusted and each install and payment step is explicitly approved.

Risk: Inputs may contain medical or financial data.

Mitigation: Process only materials you are authorized to handle and keep inputs local according to the skill's stated local-execution boundary.

Risk: The free release does not run several checks reserved for the paid version, including appeal amount overage, appeal deadline, duplicate appeal, zero appealed amount, and denial-rate range checks.

Mitigation: Treat free-version results as a scoped reconciliation check and separately review any withheld checks that matter for the workflow.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chenqg618/skills/medical-insurance-denial-check-free)
- [Publisher Profile](https://clawhub.ai/user/chenqg618)
- [Full Version Purchase Instructions](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay Shelf](https://skillpay.alipay.com/public/tokendidi)
- [SkillPay Build Guide](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Human-readable console text or JSON result objects]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include source line references, executed checks, checks not run, summary counts, and local execution/network-use flags.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
