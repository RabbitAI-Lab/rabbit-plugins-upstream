## Description:

Use this skill for Formstack Documents requests through an OOMOL-connected account, including reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Formstack Documents through an OOMOL-connected account, including listing, retrieving, creating, copying, updating, and deleting document templates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, copy, or delete Formstack Documents templates.

Mitigation: Require explicit user confirmation of the target, payload, and expected effect before running write or destructive actions.

Risk: First-time setup references remote installer commands for the oo CLI.

Mitigation: Inspect or verify installer contents before execution and install only when OOMOL and the connector access model are trusted.

Risk: The connector operates through an OOMOL-connected Formstack Documents account.

Mitigation: Use accounts and scopes appropriate to the task, and re-check connection or credential errors before retrying privileged operations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-formstack-documents)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Formstack Documents Homepage](https://forms.formstack.com/products/documents)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector commands that return JSON responses containing data and execution metadata.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
