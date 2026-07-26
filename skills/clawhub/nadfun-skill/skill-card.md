## Description: <br>
Launch, trade, and monitor Monad blockchain tokens using bonding curves, permit signatures, and on-chain event queries with viem integration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaki9501](https://clawhub.ai/user/zaki9501) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to guide NadFun and Monad token launchpad workflows, including token creation, trading, quoting, event monitoring, wallet setup, and API key management. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Wallet or API-key misuse could expose funds or credentials. <br>
Mitigation: Use a dedicated low-balance wallet, avoid primary wallets and treasury keys, and keep private keys, cookies, and API keys out of logs and commits. <br>
Risk: Incorrect transaction parameters could send funds to the wrong target or create unintended trades. <br>
Mitigation: Require manual confirmation of token, amount, slippage, deadline, gas, recipient, and contract address before any transaction. <br>
Risk: The security evidence flags high-impact wallet and API-key authority without enough explicit safety boundaries. <br>
Mitigation: Review and scan the skill before deployment, and install it only when NadFun or Monad trading and token-launch workflows are intended. <br>


## Reference(s): <br>
- [NadFun Integration Guide](https://nad.fun/skill.md) <br>
- [NadFun ABI Reference](https://nad.fun/abi.md) <br>
- [NadFun Quote Reference](https://nad.fun/quote.md) <br>
- [NadFun Trading Reference](https://nad.fun/trading.md) <br>
- [NadFun Token Reference](https://nad.fun/token.md) <br>
- [NadFun Token Creation Reference](https://nad.fun/create.md) <br>
- [NadFun Indexer Reference](https://nad.fun/indexer.md) <br>
- [NadFun Agent API Reference](https://nad.fun/agent-api.md) <br>
- [NadFun Wallet Reference](https://nad.fun/wallet.md) <br>
- [NadFun AUSD Reference](https://nad.fun/ausd.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/zaki9501/skills/nadfun-skill) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with TypeScript and bash snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes transaction setup, network constants, contract addresses, wallet handling, API key handling, and manual confirmation guidance.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
