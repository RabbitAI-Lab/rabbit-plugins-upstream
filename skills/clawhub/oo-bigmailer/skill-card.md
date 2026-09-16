## Description:

BigMailer enables agents to read, create, update, and delete BigMailer brands, contacts, and contact lists through the OOMOL-connected oo CLI instead of calling the BigMailer API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to manage BigMailer account data through authenticated OOMOL connector actions, including brand lookup and contact/list create, read, update, upsert, and delete workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands that can execute downloaded scripts.

Mitigation: Review the official installer source, version, and integrity before running installation commands, and use the skill only if OOMOL and the oo CLI distribution channel are trusted.

Risk: Write and destructive BigMailer actions can create, update, overwrite, or delete account data.

Mitigation: Confirm the exact target, payload, and expected effect with the user before allowing any write or destructive action.

## Reference(s):

- [BigMailer homepage](https://www.bigmailer.io/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [BigMailer skill page](https://clawhub.ai/oomol/skills/oo-bigmailer)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution and returns connector responses as JSON.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
