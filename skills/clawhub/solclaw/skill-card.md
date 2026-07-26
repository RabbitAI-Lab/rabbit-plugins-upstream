## Description: <br>
SolClaw enables non-custodial USDC payments on Solana devnet by agent name, including registration, balances, subscriptions, allowances, invoices, and read-only API queries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sterdam](https://clawhub.ai/user/sterdam) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and autonomous agent operators use SolClaw to send, receive, monitor, and automate non-custodial USDC payments on Solana devnet using agent names instead of wallet addresses. The skill also helps users inspect balances, invoices, subscriptions, allowances, reputation, and read-only API state. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill manages Solana signing keys and may import or export private keys. <br>
Mitigation: Use a dedicated low-balance wallet, avoid pasting private keys directly into shell commands, and review key import or export commands before running them. <br>
Risk: Payment, allowance, subscription, and invoice commands can authorize or move funds. <br>
Mitigation: Verify recipient agent names, amounts, allowances, and invoices before execution, and use spending caps for routine activity. <br>
Risk: Heartbeat guidance includes cron persistence for repeated local execution. <br>
Mitigation: Review any cron entry before installation, confirm the log destination, and know how to disable the scheduled job. <br>


## Reference(s): <br>
- [SolClaw Skill](https://solclaw.xyz/skill.md) <br>
- [SolClaw Heartbeat](https://solclaw.xyz/heartbeat.md) <br>
- [SolClaw API Health](https://solclaw.xyz/api/health) <br>
- [ClawHub Skill Page](https://clawhub.ai/sterdam/skills/solclaw) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, command tables, and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes commands that may sign local Solana transactions or configure recurring heartbeat checks.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
