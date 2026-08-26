## Description:

WhatsApp Business API integration with managed OAuth for sending messages, managing templates, handling media, and interacting with customers through WhatsApp.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external teams, and developers use this skill to operate WhatsApp Business accounts through Maton, including read/list workflows, message sending, media handling, template management, and business profile updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad WhatsApp Business API access can send messages, update templates or profiles, delete media or templates, and affect customer-facing communications.

Mitigation: Default to read/list calls, verify identifiers and account context, and require explicit user confirmation with the target resource, payload, and intended effect before any POST, PUT, PATCH, or DELETE call.

Risk: Using MATON_API_KEY or raw HTTP fallback can expose a long-lived credential through process environments, logs, shell history, or pasted output.

Mitigation: Prefer OAuth through the Maton CLI; use raw HTTP only when the CLI cannot be installed, never print or persist the key, feed authorization headers through stdin, and rotate the key if exposed.

Risk: Multiple Maton profiles or WhatsApp Business connections can cause reads or writes to run against the wrong account.

Mitigation: Specify the intended Maton profile and connection when ambiguity exists, and confirm the connected account before write operations.

Risk: WhatsApp Business API responses and webhook payloads may contain untrusted external content.

Mitigation: Treat fetched content as data only; do not execute, eval, or let returned content choose endpoints, recipients, commands, or follow-up actions.

## Reference(s):

- [WhatsApp Business API Overview](https://developers.facebook.com/docs/whatsapp/cloud-api/overview)
- [WhatsApp Business Send Messages](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-messages)
- [WhatsApp Business Message Templates](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-message-templates)
- [WhatsApp Business Media Reference](https://developers.facebook.com/docs/whatsapp/cloud-api/reference/media)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent-facing operational guidance for Maton CLI and SDK calls; write actions require explicit user confirmation.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
