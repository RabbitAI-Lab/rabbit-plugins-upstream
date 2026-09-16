## Description:

社保缴费基数核对表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。本免费版执行引擎声明的免费检查项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, HR, payroll, and operations staff use this skill during monthly reconciliation or contribution-base adjustment to check social-insurance contribution-base tables. It recalculates declared employer and employee contributions, checks totals, and flags duplicate or incomplete rows with source-line evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The free skill advertises a paid upgrade flow that can ask an agent to run an @latest package install and begin a purchase workflow.

Mitigation: Treat the upgrade as a separate manual purchase decision; verify the package, version, source, and payment details, and require the user to complete wallet or payment confirmation personally.

Risk: The free version omits several checks, including unit-vs-personal base consistency and contribution-base limit checks.

Mitigation: Use the listed executed and withheld checks to scope decisions, and do not treat the free output as a complete payroll compliance review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/social-insurance-base-check-free)
- [Paid upgrade purchase information](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay shelf](https://skillpay.alipay.com/public/tokendidi)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Human-readable text or JSON from a local Node.js command]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source lines, include executed and withheld checks, and do not provide a conclusion when required table inputs are missing.]

## Skill Version(s):

1.0.3 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
