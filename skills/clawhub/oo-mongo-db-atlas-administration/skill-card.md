## Description:

MongoDB Atlas Administration helps agents inspect MongoDB Atlas projects and clusters through the OOMOL connector and oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, database operators, and support agents use this skill to list MongoDB Atlas projects and clusters and retrieve details for specific projects or clusters through a connected Atlas account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer one-liners that execute immediately.

Mitigation: Before installation, review the installer source or use a verified, pinned, or manually reviewed oo CLI installation method.

Risk: The skill depends on the connected MongoDB Atlas account and OOMOL connector permissions.

Mitigation: Use a least-privilege Atlas API key and confirm account, project, and cluster targets before sharing or acting on returned data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mongo-db-atlas-administration)
- [MongoDB Atlas](https://www.mongodb.com/products/platform/atlas-database)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are returned as JSON data with execution metadata when actions are run.]

## Skill Version(s):

1.0.2 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
