## Description:

Guides agents through SchoolPass parent-account API requests with curl, including account reads and optional student arrival or dismissal changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and their authorized agents can check students, calendars, drivers, pickup changes, and school information from a terminal. The reference also provides commands that can change or cancel student arrival and dismissal records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The reference includes commands that can create or delete student arrival and dismissal changes despite the read-focused description.

Mitigation: Avoid or remove write and delete recipes unless changes are intended; require explicit confirmation before each POST or DELETE request.

Risk: Using the skill gives an agent SchoolPass parent credentials and access to live account data.

Mitigation: Review the skill before installing, grant access only when appropriate, and do not disclose passwords or bearer tokens in shared transcripts.

## Reference(s):

- [SchoolPass curl request examples](references/requests.md)
- [SchoolPass Curl release on ClawHub](https://clawhub.ai/chrischall/skills/schoolpass-curl)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a SchoolPass parent account, school code, and regional API host.]

## Skill Version(s):

1.0.10 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
