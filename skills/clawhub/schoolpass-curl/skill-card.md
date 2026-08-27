## Description:

Read a SchoolPass parent account directly with curl against the regional SchoolPass REST API for one-off terminal access to students, calendars, pickup changes, drivers, dismissal locations, and school information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate curl and jq guidance for direct, one-off SchoolPass parent-account API checks from a terminal. It is suited to reading account, student, dismissal-calendar, driver, pickup-change, and school information when the user intentionally provides SchoolPass credentials and school code.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live POST and DELETE examples can change student dismissal records.

Mitigation: Require explicit human confirmation before running write or delete commands, and re-read the calendar afterward to verify the result.

Risk: SchoolPass passwords, bearer tokens, and student data may be exposed in shared logs or transcripts.

Mitigation: Keep credentials in environment variables, do not echo passwords or bearer tokens, and redact student data before sharing output.

Risk: Repeated failed login attempts can trigger SchoolPass reCAPTCHA or account challenge flows.

Mitigation: Stop after a rejected login, correct credentials out of band, and retry only once the email, password, school code, and API host are confirmed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/schoolpass-curl)
- [Ready-to-run requests](references/requests.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash and jq code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include live SchoolPass API request examples that require user-provided credentials, bearer tokens, school codes, student IDs, and confirmation before write or delete operations.]

## Skill Version(s):

0.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
