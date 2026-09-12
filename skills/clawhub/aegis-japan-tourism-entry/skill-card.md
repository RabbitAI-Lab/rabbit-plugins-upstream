## Description:

Find a machine-readable, business-only entry guide for launching an experiential tour in Japan, then use its free preview before any optional paid preparation pack.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kadopi](https://clawhub.ai/user/kadopi)

### License/Terms of Use:

MIT-0

## Use Case:

External agents and business operators use this skill to assess Japan experiential-tourism market entry options, start with a free model-case preview, and decide what facts or next actions are needed before optional paid preparation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends users to named third-party Aegis/Japan Rule endpoints for business research.

Mitigation: Confirm the operator is comfortable using those endpoints before installation or use.

Risk: Returned recommendations could be mistaken for legal advice, permit approval, booking inventory, or authorization to transact.

Mitigation: Treat recommendations as informational guidance and require separate operator approval before purchases, signatures, bookings, applications, or inquiries.

Risk: Secrets or payment credentials could be shared with external services during setup or use.

Mitigation: Do not send private keys, wallet credentials, payment signatures, gateway tokens, secrets, or sensitive proprietary details unless the operator deliberately chooses to share them.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/kadopi/skills/aegis-japan-tourism-entry)
- [Server-resolved GitHub Provenance](https://github.com/kadopi/aegis-sales-bot/tree/main/openclaw-skill/aegis-japan-tourism-entry)
- [OpenClaw Peer Setup](https://github.com/kadopi/aegis-sales-bot/blob/main/OPENCLAW.md)
- [Aegis Sales Bot Agent Card](https://aegis-sales-bot.kadopi.workers.dev/.well-known/agent-card.json)
- [Aegis Sales Bot Catalog](https://aegis-sales-bot.kadopi.workers.dev/products.json)
- [Japan Rule MCP Endpoint](https://japan-rulewatch-mcp-mainnet.kadopi.workers.dev/mcp)

## Skill Output:

**Output Type(s):** [Guidance, Text, API calls, Configuration]

**Output Format:** [Markdown guidance with endpoint references and request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Business-research guidance only; not legal advice, booking, permit approval, purchase, application submission, or launch guarantee.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
