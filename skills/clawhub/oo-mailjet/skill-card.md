## Description:

This skill lets an agent read, create, and update Mailjet contact data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Mailjet contacts from an agent, including listing, retrieving, creating, and updating contact records after inspecting live action schemas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructions include direct internet installer commands that evidence.security flags as suspicious.

Mitigation: Use an official, verified installation method and review installer contents before running setup commands.

Risk: Mailjet write actions can change contact records.

Mitigation: Confirm every write payload and intended effect with the user before executing create or update actions.

Risk: The skill relies on OOMOL as the connector layer with OOMOL-managed credentials.

Mitigation: Install only when that trust relationship is acceptable for the Mailjet account.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-mailjet)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Mailjet Homepage](https://www.mailjet.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the OOMOL oo CLI and can return JSON responses from Mailjet actions.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
