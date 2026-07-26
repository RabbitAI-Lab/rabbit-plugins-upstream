## Description: <br>
Comprehensive guide for Polygon PoS blockchain development. Use when deploying smart contracts to Polygon, testing on Amoy testnet, getting test tokens from faucets, or verifying contracts on Polygonscan. Supports Foundry framework with deployment scripts and testing strategies. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[akshatgada](https://clawhub.ai/user/akshatgada) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to create, test, deploy, and verify smart contracts on Polygon PoS using Foundry, with Amoy testnet as the default path before mainnet deployment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow handles private keys and API keys for blockchain deployment. <br>
Mitigation: Use a dedicated low-balance wallet, store secrets in an uncommitted .env file, and avoid exposing keys in logs or shared terminals. <br>
Risk: Broadcasting deployment or cast commands can send real transactions on the selected network. <br>
Mitigation: Manually confirm the network, wallet, gas cost, contract address, and transaction details before using --broadcast or cast send. <br>
Risk: The setup path includes curl-to-bash installation commands. <br>
Mitigation: Review installer scripts before running them and install tooling from trusted sources. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/akshatgada/skills/polygon-pos-dev) <br>
- [Foundry Deployment Guide for Polygon PoS](references/foundry-deployment.md) <br>
- [Testing Strategies for Polygon PoS](references/testing-strategies.md) <br>
- [Contract Verification on Polygonscan](references/contract-verification.md) <br>
- [Foundry Documentation](https://book.getfoundry.sh/) <br>
- [Polygon Documentation](https://docs.polygon.technology/) <br>
- [Polygon Gas Station](https://gasstation.polygon.technology/) <br>
- [Polygon Amoy Faucet](https://www.alchemy.com/faucets/polygon-amoy) <br>
- [Amoy Polygonscan](https://amoy.polygonscan.com) <br>
- [Polygonscan](https://polygonscan.com) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline bash, TOML, and Solidity code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes deployment checklists, network configuration, verification guidance, testing patterns, and wallet key-handling cautions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
