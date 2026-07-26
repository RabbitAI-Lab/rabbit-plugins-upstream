## Description: <br>
Tracks BTC self-custody metrics including COLDCARD Q vault health, mempool fee estimation, UTXO management, and on-chain verification for sovereign holders. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[1beekeeper](https://clawhub.ai/user/1beekeeper) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Bitcoin self-custody holders and developers use this skill to check watch-only BTC balances, fee conditions, UTXOs, block height, price, and COLDCARD vault status while preferring local-node alternatives for privacy. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A command sends a watched Bitcoin address to an unexpected lookalike domain, which can expose holdings or transaction timing to an unintended third party. <br>
Mitigation: Review commands before execution and replace the lookalike endpoint with the intended mempool.space endpoint or a self-hosted/local Bitcoin data source. <br>
Risk: Third-party blockchain and price APIs can reveal watch-only address lookups and request timing. <br>
Mitigation: Use a local Bitcoin Core, Electrum, or self-hosted mempool source when address privacy is important. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/1beekeeper/skills/btc-sovereign-tracker) <br>
- [Skill Homepage](https://gitlab.com/1Beekeeper/zk-bankir) <br>
- [mempool.space API](https://mempool.space/api) <br>
- [CoinGecko Simple Price API](https://api.coingecko.com/api/v3/simple/price) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only watch-address workflows; requires curl and jq for command examples.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
