## Description: <br>
Skill for managing EVM wallets, transactions, and network helpers via cast; covers onboarding, checks, and operating procedures. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tezatezaz](https://clawhub.ai/user/tezatezaz) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to set up and operate a local EVM hot-wallet workflow with Foundry cast, including wallet creation or import, network selection, token metadata lookup, balance checks, transfers, and transaction review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores powerful wallet secrets locally, including generated or imported key material, keystores, password files, and short-lived mnemonic backups. <br>
Mitigation: Use only low-value hot wallets, avoid importing valuable seed phrases, prefer hardware-wallet or manual Foundry workflows for significant funds, and remove plaintext secret files after setup. <br>
Risk: The onboarding flow can install Foundry/cast and change local wallet state before funds are managed. <br>
Mitigation: Review the installation and wallet setup steps before execution, run them in a controlled workspace, and confirm the selected network and RPC endpoint before signing transactions. <br>
Risk: Transaction references may be logged locally for later review. <br>
Mitigation: Treat transaction logs as sensitive operational history and remove them when they are no longer needed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/tezatezaz/skills/cast) <br>
- [ClawAudit Report](https://clawaudit.duckdns.org/audit/7737be97-edda-4cd4-9070-fa47547dd44a) <br>
- [Foundry Installer](https://foundry.paradigm.xyz) <br>
- [EVM Network Metadata](artifact/assets/evm-networks.json) <br>
- [EVM Token Metadata](artifact/assets/evm-network-tokens.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and local configuration updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides interactive wallet setup and records local wallet, network, token, and transaction-reference state.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
