## Description:

Guides agents in accessing a Crown Town Compost customer account through shell requests to review service history, invoices, upcoming pickups, and account details without the MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Customers and their authorized agents use shell-based guidance to check pickup history, billing, and upcoming service, or to manage their Crown Town Compost account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent session cookies could expose a live customer account if the cookie jar is accessed by others.

Mitigation: Use a temporary cookie jar restricted to the account owner (chmod 600), and delete it after use.

Risk: Commands can skip service, change profile details, contact support, report missed pickups, or request cancellation.

Mitigation: Require explicit confirmation before any account-changing action and re-read the account afterward to verify the result.

## Reference(s):

- [Crown Town Compost portal endpoint reference](artifact/references/endpoints.md)
- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/crowntowncompost-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can retrieve account data or submit account changes when authorized.]

## Skill Version(s):

1.1.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
