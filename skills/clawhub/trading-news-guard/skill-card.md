## Description:

Paid news-status check before trading: fetch live high-impact event data for NFP, CPI, and FOMC via the x402 pay-per-call API and report whether a blackout window is active.

This skill is ready for commercial/non-commercial use.

## Publisher:

[northcap-group](https://clawhub.ai/user/northcap-group)

### License/Terms of Use:

MIT-0

## Use Case:

External users and trading-agent developers use this skill to request current high-impact market news status before a trade entry. The skill returns data for the agent to decide whether to pause trading during a blackout window.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a spending-capable X402_API_KEY for paid per-call API requests.

Mitigation: Use a dedicated low-limit key, monitor usage, and run the skill only when paid requests are intended.

Risk: The default service is a raw-IP HTTPS endpoint, and X402_BASE can redirect requests to another endpoint.

Mitigation: Keep X402_BASE unset or set it only to a trusted HTTPS provider; do not enable X402_ALLOW_HTTP outside a controlled test environment.

Risk: API failures can leave the agent without current news-status data before a trade decision.

Mitigation: Treat API failures as a trading blackout, matching the skill guidance to fail closed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/northcap-group/skills/trading-news-guard)
- [x402 API](https://github.com/MohamedAbdisamed/x402-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python 3, network access to the configured x402 endpoint, and X402_API_KEY.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
