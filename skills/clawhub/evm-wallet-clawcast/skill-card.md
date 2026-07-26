## Description: <br>
This skill is focused on crypto/EVM wallet operations and transaction workflows using cast. It covers wallet creation, importing or generating keys, checking balances, sending coins or tokens, monitoring tokens, creating and verifying transactions, and keeping agent keystores secure so the agent can guide the user through the core crypto operations a wallet handles. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tezatezaz](https://clawhub.ai/user/tezatezaz) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external users can use this skill to guide EVM wallet onboarding, network selection, balance checks, token tracking, transaction preparation, and wallet cleanup with Foundry cast. It is intended for normal ClawHub agent use where the user explicitly approves wallet setup and any transaction broadcast. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill manages a hot EVM wallet and stores sensitive wallet files locally, including a password file and keystore. <br>
Mitigation: Use a new low-balance wallet, avoid importing valuable seed phrases or private keys, and inspect ~/.agent-wallet after setup, especially pw.txt and keystore.json. <br>
Risk: Setup can install Foundry/cast and may request sudo or package-manager approval for helper tooling. <br>
Mitigation: Review installer and sudo prompts before approving them, and stop setup if the requested system change is unexpected. <br>
Risk: Live EVM transactions can transfer funds or grant token permissions irreversibly. <br>
Mitigation: Manually confirm the chain, recipient, token contract, amount, gas settings, and calldata before any broadcast. <br>
Risk: Temporary mnemonic or private-key material may persist if automated cleanup does not complete. <br>
Mitigation: Verify cleanup after onboarding and use the removal script when finished. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/tezatezaz/skills/evm-wallet-clawcast) <br>
- [Foundry Installer](https://foundry.paradigm.xyz) <br>
- [EVM Network Metadata](artifact/assets/evm-networks.json) <br>
- [EVM Token Metadata](artifact/assets/evm-network-tokens.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and local configuration files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local wallet state, keystore, password, temporary private key, and temporary mnemonic files during setup; transaction broadcasts require user review.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
