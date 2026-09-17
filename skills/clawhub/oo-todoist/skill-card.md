## Description:

Todoist lets an agent read and manage Todoist tasks, projects, sections, labels, and comments through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent retrieve, create, update, complete, and comment on Todoist work items while relying on OOMOL account connections instead of direct Todoist API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote shell installer commands that could run arbitrary code if the installer is not independently trusted.

Mitigation: Verify the oo CLI installer and source before running curl-to-bash or PowerShell iex setup commands.

Risk: The Todoist connector is account-linked and can create, update, close, or comment on Todoist objects.

Mitigation: Confirm the exact target, payload, and expected effect with the user before write-capable actions.

Risk: Assuming connector fields without the live schema can produce invalid or unintended Todoist changes.

Mitigation: Fetch the live Todoist connector schema before building each action payload.

## Reference(s):

- [ClawHub Todoist skill page](https://clawhub.ai/oomol/skills/oo-todoist)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Todoist homepage](https://www.todoist.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before actions; write-capable Todoist actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
