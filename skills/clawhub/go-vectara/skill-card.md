## Description:

Helps Go developers use the unofficial go-vectara client for Vectara API v2.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to add and call the unofficial Vectara API v2 Go client in Go projects. It guides installation, authentication, endpoint selection, and response handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence rates the skill suspicious because its OAuth instructions describe credential-bearing requests to auth.vectara.io, outside the declared api.vectara.io network scope.

Mitigation: Before installation, check whether OAuth setup is needed and confirm auth.vectara.io is allowed in the environment and is an intended destination.

Risk: The security scan was partial and could not resolve two local references, so its assessment is incomplete.

Mitigation: Review the full package and unresolved references before relying on the scan assessment.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Project repository](https://github.com/psyb0t/go-vectara)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-vectara)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Usage examples and API integration guidance; no generated files.]

## Skill Version(s):

0.3.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
