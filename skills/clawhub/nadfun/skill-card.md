## Description: <br>
Nadfun helps agents work with the NadFun Monad token launchpad for bonding curve trading, token creation, real-time event streaming, and historical data queries using viem and REST APIs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[portdeveloper](https://clawhub.ai/user/portdeveloper) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, trading bot builders, and analytics teams use this skill to integrate with NadFun on Monad for wallet setup, quotes, token trading, token creation, holdings, market data, and event indexing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide wallet and API workflows that expose private keys, session cookies, or API keys if copied into prompts, logs, source control, or console output. <br>
Mitigation: Use a dedicated low-balance wallet, store secrets in a secret manager or environment variables, and keep private keys, session cookies, and API keys out of prompts, logs, and repositories. <br>
Risk: The skill can help prepare or sign fund-moving transactions and token approvals on Monad. <br>
Mitigation: Verify the selected network, contract address, spender address, slippage, deadline, and approval scope before signing; avoid unlimited approvals unless explicitly intended. <br>
Risk: Downloaded nad.fun documentation or configuration may change over time. <br>
Mitigation: Review downloaded NadFun files and server-resolved release evidence before relying on them in an agent workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/portdeveloper/skills/nadfun) <br>
- [nad.fun](https://nad.fun) <br>
- [NadFun skill guide](https://nad.fun/skill.md) <br>
- [NadFun Agent API guide](https://nad.fun/agent-api.md) <br>
- [NadFun trading guide](https://nad.fun/trading.md) <br>
- [NadFun token creation guide](https://nad.fun/create.md) <br>
- [NadFun indexer guide](https://nad.fun/indexer.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with TypeScript, JSON, bash, and curl examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance can include wallet, API key, RPC endpoint, contract address, and transaction-signing configuration.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
