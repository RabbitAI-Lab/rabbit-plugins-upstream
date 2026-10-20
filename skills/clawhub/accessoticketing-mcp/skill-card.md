## Description:

Read accesso-powered mobile ticket links (accessoticketing.com media-engine URLs from confirmation emails) — order number, per-ticket product, participant, date/time, barcodes, Google Wallet passes — with curl.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Ticket holders and developers can use the skill to read order and ticket details from accesso mobile-ticket links, including participant, product, date, and time information. It can also expose barcode data, optionally save barcode images, and help retrieve Google Wallet links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Barcode export can create files outside the folder you choose if filenames are manipulated.

Mitigation: Avoid barcode export until filenames are sanitized and output paths are confined to your chosen folder.

Risk: Ticket and Wallet links grant access to tickets and barcodes.

Mitigation: Keep ticket and Wallet links private; do not paste them into files, commits, or issues.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/accessoticketing-mcp)
- [Ticket parser](artifact/references/parse-tickets.mjs)
- [Ticket usage recipes](artifact/references/recipes.md)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Files]

**Output Format:** [JSON ticket data on stdout, with optional barcode PNG files and Google Wallet links]

**Output Parameters:** [Ticket URL or saved page; optional barcode output directory]

**Other Properties Related to Output:** [Ticket and Wallet URLs contain access credentials and should be kept private.]

## Skill Version(s):

1.1.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
