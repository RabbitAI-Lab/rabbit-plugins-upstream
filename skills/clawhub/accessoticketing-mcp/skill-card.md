## Description:

Reads accesso mobile-ticket links from confirmation emails to extract order details, ticket information, barcodes, and Google Wallet pass links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People managing accesso-powered mobile tickets can use this skill to review order and per-ticket details, retrieve wallet pass links, and optionally export scannable barcodes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ticket links, barcode values, and wallet links can grant access to tickets if shared.

Mitigation: Treat these values as secrets and avoid sharing them or placing them in commits and issues.

Risk: Exported barcode images can remain accessible after use.

Mitigation: Avoid shared, synced, or long-lived storage and delete exported images when finished.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/accessoticketing-mcp)
- [Ticket parsing and usage recipes](references/recipes.md)
- [Ticket parser](references/parse-tickets.mjs)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Files]

**Output Format:** [JSON ticket details and optional PNG barcode files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include order details, participants, dates, barcode values, and Google Wallet pass links.]

## Skill Version(s):

1.0.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
