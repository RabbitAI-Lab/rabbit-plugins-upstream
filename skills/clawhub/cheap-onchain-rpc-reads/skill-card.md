## Description: <br>
Cheap, keyless on-chain reads for agents across native and ERC-20 balances, gas price, transaction status, token supply, ENS, and nonce on Base, Ethereum, Optimism, Arbitrum, and Polygon. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rccola990-cloud](https://clawhub.ai/user/rccola990-cloud) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill to guide agents through paid, read-only blockchain RPC queries without running a node, managing RPC keys, or signing up for an API account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Queries use a third-party endpoint and can reveal wallet addresses, transaction hashes, ENS names, and chains requested. <br>
Mitigation: Review whether the requested chain data is acceptable to disclose to the endpoint before using the skill. <br>
Risk: Calls are described as paid USDC requests even though the skill itself is read-only. <br>
Mitigation: Confirm the x402 client displays the price before authorizing payment. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/rccola990-cloud/skills/cheap-onchain-rpc-reads) <br>
- [Free Sample Endpoint](https://store.agentexchange.work/samples) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API Calls] <br>
**Output Format:** [Markdown with HTTP GET examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance centers on read-only x402 requests that show price before payment.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
