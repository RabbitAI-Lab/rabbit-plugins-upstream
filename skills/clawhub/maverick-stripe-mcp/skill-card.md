## Description:

Safely inspect Stripe payments, customers, invoices, and subscriptions through Stripe's official remote MCP with MCP-native OAuth and an allowlisted read-only tool set.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maverick](https://clawhub.ai/user/maverick)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, finance operators, and support teams use this skill to inspect single-account Stripe payments, customers, invoices, subscriptions, account context, and Stripe documentation through allowlisted read tools. It is intended for sandbox-first validation before account-data reads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may read live Stripe account data if the connected authorization is not confirmed as sandbox.

Mitigation: Use sandbox first and confirm whether the authorization is sandbox or live before account-data reads.

Risk: Re-running setup with stale OAuth values can overwrite a newer stored refresh token.

Mitigation: Run setup only after fresh authorization or intentional credential rotation.

Risk: The allowlist restricts tool names, while broad GET-style Stripe API paths may still reach unexpected readable resources.

Mitigation: Discover the live tool schema before use and review requested Stripe API paths before executing reads.

Risk: A saved local authorization state does not prove Stripe access remains valid after dashboard revocation.

Mitigation: Treat remote call success as the practical authorization check and disconnect or reauthorize when revocation is suspected.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/maverick/skills/maverick-stripe-mcp)
- [Stripe MCP overview and OAuth notes](https://docs.stripe.com/mcp)
- [Model Context Protocol authorization](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)
- [Stripe restricted API keys](https://docs.stripe.com/keys/restricted-api-keys)
- [mcporter config reference](https://github.com/openclaw/mcporter/blob/main/docs/config.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls]

**Output Format:** [Markdown guidance with shell commands and optional JSON MCP responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses allowlisted Stripe MCP read tools and OAuth-backed local credential storage.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
