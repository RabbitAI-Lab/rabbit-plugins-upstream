## Description:

Reads accesso-powered mobile ticket links from confirmation emails and extracts order details, ticket fields, barcodes, and Google Wallet pass URLs with curl and a dependency-free Node parser.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to process user-provided accesso Passport ticket links, inspect order and per-ticket details, and optionally prepare barcode or Google Wallet outputs for the ticket holder.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ticket URLs, Google Wallet URLs, parsed JSON, and barcode PNGs can grant access to tickets.

Mitigation: Process only user-provided ticket links, store outputs in private locations, avoid committing or sharing credentials, and delete generated barcode files when no longer needed.

Risk: Expired or invalid ticket links can return HTTP 200 while containing no usable tickets.

Mitigation: Check parser exit codes and messages before relying on extracted ticket data.

Risk: Merchant page structure can drift, which may affect ticketId and Google Wallet URL mapping.

Mitigation: Treat parser warnings about count mismatches as blocking for Wallet URL use and re-check the source page before trusting those fields.

## Reference(s):

- [parse-tickets.mjs](references/parse-tickets.mjs)
- [accesso ticket recipes](references/recipes.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON output from the parser]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can write barcode PNG files when requested; parsed JSON and generated barcode files may contain sensitive ticket credentials.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
