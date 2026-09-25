## Description:

Read accesso-powered mobile ticket links (accessoticketing.com media-engine URLs from confirmation emails) -- order number, per-ticket product, participant, date/time, barcodes, Google Wallet passes -- with curl.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to extract structured details from accesso Passport ticket links they already possess, including order data, ticket fields, barcodes, and Google Wallet pass URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ticket URLs, Google Wallet save links, parser output, and exported barcode images can reveal or grant access to tickets.

Mitigation: Treat them as secrets, avoid placing them in commits, issues, or logs, and delete exported barcode files when they are no longer needed.

Risk: Expired or invalid accesso links can return HTTP 200 with a no-tickets body, so status-only checks can be misleading.

Mitigation: Use the parser body checks and refresh from the latest confirmation email when no tickets are found.

Risk: Accesso page layout changes can prevent reliable ticketId or Google Wallet URL mapping.

Mitigation: Review parser warnings and raw page bytes before relying on affected fields.

## Reference(s):

- [accesso ticket recipes](artifact/references/recipes.md)
- [parse-tickets.mjs](artifact/references/parse-tickets.mjs)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/accessoticketing-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, JSON, Files]

**Output Format:** [Markdown guidance with inline bash examples; parser output is structured JSON and optional PNG barcode files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Ticket URLs, Google Wallet save links, parser output, and exported barcode images should be treated as secrets.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
