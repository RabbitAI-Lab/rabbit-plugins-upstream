## Description:

Provides curl and jq recipes for reading a SchoolPass parent account, with additional examples that can submit or cancel student attendance and dismissal changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and authorized account users can check students, calendars, pickup changes, drivers, and school information from the terminal. The included write examples can also change or cancel student records and require explicit approval before use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write and delete examples can change or cancel live student attendance or dismissal records despite the read-oriented description.

Mitigation: Use read-only requests for routine checks; require explicit confirmation before any write or delete and verify the resulting record.

Risk: Running account requests exposes credentials and bearer tokens if commands or output are shared.

Mitigation: Keep credentials and tokens out of shared transcripts and limit access to local session data.

## Reference(s):

- [Ready-to-run SchoolPass requests](artifact/references/requests.md)
- [SchoolPass Curl on ClawHub](https://clawhub.ai/chrischall/skills/schoolpass-curl)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with bash commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SchoolPass account credentials and a school code; commands may return account and student data.]

## Skill Version(s):

1.0.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
