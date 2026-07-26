## Description: <br>
Manages OKX Simple Earn, Flash Earn, On-chain Earn, Dual Investment, and AutoEarn via the okx CLI for checking balances, browsing products, subscribing or redeeming earn products, setting lending rates, and managing earn positions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[searchworld](https://clawhub.ai/user/searchworld) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and agents use this skill to operate OKX Earn products through the okx CLI, including account checks, product discovery, subscriptions, redemptions, lending-rate settings, and periodic monitoring workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can operate with live OKX financial authority, including subscriptions, redemptions, lending-rate changes, and earn-product actions. <br>
Mitigation: Use a dedicated OKX subaccount or limited API profile, avoid Withdraw permission unless intentionally needed, and require a fresh explicit confirmation before every financial action. <br>
Risk: The skill depends on a globally installed OKX CLI from npm that receives access to the user's OKX account context. <br>
Mitigation: Install only after reviewing the package and version, and configure account access through okx config init rather than pasting credentials into chat. <br>
Risk: Periodic /loop monitoring can repeatedly inspect account or product state and may encourage recurring actions if boundaries are unclear. <br>
Mitigation: Set explicit currency, cadence, duration, and stop rules before running monitoring workflows, and keep financial actions gated behind separate user confirmation. <br>
Risk: Some OKX Earn operations have product-specific constraints such as live-only execution, fixed-term locks, DCD quote timing, and AutoEarn's 24-hour disable restriction. <br>
Mitigation: Show product-specific summaries, warnings, and current terms before execution, then verify the resulting order or balance after each action. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/searchworld/skills/okx-cex-earn) <br>
- [OKX](https://www.okx.com) <br>
- [AutoEarn Command Reference](references/autoearn-commands.md) <br>
- [DCD Command Reference](references/dcd-commands.md) <br>
- [Flash Earn Command Reference](references/flash-earn-commands.md) <br>
- [On-chain Earn Command Reference](references/onchain-commands.md) <br>
- [Simple Earn Command Reference](references/savings-commands.md) <br>
- [Templates and Reference](references/templates.md) <br>
- [Multi-Step Workflows](references/workflows.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with inline shell commands and tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses JSON CLI output for account and product queries, then presents human-readable summaries rather than raw terminal output.] <br>

## Skill Version(s): <br>
1.4.0 (source: artifact/SKILL.md frontmatter metadata.version and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
