## Description:

Connects an agent to Formstack through the OOMOL oo CLI to list, retrieve, create, update, and delete Formstack forms, fields, and submissions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business operations teams use this skill to work with Formstack forms and submissions through an authenticated OOMOL connection. It supports read workflows and user-approved write or delete workflows that change Formstack data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path asks users to run a remote installer.

Mitigation: Use safer oo CLI installation steps when available, verify the installer source and integrity, and avoid administrator privileges unless clearly required.

Risk: Write actions can create or update Formstack submissions.

Mitigation: Review the live action schema, exact payload, target form, and expected effect before approving create or update actions.

Risk: The delete action can permanently remove Formstack submissions and associated data.

Mitigation: Require explicit user approval for the specific submission target before running destructive delete actions.

## Reference(s):

- [ClawHub Formstack Skill](https://clawhub.ai/oomol/skills/oo-formstack)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Formstack Homepage](https://www.formstack.com/)
- [OOMOL oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON connector payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an installed, authenticated oo CLI and a connected Formstack account.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
