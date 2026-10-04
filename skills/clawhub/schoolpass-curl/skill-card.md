## Description:

Provides curl examples to read SchoolPass parent-account information and submit or cancel student arrival and dismissal changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

SchoolPass parent-account users and developers can use one-off shell commands to check student schedules, pickup changes, drivers, and school information. The reference also includes commands to submit or cancel arrival and dismissal changes, which require explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Although described as read-only, the reference includes live commands to submit or cancel student arrival and dismissal changes.

Mitigation: Require explicit user confirmation before any studentchange POST or DELETE command; verify the intended student, date, and action.

Risk: SchoolPass credentials and responses may expose sensitive parent and student information.

Mitigation: Limit access to trusted agents and avoid displaying passwords, bearer tokens, or student details in shared transcripts.

## Reference(s):

- [SchoolPass curl skill on ClawHub](https://clawhub.ai/chrischall/skills/schoolpass-curl)
- [Ready-to-run requests](references/requests.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with curl and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands require SchoolPass parent credentials and a school code.]

## Skill Version(s):

1.0.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
