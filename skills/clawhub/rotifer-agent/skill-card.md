## Description:

Guides developers through selecting Rotifer Genes, composing a Genome, creating an Agent, and testing its pipeline.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaoba-dev](https://clawhub.ai/user/xiaoba-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to build Rotifer-specific Agents by decomposing a task into Genes, selecting and composing them, and validating the resulting Agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned npm commands may fetch packages whose contents change between runs.

Mitigation: Prefer a pinned npm version or project-local dependency and review installation commands before approving them.

Risk: CLI actions can read and write project files, contact registry services, or run an Agent.

Mitigation: Review the command and its effects before approving installs, publishing, overwrites, or Agent runs.

## Reference(s):

- [Rotifer documentation](https://rotifer.dev/docs)
- [Rotifer protocol specification](https://github.com/rotifer-protocol/rotifer-spec)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with tables and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide creation of project-local Genes and Agent configuration files.]

## Skill Version(s):

1.2.3 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
