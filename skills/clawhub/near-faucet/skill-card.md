## Description: <br>
OpenClaw skill for requesting NEAR testnet tokens via faucet. Provides faucet requests, status checking, and balance queries with rate limiting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shaiss](https://clawhub.ai/user/shaiss) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use Near Faucet to request NEAR testnet tokens for test accounts and check balances while building or testing NEAR applications. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Provided NEAR account IDs are sent to NEAR testnet faucet and RPC services. <br>
Mitigation: Use only testnet account identifiers and avoid entering sensitive or mainnet account information. <br>
Risk: Users may assume advertised status tracking, default account, or local rate limiting behavior is enforced. <br>
Mitigation: Confirm the behavior in the installed version and use external tracking or rate controls where those safeguards matter. <br>


## Reference(s): <br>
- [NEAR Testnet Faucet](https://wallet.testnet.near.org/) <br>
- [NEAR CLI Documentation](https://docs.near.org/tools/near-cli) <br>
- [ClawHub Skill Page](https://clawhub.ai/shaiss/skills/near-faucet) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Text, Guidance] <br>
**Output Format:** [Plain text CLI output and Markdown usage guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requests send provided NEAR testnet account IDs to NEAR testnet faucet and RPC services.] <br>

## Skill Version(s): <br>
1.0.0 (source: package.json and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
