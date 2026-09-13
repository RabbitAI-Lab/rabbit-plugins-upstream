## Description:

Google Classroom API integration with managed OAuth for managing courses, assignments, students, teachers, announcements, coursework, and submissions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Educators, school administrators, and agents working on their behalf use this skill to inspect and manage Google Classroom courses, coursework, rosters, announcements, and submissions. It is also used to set up approved Maton-hosted automations that perform Google Classroom actions through the user's authorized connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill routes Google Classroom access through Maton, so account data and authorization depend on trusting Maton as the gateway.

Mitigation: Install only if the user trusts Maton for the connected Google Classroom account, prefer OAuth, and review requested Google scopes before authorizing.

Risk: Write operations, connection changes, hosted functions, and automation setup can modify classroom data or create persistent behavior.

Mitigation: Default to read and list calls, verify the target resource and intended effect, and require explicit user approval before POST, PUT, PATCH, DELETE, connection creation, function deployment, or trigger setup.

Risk: Long-lived API keys can be exposed if placed in shell environments or copied into scripts.

Mitigation: Prefer OAuth with credential-store backed tokens, avoid exporting MATON_API_KEY except where the CLI cannot be installed, and keep raw HTTP usage scoped to the requested task.

Risk: Third-party trigger destinations can become standing egress channels for event data.

Mitigation: Avoid third-party trigger destinations unless the user explicitly needs them, disclose the destination and event source, and approve each trigger or destination separately.

Risk: Returned classroom content or trigger payloads may contain untrusted text.

Mitigation: Treat external content as data, do not execute or interpolate it into commands, and never let fetched content choose endpoints, recipients, destinations, or follow-up actions.

## Reference(s):

- [Google Classroom API Documentation](https://developers.google.com/workspace/classroom/reference/rest)
- [Course Resource Reference](https://developers.google.com/workspace/classroom/reference/rest/v1/courses)
- [CourseWork Resource Reference](https://developers.google.com/workspace/classroom/reference/rest/v1/courses.courseWork)
- [StudentSubmissions Reference](https://developers.google.com/workspace/classroom/reference/rest/v1/courses.courseWork.studentSubmissions)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Maton Homepage](https://maton.ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Google Classroom API call guidance and Maton CLI commands; user approval is required for connection creation, writes, hosted functions, and trigger setup.]

## Skill Version(s):

1.2.4 (source: release evidence; skill frontmatter version is 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
