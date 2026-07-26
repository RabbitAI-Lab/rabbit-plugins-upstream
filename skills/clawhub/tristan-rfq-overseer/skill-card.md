## Description: <br>
Runs an end-to-end RFQ pipeline for procurement teams, covering email or Telegram intake, Obsidian-vault storage, pricing calculation, supplier quote comparison, and confirmed-send quotation drafting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yrc96](https://clawhub.ai/user/yrc96) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Procurement and sourcing operators use this skill to manage RFQs from intake through quote drafting while keeping RFQ state in an Obsidian vault. It supports pricing baselines, optional pricing strategies, supplier comparison, certificate tracking, and explicit confirmation before outbound email delivery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill operates on RFQ vault contents and connected email and Telegram channels. <br>
Mitigation: Use a dedicated vault or narrow RFQ folders, connect only the required channels, and run a dry test before deployment. <br>
Risk: An outbound quotation could be sent before the account owner has reviewed the draft. <br>
Mitigation: Verify that the email connector enforces explicit live confirmation before any quote is sent, and re-confirm after draft edits. <br>
Risk: Inbound emails, Telegram messages, or vault notes may contain instructions from external parties. <br>
Mitigation: Treat those contents as data and act only on the documented skill triggers and account-owner confirmations. <br>
Risk: Incomplete supplier prices, certificate details, or line items could produce misleading quotes or rankings. <br>
Mitigation: Keep placeholders for missing values, review pricing and supplier comparisons, and confirm certificate and cost inputs before sending a client quote. <br>


## Reference(s): <br>
- [Vault Schema](references/vault-schema.md) <br>
- [Email Conventions](references/email-conventions.md) <br>
- [Telegram Conventions](references/telegram-conventions.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/yrc96/skills/tristan-rfq-overseer) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, JSON, and shell-command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May update RFQ notes or produce draft quotation text only after the configured workflow and user confirmation checks are satisfied.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
