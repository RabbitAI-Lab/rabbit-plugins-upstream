## Description:

Reads accesso-powered mobile ticket links to extract order and ticket details, barcodes, and Google Wallet pass links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Ticket holders and their authorized assistants use this skill to retrieve order details, check dates and participants, and access ticket barcodes or wallet passes from confirmation links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ticket links and wallet pass links can grant access to live tickets and barcodes.

Mitigation: Use only links you are authorized to access; treat links, JWTs, barcodes, and parsed ticket data as credentials and do not share or publish them.

Risk: Exported barcode images and saved ticket details can expose tickets if stored in shared or synced locations.

Mitigation: Export to a private, non-synced location and remove saved outputs when no longer needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/accessoticketing-mcp)
- [Ticket parsing reference](references/parse-tickets.mjs)
- [Ticket usage recipes](references/recipes.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON, Files]

**Output Format:** [Ticket details as JSON; optional barcode PNG files and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include order numbers, participant details, barcodes, and wallet pass links.]

## Skill Version(s):

1.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
