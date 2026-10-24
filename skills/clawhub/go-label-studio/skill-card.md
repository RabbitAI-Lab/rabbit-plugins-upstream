## Description:

Provides Go developers with guidance for using an unofficial, typed client to integrate with the Label Studio API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to integrate applications with Label Studio, including configuring authentication and calling API operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials and task or annotation data are sent to the configured Label Studio server.

Mitigation: Use a trusted server URL, HTTPS for remote servers, and a token with only the permissions needed; keep credentials out of source control and logs.

Risk: Create, update, and delete API operations can change server data.

Mitigation: Perform data-changing operations only when explicitly requested and within the user's authorized scope.

Risk: The bundled guidance was reviewed, but the external Go dependency was not audited.

Mitigation: Review and pin the dependency version, and verify its behavior before using it in production.

## Reference(s):

- [Setup and reference guide](artifact/references/setup.md)
- [go-label-studio package documentation](https://pkg.go.dev/github.com/psyb0t/go-label-studio)
- [go-label-studio project page](https://github.com/psyb0t/go-label-studio)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.2.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
