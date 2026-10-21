## Description:

Helps agents check current and historical Base gas prices, estimate transaction costs, compare chains, and identify useful transaction windows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[memosr](https://clawhub.ai/user/memosr)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and on-chain agents use this skill to estimate Base transaction fees, compare gas costs across chains, and decide whether or when to transact.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid queries can spend funds from an AgentCash wallet, especially if repeatedly polled.

Mitigation: Check the free health route first, verify the endpoint and price before each paid call, and avoid automated polling.

Risk: Using an unpinned AgentCash CLI version may run newly published code.

Mitigation: Use a pinned or otherwise verified AgentCash CLI version instead of @latest.

## Reference(s):

- [Base Gas homepage](https://base-gas-x402.vercel.app)
- [Choosing an endpoint](rules/choosing-an-endpoint.md)
- [Getting started](rules/getting-started.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Markdown with gas-data summaries and inline commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Gas estimates may include gwei, ETH, and USD values; historical guidance depends on available coverage.]

## Skill Version(s):

1.0.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
