## Description: <br>
Guides an agent through adding liquidity, removing liquidity, and collecting fees on Uniswap V2/V3/V4 pools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill when asking an agent to manage Uniswap liquidity positions, including pool selection, withdrawals, and fee collection. Because the release covers real liquidity actions, it should be used only with explicit transaction previews and confirmations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill covers real Uniswap liquidity operations while the release security summary says the instructions are broad and under-scoped for financial automation. <br>
Mitigation: Review the skill carefully before installing and require explicit previews and confirmations for every wallet-affecting action. <br>
Risk: Unattended approvals, deposits, withdrawals, fee claims, command execution, or broad file access could create financial or operational exposure. <br>
Mitigation: Do not allow unattended wallet approvals, deposits, withdrawals, fee claims, command execution, or broad file access from this skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/manage-liquidity) <br>
- [Skill source artifact](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON-style result summaries and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include execution logs, transaction status, and configuration guidance; wallet-affecting actions require explicit preview and confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
