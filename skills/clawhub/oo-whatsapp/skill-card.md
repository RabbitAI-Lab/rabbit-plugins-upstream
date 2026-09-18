## Description:

WhatsApp (whatsapp.com) operations through OOMOL's oo CLI for reading, creating, updating, and deleting WhatsApp Business data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate a connected WhatsApp Business account through OOMOL, including reading business profile and template data, sending messages, uploading media, and managing message templates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks for broad oo CLI authority over a connected WhatsApp Business account.

Mitigation: Install only when the user trusts OOMOL and is comfortable with an agent using the connected account.

Risk: Write and destructive actions can send messages, upload media, create templates, or delete templates.

Mitigation: Inspect the live action schema and confirm the exact payload and effect with the user before any write or destructive action.

Risk: The security guidance flags unsafe direct remote installer commands.

Mitigation: Prefer installation instructions that verify downloaded installers before execution, and install the CLI only when it is missing or needed after an auth or connection failure.

## Reference(s):

- [ClawHub WhatsApp skill listing](https://clawhub.ai/oomol/skills/oo-whatsapp)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [WhatsApp homepage](https://www.whatsapp.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
