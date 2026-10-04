## Description:

Checks enabled OpenClaw models against vendor-published context windows and proposes a 60% setting, applying window changes only after user confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dtsola](https://clawhub.ai/user/dtsola)

### License/Terms of Use:

MIT

## Use Case:

OpenClaw users and administrators check the context-window settings of enabled models against official vendor specifications and, after reviewing the proposed changes, adjust the configured windows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Incorrect context-window settings can affect model behavior or disrupt configuration.

Mitigation: Check the cited vendor specification and proposed changes before confirming; verify the active window after applying.

Risk: A broad context-check request could initiate an unexpected read-only scan of model settings.

Mitigation: Invoke the skill deliberately and review its decision card before authorizing any configuration changes.

## Reference(s):

- [OpenClaw Context Budget on ClawHub](https://clawhub.ai/dtsola/skills/xiaoyaoclaw-context-budget)
- [OpenClaw Context Budget design documentation](docs/DESIGN.md)

## Skill Output:

**Output Type(s):** [Analysis, Configuration guidance]

**Output Format:** [Markdown decision card and change summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Shows vendor sources and proposed old-to-new window values; changes require confirmation.]

## Skill Version(s):

1.0.8 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
