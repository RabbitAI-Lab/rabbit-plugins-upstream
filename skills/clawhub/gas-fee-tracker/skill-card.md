## Description: <br>
Track live EVM gas fees across Ethereum, Base, Polygon, and Arbitrum using free public RPC endpoints with no API key required. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ssidharhubble](https://clawhub.ai/user/ssidharhubble) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to check current gas prices before timing EVM transactions, contract deployments, batch operations, and automation gates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill contacts publicnode.com RPC services when run. <br>
Mitigation: Run it only in environments where outbound HTTPS requests to those public RPC endpoints are acceptable. <br>
Risk: The --log option appends gas snapshots to a local path selected by the user. <br>
Mitigation: Use --log only with an intended writable history file and manage that file according to local retention needs. <br>
Risk: The skill reports current legacy eth_gasPrice data rather than EIP-1559 fee breakdowns or future-block estimates. <br>
Mitigation: Treat results as current gas snapshots and verify fees before submitting time-sensitive or high-value transactions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ssidharhubble/skills/gas-fee-tracker) <br>
- [Publisher profile](https://clawhub.ai/user/ssidharhubble) <br>
- [Ethereum PublicNode RPC endpoint](https://ethereum.publicnode.com) <br>
- [Base PublicNode RPC endpoint](https://base.publicnode.com) <br>
- [Polygon PublicNode RPC endpoint](https://polygon-bor-rpc.publicnode.com) <br>
- [Arbitrum One PublicNode RPC endpoint](https://arbitrum-one.publicnode.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, files, guidance] <br>
**Output Format:** [Plain text table, JSON, JSONL log entries, and shell exit status for threshold alerts.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can append timestamped snapshots to a user-selected local log file and return success or failure for alert-gated scripts.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
