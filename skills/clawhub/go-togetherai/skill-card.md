## Description:

Guides Go developers in using the unofficial go-togetherai client to call the Together AI REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to install and integrate a typed Go client for Together AI API operations, configure bearer authentication, and handle responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An exposed Together AI API key could be misused.

Mitigation: Read the key from an environment variable, keep it out of source code, and do not log credentials or request headers.

Risk: Requests may share data with Together AI or initiate paid or destructive operations.

Mitigation: Send only data intended for Together AI, and perform paid or destructive actions only when explicitly requested.

## Reference(s):

- [go-togetherai project](https://github.com/psyb0t/go-togetherai)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-togetherai)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with Go and shell code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typed Go client integration examples and response-handling guidance.]

## Skill Version(s):

0.2.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
