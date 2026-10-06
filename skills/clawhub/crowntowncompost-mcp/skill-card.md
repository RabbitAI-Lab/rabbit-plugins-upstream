## Description:

Guides an agent through accessing Crown Town Compost customer information and submitting service requests from a shell without an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Crown Town Compost customers and their authorized agents can check pickup history, invoices, upcoming service, and account details, or prepare service and account changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated requests can change live service or account settings.

Mitigation: Require explicit review before skip, account update, support, missed-pickup, or cancellation-related requests; re-read the account to verify changes.

Risk: Persistent login cookies may expose access to the customer account.

Mitigation: Keep the cookie jar temporary or restrict it to the owner with chmod 600, and delete it after use.

Risk: Account responses can contain contact and billing information.

Mitigation: Avoid logging or exporting billing and contact data unless needed.

## Reference(s):

- [Portal endpoint reference](artifact/references/endpoints.md)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/crowntowncompost-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May surface private account and billing information; account-changing requests require review.]

## Skill Version(s):

1.1.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
