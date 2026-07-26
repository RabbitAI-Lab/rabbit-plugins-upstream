## Description: <br>
Deploy websites and files permanently on MegaETH mainnet using SSTORE2. Agents use their own wallet and pay gas. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[planetai87](https://clawhub.ai/user/planetai87) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to publish HTML or file content as permanent on-chain website data on MegaETH mainnet. It is intended for deployments where the user controls the wallet and accepts real gas costs and immutable publication. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill publishes content permanently on MegaETH mainnet and spends gas from the user's wallet. <br>
Mitigation: Use a dedicated low-balance deployer wallet, review the exact content before deployment, and confirm the gas-spending intent before running the deploy command. <br>
Risk: The deployment requires a private key for signing transactions. <br>
Mitigation: Prefer environment or secret-manager injection over passing --private-key on the command line, and do not log, store, or share the key. <br>
Risk: On-chain content cannot be withdrawn or edited after publication. <br>
Mitigation: Treat each deployment as final and verify the content, target network, and contract settings before signing transactions. <br>


## Reference(s): <br>
- [Warren website](https://thewarren.app) <br>
- [Declared project source](https://github.com/planetai87/warren-tools) <br>
- [MegaETH mainnet RPC endpoint](https://mainnet.megaeth.com/rpc) <br>
- [MegaETH Blockscout explorer](https://megaeth.blockscout.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, JSON] <br>
**Output Format:** [Markdown guidance with shell commands and deployment-result JSON] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js and PRIVATE_KEY; deploys up to 500KB and publishes immutable mainnet content.] <br>

## Skill Version(s): <br>
1.0.6 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
