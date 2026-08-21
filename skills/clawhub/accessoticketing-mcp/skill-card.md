## Description:

Read accesso-powered mobile ticket links (accessoticketing.com media-engine URLs from confirmation emails) - order number, per-ticket product, participant, date/time, barcodes, Google Wallet passes - with curl.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, support teams, and ticket holders use this skill to inspect user-provided accesso Passport ticket links and extract order, attendee, schedule, barcode, and Google Wallet pass details without a browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ticket URLs, parsed barcodes, wallet endpoint URLs, JWTs, and generated save links can function as bearer secrets for ticket access.

Mitigation: Treat these values as secrets: avoid committing, logging, pasting into issues, or sharing them, and store generated barcode files only in locations appropriate for sensitive ticket data.

Risk: Expired or invalid accesso links can return HTTP 200 with an unavailable-ticket message, so status code alone can mislead users.

Mitigation: Use the parser's body checks and exit codes to distinguish expired links or layout drift from successful ticket extraction.

## Reference(s):

- [Parser script](references/parse-tickets.mjs)
- [Accesso ticket recipes](references/recipes.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/accessoticketing-mcp)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, files]

**Output Format:** [Markdown guidance with bash examples; parser output is JSON with optional PNG barcode files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Handles user-provided ticket URLs, saved HTML, or stdin; optional flags include barcode image export and terms inclusion.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
