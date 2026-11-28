## Description:

Manages Fastmail email and calendar via JMAP and CalDAV APIs for reading, sending, searching, organizing, bulk email operations, threads, calendar events, reminders, and invitation responses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[witooh](https://clawhub.ai/user/witooh)

### License/Terms of Use:


## Use Case:

External users and developers use this skill to connect an agent to a Fastmail account for email triage, sending replies, organizing mail, and managing calendars, reminders, and invitations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive email and calendar data.

Mitigation: Use a dedicated, narrowly scoped Fastmail token and app password where possible.

Risk: Credentials may be exposed if stored in shell profiles, committed environment files, or shared setup locations.

Mitigation: Store credentials outside committed files and avoid placing secrets in shared shell profiles.

Risk: Send, reply-all, delete, bulk delete, calendar deletion, and invitation response actions can have account-visible or destructive effects.

Mitigation: Require explicit human review before executing those actions.

Risk: Blindly running installer commands can introduce local execution risk.

Mitigation: Review installer commands before running them.

## Reference(s):

- [Fastmail Tools Reference](references/TOOLS.md)
- [Fastmail](https://www.fastmail.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [JSON tool responses and Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Fastmail JMAP and CalDAV credentials from environment variables and returns tool-specific JSON data with timestamps.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
