## Description:

TemplateFox enables agents to read, create, and update TemplateFox data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect TemplateFox connector schemas, run TemplateFox actions, generate PDFs and images, perform PDF utilities, and retrieve account or template information through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: TemplateFox actions can send private URLs, template fields, PDFs, or image inputs through OOMOL as the intermediary for TemplateFox operations.

Mitigation: Confirm the user is comfortable with OOMOL-mediated TemplateFox actions and review exact payloads before approving work involving private URLs or generated files.

Risk: Write actions can generate PDFs, generate images, or merge PDFs from user-provided inputs.

Mitigation: Fetch the live action schema before constructing payloads and require user confirmation for write or destructive actions before running the connector command.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-templatefox)
- [TemplateFox Homepage](https://templatefox.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [OOMOL TemplateFox Connection](https://console.oomol.com/app-connections?provider=templatefox)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions may return JSON data and meta.executionId values, including signed download URLs for generated files.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
