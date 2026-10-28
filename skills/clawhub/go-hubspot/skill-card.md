## Description:

Unofficial Go client for the HubSpot API. `hubspot.NewClientWithResponses("https://api.hubapi.com", ...)` from `github.com/psyb0t/go-hubspot` gives a typed method for every path in HubSpot's 2026-03 OpenAPI documents, including CRM objects such as contacts and companies, single-deal reads and updates, associations, properties, search, marketing, CMS, automation, conversations, files and webhooks. Auth is a Bearer private app or OAuth access token set through a request editor. Responses decode into typed `JSON200`/`JSON201` fields. Use when Go code needs to read or write HubSpot data, or already imports go-hubspot.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to write Go applications that read and manage HubSpot data through typed client methods, and to look up the request, response, authentication, and endpoint details needed for those integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write, archive, delete, merge, and purge operations can change live HubSpot records.

Mitigation: Make changes only when the user requested them, and only to records the task owns; use only the permissions and scopes needed for the task.

Risk: HubSpot access tokens or developer API keys could be exposed.

Mitigation: Read credentials from environment variables, keep them out of source control and logs, and do not print request headers.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-hubspot)
- [Project homepage](https://github.com/psyb0t/go-hubspot)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown instructions with Go code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
