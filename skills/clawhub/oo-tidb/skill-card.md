## Description:

Use this skill to operate TiDB Cloud through the OOMOL-connected oo CLI for reading, creating, and updating TiDB Cloud resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect TiDB Cloud action schemas, retrieve cluster and account resources, and run validated connector actions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include executing remote installer scripts for the oo CLI.

Mitigation: Review and validate the installer source or use a verified package before installation, and avoid elevated shells unless required.

Risk: The skill runs through an OOMOL-connected account that can access TiDB Cloud resources.

Mitigation: Install only when the publisher is trusted, review account scopes and connection state, and keep credentials managed through the connected account flow.

Risk: Write-tagged actions can change TiDB Cloud state.

Mitigation: Fetch the live action schema, confirm the exact payload and effect with the user, and reserve destructive action approval for explicit target confirmation.

## Reference(s):

- [TiDB Cloud homepage](https://www.pingcap.com/tidb/cloud/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub TiDB Cloud skill page](https://clawhub.ai/oomol/skills/oo-tidb)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands target the OOMOL oo CLI and may return TiDB Cloud connector JSON responses.]

## Skill Version(s):

1.0.3 (source: artifact frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
