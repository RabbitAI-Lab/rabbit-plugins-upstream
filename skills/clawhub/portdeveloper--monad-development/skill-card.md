## Description: <br>
Monad Development helps coding agents build Monad dapps, deploy and verify smart contracts with Foundry, and configure frontend integrations with viem or wagmi. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[portdeveloper](https://clawhub.ai/user/portdeveloper) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and coding agents use this skill to create Monad smart contract projects, deploy contracts to Monad testnet or mainnet, verify contracts across Monad explorers, request testnet funding, and set up frontend wallet integrations. <br>

### Deployment Geography for Use: <br>
Global: Asia-Pacific (APAC); Europe, Middle East, and Africa (EMEA); Latin America (LATAM); North America (NAM). <br>

## Known Risks and Mitigations: <br>
Risk: Wallet private keys may be persisted in local files or environment files during deployment workflows. <br>
Mitigation: Use a dedicated low-value deployment wallet, avoid valuable private keys in plaintext or project .env files, restrict wallet files to the user, and review where credentials are stored. <br>
Risk: Mainnet deployment commands can broadcast irreversible blockchain transactions. <br>
Mitigation: Default to testnet unless mainnet is explicitly requested, require user confirmation before any mainnet broadcast, and review transaction parameters before execution. <br>
Risk: Contract verification and faucet workflows may send contract or wallet data to external APIs. <br>
Mitigation: Review verification payloads and wallet addresses before sending them to external services. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/portdeveloper/skills/monad-development) <br>
- [Monad documentation](https://docs.monad.xyz) <br>
- [Monad testnet faucet](https://faucet.monad.xyz) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with command snippets, Solidity examples, TypeScript configuration, and deployment steps.] <br>
**Output Parameters:** [User requests, target Monad network, contract details, wallet or deployment settings, and verification inputs.] <br>
**Other Properties Related to Output:** [Outputs are intended for supervised agent execution and may include commands that interact with wallets, RPC endpoints, faucets, and contract verification services.] <br>

## Skill Version(s): <br>
1.0.0 <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
