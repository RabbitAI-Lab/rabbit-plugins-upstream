## Description:

TiDB Cloud helps agents inspect action schemas and operate TiDB Cloud through the OOMOL-connected oo CLI for reading, creating, and updating TiDB Cloud resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to query TiDB Cloud resources, inspect live action contracts, and run approved TiDB Cloud connector actions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands that may execute changing code on a user's machine.

Mitigation: Install the oo CLI through a trusted, versioned, and verifiable method, and review setup commands before execution.

Risk: Connected TiDB Cloud credentials may allow access to organization resources.

Mitigation: Grant only the minimum TiDB Cloud privileges required for the task and review visible resources before use.

Risk: Write-capable actions can change TiDB Cloud state.

Mitigation: Inspect the live action schema, confirm the exact payload and expected effect with the user, and require explicit approval before write or destructive operations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-tidb)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [TiDB Cloud](https://www.pingcap.com/tidb/cloud/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs agents to inspect live connector schemas before constructing JSON payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
