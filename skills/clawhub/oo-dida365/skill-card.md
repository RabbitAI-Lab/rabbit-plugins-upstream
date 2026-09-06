## Description:

Dida365 helps an agent read, create, update, move, complete, delete, and filter Dida365 tasks, projects, habits, and habit check-ins through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent operate a connected Dida365 account for task, project, and habit workflows. It supports read-only lookups as well as reviewed state-changing actions such as creating tasks, moving tasks, completing tasks, and deleting projects or tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can change tasks, projects, habits, or scheduling data in the connected Dida365 account.

Mitigation: Confirm the exact payload and expected effect with the user before running create, update, move, completion, or habit check-in actions.

Risk: Delete actions can remove task or project data.

Mitigation: Get explicit approval for the target project or task before running delete_project or delete_task.

Risk: Setup, account-connection, and billing commands can start account linking or payment-related flows.

Mitigation: Only run setup, connection, or billing commands after a command fails with the matching auth, connection, scope, expiration, app, or credit error.

## Reference(s):

- [ClawHub Dida365 skill listing](https://clawhub.ai/oomol/skills/oo-dida365)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Dida365 homepage](https://dida365.com)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action results are JSON responses containing data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
