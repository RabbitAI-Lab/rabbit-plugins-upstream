## Description:

An unofficial, typed Go client for the Intercom REST API, covering workspace data and requested actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

External developers use this skill in Go projects to integrate with Intercom workspace data and carry out requested support or customer data actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The access token can permit workspace changes, including contact deletion, according to its granted scopes.

Mitigation: Use a token with only the scopes needed and perform changes or deletions only when requested for the specified resources.

Risk: The security analysis is incomplete because two local references could not be resolved.

Mitigation: Review the skill and its dependencies before using it with workspace credentials.

## Reference(s):

- [Setup and API usage](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-intercom)
- [Project homepage](https://github.com/psyb0t/go-intercom)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code and concise Markdown setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the selected Intercom workspace region and an access token with the required scopes.]

## Skill Version(s):

0.9.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
