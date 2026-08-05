## Description: <br>
Purchases Api3 data feed subscriptions from market.api3.org. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[api3dao](https://clawhub.ai/user/api3dao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to select an Api3 data feed, validate the target chain and deviation threshold, inspect provider-reported values, get a subscription quote, purchase the subscription on-chain, and read the resulting proxy. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a wallet mnemonic from a local environment file and can sign a real blockchain purchase transaction. <br>
Mitigation: Use only a dedicated low-value wallet, avoid main-wallet seed phrases, and confirm the chain, feed, deviation threshold, quoted amount, and transaction before approval. <br>
Risk: The purchase flow depends on live market data and on-chain state that can affect quoted amounts and execution results. <br>
Mitigation: Review the generated quote immediately before purchase and stop if the amount, chain, feed, sponsor wallet, or subscription details do not match expectations. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/api3dao/skills/api3-data-feed-purchase) <br>
- [Api3 Market](https://market.api3.org) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Text] <br>
**Output Format:** [Markdown guidance with shell command invocations and tabular summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires pnpm, ts-node, and WALLET_MNEMONIC when executing purchases; the purchase phase may submit an on-chain transaction after user approval.] <br>

## Skill Version(s): <br>
0.7.0 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
