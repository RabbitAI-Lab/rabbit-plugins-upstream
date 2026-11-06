## Description:

Read accesso-powered mobile ticket links (accessoticketing.com media-engine URLs from confirmation emails) — order number, per-ticket product, participant, date/time, barcodes, Google Wallet passes — with curl.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People with accesso Passport mobile-ticket links use this skill to retrieve order and per-ticket details, including dates, participants, barcode data, and Google Wallet pass URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A crafted ticket page can make barcode saving create files outside the selected folder.

Mitigation: Avoid --barcodes until filenames are sanitized, output paths are confined to the selected folder, and PNG content is validated.

Risk: Ticket URLs, Wallet links, and barcodes can expose private ticket access.

Mitigation: Use verified ticket links and keep ticket URLs, Wallet links, and barcodes private.

## Reference(s):

- [Ticket parser](references/parse-tickets.mjs)
- [Ticket usage recipes](references/recipes.md)
- [ClawHub release](https://clawhub.ai/chrischall/skills/accessoticketing-mcp)

## Skill Output:

**Output Type(s):** [JSON, PNG files, Shell commands, Guidance]

**Output Format:** [JSON ticket details, with optional PNG barcode files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Ticket fields vary by merchant; terms are optional, and barcode PNG files can be saved on request.]

## Skill Version(s):

1.2.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
