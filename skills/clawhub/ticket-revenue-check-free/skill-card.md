## Description:

A local checker for ticket revenue and channel settlement tables that recomputes row-level ticket revenue, channel commission, refunds, settlement amounts, and total-row arithmetic without validating box-office authenticity or tax treatment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and ticket-settlement staff at venues, performance companies, scenic attractions, and ticketing operators use this skill to check monthly channel settlement tables for arithmetic mismatches, duplicate order numbers, missing fields, placeholders, negative values, and total-row inconsistencies. It supports review of the supplied table only and does not verify real ticket sales, bank receipts, contract terms, or taxes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat arithmetic checks as confirmation that ticket sales, channel receipts, contract terms, or tax treatment are correct.

Mitigation: Use the output as a table-internal arithmetic review only and verify sales records, bank receipts, channel contracts, invoices, and tax positions through the appropriate source systems and professional review.

Risk: The checker requires exported table text and does not read original Excel, ticketing-system, or channel-statement files directly.

Mitigation: Export or copy the table with headers into the expected text or JSON input format, then retain the original source files for audit and reconciliation.

Risk: The skill is primarily documented and presented in Chinese, which may limit effective review by non-Chinese-speaking users.

Mitigation: Use it only where reviewers understand the Chinese prompts and findings, or translate and validate the output before relying on it.

Risk: Documentation mentions anonymous usage statistics while the security guidance notes that this appears unimplemented in inspected code.

Mitigation: Review the installed package behavior before deployment and ask the publisher to align documentation with the shipped implementation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/ticket-revenue-check-free)
- [artifact/SKILL.md](artifact/SKILL.md)
- [artifact/templates/sample.json](artifact/templates/sample.json)

## Skill Output:

**Output Type(s):** [analysis, json, shell commands, guidance]

**Output Format:** [Markdown status text or JSON containing ok, tier, capability, checks_given, checks_withheld, result.scope, findings, summary, and checks_out_of_scope.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include severity level, category, source line, message, and advice; insufficient inputs return missing-field guidance and no positive conclusion.]

## Skill Version(s):

1.0.1 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
