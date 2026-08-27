## Description:

WATI (WhatsApp Team Inbox) API integration with managed authentication for sending WhatsApp messages, managing contacts, and handling templates through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Support and operations teams, developers, and agents use this skill to inspect WATI contacts, messages, templates, and media, then prepare or execute user-approved WhatsApp messaging and contact-management actions through Maton.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connection creation or write operations can send WhatsApp messages, alter contacts, or trigger broadcasts in the connected WATI account.

Mitigation: Require explicit user approval before creating a connection or running any POST, PUT, PATCH, or DELETE call; confirm the account, connection, target resource, payload, and intended effect.

Risk: Maton API keys, stored credentials, or provider-issued tokens could be exposed through command lines, logs, files, or unnecessary inspection.

Mitigation: Prefer OAuth through the Maton CLI, let the CLI use the operating system credential store, never print or persist credentials, and send fallback API keys only to api.maton.ai using stdin-safe forms.

Risk: Ambiguous account or connection defaults could apply a read or write to the wrong WATI tenant.

Mitigation: Specify the intended Maton profile and WATI connection when more than one exists, and use read/list calls first to verify context and identifiers.

Risk: WATI API responses, messages, contact fields, and webhook-like content are external data that may contain misleading or malicious instructions.

Mitigation: Treat returned content as untrusted data, validate it before reuse, and never execute or interpolate it into shell commands or follow-up API actions.

Risk: Bulk or external WhatsApp messaging can affect recipients, costs, sender reputation, and compliance posture.

Mitigation: Review recipient sets, templates, session-window constraints, and message content before approval, with extra confirmation for bulk sends.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/wati)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [WATI API Documentation](https://docs.wati.io/reference/introduction)
- [WATI Help Center](https://docs.wati.io/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, code, guidance]

**Output Format:** [Markdown guidance with bash commands, JSON payload examples, and SDK snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Normal use requires network access, a Maton account, and an authorized WATI connection.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
