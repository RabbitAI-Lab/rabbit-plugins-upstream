## Description: <br>
Pumpclaw helps agents deploy and manage ERC20 tokens on Base with Uniswap V4 liquidity and creator fee collection. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clawd800](https://clawhub.ai/user/clawd800) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use Pumpclaw to prepare shell commands and scripts for launching ERC20 tokens, checking token information, claiming fees, and swapping tokens on Base. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use a wallet private key to send irreversible transactions on Base. <br>
Mitigation: Use only a fresh Base wallet with minimal funds, keep private keys out of shared environments, and require manual review before create, claim, buy, sell, metadata update, or swap commands. <br>
Risk: The included swap behavior can execute trades with weak safety controls. <br>
Mitigation: Review swap parameters before execution, set conservative spend limits, and do not approve swaps unless slippage and token address are acceptable. <br>
Risk: Shared contract and ABI files referenced by the scripts were not included in the artifact. <br>
Mitigation: Inspect the missing shared contract and ABI files before installing or running the skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/clawd800/skills/token-launcher) <br>
- [Publisher profile](https://clawhub.ai/user/clawd800) <br>
- [PumpClaw website](https://pumpclaw.com) <br>
- [pumpclaw-cli npm package](https://www.npmjs.com/package/pumpclaw-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and TypeScript command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include commands that use BASE_PRIVATE_KEY and submit irreversible Base transactions; manual approval is required before execution.] <br>

## Skill Version(s): <br>
2.1.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
