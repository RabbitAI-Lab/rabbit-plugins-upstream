## Description:

A free local invoice and expense-claim consistency checker that reports recomputable arithmetic, text, duplicate-invoice, date, placeholder, and party-name findings with cited evidence from the supplied invoice text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, operations, and reimbursement reviewers use this skill to check invoice or expense-claim text before submission or review. It helps identify internal inconsistencies in amounts, taxes, dates, invoice duplicates, placeholders, and purchaser or reimbursement entity names.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A clean consistency result can be mistaken for invoice authenticity, tax compliance, or approval to reimburse.

Mitigation: Use the findings as a pre-review aid only; keep tax verification, audit judgment, business approval, and policy checks in the normal human review process.

Risk: The checker can miss issues when source material is image-only, unlabeled, sparsely labeled, or arranged in complex multi-line layouts.

Mitigation: Provide clear OCR or text with labels for invoice numbers, dates, amounts, tax rates, parties, and line items, and manually review cases that return insufficient input or no recognizable objects.

Risk: Party-name matching only normalizes punctuation and whitespace, so abbreviations, aliases, or historical company names may be flagged or missed.

Mitigation: Treat party-name findings as prompts for confirmation against vendor, customer, or company master data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chenqg618/skills/invoice-consistency-check-free)
- [Free Web Checker](https://www.tokendidi.cn/check)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Plain text or JSON findings with severity, category, line, message, advice, evidence, summary counts, checks run, and checks withheld.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally over supplied invoice text; returns insufficient-input status rather than a clean finding when the input lacks enough recognizable invoice elements.]

## Skill Version(s):

1.0.5 (source: server release evidence; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
