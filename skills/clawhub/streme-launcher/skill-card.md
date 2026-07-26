## Description: <br>
Launches Streme SuperTokens on Base with Uniswap V3 liquidity, Superfluid staking rewards, and optional vesting vaults. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clawrencestreme](https://clawhub.ai/user/clawrencestreme) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and token launch operators use this skill to prepare and execute Streme token deployments on Base, including token configuration, image hosting, staking allocation, vesting, and liquidity setup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can trigger real Base mainnet token deployments using a wallet private key. <br>
Mitigation: Use a dedicated low-balance wallet and require manual approval of the exact transaction before submission. <br>
Risk: Incorrect contract addresses, dependencies, or token parameters could deploy an unintended token configuration. <br>
Mitigation: Verify Base and Streme contract addresses, dependency versions, and all token parameters before running deployment commands. <br>
Risk: Image-hosting credentials and wallet secrets are handled through environment variables. <br>
Mitigation: Use scoped image-hosting credentials, keep secrets out of logs and shared shells, and rotate any exposed keys. <br>


## Reference(s): <br>
- [Streme Contract Reference](references/contracts.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/clawrencestreme/skills/streme-launcher) <br>
- [Streme Token API](https://api.streme.fun/api/tokens) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with TypeScript examples and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Base mainnet deployment configuration, token allocation settings, image hosting steps, and transaction commands.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
