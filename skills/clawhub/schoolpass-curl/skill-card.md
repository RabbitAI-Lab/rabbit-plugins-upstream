## Description:

Provides curl and jq guidance for accessing a SchoolPass parent account, including student records, dismissal information, and pickup-change requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and their authorized assistants use shell commands to check SchoolPass students, calendars, drivers, and dismissal details, or manage pickup changes when explicitly intended.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The examples include live POST and DELETE requests that can create or cancel arrival and dismissal changes, despite the read-only description.

Mitigation: Review commands before execution and require explicit confirmation for every non-authentication POST or DELETE request.

Risk: Parent credentials and bearer tokens may be exposed through shell environments, command history, or shared transcripts.

Mitigation: Keep credentials and tokens out of shared transcripts and command history; restrict access to the shell session.

Risk: Responses may contain sensitive student and family information.

Mitigation: Limit access and sharing to authorized people, and avoid printing unnecessary personal data.

## Reference(s):

- [Schoolpass Curl on ClawHub](https://clawhub.ai/chrischall/skills/schoolpass-curl)
- [Ready-to-run requests](references/requests.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with bash commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SchoolPass parent credentials, a school code, and the appropriate regional API host.]

## Skill Version(s):

1.0.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
