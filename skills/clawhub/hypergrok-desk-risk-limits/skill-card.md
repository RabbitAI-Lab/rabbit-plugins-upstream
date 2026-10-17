## Description:

Guides a trading desk through setting risk limits, sizing proposed Hyperliquid trades against live account and market data, and issuing documented PASS or REJECT decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galleonlabs](https://clawhub.ai/user/galleonlabs)

### License/Terms of Use:

MIT

## Use Case:

Trading desk operators use this skill to record user-defined risk limits, check proposed trades against live account and exchange constraints, and review open exposure before approving additional risk.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Stale or incomplete account and market data could produce an unsafe trade assessment.

Mitigation: Require fresh account and market state; reject proposals when inputs are missing or inconsistent.

Risk: Stops and sizing estimates cannot prevent losses from gaps, slippage, or liquidation.

Mitigation: Review user-defined limits and stressed sizing assumptions before relying on a PASS; require explicit approval for trades that add exposure.

Risk: Desk records or protective orders may change live trading workflows.

Mitigation: Review configured limits and authorized actions; restrict standing approval to reduce-only protection.

## Reference(s):

- [HyperGrok Desk Risk Limits release](https://clawhub.ai/galleonlabs/skills/hypergrok-desk-risk-limits)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Configuration]

**Output Format:** [Markdown risk limits, trade assessments, and book checks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [PASS/REJECT decisions include sizing calculations, applicable limits, and ticket fields; written book checks may be saved as Markdown.]

## Skill Version(s):

1.6.1 (source: server-resolved release; artifact frontmatter says 1.1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
