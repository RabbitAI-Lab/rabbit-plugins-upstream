## Description:

Manage Dub short links, track conversions, and read link attribution analytics through the superagnt unified API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent manage Dub short links, conversion tracking, customer records, custom domains, partner workflows, commissions, and attribution analytics through the Superagnt connection API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform destructive or account-changing Dub operations, including deletes, customer or domain changes, partner bans or deactivations, bounty decisions, and commission updates.

Mitigation: Require explicit user confirmation before destructive, outbound, payout-related, or record-changing actions, and limit calls to endpoints needed for the user's request.

Risk: The integration operates against the user's connected Dub workspace through Superagnt.

Mitigation: Install only when the user trusts Superagnt and intends to let an agent operate that connected workspace.

Risk: Calls depend on the user's Dub credentials, vendor-side rate limits, and billing.

Mitigation: Verify the Superagnt API key and Dub connection before use, and treat vendor connection or rate-limit errors as operational constraints for the user's account.

## Reference(s):

- [Superagnt Dub Documentation](https://superagnt.com/r/ch-dub-links-docs)
- [ClawHub Listing](https://clawhub.ai/superagnt/skills/dub-links)
- [Superagnt Connections Dashboard](https://app.superagnt.com/dashboard/connections)
- [Superagnt MCP Server](https://mcp.superagnt.com/mcp)
- [MCP Client Setup](https://mcp.superagnt.com/agent-setup/prompt.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls]

**Output Format:** [Markdown with inline bash commands and JSON API schema examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY and a connected Dub account.]

## Skill Version(s):

2.0.6 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
