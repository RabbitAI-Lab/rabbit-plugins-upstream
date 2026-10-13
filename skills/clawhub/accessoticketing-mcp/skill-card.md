## Description:

Reads accesso mobile-ticket links to extract order and ticket details, barcodes, and Google Wallet pass links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Ticket holders and their agents use the skill to inspect accesso confirmation links, summarize ticket times and participants, and retrieve barcodes or Google Wallet pass links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ticket URLs, barcodes, parsed JSON, and wallet links may function as live ticket credentials.

Mitigation: Keep them out of issues, commits, shared chats, logs, screenshots, and synced folders; delete exported barcode files when no longer needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/accessoticketing-mcp)
- [Ticket parsing recipes](references/recipes.md)
- [Ticket parser](references/parse-tickets.mjs)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON, PNG images]

**Output Format:** [Text and shell commands; structured JSON ticket details and optional PNG barcodes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Ticket links, parsed details, barcode files, and wallet links can grant access to tickets.]

## Skill Version(s):

1.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
