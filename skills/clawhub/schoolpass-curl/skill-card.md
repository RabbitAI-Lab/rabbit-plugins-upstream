## Description:

Provides curl-based recipes for accessing authorized SchoolPass parent account data through the regional SchoolPass REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Authorized SchoolPass parents and developers use this skill for one-off terminal checks of students, arrival and dismissal calendars, pickup changes, drivers, dismissal locations, and school information. It is suited to controlled shell sessions where the user can provide SchoolPass credentials and a school code.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires real SchoolPass parent credentials and can expose student information.

Mitigation: Use it only in controlled terminals, keep credentials and bearer tokens out of chat and logs, and prefer environment variables for secrets.

Risk: The reference material includes live write and delete examples for dismissal records despite the skill's read-focused summary.

Mitigation: Run only read examples unless you intentionally want to alter SchoolPass records, and review any POST or DELETE command before execution.

## Reference(s):

- [Ready-to-run requests](artifact/references/requests.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash, curl, and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-provided SchoolPass credentials, school code, and regional API host; examples can call live SchoolPass APIs when run.]

## Skill Version(s):

0.4.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
