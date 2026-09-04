## Description:

Google Classroom API integration with managed OAuth for managing courses, assignments, students, teachers, announcements, and submissions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Educators, administrators, and developers use this skill to inspect and manage Google Classroom courses, coursework, submissions, rosters, announcements, topics, and invitations through Maton-managed OAuth.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes broad raw Google Classroom API access, including write and management actions beyond simple read/list workflows.

Mitigation: Default to read/list calls, confirm target resources and payloads before POST, PUT, PATCH, or DELETE requests, and use the narrowest available OAuth scopes.

Risk: The raw HTTP/API-key fallback can expose a long-lived Maton credential through environment leakage, logs, shell history, or pasted output.

Mitigation: Prefer OAuth through the Maton CLI; use the API-key fallback only when the CLI cannot be used, never print or persist the key, and rotate it if exposed.

Risk: Multiple Maton accounts or Google Classroom connections can cause actions to land in the wrong classroom account.

Mitigation: Specify the intended profile and connection before write operations, especially when more than one active connection exists.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-classroom)
- [Maton](https://maton.ai)
- [Google Classroom API Documentation](https://developers.google.com/workspace/classroom/reference/rest)
- [Course Resource Reference](https://developers.google.com/workspace/classroom/reference/rest/v1/courses)
- [CourseWork Resource Reference](https://developers.google.com/workspace/classroom/reference/rest/v1/courses.courseWork)
- [StudentSubmissions Reference](https://developers.google.com/workspace/classroom/reference/rest/v1/courses.courseWork.studentSubmissions)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, API calls]

**Output Format:** [Markdown guidance with inline shell, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, Maton authentication, and explicit user approval for connection creation or write operations.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
