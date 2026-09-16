## Description:

QuintaDB (quintadb.com). Use this skill for ANY QuintaDB request - reading, creating, updating, and deleting data. Whenever a task involves QuintaDB, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage QuintaDB databases, forms, fields, and records through an OOMOL-connected oo CLI session. It supports read actions and confirmed create, update, and delete workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can execute a remotely downloaded oo CLI installer.

Mitigation: Review the installer and prefer a trusted, versioned, verifiable installation method before running it.

Risk: Connected QuintaDB credentials can grant access to account data.

Mitigation: Connect only accounts whose QuintaDB data the agent should access and review permission scopes before use.

Risk: Create, update, and delete actions can change or remove QuintaDB records.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [QuintaDB homepage](https://quintadb.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [OOMOL QuintaDB connection](https://console.oomol.com/app-connections?provider=quintadb)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution and returns oo CLI JSON responses with execution metadata.]

## Skill Version(s):

1.0.2 (source: artifact frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
