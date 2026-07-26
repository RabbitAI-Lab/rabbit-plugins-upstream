## Description: <br>
Starknet DeFi Toolkit helps AI agents read Starknet ERC-20 balances, fetch STRK/ETH USD quotes, list Ekubo and JediSwap pools, simulate swaps, and generate Cairo/Sierra contract skeletons. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ssidharhubble](https://clawhub.ai/user/ssidharhubble) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and AI agents use this skill to inspect Starknet DeFi state, estimate swaps, retrieve token prices, and draft Cairo contract skeletons without submitting transactions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Balance queries disclose the queried wallet address to the selected RPC provider. <br>
Mitigation: Use a trusted RPC provider through STARKNET_RPC_URL and avoid querying sensitive wallet addresses where disclosure is unacceptable. <br>
Risk: Generated Cairo skeletons and balance logic are not audited production code. <br>
Mitigation: Treat generated code as a starting point and require review, testing, and security audit before deployment or fund handling. <br>
Risk: The scaffold command writes a local .cairo file and may overwrite an existing file with the same generated name. <br>
Mitigation: Run scaffold commands in a controlled working directory and check for existing output files before execution. <br>
Risk: Public RPC and API endpoints may be rate-limited or unavailable. <br>
Mitigation: Use a production-grade provider endpoint for operational workflows and verify important results against reliable on-chain sources. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ssidharhubble/skills/starknet-defi-toolkit) <br>
- [Starknet public RPC endpoint](https://rpc.starknet.lava.build) <br>
- [Starknet Sepolia public RPC endpoint](https://rpc.starknet-testnet.lava.build) <br>
- [CoinGecko simple price API](https://api.coingecko.com/api/v3/simple/price) <br>
- [Ekubo pools API](https://mainnet-api.ekubo.org/pools) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration] <br>
**Output Format:** [CLI text output and generated Cairo source files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only RPC/API calls; the scaffold command writes a local .cairo file.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
