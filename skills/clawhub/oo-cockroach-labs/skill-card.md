## Description:

Cockroach Labs lets agents search and read CockroachDB Cloud organization, cluster, region, database, node, and SQL user data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent inspect CockroachDB Cloud organizations, clusters, available regions, cluster nodes, databases, and SQL users through the OOMOL Cockroach Labs connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions may lead an agent to run a remote oo CLI installer without integrity verification.

Mitigation: Prefer a pinned, verifiable package or manually review the installer before execution.

## Reference(s):

- [Cockroach Labs Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-cockroach-labs)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Cockroach Labs](https://www.cockroachlabs.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands run through the oo CLI and may return JSON data with execution metadata.]

## Skill Version(s):

1.0.2 (source: server evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
