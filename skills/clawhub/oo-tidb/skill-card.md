## Description:

Helps agents search and read TiDB Cloud clusters, branches, regions, quotas, API keys, audit logs, imports, and exports through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators use this skill to inspect TiDB Cloud resources and operational records from an OOMOL-connected account without handling raw TiDB Cloud tokens directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installer guidance pipes remote OOMOL CLI scripts into a shell without an integrity check.

Mitigation: Review the installer before running it, or use a verified package, checksum, or signature workflow when available.

Risk: Connected OOMOL credentials can expose TiDB Cloud data visible to the organization, including API key listings and audit logs.

Mitigation: Install and connect the skill only when OOMOL is trusted with that TiDB Cloud access, and use the least-privileged organization credentials available.

## Reference(s):

- [TiDB Cloud homepage](https://www.pingcap.com/tidb/cloud/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-tidb)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; read-oriented TiDB Cloud actions return JSON responses from the oo CLI.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
