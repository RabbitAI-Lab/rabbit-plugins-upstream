## Description: <br>
Build and test Solidity smart contracts with Foundry, including Forge tests, deployment scripts, and Cast/Anvil debugging. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tenequm](https://clawhub.ai/user/tenequm) <br>

### License/Terms of Use: <br>
Apache 2.0 <br>


## Use Case: <br>
Developers and smart contract engineers use this skill to build, test, configure, debug, and deploy Ethereum/EVM contracts with Foundry tools. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill includes live blockchain transaction examples and private-key usage patterns. <br>
Mitigation: Use dry runs, forks, or testnets by default; verify the chain ID and account before any broadcast or send operation. <br>
Risk: Private keys, mnemonics, and API keys may be exposed if copied directly into commands or configuration. <br>
Mitigation: Prefer isolated deployer keys, keystores, hardware wallets, and CI secrets with approval gates; avoid placing secrets directly on the command line. <br>
Risk: Funded wallets or production contracts can be affected by incorrect deployment or interaction commands. <br>
Mitigation: Review generated commands before execution and test contract interactions against local forks or non-production networks first. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/tenequm/skills/foundry-solidity) <br>
- [Skill Homepage](https://github.com/tenequm/skills/tree/main/skills/foundry-solidity) <br>
- [Foundry Testing Guide](references/testing.md) <br>
- [Foundry Deployment Guide](references/deployment.md) <br>
- [Solidity Security & Audit Patterns](references/security.md) <br>
- [Foundry Configuration Reference](references/configuration.md) <br>
- [forge-std API Reference](references/forge-std-api.md) <br>
- [Foundry & Solidity Resources](references/resources.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with Solidity, TOML, YAML, and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include deployment commands that require external RPC endpoints, API keys, or signing keys.] <br>

## Skill Version(s): <br>
0.2.3 (source: SKILL.md frontmatter and evidence release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
