## Description: <br>
End-to-end MegaETH development playbook covering wallet operations, token swaps, instant transaction receipts, RPC batching, real-time mini-block subscriptions, storage-aware contract patterns, the MegaEVM gas model, WebSocket keepalive, bridging from Ethereum, and debugging with mega-evme. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[0xbreadguy](https://clawhub.ai/user/0xbreadguy) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to build, test, debug, and operate applications and smart contracts on MegaETH. It helps agents produce chain-aware wallet, transaction, frontend, RPC, gas, storage, bridge, and security guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Guidance and examples may lead an agent to propose blockchain transactions, swaps, approvals, bridging, or deployments that affect real assets. <br>
Mitigation: Before executing any generated command or transaction, verify the chain ID, recipient, token, amount, spender, slippage, bridge address, and gas settings; prefer testnet or small-value trials first. <br>
Risk: Approval examples can create excessive token spending permissions if adapted without review. <br>
Mitigation: Avoid unlimited approvals unless the spender is fully trusted, and review spender addresses and allowance amounts before signing. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/0xbreadguy/skills/megaeth-ai-developer-skills) <br>
- [MegaETH Docs](https://docs.megaeth.com) <br>
- [MegaETH Real-time API](https://docs.megaeth.com/realtime-api) <br>
- [MegaETH Testnet Guide](https://docs.megaeth.com/testnet) <br>
- [MegaETH Frontier](https://docs.megaeth.com/frontier) <br>
- [MegaEVM](https://github.com/megaeth-labs/mega-evm) <br>
- [MegaEVM Spec](https://github.com/megaeth-labs/mega-evm/blob/main/specs/MiniRex.md) <br>
- [MegaETH Token List](https://github.com/megaeth-labs/mega-tokenlist) <br>
- [EIP-7966 eth_sendRawTransactionSync](https://ethereum-magicians.org/t/eip-7966-eth-sendrawtransactionsync-method/24640) <br>
- [Solady](https://github.com/Vectorized/solady) <br>
- [KyberSwap Aggregator Docs](https://docs.kyberswap.com/kyberswap-solutions/kyberswap-aggregator) <br>
- [viem](https://viem.sh) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline TypeScript, Solidity, JSON, and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include transaction, deployment, gas, storage, RPC, bridge, and security review notes.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
