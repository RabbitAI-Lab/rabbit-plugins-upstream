## Description:

Google Classroom API integration with managed OAuth for managing courses, assignments, students, teachers, announcements, and submissions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Google Classroom through Maton-managed OAuth, including reading classroom data and performing user-approved course, coursework, roster, submission, and announcement actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorizing the integration can grant access to the selected Google Classroom account.

Mitigation: Prefer OAuth, review requested scopes, and connect only the account needed for the current task.

Risk: Writes, new connections, hosted functions, triggers, and persistent forwarding can change classroom data or continue moving event data after setup.

Mitigation: Confirm each write or automation with the user, review destinations and scopes, and delete unused connections, functions, or triggers when the task is complete.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/google-classroom)
- [Maton homepage](https://maton.ai)
- [Google Classroom API Documentation](https://developers.google.com/workspace/classroom/reference/rest)
- [Course Resource Reference](https://developers.google.com/workspace/classroom/reference/rest/v1/courses)
- [CourseWork Resource Reference](https://developers.google.com/workspace/classroom/reference/rest/v1/courses.courseWork)
- [StudentSubmissions Reference](https://developers.google.com/workspace/classroom/reference/rest/v1/courses.courseWork.studentSubmissions)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](references/time/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Code, API Calls]

**Output Format:** [Markdown guidance with inline shell, Python, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Maton CLI commands, raw HTTP examples, or hosted function snippets for user-approved Google Classroom workflows.]

## Skill Version(s):

1.2.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
