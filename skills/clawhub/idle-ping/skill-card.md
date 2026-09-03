## Description:

Install a complete proactive outreach system — idle detection, randomized dice delivery, topic-driven crawler, share queue, and persona-based messages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[leslie311](https://clawhub.ai/user/leslie311)

### License/Terms of Use:

MIT

## Use Case:

Developers and OpenClaw users use this skill to install a proactive outreach workflow that monitors idle time, queues discovered content, and sends occasional persona-based messages through a configured chat channel.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent background automation may send unsolicited messages and continue running after installation.

Mitigation: Use --dry-run or --no-cron before enabling cron jobs, configure quiet hours and a daily cap, and document the cron removal or disable path before installation.

Risk: The workflow reads local session and optional persona context while preparing outbound messages.

Mitigation: Install only in a trusted workspace, keep runtime paths simple and controlled, and avoid placing sensitive persona or memory files where this workflow should not read them.

Risk: Outbound Telegram delivery depends on a configured chat identifier.

Mitigation: Verify TELEGRAM_ID before enabling delivery and test manually with a non-sensitive message or dry-run configuration.

Risk: The content pipeline crawls external sources and stores local queue, state, and history data.

Mitigation: Review queued content before broad use, keep local storage private, and monitor or rotate the generated queue and history files as needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/leslie311/skills/idle-ping)
- [OpenClaw](https://openclaw.ai)
- [README](artifact/README.md)
- [Configuration example](artifact/scripts/idle-ping.env.example)
- [License](artifact/LICENSE)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and plain text with shell commands, configuration files, JSON state, and agent message prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Installs recurring OpenClaw cron jobs and local scripts that generate queued content and outbound chat messages.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
