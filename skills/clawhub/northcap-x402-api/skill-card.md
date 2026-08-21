## Description:

Provides pay-per-call crypto trading signals with entry, stop-loss and take-profit via the x402 standard (USDC on Ethereum). Live DRT/ICT signals for agents and traders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[northcap-group](https://clawhub.ai/user/northcap-group)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to discover, purchase, and call a paid x402 crypto-signal API for BTC and altcoin trading signal data. The signals are informational and require payment, an API key, and acceptance of trading risk.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can cause an agent to spend USDC for paid crypto-signal API calls.

Mitigation: Install and run it only with explicit budget approval, and confirm the current price and endpoint before allowing calls.

Risk: The skill sends X402_API_KEY and request details to an external API endpoint.

Mitigation: Store the API key securely, limit its scope where possible, and use only the documented HTTPS endpoint.

Risk: Crypto trading signals may be incorrect or financially harmful if treated as guaranteed advice.

Mitigation: Treat signals as risky informational output and require human or policy review before any trading action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/northcap-group/skills/northcap-x402-api)
- [Northcap publisher profile](https://clawhub.ai/user/northcap-group)
- [Northcap x402 API endpoint](https://show-zum-anyway-sanyo.trycloudflare.com)

## Skill Output:

**Output Type(s):** [guidance, configuration, JSON]

**Output Format:** [Markdown instructions with JSON API response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires HTTPS network access, X402_API_KEY, and paid USDC calls before signal retrieval.]

## Skill Version(s):

1.0.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
