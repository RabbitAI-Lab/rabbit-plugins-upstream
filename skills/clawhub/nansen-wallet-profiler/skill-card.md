## Description:

Profiles blockchain wallets with Nansen for balances, PnL, labels, transactions, counterparties, related wallets, batch analysis, tracing, and wallet comparisons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run Nansen CLI wallet-analysis workflows for specific wallet addresses, including profiling, relationship tracing, batch review, and comparing wallets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Wallet profiling and tracing can expose or amplify privacy-sensitive inferences about addresses and related individuals.

Mitigation: Use the skill for legitimate analysis only and avoid sharing deanonymizing inferences about private individuals.

Risk: Trace, relationship, batch, and compare workflows may trigger many Nansen API calls and increase API cost.

Mitigation: Keep trace depth and width conservative and review proposed commands before execution.

Risk: The skill requires a Nansen API key for analysis requests.

Mitigation: Provide NANSEN_API_KEY through a managed environment or secret store and avoid pasting credentials into prompts or shared logs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nansen-devops/skills/nansen-wallet-profiler)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands and concise analysis guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires NANSEN_API_KEY and the nansen CLI; trace depth and width can increase API calls and cost.]

## Skill Version(s):

0.1.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
