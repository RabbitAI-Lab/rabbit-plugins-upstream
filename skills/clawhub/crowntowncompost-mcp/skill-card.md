## Description:

Guides agents through accessing a Crown Town Compost customer account from a shell to review service history, invoices, upcoming pickups, and account details without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Crown Town Compost customers and developers can use this skill to check pickups, service dates, and invoices through their customer portal, or to prepare account updates and service requests with confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Portal credentials and saved session cookies can expose a customer's account.

Mitigation: Use a password manager or interactive prompt instead of long-lived exported passwords; restrict access to and delete the cookie jar after use.

Risk: Skip requests, account updates, support messages, missed-pickup reports, and cancellation requests can change an account or contact the service provider.

Mitigation: Require deliberate confirmation before submitting these requests and recheck the account afterward to verify the intended change.

## Reference(s):

- [Crown Town Compost portal endpoint reference](references/endpoints.md)
- [Crown Town Compost customer portal](https://portal.crowntowncompost.com)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/crowntowncompost-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may return portal account data, including service and billing history.]

## Skill Version(s):

1.1.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
