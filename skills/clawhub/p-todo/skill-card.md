## Description:

P-Todo lets agents manage todos, users, comments, statistics, search, settings, and data exports through the local REST API for the P-Todo desktop app.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pondsi](https://clawhub.ai/user/pondsi)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to let a trusted local agent operate the P-Todo desktop application's task, user, comment, search, statistics, settings, and export API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unauthenticated API access can change, delete, or export P-Todo task data.

Mitigation: Use the skill only with trusted local agents or scripts, and add authentication or explicit confirmations for delete, export, and settings actions before broader use.

Risk: The API may be reachable beyond the intended local environment if binding or firewall settings are not controlled.

Mitigation: Bind the service explicitly to 127.0.0.1 or firewall the configured port before enabling agent access.

Risk: Exported todo data can contain sensitive personal or team information.

Mitigation: Treat JSON or CSV exports as sensitive files and review their destination path and sharing permissions.

## Reference(s):

- [P-Todo ClawHub release](https://clawhub.ai/pondsi/skills/p-todo)
- [P-Todo REST API Skill](artifact/SKILL.md)
- [P-Todo README](artifact/README.md)

## Skill Output:

**Output Type(s):** [API calls, Shell commands, Guidance, Configuration]

**Output Format:** [Markdown with REST endpoint descriptions and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the P-Todo app to be running on the configured local API port.]

## Skill Version(s):

1.0.0 (source: server release metadata and pom.xml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
