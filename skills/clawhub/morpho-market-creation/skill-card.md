## Description: <br>
Deploys Morpho markets backed by Api3 oracles. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[api3dao](https://clawhub.ai/user/api3dao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and DeFi operators use this skill to validate API3 feeds, prepare oracle and market parameters, deploy a Morpho oracle, and create a Morpho market with guided approval checkpoints. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Script-based deployment requires a local wallet mnemonic. <br>
Mitigation: Prefer Safe or Etherscan options when possible; if scripts are used, use a dedicated low-value deployer wallet and do not share or expose the mnemonic. <br>
Risk: Oracle deployment and market creation can submit irreversible blockchain transactions. <br>
Mitigation: Independently verify chain ID, contract addresses, oracle parameters, IRM, LLTV, and transaction details before approving execution. <br>
Risk: Incorrect feed or token address selection can create an unusable or unsafe market. <br>
Mitigation: Run the Morpho Oracle Tester, confirm successful test results, and keep API3 reader proxy addresses separate from ERC-20 token addresses. <br>


## Reference(s): <br>
- [Morpho Market Creation on ClawHub](https://clawhub.ai/api3dao/skills/morpho-market-creation) <br>
- [API3 publisher profile on ClawHub](https://clawhub.ai/user/api3dao) <br>
- [API3 Market integration page example](https://market.api3.org/ethereum/eth-usd/integrate) <br>
- [Morpho Oracle Tester](https://oracles.morpho.dev/oracle-tester) <br>
- [Morpho Blue addresses documentation](https://docs.morpho.org/get-started/resources/addresses/#morpho-blue) <br>
- [Artifact README](README.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, text] <br>
**Output Format:** [Markdown conversation with inline shell commands, URLs, and configuration-file guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires pnpm, ts-node, WALLET_MNEMONIC, oracle-params.json, and market-params.json; script paths can submit blockchain transactions after user approval.] <br>

## Skill Version(s): <br>
0.6.0 (source: SKILL.md metadata, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
