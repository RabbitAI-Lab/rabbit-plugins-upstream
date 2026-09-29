## Description:

Configure and operate the GameLearningRuntime CLI for project startup, bounded research and training, capture, run review, knowledge transfer, and verified model playback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to configure and run existing GLR projects, inspect run evidence, capture training data, and review model playback. Implementing the game adapter is outside its scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Operating a GLR project can start configured roles and maintain run history.

Mitigation: Review the project manifest and configured roles before execution; use bounded goals and inspect run evidence.

Risk: Configured recording or telemetry can expose private game assets, desktop content, or credentials.

Mitigation: Constrain capture to the intended game window and avoid sharing telemetry tokens, credentials, or sensitive recordings.

Risk: Updating GLR can replace binaries and project skills.

Mitigation: Apply updates only on explicit request and verify the selected project and release before updating.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/loonghao/skills/glr-cli)
- [GLR CLI command and contract reference](references/commands.md)
- [Data collection and rendering](references/data-collection.md)
- [Offline source packages](references/packages.md)
- [VX recording and acceptance contract](references/recording.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with command and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-specific operations require a reviewed GLR configuration and runtime evidence.]

## Skill Version(s):

0.23.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
