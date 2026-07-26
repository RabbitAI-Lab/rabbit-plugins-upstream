## Description: <br>
Interact with AgentConstitution governance contracts on Base Sepolia to check compliance, read rules, log actions, and query governance state. <br>

This skill is for research and development only. <br>

## Publisher: <br>
[ztsalexey](https://clawhub.ai/user/ztsalexey) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents operating on Base Sepolia use this skill to check agent compliance, inspect active governance rules, monitor emergency status, and prepare on-chain action logging workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Action log descriptions signed on-chain may become public and permanent. <br>
Mitigation: Do not include secrets, credentials, private prompts, personal data, or confidential operational details in logAction descriptions. <br>
Risk: Write actions require a private key and can create unintended testnet transactions if the key or target contracts are misused. <br>
Mitigation: Use a dedicated low-value testnet key and verify the Base Sepolia contract addresses before sending transactions. <br>
Risk: The skill is intended for Base Sepolia testnet contracts, not mainnet operation. <br>
Mitigation: Use the documented Base Sepolia RPC and contract addresses, and do not adapt the workflow to mainnet without a separate review. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ztsalexey/skills/agent-constitution) <br>
- [Project homepage](https://github.com/ztsalexey/bigmemkex/tree/main/projects/agent-constitution) <br>
- [BaseScan Constitution contract](https://sepolia.basescan.org/address/0xe4c4d101849f70B0CDc2bA36caf93e9c8c1d26D2) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Code, Guidance] <br>
**Output Format:** [Markdown with inline bash, Solidity, and JavaScript code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Targets Base Sepolia RPC endpoints and may require Foundry cast plus a dedicated testnet signing key for write actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
