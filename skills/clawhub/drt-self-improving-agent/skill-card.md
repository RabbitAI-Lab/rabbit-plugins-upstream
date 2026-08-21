## Description:

Self-improving DRT/ICT trading agent that journals trades, analyzes win/loss patterns, and builds a personal trading memory for future trade review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[northcap-group](https://clawhub.ai/user/northcap-group)

### License/Terms of Use:

MIT-0

## Use Case:

External users and trading workflow developers use this skill to record DRT/ICT trade outcomes, review setup patterns, and optionally query a premium x402 signal endpoint. It supports journaling and analysis; it does not guarantee trading performance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional x402 signal script sends an API key to an external endpoint when run.

Mitigation: Set X402_API_KEY only when the user trusts the destination service, and avoid overriding X402_BASE unless intentionally changing where the key is sent.

Risk: Trade analysis may be based on limited or biased journal data and can produce misleading confidence in a setup.

Mitigation: Treat analysis as decision support, review sample sizes and assumptions, and keep independent risk controls such as stop losses and trade limits.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/northcap-group/skills/drt-self-improving-agent)
- [x402 signal service endpoint](https://186.240.156.169:8791)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON]

**Output Format:** [CLI text output, JSON from the optional signal API, and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes and reads a local trades.json journal; optional x402 calls require X402_API_KEY.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
