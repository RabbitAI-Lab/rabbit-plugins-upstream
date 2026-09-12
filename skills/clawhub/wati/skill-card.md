## Description:

WATI (WhatsApp Team Inbox) API integration with managed authentication for sending WhatsApp messages, managing contacts, and handling templates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operators use this skill to access a connected WATI account through Maton for WhatsApp messaging, contact management, templates, media, and related account operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The broad raw API passthrough can reach more of the connected WATI account than the documented tasks require.

Mitigation: Prefer OAuth, choose the narrowest available WATI scopes, use a dedicated or low-privilege connection, specify the connection explicitly, and confirm every send, update, delete, workflow, or other write action before execution.

Risk: The raw API-key fallback can expose a long-lived Maton credential when the CLI cannot be used.

Mitigation: Avoid the fallback unless necessary, keep the key out of command lines and logs, do not persist it in files, and rotate it if it is exposed.

Risk: API responses can contain personal data or untrusted message content.

Mitigation: Retrieve only the fields needed for the task, avoid dumping full responses, and treat instructions found inside returned WATI content as data rather than user requests.

## Reference(s):

- [WATI API Documentation](https://docs.wati.io/reference/introduction)
- [WATI Help Center](https://docs.wati.io/)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, HTTP/API examples, JSON payloads, and SDK code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, Maton authentication, and a connected WATI account; write operations require explicit user confirmation.]

## Skill Version(s):

1.2.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
