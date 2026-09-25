## Description: <br>
Helps agents send WhatsApp Business messages, manage message templates, and handle media through the WhatsApp Business API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External business teams and developers use this skill to prepare and execute WhatsApp Business messaging workflows, including customer notifications, support replies, media messages, and approved template sends. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can trigger real outbound WhatsApp messages, media uploads, and template changes. <br>
Mitigation: Require a clear recipient and content preview plus explicit user confirmation before any send, media upload, template creation, or template deletion. <br>
Risk: The artifact includes broad API key, file-processing, and command-execution guidance that is not specific to WhatsApp messaging. <br>
Mitigation: Limit use to clearly requested WhatsApp Business tasks and do not treat generic boilerplate as permission to run unrelated commands or file operations. <br>
Risk: WhatsApp delivery depends on approved templates, the 24-hour customer-service window, valid phone numbers, and an active ClawLink connection. <br>
Mitigation: Check the active tool catalog and template status before execution, use approved templates outside the customer-service window, and confirm full recipient phone numbers before sending. <br>


## Reference(s): <br>
- [Skill source artifact](artifact/SKILL.md) <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/whatsapp-messaging) <br>
- [ClawLink WhatsApp connection](https://claw-link.dev/dashboard?add=whatsapp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes recipient and content preview guidance for write operations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence; artifact frontmatter lists 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
