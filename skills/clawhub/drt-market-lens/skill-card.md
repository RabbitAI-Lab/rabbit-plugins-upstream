## Description:

Live market data + ICT bias for 17 instruments (indices, forex, metals, crypto) via the x402 pay-per-call API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[northcap-group](https://clawhub.ai/user/northcap-group)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and trading-focused agents use this skill to retrieve 1-hour market candles and daily ICT-style bias signals for supported indices, forex, metals, and crypto instruments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The X402_API_KEY can spend value through pay-per-call API requests.

Mitigation: Use a trusted x402 API provider, apply spending controls where available, and keep the key out of untrusted environments.

Risk: Changing X402_BASE can send market-data requests and the spending-capable API key to a different host.

Mitigation: Set X402_BASE only to trusted HTTPS endpoints and avoid X402_ALLOW_HTTP except on a secure local network.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/northcap-group/skills/drt-market-lens)
- [Publisher profile](https://clawhub.ai/user/northcap-group)
- [x402 API key and purchase reference](https://github.com/MohamedAbdisamed/x402-api)
- [Default x402 API endpoint](https://186.240.156.169:8791)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration guidance]

**Output Format:** [JSON responses from Python command-line scripts, with setup guidance in Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python 3, network access to the configured x402 endpoint, and X402_API_KEY.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
