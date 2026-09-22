## Description:

Send WhatsApp messages, manage templates, handle media, and automate WhatsApp Business messaging workflows via the WhatsApp Business API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hith3sh](https://clawhub.ai/user/hith3sh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and customer communication teams use this skill to connect a WhatsApp Business account through ClawLink, discover available WhatsApp tools, send approved messages and media, and manage templates with explicit confirmation for write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a mutable third-party plugin that can send real customer messages and handle WhatsApp Business account tokens.

Mitigation: Install only from a trusted ClawHub and ClawLink path, confirm plugin source or version where possible, and require explicit approval before any message, media send, template creation, or deletion.

Risk: Messages reach real WhatsApp users and cannot be recalled after sending.

Mitigation: Preview write actions and confirm recipient phone numbers, phone number IDs, message content, and media before execution.

Risk: Free-form WhatsApp messages are constrained by the 24-hour customer service window, and templates must be approved before use.

Mitigation: Check whether the conversation is inside the service window and use approved templates when required.

Risk: Media sends and downloads can fail when media URLs are inaccessible, unsupported, or expired.

Mitigation: Validate media URLs and MIME types before upload, and refresh media download URLs with the media info tool when needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/hith3sh/skills/whatsapp-messaging)
- [WhatsApp Business Platform Cloud API Documentation](https://developers.facebook.com/docs/whatsapp/cloud-api)
- [WhatsApp Business API Message Reference](https://developers.facebook.com/docs/whatsapp/api/messages)
- [WhatsApp Message Templates Guidelines](https://developers.facebook.com/docs/whatsapp/message-templates)
- [ClawLink](https://claw-link.dev/?utm_source=clawhub&utm_medium=referral&utm_content=whatsapp-messaging)
- [ClawLink Docs](https://docs.claw-link.dev/openclaw)
- [ClawLink Verification](https://claw-link.dev/verify)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON parameter examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a connected WhatsApp Business account through ClawLink for live tool execution.]

## Skill Version(s):

1.0.6 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
