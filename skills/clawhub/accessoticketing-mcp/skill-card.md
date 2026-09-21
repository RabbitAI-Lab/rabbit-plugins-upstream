## Description:

Read accesso-powered mobile ticket links from confirmation emails to extract order numbers, ticket details, participants, dates and times, barcodes, and Google Wallet pass links with curl.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technically comfortable users use this skill to inspect accesso Passport ticket links from confirmation emails and turn them into structured ticket data, barcode assets, and Google Wallet pass links. It is intended for cases where the user already has the ticket URL and needs curl-oriented parsing and recipes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ticket URLs, parsed JSON, barcode PNGs, Google Wallet URLs, and JWT/save links may allow ticket use if exposed.

Mitigation: Treat these values as secrets; store generated barcode files only in private directories and avoid commits, shared folders, issues, and support tickets.

Risk: The skill fetches and parses user-provided accesso ticket links, including links that can expire or return a no-tickets page.

Mitigation: Review the destination before running commands and rely on the parser's no-ticket and HTTP-error handling rather than HTTP status alone.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/chrischall/skills/accessoticketing-mcp)
- [recipes.md](references/recipes.md)
- [parse-tickets.mjs](references/parse-tickets.mjs)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JavaScript parser usage, and JSON output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The referenced parser can optionally write barcode PNG files when run with --barcodes.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
