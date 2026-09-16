## Description:

Save or resume task context, record work history, and compress long records for a new session or agent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[snowsonz](https://clawhub.ai/user/snowsonz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use Handoff to continue existing task records, save handoff-ready task state, and maintain compact work history across sessions. It is also used for explicit maintenance of supported agent entry points and legacy handoff cleanup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Explicit setup maintenance can persistently add or remove handoff reminders in supported agent configuration files.

Mitigation: Review the affected client list before enabling, and use setup.py disable only when explicitly removing configured entry points.

Risk: Legacy cleanup and migration scripts can change repository-local handoff deployment files when explicitly run.

Mitigation: Run migrate.py status first, proceed only for explicit maintenance requests, and review any cleanup changes before normal project submission.

## Reference(s):

- [Handoff Skill Page](https://clawhub.ai/snowsonz/skills/agent-handoff-skill)
- [Task Handoff Protocol](PROTOCOL.md)
- [Handoff Maintenance](references/protocol.md)
- [Cross-Client Validation](references/compatibility.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown task records, concise guidance, and shell commands for explicit maintenance requests]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update workspace task records; user-level agent configuration changes occur only for explicit setup maintenance requests.]

## Skill Version(s):

0.4.0 (source: evidence.release.version and VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
