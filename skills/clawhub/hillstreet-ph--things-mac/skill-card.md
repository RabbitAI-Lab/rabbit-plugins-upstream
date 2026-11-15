## Description:

Add, update, list, search, or inspect Things 3 todos, inbox, today, projects, areas, and tags on macOS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hillstreet-ph](https://clawhub.ai/user/hillstreet-ph)

### License/Terms of Use:

MIT-0

## Use Case:

macOS users use this skill to read Things 3 task data and add or update todos through the Things CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A local reference could not be resolved, limiting confidence in the security review.

Mitigation: Resolve and review the referenced content before relying on the skill.

Risk: Add and update commands can change Things todos.

Mitigation: Use the documented --dry-run preview before write operations and confirm the selected todo ID before updates.

## Reference(s):

- [Things Mac on ClawHub](https://clawhub.ai/hillstreet-ph/skills/things-mac)
- [Things 3 CLI repository](https://github.com/ossianhempel/things3-cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Text responses with shell commands and Things task data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task details or dry-run URL previews.]

## Skill Version(s):

1.0.2 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
