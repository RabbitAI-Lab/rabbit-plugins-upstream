## Description: <br>
Provides basic guidance for writing WhatsApp-formatted messages, including native bold, italic, strikethrough and list syntax, unsupported Markdown alternatives, and simple order or logistics notification templates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and content authors use this skill to convert business notifications or everyday messages into WhatsApp-friendly text that avoids unsupported Markdown patterns. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill manifest requests shell execution even though the guide is documented as pure Markdown guidance. <br>
Mitigation: Review requested tool permissions before installation; prefer a version without exec access and grant write access only when local file edits are expected. <br>
Risk: WhatsApp formatting may render differently across clients or fail when unsupported Markdown patterns remain in the message. <br>
Mitigation: Preview or test important messages in the target WhatsApp client and check for unsupported table, heading, double-asterisk, or double-tilde syntax before sending. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/whatsapp-styling-guide-free) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown-like WhatsApp message text with concise explanatory guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Does not send messages or call the WhatsApp API; generated text should be reviewed before use.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
