## Description:

Unofficial Go client for the HubSpot API. `hubspot.NewClientWithResponses("https://api.hubapi.com", ...)` from `github.com/psyb0t/go-hubspot` gives a typed method for every path in HubSpot's 2026-03 OpenAPI documents, including CRM objects such as contacts and companies, single-deal reads and updates, associations, properties, search, marketing, CMS, automation, conversations, files and webhooks. Auth is a Bearer private app or OAuth access token set through a request editor. Responses decode into typed `JSON200`/`JSON201` fields. Use when Go code needs to read or write HubSpot data, or already imports go-hubspot.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to add typed HubSpot API calls to an application, including reading, searching, creating, and updating HubSpot data. It also helps developers configure authentication and check generated client methods and response handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: HubSpot credentials could expose account data if mishandled.

Mitigation: Use narrowly scoped credentials, keep tokens in environment variables, and do not commit or log them.

Risk: Create, update, merge, archive, delete, or GDPR purge calls can change a live HubSpot account.

Mitigation: Make account changes only when the user requests them, and only for records within the task's scope.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-hubspot on pkg.go.dev](https://pkg.go.dev/github.com/psyb0t/go-hubspot)
- [go-hubspot project](https://github.com/psyb0t/go-hubspot)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with Go code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.3.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
