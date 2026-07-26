## Description: <br>
Monitors large cryptocurrency wallet balances on-chain using Web3 RPC to detect potential market-moving activity. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[waleolapo](https://clawhub.ai/user/waleolapo) <br>

### License/Terms of Use: <br>
ISC <br>


## Use Case: <br>
Developers and analysts use this skill to check public Ethereum wallet balances from a configured wallet list or custom addresses and identify balances above a whale threshold. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Monitored wallet addresses are sent to the configured Ethereum RPC provider. <br>
Mitigation: Use an RPC provider you trust and a limited-purpose RPC key if RPC_URL contains credentials. <br>
Risk: Scheduling the monitor can create ongoing background checks. <br>
Mitigation: Create a cron job only when intentional and review the schedule and command before enabling it. <br>


## Reference(s): <br>
- [Known Whale Wallet Addresses](references/wallets.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/waleolapo/skills/crypto-whale-monitor) <br>
- [Default Ethereum RPC Endpoint](https://eth.llamarpc.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Console text and markdown guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reads wallet addresses from references/wallets.md or command-line arguments and can use RPC_URL for a custom Ethereum RPC provider.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
