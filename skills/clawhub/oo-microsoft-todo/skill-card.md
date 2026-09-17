## Description:

Operate Microsoft To Do through an OOMOL-connected account to read, create, update, and delete task lists, tasks, and checklist items.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to manage Microsoft To Do content through the OOMOL Microsoft To Do connector, including task lists, tasks, and checklist items. It supports read workflows as well as user-approved write and destructive workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup references a remote installer with broad local execution impact.

Mitigation: Do not let an agent run the remote installer automatically; install the oo CLI through a trusted, verified method.

Risk: Write and destructive actions can change or delete Microsoft To Do data.

Mitigation: Confirm the exact payload, target, and effect with the user before running write actions, and require explicit approval before destructive actions.

## Reference(s):

- [ClawHub Microsoft To Do skill page](https://clawhub.ai/oomol/skills/oo-microsoft-todo)
- [Microsoft To Do homepage](https://to-do.office.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are returned as JSON when actions are run with the oo CLI.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
