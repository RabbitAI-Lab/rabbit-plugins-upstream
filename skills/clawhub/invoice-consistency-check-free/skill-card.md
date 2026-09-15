## Description:

A free local consistency checker for invoice and expense-claim text that returns evidence-backed findings for arithmetic, tax, total, amount-wording, entity, date, duplicate-invoice, placeholder, and blank-field issues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, operations, and developer users can run the local checker before reimbursement or invoice review to identify recomputable inconsistencies in pasted text or JSON invoice inputs. It supports human review and does not replace tax, audit, authenticity, or policy decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documentation includes a paid-upgrade prompt that asks an assistant to install and buy a separate product through remote code.

Mitigation: Install only the free checker unless the paid package, SkillPay instructions, and newly installed skill are separately reviewed in a constrained environment; require the user to confirm any wallet authorization or payment.

Risk: The skill checks invoice text consistency but does not verify authenticity, legality, tax treatment, audit status, or business appropriateness.

Mitigation: Use findings as evidence for human finance, tax, or audit review, and keep official validation and policy decisions outside this tool.

Risk: Unlabeled, ambiguous, oversized, image/PDF, or poorly structured inputs may be insufficient or only partially in scope.

Mitigation: Provide labeled text or JSON input, convert images/PDFs to text first, and review checks_withheld or insufficient_input output before relying on the result.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/chenqg618/skills/invoice-consistency-check-free)
- [SkillPay paid upgrade listing referenced by the skill](https://skillpay.alipay.com/public/tokendidi)
- [SkillPay build guide referenced by the skill](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Plain text or JSON findings, with optional shell commands for running the local Node.js checker.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include severity, category, line, message, advice, evidence, executed checks, withheld checks, and insufficient-input status when needed.]

## Skill Version(s):

1.0.9 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
