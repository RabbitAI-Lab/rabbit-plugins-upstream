## Description:

Google Classroom API integration with managed OAuth for managing courses, assignments, students, teachers, and announcements through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Educators, administrators, and agent operators use this skill to list, inspect, and manage Google Classroom courses, coursework, rosters, submissions, invitations, topics, and announcements through Maton-managed OAuth. It is most useful when an agent needs to prepare safe Google Classroom API calls, default to read/list operations, and request confirmation before connection creation or data-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill routes Google Classroom access through Maton, so users must trust Maton as the API gateway for classroom data.

Mitigation: Confirm trust in Maton before installation or use, and prefer OAuth through the Maton CLI so credentials remain in the platform credential store.

Risk: Course, roster, grading, invitation, announcement, and deletion operations can change classroom data.

Mitigation: Require explicit user confirmation before any data-changing call and review the target resource, payload, and intended effect.

Risk: Using an incomplete endpoint path may send an invalid or unintended Maton API request.

Mitigation: Use the documented /google-classroom/ prefix unless current Maton documentation says otherwise.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-classroom)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Google Classroom API Documentation](https://developers.google.com/workspace/classroom/reference/rest)
- [Google Classroom Courses Reference](https://developers.google.com/workspace/classroom/reference/rest/v1/courses)
- [Google Classroom CourseWork Reference](https://developers.google.com/workspace/classroom/reference/rest/v1/courses.courseWork)
- [Google Classroom StudentSubmissions Reference](https://developers.google.com/workspace/classroom/reference/rest/v1/courses.courseWork.studentSubmissions)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance centers on Maton CLI and SDK calls for Google Classroom API operations.]

## Skill Version(s):

1.1.0 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
