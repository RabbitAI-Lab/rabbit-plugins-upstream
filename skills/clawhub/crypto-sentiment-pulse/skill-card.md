## Description:

Crypto Fear & Greed index and market sentiment via the x402 pay-per-call API, with explicit disclosure that each run costs money and sends the configured API key to the API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[northcap-group](https://clawhub.ai/user/northcap-group)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent builders use this skill to fetch crypto Fear & Greed and market sentiment data before an agent evaluates a trading or market-positioning decision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Each run can spend funds through a billing-capable x402 API key.

Mitigation: Use only scoped, low-limit, rotatable keys and run the skill only when a paid sentiment lookup is intended.

Risk: The default paid API endpoint is identified by raw IP and X402_BASE can redirect calls to another host.

Mitigation: Confirm the API operator and endpoint before use, and avoid setting X402_BASE to untrusted hosts.

Risk: Enabling HTTP would send a spending-capable key over an unencrypted connection.

Mitigation: Keep HTTPS enabled and do not set X402_ALLOW_HTTP=1 unless the plaintext-key risk is explicitly accepted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/northcap-group/skills/crypto-sentiment-pulse)
- [Configured x402 API endpoint](https://186.240.156.169:8791)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON returned by the sentiment script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python 3, network access to the configured x402 endpoint, and X402_API_KEY.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
