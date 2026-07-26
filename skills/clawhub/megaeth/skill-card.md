## Description: <br>
End-to-end MegaETH development playbook covering wallet operations, token swaps, synchronous transaction receipts, RPC optimization, real-time mini-block subscriptions, storage-aware contract patterns, MegaEVM gas behavior, bridging, and debugging. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[0xguardbot](https://clawhub.ai/user/0xguardbot) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and AI coding agents use this skill to build, test, deploy, and troubleshoot MegaETH dApps, wallet flows, transactions, smart contracts, RPC integrations, and real-time WebSocket features. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can provide ready-to-run blockchain transaction, bridge, swap, approval, deployment, or broadcast guidance for irreversible asset-moving actions. <br>
Mitigation: Verify chain ID, destination or contract address, amount, spender, fees, and calldata; prefer testnet or dry-run first; require explicit confirmation before broadcasting. <br>
Risk: MegaETH-specific gas and storage behavior can make transactions unexpectedly fail or become expensive if standard EVM assumptions are reused. <br>
Mitigation: Use MegaETH-aware remote gas estimation for non-trivial operations, review SSTORE-heavy patterns, and test with MegaETH-specific debugging or replay tooling. <br>
Risk: Immediate transaction receipts may be mistaken for final settlement in high-value workflows. <br>
Mitigation: Treat synchronous receipts as soft-finality and wait for additional confirmations or L1 finalization for high-value or otherwise irreversible actions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/0xguardbot/skills/megaeth) <br>
- [MegaETH Documentation](https://docs.megaeth.com) <br>
- [MegaETH Real-time API](https://docs.megaeth.com/realtime-api) <br>
- [MegaEVM Specification](https://github.com/megaeth-labs/mega-evm/blob/main/specs/MiniRex.md) <br>
- [EIP-7966 eth_sendRawTransactionSync](https://ethereum-magicians.org/t/eip-7966-eth-sendrawtransactionsync-method/24640) <br>
- [MegaETH Token List](https://github.com/megaeth-labs/mega-tokenlist) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline code blocks, command examples, configuration snippets, and implementation guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include blockchain transaction, deployment, wallet, RPC, and smart contract guidance that should be reviewed before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
