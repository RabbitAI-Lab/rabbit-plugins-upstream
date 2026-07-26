## Description: <br>
Skill for managing EVM wallets, transactions, and network helpers via cast; covers onboarding, checks, and operating procedures. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tezatezaz](https://clawhub.ai/user/tezatezaz) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to set up and operate a local EVM hot wallet with Foundry cast, including wallet onboarding, network selection, balance checks, token metadata lookups, transaction helpers, and wallet removal. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill manages a local hot wallet and may store wallet-control material under ~/.agent-wallet and Foundry keystores. <br>
Mitigation: Use it only for wallets intended for local agent operation, avoid importing valuable existing seed phrases or private keys, and inspect or delete any plaintext mnemonic or password files after setup. <br>
Risk: Setup can modify the host by installing Foundry/cast and may request elevated package installation for cleanup scheduling. <br>
Mitigation: Review the Foundry installation step and any sudo prompt before proceeding. <br>
Risk: Transaction mention logs can contain sensitive financial metadata. <br>
Mitigation: Treat logs/tx_mentions.log as sensitive and remove or protect it according to the workspace's data-handling policy. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tezatezaz/skills/clawcast-wallet) <br>
- [Foundry installer](https://foundry.paradigm.xyz) <br>
- [EVM network list](artifact/assets/evm-networks.json) <br>
- [EVM token metadata](artifact/assets/evm-network-tokens.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and local configuration updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May prompt for wallet, password, network, RPC, and token choices during interactive operation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
