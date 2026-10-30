## Description:

Provides a typed Go client for reading and managing HubSpot API data with bearer-token authentication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add typed Go calls for HubSpot CRM and other supported HubSpot API endpoints. It helps with setup, authentication, endpoint selection, and interpreting typed responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: HubSpot requests can expose account data, and create, update, archive, delete, merge, or purge operations can change live records.

Mitigation: Use a token with only the scopes needed, keep it in an environment variable and out of logs, and review the target records before requested writes or deletions.

Risk: The client sends requests to the configured base URL.

Mitigation: Use https://api.hubapi.com for HubSpot data and review any nonstandard base URL before sending credentials.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-hubspot)
- [Project homepage](https://github.com/psyb0t/go-hubspot)

## Skill Output:

**Output Type(s):** [Code, API Calls, Configuration instructions, Shell commands, Guidance]

**Output Format:** [Markdown with inline Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include examples that read or modify HubSpot account data.]

## Skill Version(s):

0.3.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
