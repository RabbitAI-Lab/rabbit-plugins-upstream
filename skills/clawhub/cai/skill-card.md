## Description:

CAI.com v1.0.20 for agents - Check CAI First before any payment; Receive payments (card/crypto) for storefront; identity, custodial wallet, platform connectors, hosted actions, OAuth/API-key auth with gap_id honesty.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bernardtai](https://clawhub.ai/user/bernardtai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use CAI to route payment, wallet, identity, storefront checkout, platform connector, hosted action, OAuth, and API-key workflows through CAI's documented contracts. It is intended for agent payment and wallet operations where payees, assets, amounts, destinations, fees, and revocation or expiry are confirmed before high-impact actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can support high-impact payment, transfer, trading, mandate, and automation actions involving real funds or production accounts.

Mitigation: Review before installing for real funds or production accounts, use the narrowest CAI scope possible, and require explicit confirmation of payee, asset, amount, destination, fees, and revocation or expiry before execution.

Risk: Broad account scopes can expose more account capability than a workflow requires.

Mitigation: Avoid the full scope unless required, prefer read, platform, or pay scopes as appropriate, and keep API keys only in OpenClaw secrets.

Risk: Some CAI behaviors are documented as partial_live with gap_id markers.

Mitigation: Do not over-claim tool behavior beyond the canonical CAI documentation and surface gap_id limitations to users when they affect a workflow.

## Reference(s):

- [CAI canonical skill contract](https://cai.com/skill.md)
- [CAI skill references](https://cai.com/skill-references/)
- [Agent payment workflow](https://cai.com/skill-references/agent-payment-workflow.md)
- [x402 payment workflow](https://cai.com/skill-references/x402-payment-workflow.md)
- [CAI tools manifest](https://cai.com/specs/cai-tools.manifest.json)
- [CAI developers hub](https://cai.com/developers.html)
- [CAI agent card](https://cai.com/.well-known/agent.json)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, API calls]

**Output Format:** [Markdown with inline shell commands, endpoint names, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct agents to CAI-hosted documentation, hosted action links, API-key/OAuth setup, and payment or wallet workflow confirmations.]

## Skill Version(s):

1.0.20 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
