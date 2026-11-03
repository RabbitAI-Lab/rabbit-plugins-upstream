## Description:

Provides guidance for using the unofficial go-hubspot Go client to make typed HubSpot API requests, authenticate with Bearer tokens, and handle responses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers using Go can follow this skill to add the go-hubspot client and write typed code for reading or changing HubSpot data. It covers authentication, endpoint and type discovery, response handling, and safe handling of live record changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: HubSpot examples can make changes to live records, and mishandled credentials could expose account access.

Mitigation: Use a least-privilege token, read it from an environment variable, keep the base URL at https://api.hubapi.com, avoid logging credentials or headers, and authorize specific record changes before running generated code.

Risk: The downloaded third-party Go module was not covered by the scan of the bundled documentation.

Mitigation: Review and pin the module before production use.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-hubspot repository](https://github.com/psyb0t/go-hubspot)
- [go-hubspot API documentation](https://pkg.go.dev/github.com/psyb0t/go-hubspot)

## Skill Output:

**Output Type(s):** [Code, Configuration instructions, Shell commands, Guidance]

**Output Format:** [Markdown with Go examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.4.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
