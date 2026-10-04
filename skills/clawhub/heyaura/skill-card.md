## Description:

Fetches and summarizes a multichain EVM wallet portfolio through heyAura's paid x402 API, including balances, USD values, and DeFi positions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heyaura](https://clawhub.ai/user/heyaura)

### License/Terms of Use:

MIT-0

## Use Case:

Wallet holders and agents use this skill to inspect an EVM address or ENS name and summarize its token holdings, portfolio value by network, and DeFi positions. A paid request requires explicit authorization of the live payment terms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid portfolio requests can spend funds or settle a second payment after an uncertain result.

Mitigation: Use a dedicated low-balance payer wallet; confirm the live amount, network, and payee against explicit authorization, and investigate ambiguous payments before retrying.

Risk: The bundled dependency lockfile includes a vulnerable fast-uri dependency line.

Mitigation: Update the dependency lockfile to a patched fast-uri line before routine use.

## Reference(s):

- [heyAura ClawHub listing](https://clawhub.ai/heyaura/skills/heyaura)
- [heyAura portfolio API reference](references/portfolio-api.md)
- [heyAura OpenAPI specification](https://aura.adex.network/.well-known/openapi.json)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown portfolio summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summarizes total USD value, network totals, token holdings, and DeFi positions; reports payment details when relevant.]

## Skill Version(s):

1.0.1 (source: ClawHub release, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
