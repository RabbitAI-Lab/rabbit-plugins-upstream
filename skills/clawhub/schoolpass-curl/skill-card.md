## Description:

Read a SchoolPass parent account directly with curl against the regional SchoolPass REST API (a busapi shard on school-pass.net), without running the MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and authorized SchoolPass parent account users use this skill for one-off terminal reads of student, calendar, pickup-change, driver, dismissal-location, and school information through curl and jq examples.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The reference material includes write and delete commands that can change live student dismissal or arrival records.

Mitigation: Review commands before execution and use the write/delete examples only when the user intends to modify live SchoolPass data.

Risk: SchoolPass credentials and bearer tokens could be exposed in shared transcripts or logs.

Mitigation: Keep credentials local, avoid echoing passwords or bearer tokens, and use the skill only with accounts the user is authorized to access.

## Reference(s):

- [Ready-to-run requests](references/requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/schoolpass-curl)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with curl, jq, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SchoolPass email, password, school code, and regional API host supplied by the user.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
