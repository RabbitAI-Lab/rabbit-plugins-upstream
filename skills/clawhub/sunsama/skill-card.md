## Description:

Helps agents manage Sunsama tasks, daily plans, calendars, objectives, time tracking, and connected email threads through an authorized account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and teams use this skill to find and organize Sunsama tasks, plan calendar time, track objectives, and work with email threads in connected accounts. With separate approval, they can set up scheduled or event-driven actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Task, calendar, meeting RSVP, or email-thread changes could affect the wrong item or connected account.

Mitigation: Default to reading first; verify the account, target, and intended effect, and obtain explicit approval for every write or deletion.

Risk: Functions, triggers, and destinations can continue acting or forwarding data after the current session.

Mitigation: Explain the schedule, action, and destination, and obtain separate approval before enabling persistent automation or event forwarding.

Risk: Long-lived API keys can expose connected account access.

Mitigation: Prefer OAuth login through the CLI; do not print, log, or embed credentials in commands or destinations.

## Reference(s):

- [Sunsama skill release](https://clawhub.ai/byungkyu/skills/sunsama)
- [Maton](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Time trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with command, code, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions require an authorized Sunsama connection; writes require user confirmation.]

## Skill Version(s):

1.2.6 (source: server-resolved ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
