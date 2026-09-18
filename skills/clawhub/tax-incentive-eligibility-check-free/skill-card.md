## Description:

税收优惠适用条件自查核对（免费版）帮助财务或税务人员在本机逐行复算税收优惠适用条件自查表，检查合计勾稽、重复行、空缺和负数，并让每条结论引用原文依据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

财务、出纳和税务人员 use this skill to check copied tax incentive eligibility self-check tables during closing, reconciliation, review, or inventory workflows. It performs scoped table-internal recalculation and consistency checks, then reports findings with source context instead of making tax-law eligibility conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional paid-upgrade flow asks an AI agent to run an unpinned remote installer and follow newly downloaded purchase instructions.

Mitigation: Treat the upgrade as a separate high-trust action: independently verify the package, source, permissions, and payment flow before allowing installation, purchase initiation, or follow-on instructions.

Risk: The free release performs only the declared free checks and leaves several policy-oriented or full-tier checks unexecuted.

Mitigation: Review the reported checks_not_run and do not treat a clean result as a complete tax incentive eligibility determination.

Risk: The skill does not provide legal or tax conclusions, file tax forms, or calculate back taxes, interest, or penalties.

Mitigation: Have qualified tax personnel confirm policy applicability, current authority guidance, and downstream filing decisions before relying on the result.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/tax-incentive-eligibility-check-free)
- [AI 核对工具铺](https://skillpay.alipay.com/public/tokendidi)
- [完整档购买说明](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay build guide](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Human-readable console text by default, or structured JSON when run with --json]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports executed checks, withheld checks, scoped findings, source context, and insufficient-input messages when materials cannot be evaluated.]

## Skill Version(s):

1.0.3 (source: ClawHub release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
