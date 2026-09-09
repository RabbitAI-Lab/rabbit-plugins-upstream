## Description:

agent-notify lets agents such as Claude Code, Codex, Hermes, and OpenClaw announce task completion or stuck states to a configured voice device through a local notifier daemon.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chujindan-dotcom](https://clawhub.ai/user/chujindan-dotcom)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to configure and run task-status voice notifications for long-running agent work. It monitors supported local agent session logs and sends completion or stuck-status messages to a trusted voice-notification backend.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The notifier runs as a persistent background process that reads local agent session logs and sends task text plus device and host metadata to a WebSocket backend.

Mitigation: Use only with a trusted backend, review what local session data may be exposed, and stop the daemon when notifications are no longer needed.

Risk: Setup uses a backend WebSocket address, device identifier, and authorization code that can be sensitive if exposed or reused.

Mitigation: Prefer wss:// endpoints, avoid placing long-lived authorization codes in shell history, and rotate or revoke codes through the backend when needed.

Risk: The self-test path has a temporary-file issue called out by the authoritative security guidance for shared multi-user machines.

Mitigation: Do not run selftest on shared multi-user systems unless that issue is fixed; use an isolated development machine or disposable environment for testing.

## Reference(s):

- [ClawHub agent-notify Skill Page](https://clawhub.ai/chujindan-dotcom/skills/agent-notify)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON WebSocket payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Chinese task-status notification text and structured task, status, time, detail, agent, host, and device metadata for a voice backend.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
