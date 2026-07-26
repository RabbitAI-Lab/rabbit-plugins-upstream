## Description: <br>
Checks live gas prices across Ethereum, Base, Arbitrum, Optimism, and Polygon, estimates USD transaction cost from live ETH and MATIC prices, and ranks chains cheapest-first for a supplied gas limit. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ssidharhubble](https://clawhub.ai/user/ssidharhubble) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External crypto traders, DeFi users, and smart contract deployers use this skill to compare current transaction costs across supported EVM chains before bridging, swapping, claiming, minting, or deploying contracts. It helps choose a cheaper chain or a better timing window while leaving transaction approval and signing outside the skill. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill makes live network requests to public RPC services and CoinGecko when its script is run. <br>
Mitigation: Install and run it only where outbound requests to those disclosed services are acceptable. <br>
Risk: Estimated transaction costs can differ from actual costs because gas usage varies by transaction and public RPC data can be delayed, rate-limited, or temporarily unavailable. <br>
Mitigation: Treat results as pre-transaction estimates, review per-chain errors, and confirm final costs in the wallet or execution environment before signing. <br>
Risk: The timing note is a general historical heuristic, not a live congestion forecast. <br>
Mitigation: Use the timing note only alongside the live gas numbers and current transaction urgency. <br>
Risk: Wallet secrets, private keys, seed phrases, or signing authority would expand the risk beyond the reviewed evidence. <br>
Mitigation: Do not provide wallet secrets or transaction-signing capability to this read-only skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ssidharhubble/skills/crypto-gas-fee-optimizer) <br>
- [CoinGecko simple price endpoint used for USD conversion](https://api.coingecko.com/api/v3/simple/price?ids=ethereum,matic-network&vs_currencies=usd) <br>
- [PublicNode Ethereum RPC endpoint](https://ethereum-rpc.publicnode.com) <br>
- [PublicNode Base RPC endpoint](https://base-rpc.publicnode.com) <br>
- [PublicNode Arbitrum RPC endpoint](https://arbitrum-one-rpc.publicnode.com) <br>
- [PublicNode Optimism RPC endpoint](https://optimism-rpc.publicnode.com) <br>
- [PublicNode Polygon RPC endpoint](https://polygon-bor-rpc.publicnode.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, JSON, guidance] <br>
**Output Format:** [Markdown guidance with shell commands; the included script emits a terminal table or JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires live network access to publicnode.com and CoinGecko; no API keys, wallet secrets, private keys, signing, or transaction broadcast authority are required.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
