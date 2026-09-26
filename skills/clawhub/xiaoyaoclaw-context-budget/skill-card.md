## Description:

Checks enabled OpenClaw models against vendor-published context windows, recommends a 60% setting, and changes context-window configuration only after user confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dtsola](https://clawhub.ai/user/dtsola)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users and administrators check enabled models' context-window settings against vendor documentation and, after reviewing and confirming the proposed changes, update those settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An incorrect vendor window or proposed setting could lead to an unsuitable persistent model configuration.

Mitigation: Review the vendor source, decision card, and full proposed diff before confirming any change.

Risk: Reading model settings may expose unrelated configuration if the full configuration is displayed or shared.

Mitigation: Limit inspection and output to model and context-window fields; do not disclose credentials or other configuration.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dtsola/skills/xiaoyaoclaw-context-budget)
- [Project installation and usage documentation](https://github.com/dtsola/xiaoyaoclaw-context-budget)
- [Design documentation](docs/DESIGN.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration instructions]

**Output Format:** [Markdown decision card, proposed configuration diff, and result summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Shows vendor sources and recommended windows; applies changes only after confirmation.]

## Skill Version(s):

1.0.7 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
