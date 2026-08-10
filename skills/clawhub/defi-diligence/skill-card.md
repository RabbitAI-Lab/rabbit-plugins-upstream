## Description:

defi-diligence helps agents screen Base and Solana crypto tokens before purchase by returning PASS/WATCH/FLAG risk verdicts, kill-switch checks, scored due-diligence signals, and paid x402 report access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[trdyqs6bsr-lksnf](https://clawhub.ai/user/trdyqs6bsr-lksnf)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to check an unverified Base or Solana token before buying, using a symbol or contract address to obtain risk verdicts, kill-switch indicators, and scored due-diligence data. It supports risk review only and should not be used to provide price targets or financial advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review warns that agents with an x402 wallet may pay for reports automatically without fresh user approval.

Mitigation: Configure any x402 wallet to require explicit approval before each $2 USDC payment and avoid invoking the skill from casual crypto-buy questions.

Risk: The server security verdict is suspicious for this release.

Mitigation: Review before installing, keep outputs limited to token risk data, and do not treat verdicts as financial advice.

Risk: Symbol-only token checks can be ambiguous and may not support contract-level checks.

Mitigation: Prefer a contract address with an explicit Base or Solana chain and return an unresolved-token result instead of guessing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/trdyqs6bsr-lksnf/skills/defi-diligence)
- [Service homepage](https://crypto-api-blush.vercel.app)
- [OpenAPI schema](https://crypto-api-blush.vercel.app/openapi.json)

## Skill Output:

**Output Type(s):** [guidance, API calls, JSON]

**Output Format:** [Markdown guidance with JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl and jq for command-line use; full scored reports use a $2 USDC x402 payment path.]

## Skill Version(s):

1.1.0 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
