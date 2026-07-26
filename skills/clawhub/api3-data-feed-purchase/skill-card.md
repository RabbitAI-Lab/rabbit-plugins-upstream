## Description: <br>
Purchases Api3 data feed subscriptions from market.api3.org. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[metobom](https://clawhub.ai/user/metobom) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and Web3 operators use this skill to choose an Api3 dAPI feed, chain, and deviation threshold, inspect live provider values, quote the subscription price, execute the on-chain purchase, and optionally verify the reader proxy. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a local WALLET_MNEMONIC to sign real blockchain purchase transactions. <br>
Mitigation: Use only a limited-purpose wallet with minimal funds and avoid storing a primary seed phrase in the skill directory. <br>
Risk: The purchase transaction is an on-chain action that can spend ETH and should be treated as irreversible. <br>
Mitigation: Confirm the exact chain, feed, deviation threshold, quoted price, and amount to send before approving the purchase script. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/metobom/skills/api3-data-feed-purchase) <br>
- [API3 Market](https://market.api3.org) <br>
- [API3 Signed API public endpoint pattern](https://signed-api.api3.org/public/${api.airnode}) <br>
- [API3 pricing data path pattern](https://api3dao.github.io/data-feeds/market/dapi-pricing/${chainId}/${path}.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, plain-text command output summaries, and tables.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires feed, chain, and deviation choices; purchase execution requires WALLET_MNEMONIC in the environment, and feed reading requires a reader proxy address.] <br>

## Skill Version(s): <br>
0.3.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
