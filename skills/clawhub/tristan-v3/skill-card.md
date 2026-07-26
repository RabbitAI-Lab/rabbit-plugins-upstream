## Description: <br>
Use this skill to run an end-to-end RFQ pipeline for procurement and sourcing operations, including email or Telegram intake, Obsidian-vault storage, pricing calculation, supplier quote comparison, and confirmed-send drafting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yrc96](https://clawhub.ai/user/yrc96) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Procurement and sourcing operators use this skill to manage RFQs from intake through pricing, supplier comparison, draft quote preparation, and confirmed email delivery. It is intended for teams that keep RFQ state in an Obsidian vault and use configured email and Telegram channels for intake and updates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Misconfigured email or Telegram channels could route RFQ information to the wrong place. <br>
Mitigation: Install with a dedicated procurement vault and trusted, explicitly configured email and Telegram channels. <br>
Risk: A drafted quotation could include incorrect pricing or supplier assumptions if placeholders or inputs are not reviewed. <br>
Mitigation: Review every draft and fill required placeholders before confirming any send. <br>
Risk: Highly confidential RFQs may exceed the retention and access controls of the configured vault or messaging channels. <br>
Mitigation: Use only when vault permissions and messaging retention policies are appropriate for the RFQ sensitivity. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yrc96/skills/tristan-v3) <br>
- [Vault Schema](references/vault-schema.md) <br>
- [Telegram Conventions](references/telegram-conventions.md) <br>
- [Email Conventions](references/email-conventions.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, JSON, shell commands, and Obsidian note templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces RFQ notes, response drafts, pricing calculations, supplier rankings, and operational guidance for configured vault, email, and Telegram workflows.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
