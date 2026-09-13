## Description:

Read a SchoolPass parent account directly with curl against the regional SchoolPass REST API (a busapi shard on school-pass.net), without running the MCP server. Use for a one-off shell read of your students, arrival/dismissal calendar, pending pickup changes, drivers, dismissal locations, or school info — "check SchoolPass from the terminal", "list my kids in SchoolPass", "any dismissal changes today". Requires SCHOOLPASS_EMAIL / SCHOOLPASS_PASSWORD / SCHOOLPASS_SCHOOL_CODE.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, developers, and support users can use this skill for one-off terminal access to a SchoolPass parent account, including student lists, arrival and dismissal calendars, pickup changes, drivers, dismissal locations, and school information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is positioned mostly for read-only SchoolPass access but includes commands that can submit or cancel live student dismissal or arrival changes.

Mitigation: Use write and delete commands only after deliberately verifying the student ID, date, change type, and intended effect; re-read the calendar afterward to confirm the result.

Risk: SchoolPass credentials and bearer tokens can be exposed through shared shell history, transcripts, or copied command output.

Mitigation: Keep credentials in environment variables, avoid echoing passwords or tokens, and remove sensitive values before sharing terminal output.

Risk: Repeated rejected logins can trigger SchoolPass reCAPTCHA challenges and block shell login.

Mitigation: Do not retry failed logins blindly; correct the credential or school code first, then try once.

## Reference(s):

- [Ready-to-run requests](references/requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/schoolpass-curl)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SchoolPass email, password, school code, and regional API host environment variables.]

## Skill Version(s):

0.4.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
