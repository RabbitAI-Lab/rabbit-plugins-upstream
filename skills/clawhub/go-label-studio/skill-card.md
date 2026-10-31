## Description:

Guides Go developers in integrating the unofficial go-label-studio client with Label Studio APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers can use this skill to add and configure the go-label-studio client, call Label Studio endpoints, and handle responses, pagination, and API errors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials and task or annotation data are sent to the configured Label Studio server.

Mitigation: Use a least-privilege token, verify the server address before sending credentials or data, and use HTTPS for remote servers.

Risk: API calls can create, update, or delete Label Studio data.

Mitigation: Explicitly authorize data-changing operations and keep them within the user's scope.

Risk: The security review covers the bundled instructions, not the external Go dependency implementation.

Mitigation: Review and pin the external Go dependency.

## Reference(s):

- [Setup and reference](artifact/references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-label-studio)
- [Project homepage](https://github.com/psyb0t/go-label-studio)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes Go API examples, dependency installation commands, and environment variable configuration guidance.]

## Skill Version(s):

0.4.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
