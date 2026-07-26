## Description: <br>
Launch tokens on Solana using Metaplex Genesis protocol. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[blockiosaurus](https://clawhub.ai/user/blockiosaurus) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and token launch operators use this skill to plan and execute Solana token launches with Metaplex Genesis, including LaunchPool, unlocked allocation, Raydium pool, timing, and wallet setup guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Launching tokens on Solana can initiate real financial blockchain transactions and spend SOL. <br>
Mitigation: Use a dedicated low-balance wallet and review the wallet address, network, allocations, fees, metadata upload, and finalization before signing. <br>
Risk: Private key material could be exposed if copied into chat or logs. <br>
Mitigation: Configure the wallet through a keypair path or environment variable and do not paste private keys into the agent conversation. <br>
Risk: Incorrect bucket allocations or ordering can lead to an invalid or unintended launch configuration. <br>
Mitigation: Confirm allocations sum to exactly 100 percent and verify Raydium, LaunchPool, and unlocked bucket indexes before finalization. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/blockiosaurus/skills/mplx-genesis) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with tool-call names and configuration details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a wallet-enabled Genesis plugin configuration and a funded Solana wallet.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
