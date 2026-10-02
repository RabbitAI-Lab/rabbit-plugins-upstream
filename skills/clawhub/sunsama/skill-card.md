## Description:

Helps agents manage Sunsama tasks, daily plans, calendar events, objectives, timers, and connected email threads through a user-authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Sunsama users can ask an agent to review and organize tasks, schedule work, track time, and manage calendar events or connected email threads, with approval before changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Task, calendar, and connected email actions can alter or delete user data.

Mitigation: Verify the account and target, prefer reads, and confirm each write, deletion, RSVP, or email action before execution.

Risk: Automation triggers and destinations can run actions or forward events persistently.

Mitigation: Review the function, trigger, destination, payload, and recipient; require separate approval for persistent event forwarding.

Risk: Credentials or overly broad connections could expose account access.

Mitigation: Verify the Maton profile and Sunsama connection, use least-privilege access, and avoid raw API keys unless the CLI cannot be used.

## Reference(s):

- [Sunsama skill listing](https://clawhub.ai/byungkyu/skills/sunsama)
- [Maton](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Sunsama](https://sunsama.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Markdown]

**Output Format:** [Markdown with inline commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Account actions require user authorization and confirmation before changes.]

## Skill Version(s):

1.2.7 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
