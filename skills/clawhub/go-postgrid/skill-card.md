## Description:

An unofficial, typed Go client and integration guide for PostGrid print and mail resources and address verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to integrate an application with PostGrid for print and mail operations, address verification, and related account resources. It guides them through authentication, generated method signatures, response handling, and safe use of live operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live mail operations can send physical mail and incur charges; bulk address verification and targeted list builds may also be billable.

Mitigation: Use test credentials during development, and review recipients, content, and charges before requesting live operations.

Risk: Supplying live credentials to an unofficial dependency adds dependency and credential-handling risk.

Mitigation: Keep the API key in POSTGRID_API_KEY, review and pin the Go dependency before using live credentials, and do not hardcode, commit, or log the key.

## Reference(s):

- [Setup and operation reference](references/setup.md)
- [PostGrid API documentation](https://guides.postgrid.com/)
- [PostGrid OpenAPI document](https://guides.postgrid.com/api/openapi.yaml)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-postgrid)
- [Project homepage](https://github.com/psyb0t/go-postgrid)

## Skill Output:

**Output Type(s):** [Code, API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Go integration examples and operational guidance; does not itself perform API calls.]

## Skill Version(s):

0.2.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
