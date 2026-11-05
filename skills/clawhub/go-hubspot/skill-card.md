## Description:

Guides Go developers in using the unofficial go-hubspot client to call HubSpot APIs with typed requests and responses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to integrate applications with HubSpot through typed client methods for reading and changing account data. It provides setup, authentication, endpoint-discovery, and response-handling guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: HubSpot API calls can change live account records, including through create, update, archive, delete, merge, and purge operations.

Mitigation: Review the target records and make changes only when requested and only to records the task owns.

Risk: Access tokens, developer-key URLs, or private response data could be exposed in code or logs.

Mitigation: Use a least-privilege token, keep credentials in environment variables, and keep tokens, developer-key URLs, and private response data out of logs.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-hubspot project](https://github.com/psyb0t/go-hubspot)
- [go-hubspot on pkg.go.dev](https://pkg.go.dev/github.com/psyb0t/go-hubspot)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance and examples for Go integrations; API operations may read or change HubSpot account data.]

## Skill Version(s):

0.5.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
