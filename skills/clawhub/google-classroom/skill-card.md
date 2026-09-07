## Description:

Google Classroom API integration with managed OAuth for managing courses, assignments, students, teachers, announcements, and submissions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and education operations teams use this skill to let an agent access Google Classroom through Maton for course, coursework, roster, submission, grading, and announcement workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Google Classroom write operations can change courses, rosters, grades, announcements, invitations, or deleted resources.

Mitigation: Default to read and list calls, then confirm the exact target, payload, and intended effect before any POST, PUT, PATCH, or DELETE request.

Risk: Broad or ambiguous Google Classroom authorization can expose more course data than the task requires.

Mitigation: Prefer OAuth, select least-privilege scopes where available, and specify the intended Maton connection when multiple connections exist.

Risk: The raw API-key fallback uses a long-lived credential that can leak through logs, shell history, child processes, or pasted output.

Mitigation: Use the CLI and OAuth when possible; use the raw API-key fallback only when the CLI cannot be installed, never print or persist the key, and send it only to api.maton.ai.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-classroom)
- [Maton Homepage](https://maton.ai)
- [Google Classroom API Documentation](https://developers.google.com/workspace/classroom/reference/rest)
- [Course Resource Reference](https://developers.google.com/workspace/classroom/reference/rest/v1/courses)
- [CourseWork Resource Reference](https://developers.google.com/workspace/classroom/reference/rest/v1/courses.courseWork)
- [StudentSubmissions Reference](https://developers.google.com/workspace/classroom/reference/rest/v1/courses.courseWork.studentSubmissions)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, API paths, JSON request examples, and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authorized Google Classroom connection.]

## Skill Version(s):

1.2.2 (source: server release metadata; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
