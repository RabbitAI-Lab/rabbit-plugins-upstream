## Description:

Worksnaps lets agents read Worksnaps users, projects, tasks, assignments, time entries, and time reports through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Worksnaps project, task, assignment, time-entry, time-report, and current-user data from a connected Worksnaps account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer scripts executed directly in a shell.

Mitigation: Review the installer source first and prefer a trusted, versioned, checksum-verified oo CLI installation method.

Risk: The connected Worksnaps account can expose the listed user, project, task, assignment, time-entry, and report data to connector actions.

Mitigation: Connect Worksnaps only when that read access is acceptable for the account and task.

## Reference(s):

- [ClawHub Worksnaps skill listing](https://clawhub.ai/oomol/skills/oo-worksnaps)
- [Worksnaps homepage](https://www.worksnaps.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [OOMOL Worksnaps connection page](https://console.oomol.com/app-connections?provider=worksnaps)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Action execution returns JSON from the oo connector when commands are run.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
