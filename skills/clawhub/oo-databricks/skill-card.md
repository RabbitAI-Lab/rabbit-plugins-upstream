## Description:

Databricks (databricks.com). Use this skill for Databricks requests, including reading, creating, updating, and deleting data through the OOMOL `oo` CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and data platform operators use this skill to inspect Databricks action schemas and run Databricks connector actions through an OOMOL-connected account. It supports workspace, cluster, job, run, repo, and secret administration, including read, write, and destructive operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands for the `oo` CLI.

Mitigation: Use a verified, version-pinned installation path before enabling the skill.

Risk: The skill can run write and destructive Databricks actions.

Mitigation: Confirm the exact payload, target resource, and expected effect before running write or destructive operations.

Risk: The connector performs broad Databricks administration through an OOMOL-connected account.

Mitigation: Install only when that delegation model is acceptable and the connected Databricks account has appropriate least-privilege access.

## Reference(s):

- [Databricks homepage](https://www.databricks.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-databricks)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs the agent to inspect live Databricks connector schemas before constructing payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
