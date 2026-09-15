## Description:

Locally checks R&D super-deduction collection worksheets for row totals, aggregate totals, duplicate or blank projects, and the unified cap for other related expenses, with each finding tied to source lines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, tax, and operations teams at companies with R&D spending use this skill during quarterly prepayment and annual settlement reviews to reconcile R&D expense collection worksheets before relying on the figures. It is a worksheet reconciliation aid and does not provide tax advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill text includes an optional paid upgrade flow that asks an agent to run an unpinned remote installer.

Mitigation: Do not let an agent run the upgrade command or install the paid version automatically; independently verify the package source, exact version, and onboarding instructions first.

Risk: The workflow involves payment or wallet approval for the optional full version.

Mitigation: Keep payment approval manual and require the user to confirm any official link, QR code, wallet authorization, or purchase step personally.

Risk: Worksheet reconciliation findings may be mistaken for tax advice or may be affected by malformed and unusual numeric cells.

Mitigation: Treat the checker as a reconciliation aid, review unusual cells manually, and obtain qualified tax review before making filing decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/rd-expense-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)
- [SkillPay shelf referenced by the skill](https://skillpay.alipay.com/public/tokendidi)
- [SkillPay installation guide referenced by the skill](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Shell commands, Guidance]

**Output Format:** [Human-readable console text or JSON findings, often accompanied by Markdown instructions and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source lines; insufficient input produces missing-field guidance instead of a pass/fail conclusion.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
