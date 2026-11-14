## Description:

Guides Go developers in using a typed client for HubSpot API operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers building Go applications can use the generated client to read and manage HubSpot CRM and other supported API data. The skill provides setup, authentication, endpoint lookup, and response-handling guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The client requires a HubSpot access token, which could expose account data if mishandled.

Mitigation: Read tokens from environment variables, grant only required scopes, and never commit or log tokens or request headers.

Risk: Create, update, archive, delete, merge, and purge operations can change live HubSpot data.

Mitigation: Use these operations only when requested and only for records in scope.

Risk: The security scan had partial coverage because one local path-like reference could not be resolved.

Mitigation: Review the unresolved reference and relevant skill materials before relying on the scan as complete.

## Reference(s):

- [Setup and reference (setup.md)](references/setup.md)
- [Source repository](https://github.com/psyb0t/go-hubspot)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-hubspot)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.5.5 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
