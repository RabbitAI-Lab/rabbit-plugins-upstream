## Description:

Amplemarket lets agents operate Amplemarket through the OOMOL oo CLI to read account, contact, lead-list, and task data and perform supported task actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent work with an OOMOL-connected Amplemarket account for CRM-style contact, lead-list, and task workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup can involve remote installer scripts.

Mitigation: Inspect or verify installer scripts before running them.

Risk: Task actions can change Amplemarket state.

Mitigation: Require explicit user confirmation for task-changing actions, including complete_task and skip_task.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-amplemarket)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Amplemarket Homepage](https://www.amplemarket.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before running actions and may return connector JSON responses.]

## Skill Version(s):

1.0.2 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
