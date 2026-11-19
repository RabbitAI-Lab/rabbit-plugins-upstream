## Description:

Buy pay-per-call market intelligence through Vedetta's Base USDC and Solana x402 routes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lacryptorina](https://clawhub.ai/user/lacryptorina)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use the skill to retrieve live or cached crypto, US stock, and macro market analysis, sentiment, and related signals through free or paid x402 routes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic payment signing may not enforce the advertised price ceiling.

Mitigation: Check each live payment offer's amount and network before approving it, stop if the amount exceeds the intended limit, and use a dedicated low-balance wallet.

Risk: Task text may be sent to an external service during routing.

Mitigation: Do not include sensitive or private information in routed requests.

Risk: The security scan was partial because referenced local paths were missing, so its evidence is incomplete.

Mitigation: Review the complete skill package and referenced files before installation.

## Reference(s):

- [Vedetta service](https://vedetta.dethboy.com)
- [Vedetta install instructions](https://vedetta.dethboy.com/install)
- [Base x402 endpoint metadata](https://vedetta.dethboy.com/.well-known/x402.json)
- [Solana x402 endpoint metadata](https://vedetta.dethboy.com/.well-known/x402-sol.json)
- [ClawHub skill page](https://clawhub.ai/lacryptorina/skills/vedetta-skill)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Text]

**Output Format:** [Structured market data in JSON with concise text summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only market research; some routes are paid and free routes are rate-limited. Not financial advice.]

## Skill Version(s):

2.14.2 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
