## Description:

Provides curl and jq guidance for reading a SchoolPass parent account, with separate examples for changing arrival or dismissal records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and authorized helpers use this skill for one-off terminal checks of students, calendars, pickup changes, drivers, dismissal locations, and school information in their SchoolPass account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The reference guide includes live commands that can create or delete student arrival or dismissal changes despite the skill's read-focused description.

Mitigation: Avoid the POST and DELETE examples unless you explicitly intend to change live records; re-read the calendar to confirm any intended change.

Risk: SchoolPass passwords, bearer tokens, and student information can be exposed when commands or responses are shared.

Mitigation: Keep credentials and tokens out of shared transcripts, and copy only appCode and apiUrl when checking browser localStorage.

## Reference(s):

- [SchoolPass Curl release](https://clawhub.ai/chrischall/skills/schoolpass-curl)
- [Ready-to-run requests](references/requests.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with bash and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a SchoolPass parent account, school code, and regional API host.]

## Skill Version(s):

1.0.9 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
