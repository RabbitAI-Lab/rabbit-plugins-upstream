## Description:

Read a SchoolPass parent account directly with curl against the regional SchoolPass REST API for one-off checks of students, arrival and dismissal calendars, pickup changes, drivers, dismissal locations, and school information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and SchoolPass parent-account users can use this skill to ask an agent for curl and jq-based SchoolPass API commands for one-off account reads. It is intended for live SchoolPass credentials and should be used carefully around student, parent, token, and password data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to use SchoolPass credentials against live SchoolPass APIs, exposing sensitive student, parent, password, and token data in transcripts or environment variables.

Mitigation: Use only in trusted workspaces, keep credentials out of shared transcripts, avoid printing bearer tokens or passwords, and clear shell history or logs that may contain sensitive values.

Risk: Referenced examples include commands that can create or delete student dismissal or arrival changes.

Mitigation: Treat write and delete examples as high-impact operations; require explicit user confirmation and re-read the calendar or change record after execution to verify the intended result.

Risk: Repeated rejected logins may trigger SchoolPass reCAPTCHA or account challenges.

Mitigation: Do not retry failed logins automatically; correct the credential or school code before trying again.

## Reference(s):

- [Ready-to-run requests](references/requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/schoolpass-curl)
- [Publisher profile](https://clawhub.ai/user/chrischall)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, Code, Guidance]

**Output Format:** [Markdown with inline bash, curl, jq, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include commands that read or modify live SchoolPass data; users should review commands before execution.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
