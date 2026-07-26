## Description: <br>
Arc Security - Agent Trust Protocol provides a Python CLI for checking skill trust, paying for verified skill access, staking USDC bonds, reporting malicious skills, voting on claims, and claiming auditor earnings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shaivpidadi](https://clawhub.ai/user/shaivpidadi) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and security reviewers use this skill to inspect on-chain trust signals for ClawHub skills and operate a USDC-based bonding, usage-payment, reporting, voting, and earnings workflow. It is intended for users who can review wallet transactions, RPC endpoints, contract addresses, and downloaded package contents before execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can sign wallet transactions for payment, bonding, reporting, voting, and earnings withdrawal. <br>
Mitigation: Use a dedicated low-value testnet wallet and inspect the exact amount, chain, destination, contract address, and transaction purpose before approving any command. <br>
Risk: The skill depends on user-configured RPC, contract, and x402 server endpoints. <br>
Mitigation: Verify all endpoint and contract configuration against trusted sources before running commands that submit transactions or payment proofs. <br>
Risk: The skill can download ZIP packages after x402 payment and extract them into the working directory. <br>
Mitigation: Inspect downloaded package contents in an isolated directory before executing or installing any extracted files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/shaivpidadi/skills/arc-security) <br>
- [Publisher profile](https://clawhub.ai/user/shaivpidadi) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with CLI commands, configuration tables, and transaction status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may guide actions that sign wallet transactions, move USDC, interact with configured contracts and RPC endpoints, or download skill packages.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact skill.json reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
