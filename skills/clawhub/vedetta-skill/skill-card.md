## Description:

Fetches crypto, U.S. stock, and macro market research from free or pay-per-call endpoints on Base and Solana.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lacryptorina](https://clawhub.ai/user/lacryptorina)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use Vedetta to retrieve sentiment, narratives, price divergence, news, and prediction research about crypto, U.S. stocks, and macro assets. The results are descriptive market research, not financial advice or trade execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The payment helper does not enforce advertised route prices before signing x402 authorizations.

Mitigation: Use free endpoints until checks enforce each route's price, an overall budget, and the expected network, USDC asset, and recipient before signing. If enabling payments, use a dedicated low-balance wallet and do not rely on the written price warning alone.

## Reference(s):

- [Vedetta market intelligence service](https://vedetta.dethboy.com)
- [Vedetta install guide](https://vedetta.dethboy.com/install)
- [ClawHub skill release](https://clawhub.ai/lacryptorina/skills/vedetta-skill)
- [Base x402 service catalog](https://vedetta.dethboy.com/.well-known/x402.json)
- [Solana x402 service catalog](https://vedetta.dethboy.com/.well-known/x402-sol.json)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Text]

**Output Format:** [Structured JSON market data with concise textual research summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only market research. Free endpoints are rate-limited; paid requests authorize per-call USDC charges.]

## Skill Version(s):

2.14.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
