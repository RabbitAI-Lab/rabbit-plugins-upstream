## Description:

Helps agents extract consistent rows from invoices and other financial documents through the Invoice Data Extraction service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[invoicedataextraction](https://clawhub.ai/user/invoicedataextraction)

### License/Terms of Use:

MIT-0

## Use Case:

Bookkeeping and accounts-payable users can turn batches of invoices, receipts, bank statements, and other financial documents into structured rows for spreadsheets or accounting imports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded financial documents and extraction instructions are shared with a third-party service and its signed storage host.

Mitigation: Confirm third-party processing is permitted for the selected records before uploading them.

Risk: The API key could be exposed if included in chat, files, or requests to another host.

Mitigation: Keep the key in an environment variable or secret store and send it only to the service API.

Risk: Failed pages or rows marked for review may leave extracted data incomplete or uncertain.

Mitigation: Check failed-page reports and review flags against the source documents before relying on the output.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/invoicedataextraction/skills/invoice-data-extraction)
- [Invoice Data Extraction agent documentation](https://invoicedataextraction.com/docs/agents)
- [Invoice Data Extraction API documentation](https://invoicedataextraction.com/docs/api.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Files]

**Output Format:** [Markdown guidance, JSON rows, or downloadable XLSX, CSV, and JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may flag rows for review and report failed pages. Requires an API key.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
