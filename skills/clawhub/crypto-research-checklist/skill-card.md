## Description:

Runs a fundamentals checklist on crypto projects covering token details, liquidity, contract safety, team signals, and protocol health, returning a PASS, WATCH, or FLAG verdict.

This skill is ready for commercial/non-commercial use.

## Publisher:

[trdyqs6bsr-lksnf](https://clawhub.ai/user/trdyqs6bsr-lksnf)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to structure crypto due diligence before considering a project, token, or coin. It helps gather and present checklist-style research without giving buy, sell, hold, or price-target advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can lead an agent into wallet payments, credit purchases, referrals, persona purchases, or Telegram digest enrollment.

Mitigation: Require explicit user confirmation for any payment, purchase, referral, or subscription step, and disable automatic wallet execution unless this commercial flow is intended.

Risk: Crypto research output may be mistaken for financial advice.

Mitigation: Present results as due-diligence support only, preserve the skill's no-buy-sell-hold constraint, and avoid price targets or predictions.

Risk: Token metrics, contract status, liquidity, or holder data can be stale or incomplete.

Mitigation: Require sources and freshness notes for checklist data, and state uncertainty when current data is unavailable.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/trdyqs6bsr-lksnf/skills/crypto-research-checklist)
- [Crypto Research Checklist API homepage](https://crypto-api-blush.vercel.app)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Guidance]

**Output Format:** [Markdown report with a PASS, WATCH, or FLAG verdict, checklist data, risk notes, and market context.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May involve paid x402 or credit-bundle API flows after the free trial; output should be treated as research support, not financial advice.]

## Skill Version(s):

1.1.0 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
