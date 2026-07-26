## Description: <br>
Deploys Morpho markets backed by Api3 oracles. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[metobom](https://clawhub.ai/user/metobom) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and DeFi operators use this skill to validate API3 feeds, deploy a Morpho-compatible oracle, and create a Morpho market with confirmed token, oracle, IRM, and LLTV parameters. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A wallet seed phrase may be used for script-based oracle deployment and market creation. <br>
Mitigation: Prefer Safe, hardware wallet, or external wallet flows; if a mnemonic is used, keep it out of commits and shared logs. <br>
Risk: Incorrect chain, token, oracle, IRM, or LLTV parameters can create an unintended or unsafe market. <br>
Mitigation: Verify every chain, address, oracle parameter, token address, and LLTV before signing, and rehearse with a testnet or low-risk wallet before mainnet execution. <br>
Risk: Signed blockchain transactions are irreversible once broadcast. <br>
Mitigation: Require explicit approval before transaction execution and review the transaction details in Safe, Etherscan, or the signing wallet before submitting. <br>


## Reference(s): <br>
- [Morpho Market Creation on ClawHub](https://clawhub.ai/metobom/skills/morpho-market-creation) <br>
- [API3 Market Integration Example](https://market.api3.org/ethereum/eth-usd/integrate) <br>
- [Morpho Oracle Tester](https://oracles.morpho.dev/oracle-tester) <br>
- [Morpho Blue Addresses](https://docs.morpho.org/get-started/resources/addresses/#morpho-blue) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, configuration file instructions, transaction hashes, oracle addresses, and market IDs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires pnpm and ts-node; script-based transaction paths require WALLET_MNEMONIC, while Safe or Etherscan flows can avoid placing a seed phrase in .env.] <br>

## Skill Version(s): <br>
0.3.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
