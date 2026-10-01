## Description:

Helps agents manage Google Classroom courses, coursework, rosters, announcements, and submissions through an authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Educators, administrators, and their authorized agents use this skill to review or manage courses, assignments, participants, announcements, and student submissions. Optional scheduled or event-driven workflows require separate approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting an account grants access to Google Classroom data within its authorized scope.

Mitigation: Confirm the account and intended access before connection; grant only the scopes the task needs.

Risk: Writes to coursework, rosters, or announcements can change classroom records.

Mitigation: Default to read-only operations and obtain explicit approval for each write.

Risk: Hosted functions, triggers, or destinations may persist or forward event data.

Mitigation: Review the function, trigger scope, destination, and data flow with the user before approving each one.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/byungkyu/skills/google-classroom)
- [Maton](https://maton.ai)
- [Google Classroom API documentation](https://developers.google.com/workspace/classroom/reference/rest)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Time trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Guidance]

**Output Format:** [Markdown with CLI examples and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access and an authorized Maton account and Google Classroom connection.]

## Skill Version(s):

1.2.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
