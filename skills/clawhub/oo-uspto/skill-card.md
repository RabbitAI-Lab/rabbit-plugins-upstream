## Description:

Enables agents to use OOMOL's oo CLI for USPTO connector actions covering trademark case status, last update, and document metadata tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, employees, and external agents use this skill to inspect USPTO action schemas and run OOMOL connector commands for trademark status and document metadata workflows. Any write-labeled or schema-indicated state-changing action should be confirmed with the user before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad USPTO scope wording may lead an agent to assume capabilities beyond the listed connector actions.

Mitigation: Treat the listed actions and the live oo connector schema output as the intended scope before execution.

Risk: Write-capable connector actions could change USPTO state if run without review.

Mitigation: Require explicit user confirmation for any action whose label or schema can create, update, remove, or overwrite data.

Risk: The skill depends on the oo CLI and an OOMOL-connected USPTO account.

Mitigation: Install and use the skill only when the user is comfortable connecting USPTO through OOMOL and following the setup guidance.

## Reference(s):

- [ClawHub USPTO Skill Page](https://clawhub.ai/oomol/skills/oo-uspto)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [USPTO Homepage](https://www.uspto.gov/)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands are intended for the OOMOL oo CLI and can return JSON responses when --json is used.]

## Skill Version(s):

1.0.0 (source: frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
