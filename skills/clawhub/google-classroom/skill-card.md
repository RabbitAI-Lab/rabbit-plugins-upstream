## Description:

Helps agents manage Google Classroom courses, coursework, participants, announcements, and submissions through a connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Educators and administrators use this skill to review and manage courses, assignments, participants, and student submissions. With separate approval, they can also set up scheduled or event-driven actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting an account grants Maton access to authorized Google Classroom data.

Mitigation: Authorize only the intended account and necessary scopes after reviewing the access request.

Risk: Writes, hosted functions, and triggers can change records or run without a new prompt.

Mitigation: Confirm the target and effect of every write, connection, function, and trigger before activation.

Risk: A destination can continuously forward event data to an external host.

Mitigation: Approve destinations separately; avoid third-party forwarding unless the host and ongoing data flow are understood.

## Reference(s):

- [Google Classroom API documentation](https://developers.google.com/workspace/classroom/reference/rest)
- [Google Classroom coursework reference](https://developers.google.com/workspace/classroom/reference/rest/v1/courses.courseWork)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Maton homepage](https://maton.ai)
- [Time trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with command, API, and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a connected Google Classroom account; writes and automations require user approval.]

## Skill Version(s):

1.2.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
