## Description:

Build and test Solidity smart contracts with the Foundry toolkit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use this skill to build, test, configure, debug, and deploy Ethereum/EVM smart contracts with Foundry tools such as forge, cast, anvil, and chisel.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live transaction and private-key examples could move funds if copied without safeguards.

Mitigation: Use local or testnet keys, dry-run before any --broadcast or cast send, and manually verify chain, account, recipient, value, and approvals before execution.

Risk: Deployment and CI examples rely on sensitive environment variables such as PRIVATE_KEY and explorer API keys.

Mitigation: Store secrets only in approved local or CI secret stores, never paste production seed phrases or private keys into commands, and restrict deployment approvals.

## Reference(s):

- [Foundry Solidity ClawHub page](https://clawhub.ai/tenequm/skills/foundry-solidity)
- [Foundry Solidity homepage](https://github.com/tenequm/skills/tree/main/skills/foundry-solidity)
- [Foundry & Solidity Resources](references/resources.md)
- [Foundry Testing Guide](references/testing.md)
- [forge-std API Reference](references/forge-std-api.md)
- [Modern Solidity (0.8.30)](references/solidity-modern.md)
- [Foundry Deployment Guide](references/deployment.md)
- [Foundry Configuration Reference](references/configuration.md)
- [Solidity Gas Optimization Guide](references/gas-optimization.md)
- [Solidity Patterns and Idioms](references/patterns.md)
- [Solidity Security & Audit Patterns](references/security.md)
- [Debugging Workflows](references/debugging.md)
- [Dependency Management](references/dependencies.md)
- [CI/CD Integration](references/cicd.md)
- [Chisel REPL](references/chisel.md)
- [Cast Advanced Usage](references/cast-advanced.md)
- [Anvil Advanced Usage](references/anvil-advanced.md)
- [GitHub Actions encrypted secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets#using-encrypted-secrets-in-a-workflow)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with Solidity, TOML, YAML, and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference optional Foundry CLI tools and optional RPC, explorer API key, and deployer key environment variables.]

## Skill Version(s):

0.2.4 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
