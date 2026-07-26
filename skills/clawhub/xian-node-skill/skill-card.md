## Description: <br>
Set up and manage Xian blockchain nodes for mainnet, testnet, custom network, validator, and service-node workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[endogen](https://clawhub.ai/user/endogen) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and node operators use this skill to deploy, configure, monitor, troubleshoot, and reset Xian blockchain nodes, including validator and service-node setups. It also helps create custom network genesis files and test local node access through the Xian Python SDK. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Validator private keys and wallet secrets are high-value secrets that can be exposed through prompts, shell history, logs, or shared configuration. <br>
Mitigation: Generate and store keys locally, keep private keys out of chat and command history, restrict access to key files, and back up secrets securely. <br>
Risk: Reset, wipe, and transaction examples can delete node state or move real funds when used against production networks. <br>
Mitigation: Back up node data and configuration before reset operations, and test transaction examples on local or test networks unless mainnet activity is intentional. <br>
Risk: Incorrect seed, genesis, or validator configuration can prevent syncing or block production on a custom network. <br>
Mitigation: Review CometBFT and genesis settings before launch, verify peer connectivity and sync status, and stage changes on a test network first. <br>


## Reference(s): <br>
- [Genesis File Template](artifact/references/genesis-template.md) <br>
- [Xian Project Site](https://xian.org) <br>
- [xian-network/xian-stack](https://github.com/xian-network/xian-stack) <br>
- [xian-network/xian-core](https://github.com/xian-network/xian-core) <br>
- [xian-network/xian-py](https://github.com/xian-network/xian-py) <br>
- [CometBFT Documentation](https://docs.cometbft.com/) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Code, Configuration] <br>
**Output Format:** [Markdown guidance with bash, Python, JSON, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes node setup, validator key generation, genesis configuration, monitoring, troubleshooting, and SDK test examples.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
