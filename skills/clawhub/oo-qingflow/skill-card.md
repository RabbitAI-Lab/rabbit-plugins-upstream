## Description:

Qingflow lets agents read, create, update, and delete Qingflow data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to operate Qingflow through an OOMOL-connected account, including reading workspace data and creating, updating, commenting on, reassigning, rolling back, or processing business records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands could execute changing code on the user's machine.

Mitigation: Use an official, signed or checksum-verified, version-pinned installation path before running the oo CLI.

Risk: OOMOL mediates access to the user's Qingflow account and connected workspace.

Mitigation: Install and connect the skill only when OOMOL-mediated Qingflow access is acceptable for the workspace involved.

Risk: Write and destructive Qingflow actions can change records, workflow state, comments, reminders, assignments, or rollback targets.

Mitigation: Require explicit user confirmation of the target, payload, and expected effect before any write, rollback, reassignment, or workflow action.

## Reference(s):

- [Qingflow homepage](https://qingflow.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Qingflow skill page](https://clawhub.ai/oomol/skills/oo-qingflow)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Qingflow connector schemas before building action payloads.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
