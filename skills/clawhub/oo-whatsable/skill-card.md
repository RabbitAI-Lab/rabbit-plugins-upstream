## Description:

WhatsAble helps an agent operate the WhatsAble connector through the OOMOL-connected oo CLI for reading, creating, updating, and sending WhatsApp messages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect WhatsAble action schemas and run WhatsAble connector actions through the oo CLI, including sending WhatsApp text messages with optional attachment URLs after user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer pipelines that can execute downloaded shell or PowerShell scripts without independent verification.

Mitigation: Review the skill before installation, prefer a verified or package-manager installation path for the oo CLI, and confirm message recipients, content, and attachment URLs before send actions.

## Reference(s):

- [WhatsAble Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-whatsable)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [WhatsAble Homepage](https://whatsable.app)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, text]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [State-changing WhatsAble actions require user confirmation before execution.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
