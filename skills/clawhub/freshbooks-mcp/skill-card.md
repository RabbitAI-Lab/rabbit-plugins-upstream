## Description:

Guides shell-based FreshBooks queries and updates using curl and rotating OAuth tokens.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and business users use this skill to retrieve FreshBooks invoices, clients, payments, expenses, projects, and time records from a shell without running an MCP server. It also provides examples for changing business records when explicitly authorized.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shell commands can create or modify financial and customer records, despite the query-focused description.

Mitigation: Require explicit human confirmation before POST, PUT, email, payment, invoice, or client-change commands; re-read changed records to verify the result.

Risk: OAuth credentials and rotating refresh tokens can expose business data or interrupt access if mishandled.

Mitigation: Use a dedicated FreshBooks app and least-privileged user, keep token state private, avoid logging tokens, and do not share a token state file between tools.

## Reference(s):

- [FreshBooks MCP release on ClawHub](https://clawhub.ai/chrischall/skills/freshbooks-mcp)
- [FreshBooks developer portal](https://my.freshbooks.com/#/developer)
- [FreshBooks shell recipes](references/recipes.md)
- [OAuth bootstrap helper](references/fb-bootstrap.mjs)
- [OAuth token helper](references/fb-token.sh)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands require FreshBooks OAuth credentials and appropriate account permissions.]

## Skill Version(s):

1.1.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
