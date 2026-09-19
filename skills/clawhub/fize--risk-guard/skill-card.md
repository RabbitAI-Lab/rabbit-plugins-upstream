## Description:

Risk Guard helps agents verify quantitative trading signals, set position and stop-loss limits, and block trades when market data is missing or risk rules are breached.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fize](https://clawhub.ai/user/fize)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and trading-analysis agents use this skill as a pre-trade risk gate to check signal consistency, market regime, position limits, stop-loss levels, concentration risk, and veto conditions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill produces investment risk guidance that could be incomplete, stale, or unsuitable for a specific trading decision.

Mitigation: Treat the output as advisory, verify key numbers independently, and avoid using it as the sole basis for trades.

Risk: Missing or unverifiable market data can make the risk assessment unreliable.

Mitigation: Use the skill's fail-fast posture: block the trade with VETO: BLOCKED when required market or technical data cannot be verified.

Risk: The skill relies on Python and market-data retrieval paths that may be unavailable in some agent environments.

Mitigation: Confirm python3 and the required data-retrieval tools are available before use, and fall back to authoritative sources or block when data cannot be obtained.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fize/skills/risk-guard)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown risk-control audit report with signal checks, dynamic risk parameters, risk rating, and veto/pass decision.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Advisory output; key market data should be verified independently before trading decisions.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
