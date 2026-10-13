## Description:

Guides agents in using the do CLI to review and manage tasks, habits, and other personal records through the do app.

This skill is ready for commercial/non-commercial use.

## Publisher:

[robbeverhelst](https://clawhub.ai/user/robbeverhelst)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and agents use this skill to capture and review tasks, complete or snooze tasks, log habits, and read other personal records through the do CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Commands can change remote task and habit data without a clear warning in the skill description.

Mitigation: Require explicit approval before capturing, completing, or snoozing tasks or logging habits.

Risk: The installation guidance includes a script downloaded and executed through a shell.

Mitigation: Avoid the curl-to-bash Bun installer unless its source has been independently trusted and verified.

Risk: An API key grants access to personal account data and permitted write operations.

Mitigation: Use narrowly scoped keys and provide them to agents through environment variables rather than saved configuration or command-line arguments.

## Reference(s):

- [do CLI source and documentation](https://github.com/robbeverhelst/do)
- [do on ClawHub](https://clawhub.ai/robbeverhelst/skills/do-cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may retrieve personal data or change tasks and habit records in the connected account.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
