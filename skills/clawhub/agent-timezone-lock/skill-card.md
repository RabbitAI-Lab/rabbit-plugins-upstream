## Description:

Helps an OpenClaw agent avoid UTC-as-local mistakes by configuring a local timezone and providing scripts for accurate current-time reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ferrentinomj-dev](https://clawhub.ai/user/ferrentinomj-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill when an agent needs to answer time questions, convert UTC timestamps, or maintain a configured local timezone without guessing from internal context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional AGENTS.md patch creates a persistent timezone rule that can affect future agent sessions.

Mitigation: Use --patch-agents only when persistent behavior is intended and review the prompted change before confirming.

Risk: Time answers may be wrong if the timezone has not been configured or has changed since setup.

Mitigation: Run timezone_setup.py for the user's current timezone and verify output with now.py before relying on time-sensitive responses.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ferrentinomj-dev/skills/agent-timezone-lock)
- [Publisher profile](https://clawhub.ai/user/ferrentinomj-dev)
- [Timezone conversion rules](artifact/references/timezone_rules.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes local-time command output and optional timezone configuration files.]

## Skill Version(s):

1.2.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
