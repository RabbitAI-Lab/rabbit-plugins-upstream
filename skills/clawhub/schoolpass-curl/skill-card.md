## Description:

Provides curl commands for authorized parents to read their own SchoolPass students, calendars, pickup changes, drivers, dismissal locations, and school information from the regional SchoolPass REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill for one-off shell reads of an authorized SchoolPass parent account, including student lists, arrival and dismissal calendars, pickup changes, drivers, dismissal locations, and school information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credentials, bearer tokens, and SchoolPass student or driver data can be exposed through shell history, transcripts, files, or shared command output.

Mitigation: Use the skill only with your own authorized parent account, avoid entering passwords where shell history records them, keep .env files out of version control with restrictive permissions, and do not share output containing student or driver information.

Risk: Repeated failed logins may trigger SchoolPass reCAPTCHA or account challenges.

Mitigation: Do not repeatedly retry rejected credentials; fix the credential issue and try once.

Risk: Copying unrelated browser localStorage values can leak tokens or session data.

Mitigation: Use only the school appCode and apiUrl needed to configure the school code and regional API host.

## Reference(s):

- [Ready-to-run requests](references/requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/schoolpass-curl)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands rely on user-provided SchoolPass credentials, school code, regional API host, curl, and jq.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
