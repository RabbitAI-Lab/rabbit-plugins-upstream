## Description:

DeFi Due Diligence checks Base or Solana crypto tokens by symbol or contract address and returns PASS/WATCH/FLAG risk verdicts using honeypot, tax, authority, liquidity, volume, concentration, age, and price-change signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[trdyqs6bsr-lksnf](https://clawhub.ai/user/trdyqs6bsr-lksnf)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill before buying a crypto token to screen for rug-pull, honeypot, tax, supply-authority, liquidity, volume, concentration, age, and short-term price-change risk. The skill provides an initial verdict and can unlock a full scored report through a paid x402 flow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation wording and an automatic paid x402 wallet flow could cause unintended $2 USDC charges.

Mitigation: Require explicit user confirmation before any x402 payment and avoid auto-running the skill on casual crypto questions or bare token symbols.

Risk: The skill depends on an external paid token-checking service and the security evidence marks the release suspicious.

Mitigation: Install only when this external service is intended, review the returned risk data before acting, and do not treat the verdict as financial advice.

Risk: Symbol-only lookups can be ambiguous or unresolvable.

Mitigation: Prefer contract addresses with an explicit chain and return an unresolved-token result instead of fabricating a report.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/trdyqs6bsr-lksnf/skills/defi-diligence)
- [DeFi Due Diligence service homepage](https://crypto-api-blush.vercel.app)
- [OpenAPI schema](https://crypto-api-blush.vercel.app/openapi.json)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [PASS/WATCH/FLAG verdict with structured risk data and optional full scored report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full scored reports require a $2 USDC x402 payment; the initial response may be limited to a verdict and payment challenge.]

## Skill Version(s):

1.0.1 (source: server release metadata; SKILL.md frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
