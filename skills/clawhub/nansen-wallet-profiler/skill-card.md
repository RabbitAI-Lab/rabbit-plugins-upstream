## Description:

Profiles and compares blockchain wallets using Nansen CLI research commands for balances, PnL, labels, transactions, counterparties, and related wallets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts and developers use this skill to investigate a wallet's activity, holdings, and relationships, or compare multiple wallets across supported chains.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated research calls may consume credits or trigger x402 wallet payments.

Mitigation: Confirm the CLI package is trusted and review wallet payment policy and spending limits before making calls.

Risk: Batch and multi-hop trace requests can multiply paid research calls.

Mitigation: Keep trace width and batch size conservative and confirm expected costs before running loops.

## Reference(s):

- [Nansen Wallet Profiler skill release](https://clawhub.ai/nansen-devops/skills/nansen-wallet-profiler)
- [Nansen CLI browser-login preview documentation](https://github.com/nansen-ai/nansen-cli/blob/main/docs/browser-login.md#preview-platform-scope)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with bash command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Research results depend on the selected wallet, chain, and query options; some results support pagination or CSV export.]

## Skill Version(s):

0.1.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
