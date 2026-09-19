## Description:

Read accesso-powered mobile ticket links from accessoticketing.com confirmation emails, including order number, ticket details, dates, times, barcodes, and Google Wallet pass links, using curl and a dependency-free Node parser.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to inspect user-provided accesso Passport mobile-ticket links and extract ticket metadata, barcode data, and wallet-pass endpoints into structured output. It is useful when a ticket confirmation email contains a media-engine accessoticketing.com URL that needs to be resolved or summarized without a browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ticket URLs, oToken and cToken values, barcode images, Google Wallet JWTs, and generated save links can grant access to tickets.

Mitigation: Treat these values like passwords: do not paste them into shared logs, commits, issues, or transcripts, and delete generated barcode files when no longer needed.

Risk: Expired or invalid accesso links may return HTTP 200 with an unavailable-ticket message, so status code alone can be misleading.

Mitigation: Use the parser's body checks and exit-code handling before relying on parsed ticket output.

Risk: Accesso page layout changes or ticketId count mismatches can make wallet-pass URLs unreliable.

Mitigation: Review parser warnings and re-check the raw page before trusting ticketId or googleWalletUrl values when counts disagree.

## Reference(s):

- [accesso ticket recipes](artifact/references/recipes.md)
- [parse-tickets.mjs](artifact/references/parse-tickets.mjs)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/accessoticketing-mcp)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, JSON, files]

**Output Format:** [Markdown guidance with inline shell commands; parser output is structured JSON and optional PNG barcode files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include secret-bearing ticket URLs, barcode values, Google Wallet URLs, and generated barcode image paths.]

## Skill Version(s):

0.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
