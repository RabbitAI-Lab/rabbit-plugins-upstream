## Description:

Deploy a new AI agent on AgentsPodium and pay for it in crypto over HTTP without a browser.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samorodkin](https://clawhub.ai/user/samorodkin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to provision always-on AgentsPodium agents over HTTP, handle token-based setup, create crypto payment orders, and retrieve deployed agent addresses for follow-on automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent may create paid crypto orders or initiate payment-related actions without sufficient user confirmation.

Mitigation: Require explicit user approval before creating crypto orders or sending funds, and use accounts and wallets with limited balances.

Risk: Mailbox or bearer-token access can give an agent durable control over deployment workflows.

Mitigation: Use a dedicated mailbox or mail API scope for verification codes, cache tokens securely, and avoid granting broad mailbox access.

Risk: Lifecycle actions such as deletion can have high operational impact.

Mitigation: Require explicit confirmation before deletion and prefer pause when the user's intent is unclear.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/samorodkin/skills/deploy-agent)
- [AgentsPodium API Base URL](https://app.agentspodium.com/api)
- [AgentsPodium Webhook Documentation](https://hosting.defispace.com/docs/webhooks.md)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Shell commands, Configuration]

**Output Format:** [Markdown guidance with HTTP endpoint examples and JSON request and response snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes deployment, authentication, crypto payment, webhook, A2A endpoint, and lifecycle management guidance.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
