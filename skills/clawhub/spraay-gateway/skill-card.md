## Description:

Spraay Gateway helps agents validate, estimate, and prepare user-confirmed calls to Spraay's external x402 payment gateway for batch stablecoin payouts, escrow, payroll, robot task payments, and token or chain-status lookups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[plagtech](https://clawhub.ai/user/plagtech)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to work with Spraay's gateway for validating and pricing batch payouts, checking token or chain data, and preparing paid or funds-moving API calls after explicit user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects to an external paid payment gateway and some workflows can lead to user spending or movement of user funds.

Mitigation: Review dry-run results and fee estimates, then require explicit user confirmation for each spend or funds-moving action.

Risk: SPRAAY_API_KEY grants access to paid gateway endpoints if configured.

Mitigation: Keep the key private and send it only to the intended Spraay Gateway host.

Risk: Changing SPRAAY_GATEWAY_URL could redirect requests to an untrusted gateway.

Mitigation: Use the default gateway unless the user intentionally selects a trusted self-hosted gateway.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/plagtech/skills/spraay-gateway)
- [Spraay Gateway homepage](https://gateway.spraay.app)
- [Spraay Gateway documentation](https://docs.spraay.app)
- [Endpoint examples](references/endpoints.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with curl examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses optional SPRAAY_API_KEY and SPRAAY_WALLET_ADDRESS environment variables; paid or money-moving workflows require explicit user confirmation.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
