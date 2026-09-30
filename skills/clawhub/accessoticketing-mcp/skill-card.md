## Description:

Reads accesso-powered mobile ticket links to extract order details, ticket holders, dates, barcodes, and Google Wallet pass links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Ticket holders and their assistants use this skill to read accesso mobile-ticket links from confirmation emails and organize ticket details, barcodes, and wallet-pass links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ticket links and wallet-pass URLs grant access to tickets and may be exposed if shared or committed.

Mitigation: Treat ticket URLs, barcode text, and wallet-pass links as secrets; do not paste, share, or commit them.

Risk: Exported barcode PNGs can be used like the tickets they represent.

Mitigation: Export barcodes only when needed and choose a private output directory.

## Reference(s):

- [ClawHub release listing](https://clawhub.ai/chrischall/skills/accessoticketing-mcp)
- [Ticket parsing recipes](artifact/references/recipes.md)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Files]

**Output Format:** [JSON ticket details, shell examples, and optional PNG barcode files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Barcode files are written only when requested; dates and times remain in the merchant's local format.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
