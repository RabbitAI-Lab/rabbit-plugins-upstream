## Description: <br>
Skill for managing EVM wallets, transactions, and network helpers via cast; covers onboarding, checks, and operating procedures. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tezatezaz](https://clawhub.ai/user/tezatezaz) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to onboard and operate a local EVM hot wallet, select networks and tokens, check balances, and work through cast-based transaction workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local hot-wallet secrets can expose funds if mnemonic, private key, password, or keystore files persist or are accessed by another process. <br>
Mitigation: Use a fresh low-value wallet, avoid importing valuable existing secrets, and remove plaintext password or mnemonic files promptly after setup. <br>
Risk: Setup scripts can install tools and change the host environment. <br>
Mitigation: Review the install and wallet scripts before execution and avoid granting sudo during setup unless the user explicitly accepts the host changes. <br>
Risk: A mistaken or unauthorized transaction can transfer value or grant token approvals. <br>
Mitigation: Require explicit human confirmation before any transaction is signed or broadcast, and show the destination, value, network, and calldata or function intent before proceeding. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tezatezaz/skills/clawcast) <br>
- [ClawAudit audit report](https://clawaudit.duckdns.org/audit/7737be97-edda-4cd4-9070-fa47547dd44a) <br>
- [Foundry installer](https://foundry.paradigm.xyz) <br>
- [EVM network list](assets/evm-networks.json) <br>
- [EVM token metadata](assets/evm-network-tokens.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and local configuration files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local wallet state, keystore and password helper files, transaction mention logs, and network or token JSON updates.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
