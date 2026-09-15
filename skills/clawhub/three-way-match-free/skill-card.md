## Description:

Checks purchase orders, goods receipts, and invoices for cross-document mismatches, duplicate invoice numbers, and leftover template placeholders, with each finding tied to source line evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, accounts payable, procurement, and operations users can run the skill before payment approval to compare purchase order, receipt, and invoice text for key field, quantity, unit price, amount, duplicate invoice, and placeholder issues. It is also useful for agents that need deterministic local checks with JSON or readable findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional full-edition purchase path asks the agent to run an unpinned remote installer and delegate to another installed skill.

Mitigation: Before any purchase or install step, review the package source, version, publisher, payment destination, and newly installed instructions; require the human user to confirm wallet authorization or payment.

Risk: The free checker covers only the listed matching checks and can miss issues outside that scope.

Mitigation: Use the results as local evidence for the covered checks only, and keep finance approval, invoice authenticity, supplier qualification, and withheld checks in the normal review process.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/three-way-match-free)
- [SkillPay full-edition shelf](https://skillpay.alipay.com/public/tokendidi)
- [SkillPay installation and purchase guide](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance and command output, with optional JSON results from the local Node runner]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include severity, category, line references, evidence snippets, and advice; insufficient input returns no conclusion.]

## Skill Version(s):

1.0.5 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
