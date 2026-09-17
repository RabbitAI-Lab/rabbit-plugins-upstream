## Description:

Provides read-only CockroachDB Cloud access through the OOMOL cockroach_labs connector and oo CLI for searching and reading account data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect CockroachDB Cloud organizations, clusters, nodes, databases, SQL users, and available regions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup recommends executing remote installer scripts directly in a shell.

Mitigation: Prefer a verifiable, version-pinned, or package-manager-based oo CLI installation and review the installer source before use.

Risk: Connector action inputs can vary from the examples.

Mitigation: Inspect the live action schema with oo connector schema before constructing each payload.

Risk: Connector use depends on an OOMOL account connection that can access Cockroach Labs data.

Mitigation: Confirm the intended OOMOL account, Cockroach Labs API key scope, connection status, and billing state before relying on connector results.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-cockroach-labs)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Cockroach Labs](https://www.cockroachlabs.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command output summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing JSON payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
