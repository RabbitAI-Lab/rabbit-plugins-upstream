## Description:

Wallet profiler for Nansen CLI workflows covering balances, PnL, labels, transactions, counterparties, related wallets, batch profiling, tracing, and wallet comparison.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agent operators use this skill to ask an agent for Nansen CLI commands and guidance for investigating one or more wallet addresses, including balances, PnL, labels, relationships, transaction history, traces, and comparisons.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Wallet addresses, queries, and address files may be submitted through the Nansen CLI/API.

Mitigation: Use only approved wallet lists and avoid confidential watchlists or internal research targets unless authorized and permitted under the Nansen account terms.

Risk: Trace workflows can make many API calls and may consume credits quickly.

Mitigation: Review generated commands before execution and keep trace depth and width conservative.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nansen-devops/skills/nansen-wallet-profiler)
- [ClawHub publisher profile](https://clawhub.ai/user/nansen-devops)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires NANSEN_API_KEY and the nansen CLI; generated commands may submit wallet addresses and queries through the Nansen CLI/API.]

## Skill Version(s):

0.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
