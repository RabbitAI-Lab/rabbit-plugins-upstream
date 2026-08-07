## Description:

Run a fundamentals checklist on any crypto project before you invest, covering token, liquidity, contract safety, team, and protocol health in one pass with a PASS/WATCH/FLAG result.

This skill is ready for commercial/non-commercial use.

## Publisher:

[trdyqs6bsr-lksnf](https://clawhub.ai/user/trdyqs6bsr-lksnf)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to structure crypto project due diligence before making investment-related decisions. It helps collect and report token, liquidity, holder concentration, contract, team, and protocol-health signals while avoiding buy, sell, hold, or price-prediction advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may send crypto project queries to an external Onchain Intelligence analysis API.

Mitigation: Install only when external API use for crypto due diligence is acceptable for the intended workflow.

Risk: The skill may trigger a small x402 payment from an agent wallet for a full scored report.

Mitigation: Use agents with explicit wallet payment controls and review payment challenges before completion.

Risk: PASS/WATCH/FLAG outputs could be mistaken for investment advice.

Mitigation: Treat the report as research support only and preserve the skill's restrictions against buy, sell, hold, price-target, or prediction advice.

Risk: Crypto market and on-chain data can be stale or incomplete.

Mitigation: Require sources for checklist items and state uncertainty when current metrics are unavailable.

## Reference(s):

- [Onchain Intelligence homepage](https://crypto-api-blush.vercel.app)
- [ClawHub skill listing](https://clawhub.ai/trdyqs6bsr-lksnf/skills/crypto-research-checklist)
- [Publisher profile](https://clawhub.ai/user/trdyqs6bsr-lksnf)

## Skill Output:

**Output Type(s):** [Analysis, API Calls, Markdown, Guidance]

**Output Format:** [Markdown report with PASS/WATCH/FLAG verdict, checklist entries, risks, and context]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call a paid external analysis API and may require a small x402 payment from an agent wallet.]

## Skill Version(s):

1.0.0 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
