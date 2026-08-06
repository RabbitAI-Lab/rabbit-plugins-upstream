## Description: <br>
Arb Engine helps agents support cryptocurrency arbitrage analysis workflows, including triangular arbitrage, dynamic slippage handling, structured output, and error handling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers, traders, and automation teams use this skill to guide cryptocurrency arbitrage analysis, structure market-data inputs and outputs, and reason through slippage, API-key, and error-handling concerns. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests command-execution capability in a cryptocurrency context, which can affect local systems, credentials, or trading workflows. <br>
Mitigation: Require manual confirmation for order placement, package installation, file modification, and shell commands; inspect commands before execution. <br>
Risk: Exchange API keys or market-data credentials may be exposed or over-scoped during setup or automation. <br>
Mitigation: Keep API keys read-only or minimally scoped, avoid withdrawal permissions, and enable trading permissions only when explicitly intended. <br>
Risk: Automated trading guidance may be underspecified for user controls and financial risk boundaries. <br>
Mitigation: Use the skill for analysis and workflow guidance unless a human explicitly approves live trading behavior and validates exchange, slippage, and rate-limit settings. <br>


## Reference(s): <br>
- [Arb Engine ClawHub listing](https://clawhub.ai/thcjp/skills/arb-engine) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON and Python examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include structured success and error result examples for cryptocurrency arbitrage workflows.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
