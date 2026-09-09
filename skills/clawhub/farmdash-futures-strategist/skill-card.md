## Description:

Hyperliquid perps strategist: market scans, funding rates, position sizing, and user-signed EIP-712 order execution & cancellation with drawdown guardrails.

This skill is ready for commercial/non-commercial use.

## Publisher:

[parmasanandgarlic](https://clawhub.ai/user/parmasanandgarlic)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research Hyperliquid perpetual futures markets, compare guarded strategy candidates, size positions, and submit or cancel user-signed orders after explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can help submit real Hyperliquid futures orders or cancellations after a user signs them.

Mitigation: Require fresh analysis, explicit manual confirmation, local EIP-712 signing, and user review of trade details and builder fee before each state-changing request.

Risk: Server security evidence reports a packaged schema mismatch that can make delegated-wallet risk analysis unreliable.

Mitigation: Review delegated-wallet flows before install and avoid delegated-wallet execution until the analysis schema accepts the documented account owner address.

Risk: Private keys, seed phrases, or wallet exports would create custody and account-compromise risk.

Mitigation: Never provide private key material to the skill; use only local wallet signing and the optional FarmDash bearer token for tier access.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/parmasanandgarlic/skills/farmdash-futures-strategist)
- [FarmDash Agent Hub](https://www.farmdash.one/agents)
- [FarmDash API Schema](https://www.farmdash.one/agents/openapi.yaml)
- [Canonical FarmDash Futures Strategist skill manual](https://www.farmdash.one/openclaw-skills/farmdash-futures-strategist/SKILL.md)
- [Agent integration documentation](https://www.farmdash.one/docs)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and structured JSON-style tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include strategy analysis, risk state, position sizing, confirmation prompts, and user-signed order or cancellation requests.]

## Skill Version(s):

1.0.24 (source: server release metadata; packaged skill frontmatter reports 3.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
