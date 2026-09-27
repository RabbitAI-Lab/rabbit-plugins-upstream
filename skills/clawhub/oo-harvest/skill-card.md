## Description:

Harvest (getharvest.com) support for reading, creating, updating, restarting, stopping, and deleting Harvest data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Harvest through the oo CLI, including listing users, clients, projects, tasks, task assignments, and time entries. It also supports time-entry create, update, restart, stop, and delete workflows with confirmation requirements for state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The oo CLI installer and subsequent shell commands can affect the user's local environment.

Mitigation: Verify trust in OOMOL and the oo CLI installer source before installation or command execution.

Risk: Create, update, restart, stop, and delete actions can change or remove Harvest time-entry data.

Mitigation: Confirm the exact Harvest account, target time entry, payload, and expected effect with the user before running state-changing actions.

## Reference(s):

- [ClawHub Harvest skill page](https://clawhub.ai/oomol/skills/oo-harvest)
- [Harvest homepage](https://www.getharvest.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before building payloads; write and destructive Harvest actions require user confirmation.]

## Skill Version(s):

1.0.5 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
