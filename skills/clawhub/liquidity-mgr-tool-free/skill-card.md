## Description: <br>
Guides personal users through Uniswap V2, V3, and V4 liquidity-position queries, basic add/remove liquidity workflows, fee checks, earnings estimates, and impermanent-loss calculations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External individual DeFi users and developers use this skill to guide Uniswap liquidity management tasks, including pool and position lookup, single-position liquidity changes, basic fee and range review, and impermanent-loss estimation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide wallet-connected on-chain liquidity actions that may affect user funds. <br>
Mitigation: Keep usage read-only unless the user explicitly approves a transaction, then require simulation and separate confirmation before add or remove liquidity operations. <br>
Risk: Wallet credentials or signing authority could be exposed or misused during agent-driven workflows. <br>
Mitigation: Do not give the agent wallet private keys or unattended signing access; keep credentials local and require manual wallet confirmation. <br>
Risk: Liquidity strategies can lose value through impermanent loss, range drift, gas costs, price movement, or smart-contract issues. <br>
Mitigation: Treat calculations and strategy suggestions as estimates, start with small positions, review protocol and pool risk, and include gas and market movement before executing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/liquidity-mgr-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell, Python, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include structured response examples with success status, result data, execution logs, and errors.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
