## Description:

Reads accesso mobile ticket links to identify orders, participants, dates, barcodes, and Google Wallet passes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Ticket holders and their assistants use this skill to inspect accesso ticket links from confirmation emails and summarize order details, schedules, and available barcodes or wallet passes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ticket URLs and embedded tokens can grant access to orders and barcodes.

Mitigation: Treat links and tokens like passwords; do not commit or share them in public chats or issues.

Risk: Parser output, barcode images, and Google Wallet links may expose ticket details or enable ticket use.

Mitigation: Keep outputs private and avoid leaving exported barcode files in accessible locations.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/accessoticketing-mcp)
- [Ticket parsing recipes](references/recipes.md)
- [Ticket parser](references/parse-tickets.mjs)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance and shell commands; structured ticket data as JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional barcode PNG files and Google Wallet links; outputs may contain sensitive ticket credentials and personal details.]

## Skill Version(s):

1.0.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
