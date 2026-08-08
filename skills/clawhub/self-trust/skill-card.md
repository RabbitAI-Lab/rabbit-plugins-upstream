## Description: <br>
Self-trust is a deterministic personal-finance discipline skill for bookkeeping, spending approval with cooldowns, budget goals and rewards, monthly calibration, reconciliation, debt and mortgage modeling, multi-currency workflows, and optional encrypted local ledgers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shellcdev](https://clawhub.ai/user/shellcdev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to turn natural-language personal-finance requests into deterministic ledger operations and user-facing receipts, opinions, reports, and guidance. It is intended for personal discipline and bookkeeping workflows, with explicit disclosure that trust, asset-protection, and legal topics have no legal effect. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The local ledger can contain sensitive financial profile data. <br>
Mitigation: Use a deliberate data directory and enable encryption for sensitive ledgers. <br>
Risk: Secrets supplied directly in commands or environment variables can be exposed through shell history or process environments. <br>
Mitigation: Prefer key-file mode or careful passphrase handling, and avoid retaining passwords in shell history. <br>
Risk: Incorrect inferred categories, planned status, amounts, or pending-request details can change ledger outcomes. <br>
Mitigation: Verify those values before confirming ledger-changing actions. <br>
Risk: Encrypted key-file mode depends on retaining the key file. <br>
Mitigation: Back up the key file separately because losing it can make encrypted ledger data unrecoverable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/shellcdev/skills/self-trust) <br>
- [Interaction rules](references/interaction.md) <br>
- [Rendering guide](references/rendering.md) <br>
- [Initialization guide](references/init.md) <br>
- [Spending approval guide](references/approval.md) <br>
- [Reporting guide](references/report.md) <br>
- [Data modes and reconciliation](references/data-modes.md) <br>
- [Exceptions and overrides](references/exceptions.md) <br>
- [Contract schema](references/contract-schema.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown or plain-text user responses, shell command invocations, and structured JSON emitted by the deterministic local engine.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Financial amounts, decisions, cooldowns, and reports are expected to be quoted from engine JSON rather than recalculated by the agent.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
