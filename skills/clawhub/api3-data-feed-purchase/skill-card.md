## Description: <br>
Purchases Api3 data feed subscriptions from market.api3.org. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[api3dao](https://clawhub.ai/user/api3dao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and teams integrating Api3 data feeds use this skill to select a feed, chain, and deviation threshold; inspect provider-reported values; get a subscription quote; execute the on-chain purchase; and read the resulting proxy. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The purchase flow can spend funds from the configured wallet. <br>
Mitigation: Use a dedicated low-value wallet and verify the feed, chain, price, sponsor wallet, deviation threshold, and amount before approving buy.ts. <br>
Risk: The workflow relies on WALLET_MNEMONIC in a local environment file. <br>
Mitigation: Avoid storing a valuable mnemonic in plaintext; keep the environment file local, protect it from disclosure, and remove the mnemonic when the purchase is complete. <br>
Risk: The scripts install Node packages and contact Api3-related services and RPC endpoints. <br>
Mitigation: Review the package list and command output before proceeding, and run the skill only in an environment where those network calls are acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/api3dao/skills/api3-data-feed-purchase) <br>
- [Api3 Market](https://market.api3.org) <br>
- [Api3 Market integration path example](https://market.api3.org/ethereum/eth-usd/integrate) <br>
- [Api3 signed API endpoint pattern](https://signed-api.api3.org/public/${api.airnode}) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown responses with command invocations, validation summaries, quote details, transaction status, and feed-read results.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires pnpm, ts-node, and WALLET_MNEMONIC; commands contact Api3 services and RPC endpoints and may execute a real blockchain purchase.] <br>

## Skill Version(s): <br>
0.4.1 (source: server release metadata and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
