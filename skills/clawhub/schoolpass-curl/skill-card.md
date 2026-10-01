## Description:

Guides one-off SchoolPass parent-account requests through curl for student, calendar, pickup, driver, dismissal location, and school information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents or authorized developers use shell examples to check SchoolPass account information without running the MCP server. The included reference also contains commands that can submit or cancel real student arrival and dismissal changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The reference includes live commands that submit or cancel student arrival and dismissal changes, despite the skill's read-only framing.

Mitigation: Review commands before running them; execute write or delete examples only when intentionally changing a real student's records, and confirm the result by rereading the calendar.

Risk: Live SchoolPass access exposes credentials, bearer tokens, and sensitive student information.

Mitigation: Use only with authorized accounts and keep passwords, tokens, and returned student details out of shared terminals, logs, and transcripts.

## Reference(s):

- [Ready-to-run SchoolPass requests](references/requests.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with bash and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can return JSON containing parent and student information.]

## Skill Version(s):

1.0.5 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
