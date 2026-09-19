## Description:

This skill lets agents operate QuintaDB through the OOMOL-connected oo CLI for reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect QuintaDB action schemas and operate databases, forms, fields, and records through an OOMOL-connected CLI. It is intended for QuintaDB workflows where the agent should avoid handling raw API tokens directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup instructions include remote installer commands that execute downloaded scripts in a shell.

Mitigation: Review setup instructions before installation and prefer a package-manager or verified installer flow for the oo CLI.

Risk: Create, update, and delete actions can change or permanently remove QuintaDB data.

Mitigation: Confirm the exact payload, target database, form, record, and expected effect before running write or destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-quintadb)
- [QuintaDB Homepage](https://quintadb.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance, Configuration]

**Output Format:** [Markdown with inline bash commands and JSON connector results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an installed oo CLI, an authenticated OOMOL session, and a connected QuintaDB account; write and destructive actions require confirmation.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
