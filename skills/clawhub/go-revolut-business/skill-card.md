## Description:

Unofficial Go client for the Revolut Business REST API with typed endpoint methods and bearer-token authentication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Go developers use this skill to add and use a typed client for reading Revolut Business data and performing supported API operations from Go applications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan was partial because a local reference in SKILL.md could not be resolved, leaving part of the evidence incomplete.

Mitigation: Review the local reference directly and treat the benign scanner verdict as limited evidence.

Risk: Bearer access tokens can expose Revolut Business account access if they are disclosed.

Mitigation: Read the token from an environment variable; do not hardcode, commit, log, or print request headers containing it.

Risk: Payment, transfer, exchange, and delete operations can move money or remove data.

Mitigation: Prefer the sandbox while developing and call these operations only when the user requested the action.

## Reference(s):

- [Setup and Reference](references/setup.md)
- [Package documentation](https://pkg.go.dev/github.com/psyb0t/go-revolut-business)
- [Project homepage](https://github.com/psyb0t/go-revolut-business)

## Skill Output:

**Output Type(s):** [Code, API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Revolut Business access token. Payment, transfer, exchange, and delete operations can move money or remove data.]

## Skill Version(s):

0.1.7 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
