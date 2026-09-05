## Description:

Read accesso-powered mobile ticket links from confirmation emails, including order number, per-ticket product, participant, date and time, barcodes, and Google Wallet pass links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to parse accesso Passport mobile-ticket URLs they are authorized to access and inspect ticket details, barcode data, and wallet-pass endpoints with command-line tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Accesso ticket URLs can grant access to usable tickets and barcodes.

Mitigation: Only provide ticket URLs the agent is authorized to inspect, and keep raw URLs, barcode files, and wallet-pass links out of public chats, issues, commits, and logs.

Risk: Parsed outputs can include scannable barcode data and Google Wallet pass URLs.

Mitigation: Treat generated JSON, PNG barcode files, and wallet-pass links as secrets; store them only in trusted local locations and delete them when no longer needed.

Risk: Expired or invalid links can return HTTP 200 with an error body, so status-only checks may be misleading.

Mitigation: Use the parser's body checks and error messages before relying on parsed ticket data.

## Reference(s):

- [accesso ticket recipes](references/recipes.md)
- [parse-tickets.mjs](references/parse-tickets.mjs)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/accessoticketing-mcp)
- [Publisher profile](https://clawhub.ai/user/chrischall)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with bash and jq examples; the parser produces JSON and can write PNG barcode files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Ticket URLs, barcode outputs, and wallet-pass links should be treated as secrets.]

## Skill Version(s):

0.2.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
