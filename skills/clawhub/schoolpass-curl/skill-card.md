## Description:

schoolpass-curl helps authorized SchoolPass parent-account users read student, calendar, pickup-change, driver, dismissal-location, and school information from a regional SchoolPass REST API with curl.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External authorized SchoolPass parent-account users and supporting developers use this skill for one-off terminal checks of SchoolPass students, dismissal calendars, pickup changes, authorized drivers, dismissal locations, and school information. The artifact also documents live POST and DELETE examples for dismissal or arrival changes, so those commands require explicit human confirmation before use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles SchoolPass credentials, bearer tokens, localStorage-derived school metadata, and student data.

Mitigation: Use only authorized accounts, keep credentials and tokens out of shared transcripts, and avoid sharing localStorage screenshots or other sensitive session details.

Risk: Although the skill is described primarily as read-oriented, the artifact includes POST and DELETE examples that can create or cancel live dismissal or arrival changes.

Mitigation: Require explicit human confirmation before running any POST or DELETE command, verify the student and date, and re-read the calendar afterward to confirm the result.

## Reference(s):

- [Ready-to-run requests](references/requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/schoolpass-curl)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, curl, and jq command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Terminal-oriented guidance that depends on user-provided SchoolPass credentials, school code, API host, and explicit authorization for the target account and students.]

## Skill Version(s):

0.3.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
