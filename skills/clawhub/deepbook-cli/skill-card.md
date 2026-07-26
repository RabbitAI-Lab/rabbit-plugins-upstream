## Description: <br>
Operate the deepbook CLI for DeepBook reads, global configuration and account management, on-chain spot trading, swaps, balance-manager operations, and margin trading. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[astinz](https://clawhub.ai/user/astinz) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and crypto operators use this skill to have an agent prepare DeepBook CLI commands for market inspection, wallet and configuration setup, and Sui on-chain trading workflows. It is intended for users who understand the operational and financial risk of live trading commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide agents through private-key setup for DeepBook accounts. <br>
Mitigation: Use stdin for secrets where supported, never print or log private keys, and inspect ~/.deepbook permissions and stored contents before use. <br>
Risk: The skill covers live crypto deposits, trades, withdrawals, margin operations, and configuration-changing commands. <br>
Mitigation: Require explicit user approval before fund-moving or configuration-changing commands, and run dry-run or testnet flows before mainnet execution. <br>
Risk: The security evidence flags weak confirmation boundaries for live trading assistance. <br>
Mitigation: Start with testnet or low-value accounts and verify pool keys, manager object IDs, quantities, prices, and recipient addresses before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/astinz/skills/deepbook-cli) <br>
- [Source skill definition](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown with shell command examples and CLI argument guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes dry-run, key-handling, manager selection, and live trading safety guidance.] <br>

## Skill Version(s): <br>
0.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
