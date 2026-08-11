## Description: <br>
Set hard per-purchase and daily spending limits for AI agents. Approve exceptions, pause access instantly, and get signed proof of every purchase made through Receipt. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[receiptprotocol](https://clawhub.ai/user/receiptprotocol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use SpendCap to connect or reuse a Receipt OAuth account, set daily and per-purchase spending limits for an AI agent, approve exceptions, and pause or revoke spending authority for purchases made through Receipt. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: SpendCap connects or reuses a Receipt OAuth account and makes Receipt tools available to the agent. <br>
Mitigation: Proceed only when the owner trusts Receipt, verify the Receipt authorization URL, and use Pause or Revoke controls when spending access should stop. <br>
Risk: An agent could misstate limits or setup status if it relies on chat text or page visits instead of Receipt records. <br>
Mitigation: Populate app names, limits, statuses, and approval URLs only from real Receipt responses, and confirm the saved SpendCap through receipt_get_account before declaring setup complete. <br>
Risk: Setup actions could unintentionally browse sellers, quote, purchase, reserve funds, or move money. <br>
Mitigation: During setup, restrict activity to connection, OAuth completion, exact Receipt tool-boundary verification, and free account state checks. <br>


## Reference(s): <br>
- [SpendCap homepage](https://receiptprotocol.com/spendcap) <br>
- [ClawHub SpendCap release page](https://clawhub.ai/receiptprotocol/skills/spendcap) <br>
- [SpendCap security boundary](references/SECURITY.md) <br>
- [Install SpendCap](references/INSTALL.md) <br>
- [SpendCap acceptance](references/ACCEPTANCE.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown with inline bash commands and trusted Receipt URLs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses real Receipt responses for app names, limits, statuses, and approval URLs; setup must not make purchases or move funds.] <br>

## Skill Version(s): <br>
1.0.1 (source: package.json, release evidence, skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
