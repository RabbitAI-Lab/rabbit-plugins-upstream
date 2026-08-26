## Description:

Which of these addresses are smart money? Batch-profile a list in one call.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, and developers use this skill to batch-profile wallet addresses with the Nansen CLI and identify addresses labeled as smart_money or fund.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The intended wallet-label lookup is read-only, but the allowed nansen CLI can also manage wallets and execute trades.

Mitigation: Install in agent environments that do not expose Nansen wallets, WalletConnect sessions, trading credentials, NANSEN_WALLET_PASSWORD, or Privy credentials.

Risk: The broad CLI access may exceed what is needed for a pure batch profiler lookup.

Mitigation: Prefer a version scoped to the specific research profiler batch command for label lookup workflows.

Risk: CLI telemetry could reveal usage metadata from the agent environment.

Mitigation: Consider disabling Nansen CLI telemetry with DO_NOT_TRACK=1 or NANSEN_NO_TELEMETRY=1.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nansen-devops/skills/nansen-wallet-batch)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with an inline bash command and concise filtering guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses NANSEN_API_KEY and the nansen CLI; command results may include wallet labels, balances, and per-address errors.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
