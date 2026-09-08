## Description:

Query Cournot for an event probability and supporting evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cournot-ai](https://clawhub.ai/user/cournot-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask Cournot for a prediction-market event probability and view the returned supporting evidence. The skill is intended for explicit Cournot requests, not casual odds questions or independent market-mispricing analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Event queries are sent to an external Cournot service.

Mitigation: Use the skill only for explicit Cournot requests and avoid sending unnecessary sensitive details in the event text.

Risk: Paid probability calls may transfer real on-chain assets after the free allowance is exhausted.

Mitigation: Review the payment route, amount, network, and recipient carefully, and require explicit confirmation before wallet setup or payment execution.

Risk: Prediction-market probabilities and supporting evidence could be mistaken for investment advice.

Mitigation: Present only the returned Cournot assessment and basis, preserve the investment-advice disclaimer, and do not add independent forecasts or rationale.

## Reference(s):

- [Cournot homepage](https://skill.cournot.ai/)
- [Cournot ClawHub listing](https://clawhub.ai/cournot-ai/skills/cournot)
- [Query flow](references/query-flow.md)
- [Payment flow](references/payment.md)
- [Response formatting](references/response-format.md)
- [Binance Agentic Wallet](https://github.com/binance/binance-skills-hub/tree/main/skills/binance-web3/binance-agentic-wallet)
- [x402 Foundation Buyer Quickstart](https://docs.x402.org/getting-started/quickstart-for-buyers)
- [viem Local Accounts](https://viem.sh/docs/accounts/local)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with tables, concise prose, and inline shell commands when payment or wallet setup is needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Probability answers use only Cournot API results and returned evidence; paid requests require explicit confirmation before execution.]

## Skill Version(s):

1.0.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
