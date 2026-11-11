## Description:

Paid x402 endpoint: $0.007 USDC per call on Base. Returns weekly strategy evolution insights from APEX's self-improvement engine.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kynto2001-ctrl](https://clawhub.ai/user/kynto2001-ctrl)

### License/Terms of Use:

MIT-0

## Use Case:

Agents supporting a user's weekly APEX strategy review can request structured insights to help understand how the strategy is evolving and calibrate long-term strategy alignment. Treat the response as informational when making trading decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Each request incurs a USDC payment, and repeated calls can increase the total spend.

Mitigation: Confirm the current endpoint price before requesting insights and monitor wallet spending.

Risk: The skill requires an EVM private key to authorize x402 payments.

Mitigation: Keep the key in a protected secret store or environment variable and use a wallet funded only for intended calls.

Risk: Strategy insights may be incomplete or unsuitable as a basis for a trading decision.

Mitigation: Review the response as informational analysis and independently validate it before acting.

## Reference(s):

- [APEX Evolution Insight endpoint](https://apexrunner.ai/signals/apex-evolution-insight)
- [APEX Signal Intelligence](https://apexrunner.ai/signals/signal-intelligence)
- [APEX Regime Transition](https://apexrunner.ai/signals/regime-transition)
- [APEX Runner](https://apexrunner.ai)
- [ClawHub release page](https://clawhub.ai/kynto2001-ctrl/skills/apex-evolution-insight)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Analysis]

**Output Format:** [JSON response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Weekly insight data with week, strategy_score, and top_insight fields.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
