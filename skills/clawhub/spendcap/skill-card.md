## Description: <br>
Set hard per-purchase and daily spending limits for AI agents. Approve exceptions, pause access instantly, and get signed proof of every purchase made through Receipt. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[receiptprotocol](https://clawhub.ai/user/receiptprotocol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Receipt account owners and developers use SpendCap to connect an agent to Receipt, set daily and per-purchase spending limits, review exceptions, pause or revoke access, and verify completed purchases. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The persistent Receipt connection includes purchase-capable tooling. <br>
Mitigation: Use SpendCap only when connecting a Receipt account for agent spending controls; confirm the Receipt authorization page, review dashboard limits, and do not call purchase tools during setup. <br>
Risk: A chat message or installation step could be mistaken for spending approval. <br>
Mitigation: Treat only authenticated Receipt owner actions and real Receipt responses as authority for setup status, limits, approvals, Pause, and Revoke. <br>
Risk: SpendCap may be mistaken for a universal spending control. <br>
Mitigation: State that SpendCap currently governs purchases made through Receipt, and avoid presenting it as enforcement for unrelated provider channels. <br>
Risk: Unexpected Receipt tool exposure could expand the setup boundary. <br>
Mitigation: Verify the exact eight universal Receipt tools and reject seller-specific, diagnostic, or unexpected tools before declaring setup complete. <br>


## Reference(s): <br>
- [SpendCap homepage](https://receiptprotocol.com/spendcap) <br>
- [SpendCap ClawHub page](https://clawhub.ai/receiptprotocol/skills/spendcap) <br>
- [Install SpendCap](references/INSTALL.md) <br>
- [SpendCap security boundary](references/SECURITY.md) <br>
- [SpendCap acceptance](references/ACCEPTANCE.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and Receipt URLs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Setup output must be grounded in real Receipt responses; setup must not make purchases.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release, package.json, target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
