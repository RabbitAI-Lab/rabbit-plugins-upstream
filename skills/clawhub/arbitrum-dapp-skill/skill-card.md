## Description: <br>
Opinionated guide for building dApps on Arbitrum using Stylus (Rust) and/or Solidity. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hummusonrails](https://clawhub.ai/user/hummusonrails) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use this skill to scaffold, implement, test, and deploy Arbitrum dApps with Stylus Rust contracts, Solidity contracts, a local Nitro devnode, and React frontends using viem and wagmi. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installer use can execute a remote script and send an opt-out install-count ping. <br>
Mitigation: Prefer ClawHub install or clone-and-review installation, and set ARBITRUM_SKILL_NO_ANALYTICS=1 before running install.sh to disable the install-count ping. <br>
Risk: Deployment examples can submit blockchain transactions or expose wallet keys through shell history or incorrect network selection. <br>
Mitigation: Use disposable local or test wallets, avoid pasting real private keys into shell history, and confirm RPC URLs and network names before any --broadcast or mainnet deployment command. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/hummusonrails/skills/arbitrum-dapp-skill) <br>
- [Deployment](references/deployment.md) <br>
- [Frontend Integration](references/frontend-integration.md) <br>
- [Local Devnode Setup](references/local-devnode.md) <br>
- [Solidity Contracts on Arbitrum](references/solidity-contracts.md) <br>
- [Stylus Rust Contracts](references/stylus-rust-contracts.md) <br>
- [Testing](references/testing.md) <br>
- [Arbitrum Stylus Quickstart](https://docs.arbitrum.io/stylus/quickstart) <br>
- [Stylus SDK](https://github.com/OffchainLabs/stylus-sdk-rs) <br>
- [Nitro Devnode](https://github.com/OffchainLabs/nitro-devnode) <br>
- [viem](https://viem.sh) <br>
- [wagmi](https://wagmi.sh) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with code blocks, shell commands, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include blockchain transaction and deployment commands that require user review before execution.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
