## Description:

Read accesso-powered mobile ticket links from confirmation emails, including order number, per-ticket product, participant, date/time, barcodes, and Google Wallet passes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Accesso Passport mobile-ticket links from confirmation emails, extract order and ticket details, and optionally produce barcode files or Google Wallet pass links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ticket URLs contain bearer-secret order tokens that can expose tickets and barcodes.

Mitigation: Use only trusted ticket URLs, avoid putting them in logs or shared files, and treat generated barcode images, JWTs, and Google Wallet links as secrets.

Risk: The security evidence notes an overbroad URL fetch path.

Mitigation: Review before installation and restrict fetching to expected Accesso HTTPS hosts where possible.

Risk: Google Wallet link generation can create third-party pass links from live ticket tokens.

Mitigation: Confirm the need for wallet-link creation and warn users before generating or sharing those links.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/accessoticketing-mcp)
- [parse-tickets.mjs](artifact/references/parse-tickets.mjs)
- [accesso ticket recipes](artifact/references/recipes.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands; parser output is JSON with optional PNG barcode files and Google Wallet URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Ticket URLs, barcode images, JWTs, and wallet links should be treated as secrets.]

## Skill Version(s):

0.2.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
