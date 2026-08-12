## Description:

Extracts structured receipt data from OCR or pasted receipt text and generates spending summaries by merchant, category, and total spend.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to parse receipt text from OCR, photo descriptions, copied text, or files into structured records and spending reports. It supports local expense tracking through JSON output, optional JSONL ledger append, and text or JSON report generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Receipt text and JSONL ledgers may contain sensitive financial records.

Mitigation: Store ledgers in a private location, avoid committing them to public repositories, and delete or protect old ledger files when no longer needed.

Risk: Garbled OCR, multi-line items, discounts, non-USD receipts, or unusual quantity formats can produce incomplete or inaccurate parsed records.

Mitigation: Review parsed merchant, date, item, tax, total, currency, and category fields before using reports for budgeting or business decisions.

## Reference(s):

- [Source repository](https://github.com/voronindenis5/receipt-raccoon)
- [Category Keyword Reference](references/categories.md)
- [Supported Receipt Formats](references/receipt_formats.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON, files]

**Output Format:** [Markdown guidance with shell commands; parser output is JSON, JSONL ledger files, or plain-text spending reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Python 3.10+ stdlib; optional ledger append writes parsed receipts to a user-specified JSONL file.]

## Skill Version(s):

0.1.1 (source: server release evidence; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
