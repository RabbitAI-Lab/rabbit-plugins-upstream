## Description:

Guides Go developers using the unofficial go-hubspot client to call HubSpot's API with typed requests and responses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to install and work with a typed Go client for reading and writing HubSpot API data, including CRM records and related services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Writes, merges, archives, deletions, and GDPR purges can change live HubSpot records.

Mitigation: Authorize the specific records and requested changes before making mutations.

Risk: A HubSpot access token can grant access to sensitive account data.

Mitigation: Use a token scoped to the needed endpoints, store it in an environment variable, and do not hardcode or log it.

Risk: The Go dependency is unofficial.

Mitigation: Review and pin the dependency before production use.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-hubspot)
- [Project homepage](https://github.com/psyb0t/go-hubspot)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.3.3 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
