## Description:

Build and test Solidity contracts with Foundry. Use when developing Ethereum contracts, writing Forge tests, deploying with scripts, or debugging with Cast/Anvil.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and smart contract engineers use this skill to build, test, debug, configure, and deploy Solidity contracts with Foundry tools including Forge, Cast, Anvil, and Chisel.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Commands may involve private keys, mnemonics, RPC URLs, and explorer API keys.

Mitigation: Use throwaway or testnet keys where possible and avoid pasting secrets into commands, shells, logs, or CI output.

Risk: Deployment examples can create real on-chain transactions when broadcast flags and live RPC endpoints are used.

Mitigation: Run dry-runs first, omit --broadcast unless intentional, and verify the target network and contract address before sending transactions.

Risk: Production dependency and CI examples may pull mutable external code or actions.

Mitigation: Pin dependencies and GitHub Actions versions before production use.

Risk: Broadcast artifacts or Anvil state files may contain sensitive project data.

Mitigation: Keep those artifacts out of version control when they may expose private deployment or testing data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/tenequm/skills/foundry-solidity)
- [OpenClaw Homepage](https://github.com/tenequm/skills/tree/main/skills/foundry-solidity)
- [Testing](references/testing.md)
- [Forge Std API](references/forge-std-api.md)
- [Solidity Modern](references/solidity-modern.md)
- [Deployment](references/deployment.md)
- [Configuration](references/configuration.md)
- [Gas Optimization](references/gas-optimization.md)
- [Patterns](references/patterns.md)
- [Security](references/security.md)
- [Resources](references/resources.md)
- [Debugging](references/debugging.md)
- [Dependencies](references/dependencies.md)
- [CI/CD](references/cicd.md)
- [Chisel](references/chisel.md)
- [Cast Advanced](references/cast-advanced.md)
- [Anvil Advanced](references/anvil-advanced.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Solidity, TOML, YAML, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference optional wallet, RPC, explorer API, and test address environment variables for Foundry workflows.]

## Skill Version(s):

0.2.5 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
