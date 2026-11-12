## Description:

Guides Go developers in using the unofficial typed go-hubspot client to access HubSpot's 2026-03 API, including setup, authentication, endpoint selection, and request and response handling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to add typed HubSpot API calls to Go projects, including reading and writing CRM data and using other documented HubSpot endpoints. It provides setup, authentication, endpoint lookup, and request/response guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: HubSpot API operations can create, update, merge, archive, delete, or purge live account data.

Mitigation: Use write or destructive operations only when requested, and only on records the task owns; check the affected records and response status.

Risk: The skill uses private app or OAuth credentials, and the security scan was partial because a local reference did not resolve.

Mitigation: Keep access tokens in environment variables, never hardcode or log them, and review the skill and unresolved reference before use.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-hubspot)
- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/go-hubspot)
- [Project homepage listed in the skill](https://github.com/psyb0t/go-hubspot)

## Skill Output:

**Output Type(s):** [Code, API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code blocks and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typed Go API usage examples, setup and authentication guidance, and endpoint lookup instructions.]

## Skill Version(s):

0.5.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
