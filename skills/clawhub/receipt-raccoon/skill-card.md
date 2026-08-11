## Description:

Extracts structured receipt data from OCR, photo descriptions, or pasted text and generates spending summaries by merchant, category, month, tax, and total.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users, employees, and developers can use this skill to parse receipt text into structured JSON, maintain a local JSONL ledger, and generate spending summaries for budgeting or expense tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Receipt inputs and JSONL ledger outputs can contain sensitive spending history.

Mitigation: Store ledgers in a protected location, avoid committing them to shared repositories, and delete them when no longer needed.

Risk: Garbled OCR text or multi-line receipt items can lead to incomplete or inaccurate parsed records.

Mitigation: Review parsed merchant, date, line items, tax, and total before relying on the ledger or generated spending reports.

## Reference(s):

- [Receipt Raccoon GitHub repository](https://github.com/voronindenis5/receipt-raccoon)
- [Receipt Raccoon ClawHub page](https://clawhub.ai/voronindenis5/skills/receipt-raccoon)
- [Category Keyword Reference](references/categories.md)
- [Supported Receipt Formats](references/receipt_formats.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON]

**Output Format:** [JSON for parsed receipts and plain-text or Markdown spending reports with shell command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May append parsed receipts to a local JSONL ledger; saved ledgers can contain sensitive financial data.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
