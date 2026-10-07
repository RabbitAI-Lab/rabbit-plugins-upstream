## Description:

Reads accesso-powered mobile ticket links to extract order and ticket details, barcodes, and Google Wallet links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Ticket holders and their assistants use this skill to read accesso mobile-ticket links and summarize order details, attendance times, barcodes, and wallet-pass options.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ticket links, parsed details, wallet URLs, and saved barcodes can expose access to tickets.

Mitigation: Treat these as secrets; keep them out of logs, commits, shared chats, and issue trackers.

Risk: Fetching an untrusted ticket URL can contact an unintended destination.

Mitigation: Use URL mode only with trusted accesso ticket links.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/accessoticketing-mcp)
- [Ticket parsing script](artifact/references/parse-tickets.mjs)
- [Ticket usage recipes](artifact/references/recipes.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON, PNG images]

**Output Format:** [Markdown guidance and structured ticket JSON; optional PNG barcode files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Ticket JSON may include order details, attendee names, barcodes, and Google Wallet URLs.]

## Skill Version(s):

1.0.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
