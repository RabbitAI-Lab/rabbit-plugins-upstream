## Description:

Configure and operate the GameLearningRuntime CLI for bridge startup, bounded research and training, run review, knowledge transfer, and verified model playback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to configure and operate trusted GLR projects, run bounded goal-driven training, inspect results, and review recordings and model playback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unreviewed project commands or configuration may execute unintended tasks.

Mitigation: Use only trusted GLR projects and review role commands and configuration before execution.

Risk: Dashboard tokens, recording paths, or backup destinations may expose sensitive data.

Mitigation: Review token handling and capture and backup paths before enabling these features.

Risk: An unintended update may replace the CLI or project skills.

Mitigation: Run glr update only after an explicit request to update.

## Reference(s):

- [ClawHub glr-cli release](https://clawhub.ai/loonghao/skills/glr-cli)
- [GLR CLI commands and contracts](references/commands.md)
- [Data collection and reporting](references/data-collection.md)
- [Project package handoff](references/packages.md)
- [Recording and acceptance](references/recording.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with CLI commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Instructions distinguish verified runtime results from process exit, artifact hashes, and diagnostic metrics.]

## Skill Version(s):

0.25.0 (source: ClawHub server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
