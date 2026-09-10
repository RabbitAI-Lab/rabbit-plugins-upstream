## Description:

Bark Notify lets agents send Bark push notifications for requested messages, meaningful progress, completion, and blockers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lumen01](https://clawhub.ai/user/lumen01)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use Bark Notify to let agents send Bark push notifications from terminal-capable agents. It is suited for explicit notification requests, meaningful long-running task milestones, task completion, and blockers that need user attention.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bark device keys can be exposed if printed, committed, or passed directly on the command line.

Mitigation: Store BARK_KEY in local private configuration, use standard input for setup when possible, and avoid placing real keys in commands or repository files.

Risk: Notification titles or bodies can reveal sensitive task details.

Mitigation: Keep notification content concise and avoid sensitive information in push titles or bodies.

Risk: Proactive notifications can interrupt users or create unnecessary noise.

Mitigation: Send notifications only for explicit requests, meaningful milestones, completion, or blockers, and use passive delivery only when explicitly requested.

## Reference(s):

- [Server-resolved source repository](https://github.com/Lumen01/agent-bark-notify)
- [ClawHub skill page](https://clawhub.ai/lumen01/skills/agent-bark-notify)
- [Bark project](https://github.com/Finb/Bark)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and environment configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a local Bark device key configuration and can emit dry-run or diagnostic JSON from the bundled CLI.]

## Skill Version(s):

0.1.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
